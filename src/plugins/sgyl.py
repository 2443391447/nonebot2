from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me

sgyl = on_keyword({'伤感语录'})

@sgyl.handle()
async def main(bot: Bot, event: Event, state: T_State):
    url = "https://api.iyk0.com/sg"
    resp = requests.get(url)
    txt = resp.text
    await sgyl.send("正在爬取伤感语录，请稍后……")
    await sgyl.send(txt)