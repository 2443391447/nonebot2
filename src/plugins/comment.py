from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests, json
from nonebot.permission import *
from nonebot.rule import to_me

# def comment_comment():
#     url = "https://api.iyk0.com/wyy"
#     resp = requests.get(url)
#     r = resp.text
#     x = json.loads(r)
#     song = x['data']['song']
#     url_1 = x['data']['url']
#     content = x['data']['content']
#     # print(song, url_1, content)

comment = on_keyword({'网易云评论'})

@comment.handle()
async def comment_1(bot: Bot, event: Event, state: T_State):
    url = "https://api.iyk0.com/wyy"
    resp = requests.get(url)
    r = resp.text
    x = json.loads(r)
    song = x['data']['song']
    url_1 = x['data']['url']
    content = x['data']['content']
    # print(song, url_1, content)
    # id = str(event.get_user_id())
    tu = str('歌曲名：' + song + '\n' + '歌曲网址：' + url_1 + '\n' + '评论：' + content)
    await comment.send("正在爬取评论中，请稍后……")
    await comment.send(tu)



