from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from aiocqhttp.exceptions import Error as CQHttpError

anime = on_keyword({'动漫'})

@anime.handle()
async def downloads(bot: Bot, event: Event, state: T_State):
    msg = await downloads_page()
    try:
        await anime.send(message=Message(msg))

    except CQHttpError:
        pass

async def downloads_page():
    url = "https://yanghanwen.xyz/tu/dong.php"
    resp = requests.get(url).json()
    img = resp['data']
    xians = f"[CQ:image,file={img}]"
    # xians_2 = "天天看这个，是不是肾虚？"
    return xians


    # await anime.send("正在爬取图片，请稍后……")
    # await anime.send(MessageSegment.at(id) + xians + "天天看这个，是不是肾虚!")