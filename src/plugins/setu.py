from nonebot.adapters.cqhttp import Message
from nonebot import on_keyword, on_notice, on_command
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
import requests, re
from aiocqhttp.exceptions import Error as CQHttpError
from nonebot.adapters.cqhttp import message, GroupMessageEvent, Message, MessageEvent
from nonebot.typing import T_State
from nonebot.permission import SUPERUSER
from nonebot.rule import Rule


tp = on_command('setu',priority=25,rule=Rule())


@tp.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    if args:
        state["iamge"] = args


@tp.got("iamge", prompt="什么类型图片？")
async def handle_city(bot: Bot, event: Event, state: T_State):
    msg = state["iamge"]
    if '黑丝' in str(msg):
        url = "https://api.lolicon.app/setu/v2?tag=黑丝"
        da = requests.get(url).text
        ur = re.findall(r'{"original":"(.+?)"}}]}', da)
        s1 = ur[0]
        tu = f"[CQ:image,file={s1}]"
    elif '白丝' in str(msg):
        url = "https://api.lolicon.app/setu/v2?tag=白丝"
        da = requests.get(url).text
        ur = re.findall(r'{"original":"(.+?)"}}]}', da)
        s2 = ur[0]
        tu = f"[CQ:image,file={s2}]"
    elif '萝莉' in str(msg):
        url = "https://api.lolicon.app/setu/v2?tag=萝莉"
        da = requests.get(url).text
        ur = re.findall(r'{"original":"(.+?)"}}]}', da)
        s3 = ur[0]
        tu = f"[CQ:image,file={s3}]"
    else:
        tu='没有找到'

    try:
        await tp.send(Message(tu))
    except CQHttpError:
        await tp.send('没有找到')
        pass
