from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me
from aiocqhttp.exceptions import Error as CQHttpError

"""cos"""
# xians = on_keyword({"cos"})
matcher=on_keyword({'cos'})

@matcher.handle()
async def xians_r(bot: Bot, event: Event, state: T_State):
    msg = await main()
    try:
        await matcher.send(message=Message(msg))

    except CQHttpError:
        pass


async def main():
    url = "https://yanghanwen.xyz/tu/cos.php"
    resp = requests.get(url).json()
    urls = resp['data']
    xians = f"[CQ:image,file={urls}]"
    return xians

    # await matcher.send("正在爬取cos图片，请稍后……")
    # await matcher.send(MessageSegment.at(id) + xians + "cos！少看点！")
