import aiohttp
import asyncio
import json
import re
import requests
from DrissionPage import ChromiumPage, ChromiumOptions
from bs4 import BeautifulSoup


class Main:
    def __init__(self):
        self.sites = [f"https://pvp.qq.com/web201605/herodetail/{x['id_name']}.shtml" for x in requests.get("https://pvp.qq.com/web201605/js/herolist.json").json()]

    async def fetch(self, session, url):
        async with session.get(url) as response:
            return await response.json(content_type=None)

    async def fork(self):
        async with aiohttp.ClientSession() as session:
            urls = [
                "https://pvp.qq.com/web201605/js/herolist.json",
                "https://pvp.qq.com/web201605/js/item.json",
                "https://pvp.qq.com/web201605/js/summoner.json",
                "https://pvp.qq.com/web201605/js/ming.json"
            ]
            herolist, item, summoner, ming = await asyncio.gather(*(self.fetch(session, url) for url in urls))

            for data in ming:
                data['ming_des'] = re.sub('<.*?>', '', data['ming_des'])

            for x in herolist:
                y = x['ename']
                notAvailable = [521, 544, 545, 564, 514, 159, 563, 517, 582]
                if y not in notAvailable:
                    try:
                        storyHero = await self.fetch(session, f"https://pvp.qq.com/zlkdatasys/storyhero/index{y}.json")
                        for key in storyHero:
                            if isinstance(storyHero[key], list) and len(storyHero[key]) == 1:
                                storyHero[key] = storyHero[key][0]
                    except UnicodeDecodeError:
                        storyHero = None
                else:
                    storyHero = None
                x['storyHero'] = storyHero

            r = {
                "herolist": {data["id_name"]: data for data in herolist},
                "data": {data["item_name"]: data for data in item},
                "summoner": {data["summoner_name"]: data for data in summoner},
                "ming": {data["ming_name"]: data for data in ming}
            }
            return r

    async def main(self):
        options = ChromiumOptions()
        options.auto_port()
        options.set_argument('--headless=new')
        options.set_argument('--no-sandbox')
        options.use_system_user_path()
        dp = ChromiumPage(options)
        mainData = {}
        for index, url in enumerate(self.sites):
            print(f"Processing {url} ({index + 1}/{len(self.sites)})...")
            dp.get(url)
            soup = BeautifulSoup(dp.html, features="html.parser")
            title = soup.find("h3", class_="cover-title").text
            name = soup.find("h2", class_="cover-name").text
            skills = []
            for i, skill in enumerate(soup.find_all('div', class_='show-list')):
                if i == 4:
                    break
                skillName = skill.find('b').text
                try:
                    cooldownText = skill.find_all('span')[0].text.split("：")[1]
                    costText = skill.find_all('span')[1].text
                    if "弹药消耗：" in costText:
                        costText = costText.split("弹药消耗：")[1]
                    else:
                        costText = costText.split("：")[1]
                except (ValueError, IndexError):
                    costText = "0"

                cooldown = [float(i) for i in cooldownText.split('/') if i.replace('.', '', 1).isdigit()]
                cost = [float(i) for i in costText.split('/') if i.replace('.', '', 1).isdigit()]
                skillDesc = skill.find('p', class_='skill-desc').text
                skillImg = soup.find('ul', class_="skill-u1").find_all('li')[i].find('img').get('src')
                skillImg = f"https:{skillImg}"
                skillData = {
                    "skillName": skillName,
                    "cooldown": cooldown,
                    "cost": cost,
                    "skillDesc": skillDesc,
                    "skillImg": skillImg
                }
                skills.append(skillData)
            survivalPercentage = soup.find("span", class_="cover-list-bar data-bar1 fl").find("i", class_="ibar").get("style").split(':')[1]
            attackPercentage = soup.find("span", class_="cover-list-bar data-bar2 fl").find("i", class_="ibar").get("style").split(':')[1]
            abilityPercentage = soup.find("span", class_="cover-list-bar data-bar3 fl").find("i", class_="ibar").get("style").split(':')[1]
            difficultyPercentage = soup.find("span", class_="cover-list-bar data-bar4 fl").find("i", class_="ibar").get("style").split(':')[1]
            skins = [{"skinName": skins.find('p').text, "skinImg": f"https:{skins.find('i').find('img').get('src')}"} for skins in soup.find("ul", class_="pic-pf-list pic-pf-list3").find_all('li')]
            emblems = [{"emblemName": emblems.find('p').find("em").text, "emblemDescription": ' '.join(p.text for p in emblems.find_all('p')[1:]), "emblemImg": emblems.find('img').get('src')} for emblems in soup.find("ul", class_="sugg-u1").find_all('li')]
            emblemTips = soup.find("p", class_="sugg-tips").text.split('：')[1]
            heroInfoBoxes = soup.find_all('div', class_='hero-info')
            bestPartners = self.getHeroes(heroInfoBoxes[0])
            suppressingHeroes = self.getHeroes(heroInfoBoxes[1])
            suppressedHeroes = self.getHeroes(heroInfoBoxes[2])

            data = {
                "title": title,
                "name": name,
                "skill": skills,
                "survivalPercentage": survivalPercentage,
                "attackPercentage": attackPercentage,
                "abilityPercentage": abilityPercentage,
                "difficultyPercentage": difficultyPercentage,
                "skins": skins,
                "emblems": emblems,
                "emblemTips": emblemTips,
                "bestPartners": bestPartners,
                "suppressingHeroes": suppressingHeroes,
                "suppressedHeroes": suppressedHeroes,
                "url": url
            }
            mainData[name] = data
        dp.close()
        result = {
            "main": mainData,
            "fork": await self.fork()
        }
        return result

    def getHeroes(self, heroInfo):
        heroes = {}
        heroList = heroInfo.find('ul').find_all('li')
        heroDescList = [p.text for p in heroInfo.find('div', class_='hero-list-desc').find_all('p')]
        for i, li in enumerate(heroList):
            heroImg = f"https:{li.find('img')['src']}"
            heroEname = li.find('a')['href'].split('/')[-1].split('.')[0]
            forkJson = requests.get("https://pvp.qq.com/web201605/js/herolist.json").json()
            for heroData in forkJson:
                if heroData['ename'] == int(heroEname):
                    heroName = heroData['cname']
                    heroLink = f"https://pvp.qq.com/web201605/herodetail/{heroData['id_name']}.shtml"
            heroDesc = heroDescList[i] if i < len(heroDescList) else ""
            heroes[heroName] = {
                "name": heroName,
                "thumbnail": heroImg,
                "description": heroDesc,
                "url": heroLink
            }
        return heroes


if __name__ == "__main__":
    result = asyncio.run(Main().main())
    with open("wangzhe.json", "w") as f:
        json.dump(result, f, indent=4, ensure_ascii=True)
