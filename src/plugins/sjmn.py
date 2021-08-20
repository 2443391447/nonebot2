from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me
from aiocqhttp.exceptions import Error as CQHttpError

sjmn = on_keyword({'美女'})

@sjmn.handle()
async def main(bot: Bot, event: Event, state: T_State):
    msg = await downloads()
    try:
        await sjmn.send(message=Message(msg))
    except CQHttpError:
        pass


async def downloads():
    xians = f"[CQ:image,file=https://api.iyk0.com/sjmn/]"
    return xians

    # await sjmn.send("正在爬取图片，请稍后……")
    # await sjmn.send(MessageSegment.at(id) + xians + "美女图片，少看点！")