[<img src = "made-by-qing762 (1).svg" >](https://discord.com/users/635765555277725696)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://discord.com/users/635765555277725696)
[![forthebadge](https://forthebadge.com/images/badges/kinda-sfw.svg)](https://discord.com/users/635765555277725696)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://discord.com/users/635765555277725696)
[![forthebadge](https://forthebadge.com/images/badges/open-source.svg)](https://discord.com/users/635765555277725696)

# Honor of Kings heroes API JSON File 
# 王者荣耀英雄 API JSON 文件

I scrapped the [entire website](https://pvp.qq.com/web201605/herolist.shtml) to a CSV file and converted it to a JSON file through a python script so you doesnt have to do it




## API Reference

#### Get entire json

```http
  GET https://qingbotcommand.netlify.app/wangzhe.json
  GET https://qingbotcommand.netlify.app/wangzherongyao.json
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `NONE` | `GET` | Just request a get request and you're good to go.|


## Usage/Examples
### Sample discord bot

```python
import discord, json, requests
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
intents.typing = True
intents.presences = True
intents.message_content = True

bot = commands.bot(prefix="[", intents=intents)

@bot.command(aliases=["wangzhe", "王者荣耀", "王者"])
async def wangzherongyao(ctx, agentname):
    async with ctx.typing():
        msg = await ctx.reply(content="Loading JSON file...")
        
        #Another version of the API :D
        link = 'https://qingbotcommand.netlify.app/wangzherongyao.json'
        
        f = requests.get(link)
        dt = f.json()
        result = [x for x in dt if x["cname"] == agentname]
        for abcd in result:
            e = abcd["ename"]
            c = abcd["cname"]
            t = abcd["title"]
            n = abcd["new_type"]
            h = abcd["hero_type"]
            sohai = abcd["skin_name"]
            m = abcd["moss_id"]

        # https://qingbotcommand.netlify.app/wangzhe.json
        # Saved this link locally and named it "wangzhe.json"
        with open('wangzhe.json', encoding='utf-8') as lj:
            data = json.load(lj)
            list = [key["skinname"] for key in data["heroes"] if agentname == key["name"]]
            for key in data["heroes"]:
                if agentname == key["name"]:
                    abc = key["link"]
                    s = abc.split('/')
                    shabi = s[5]
            for key in data["heroes"]:
                if agentname == key["name"]:
                    gannineh = key["name"]
                    l = key["link"]
                    codename = key["uid"]
                    t = key["tip"]
                    sd = key["shortdesc"]

            embed=discord.Embed(color=ctx.author.color)
            embed.add_field(name='Name', value=gannineh)
            embed.add_field(name="Short description", value=sd)
            embed.add_field(name="UID", value=codename)
            embed.add_field(name="Moss ID", value=m)
            embed.add_field(name="Hero code", value=shabi[0:3])
            embed.add_field(name="Hero type", value=h)
            embed.add_field(name="Tips", value=t)
            embed.add_field(name='Skins', value=", ".join(list))
            embed.add_field(name="Url", value=l)
            embed.set_author(name=gannineh, url=l, icon_url=f"https://game.gtimg.cn/images/yxzj/img201606/heroimg/{shabi[0:3]}/{shabi[0:3]}.jpg")
            embed.set_thumbnail(url=f"https://game.gtimg.cn/images/yxzj/img201606/heroimg/{shabi[0:3]}/{shabi[0:3]}-smallskin-2.jpg")
            await msg.edit(content='', embed=embed)

bot.run(YOURTOKEN)
```


## Test Screenshot
I use this JSON file for my discord bot and here's what it output with the sample python code

![App Screenshot](https://media.discordapp.net/attachments/995904492988006531/1036964279661908008/unknown.png)


## JSON file doesnt work anymore?

If it doesn't work anymore, please reach out to me by Discord: [qing762](https://discord.com/users/635765555277725696)


## FAQ

#### How you did it without an official API?

I scrapped the entire website.

#### Will this be updated in the future?

Not sure atm.

#### Will this API be available on a website?

[~Yes! And it's WIP~](https://qingbotcommand.netlify.app/wangzhe.json)

## Authors

- [@qing762](https://twitch.tv/qing762)

-----------------

[<img src = "in-memorable-of-technoblade.svg" >](https://discord.com/users/635765555277725696)
