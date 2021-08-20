from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me

sjdz = on_keyword({'随机段子'})

@sjdz.handle()
async def main(bot: Bot, event: Event, state: T_State):
    url = "https://api.iyk0.com/duanzi"
    resp = requests.get(url)
    txt = resp.text
    await sjdz.send("正在爬取随机段子，请稍后……")
    await sjdz.send(txt)