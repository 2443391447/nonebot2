from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me
from aiocqhttp.exceptions import Error as CQHttpError

sjecy = on_keyword({'二次元'})

@sjecy.handle()
async def main(bot: Bot, event: Event, state: T_State):
    msg = await downloads()
    try:
        await sjecy.send(message=Message(msg))
    except CQHttpError:
        pass


async def downloads():
    xians = f"[CQ:image,file=https://api.iyk0.com/ecy/api.php]"
    return xians


    # await sjecy.send("正在爬取二次元图片，请稍后……")
    # await sjecy.send(MessageSegment.at(id) + xians + "二次元图片！少看点！")
