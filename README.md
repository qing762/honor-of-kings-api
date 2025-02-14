> [!NOTE]  
> Join the [Discord server](https://qing762.is-a.dev/discord) for issues. Thanks a lot!

# Honor of Kings 王者荣耀 API 

An API that scrapes data from [Honor of Kings official website](https://pvp.qq.com/web201605/herolist.shtml) and convert into JSON format.

## How it works

It scrapes data from [Honor of Kings official website](https://pvp.qq.com/web201605/herolist.shtml) and format/beautify it into a JSON format.

## API Reference

### Get All Heroes Data

```http
GET /api/wangzhe
```

Returns the entire Honor of Kings heroes data.

#### Response

```json
{
    "main": {
        "廉颇": {
            "title": "正义爆轰",
            "name": "廉颇",
            "skill": [],
            "survivalPercentage": "100%",
            "attackPercentage": "30%",
            "abilityPercentage": "40%",
            "difficultyPercentage": "30%",
            "skins": [],
            "emblems": [],
            "emblemTips": "若廉颇是辅助位，则携带坦克铭文",
            "bestPartners": {},
            "suppressingHeroes": {},
            "suppressedHeroes": {},
            "url": "https://pvp.qq.com/web201605/herodetail/lianpo.shtml"
        },
        "小乔": {
            "title": "恋之微风",
            "name": "小乔",
            "skill": [],
            "survivalPercentage": "20%",
            "attackPercentage": "10%",
            "abilityPercentage": "80%",
            "difficultyPercentage": "30%",
            "skins": [],
            "emblems": [],
            "emblemTips": "猎狩提升10%移速加成，对于被动具有加速效果的小乔来说，适合放风筝，可以进行中远距离的输出，机动性高。心眼和梦魇提升法穿效果。对于小乔这种伤害比较高的英雄来说，增加法穿可以在对方出法抗时也打出高额伤害。",
            "bestPartners": {},
            "suppressingHeroes": {},
            "suppressedHeroes": {},
            "url": "https://pvp.qq.com/web201605/herodetail/xiaoqiao.shtml"
        },
        ...
    }
}
```

### Get Specific Hero Data

```http
GET /api/wangzhe/heroes/{hero}
```

Returns data for a specific Honor of Kings hero.

#### Response

```json
{
    "title": "玫瑰剑士",
    "name": "夏洛特",
    "skill": [
        {
            "skillName": "七星光芒剑",
            "cooldown": [0],
            "cost": [0],
            "skillDesc": "夏洛特任意技能命中敌人后，会将下次释放的其他技能强化为追加技，并获得一层印记，持续4秒。叠满3层印记后普攻将强化为追加技【七星光芒剑】，追击锁定敌人打出7段伤害，每段造成50~120(+25%物理攻击)物理伤害和10~20%减速，最后一段额外造成12%已损生命的物理伤害，释放期间获得21%~35%免伤。追加技对敌人附带伤残效果，每层减少10~20%攻速，持续4秒，最多叠加2层，伤残效果随敌方每次普攻移除一层。",
            "skillImg": "https://game.gtimg.cn/images/yxzj/img201606/heroimg/536/53600.png"
        },
        {
            "skillName": "迅光三角剑",
            "cooldown": [8, ...],
            "cost": [0],
            "skillDesc": "起手技：短暂延迟后，向指定方向释放迅光三角剑，对路径上的敌人造成200/230/260/290/320/350(+100%物理攻击)物理伤害，命中后增加80%持续衰减的移速，持续2秒。",
            "skillImg": "https://game.gtimg.cn/images/yxzj/img201606/heroimg/536/53610.png"
        },
        ...
    ],
    "survivalPercentage": "60%",
    "attackPercentage": "70%",
    "abilityPercentage": "50%",
    "difficultyPercentage": "70%",
    "skins": [
        {
            "skinName": "永昼",
            "skinImg": "https://game.gtimg.cn/images/yxzj/img201606/heroimg/536/536-smallskin-2.jpg"
        },
        ...
    ],
    "emblems": [
        {
            "emblemName": "异变",
            "emblemDescription": "物理攻击力+2 物理穿透+3.6",
            "emblemImg": "//game.gtimg.cn/images/yxzj/img201606/mingwen/1504.png"
        },
        ...
    ],
    "emblemTips": "提高生存能力，团战中迅捷突进，游走自由",
    "bestPartners": {
        "不知火舞": {
            "name": "不知火舞",
            "thumbnail": "https://game.gtimg.cn/images/yxzj/img201606/heroimg/157/157.jpg",
            "description": "提供控制和坦度，为夏洛特的技能增大命中概率并提供有效承伤",
            "url": "https://pvp.qq.com/web201605/herodetail/157.shtml"
        },
        ...
    },
    "suppressingHeroes": {
        "老夫子": {
            "name": "老夫子",
            "thumbnail": "https://game.gtimg.cn/images/yxzj/img201606/heroimg/139/139.jpg",
            "description": "缺乏爆发性输出，攻速下降对于依赖普攻的老夫子来说也非常致命",
            "url": "https://pvp.qq.com/web201605/herodetail/139.shtml"
        },
        ...
    },
    "suppressedHeroes": {
        "公孙离": {
            "name": "公孙离",
            "thumbnail": "https://game.gtimg.cn/images/yxzj/img201606/heroimg/199/199.jpg",
            "description": "灵活性极佳的公孙离可以极大的降低夏洛特技能的命中率，削弱她在战场上的能力",
            "url": "https://pvp.qq.com/web201605/herodetail/199.shtml"
        },
        ...
    },
    "url": "https://pvp.qq.com/web201605/herodetail/xialuote.shtml"
}
```

## Run Locally

To build the API yourself, follow the steps below:

Clone the project

```bash
git clone https://github.com/qing762/honor-of-kings-api
```

Go to the project directory

```bash
cd honor-of-kings-api
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the code 

```bash
python main.py
```

You should see a `wangzhe.json` file after this, meaning that it is built successfully and you can use the json file as an API for your projects.

## Contributing

Contributions are always welcome!

To contribute, fork this repository and improve it. After that, press the contribute button.

## Feedback / Issues

If you have any feedback or issues using the API, please join the [Discord server](https://qing762.is-a.dev/discord)

## License

[MIT LICENSE](https://choosealicense.com/licenses/mit/)