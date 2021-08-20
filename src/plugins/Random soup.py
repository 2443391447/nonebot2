from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests, json
from nonebot.permission import *
from nonebot.rule import to_me


soup = on_keyword({'随机毒汤'})

@soup.handle()
async def main(bot: Bot, event: Event, state: T_State):
    url = "https://api.iyk0.com/du"
    resp = requests.get(url)
    r = resp.text
    x = json.loads(r)
    data = x['data']
    await soup.send("正在爬取中，请稍后……")
    await soup.send(data)