from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me
from aiocqhttp.exceptions import Error as CQHttpError

sheying = on_keyword({'随机摄影'})


@sheying.handle()
async def main(bot: Bot, event: Event, state: T_State):
    msg = await downloads()
    try:
        await sheying.send(message=Message(msg))
    except CQHttpError:
        pass


async def downloads():

    url = "https://yanghanwen.xyz/tu/ren.php"
    resp = requests.get(url).json()
    url_ing = resp['data']
    xians = f"[CQ:image,file={url_ing}]"
    return xians

    # await xians.send("正在爬取图片，请稍后……")
    # await xians.send(MessageSegment.at(id) + xians + "精选摄影")