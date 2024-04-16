import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["كودرا"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/09b8ec504336aada15ab7.png",
        caption=f"""✧ 𝗧𝗵𝗲 𝗕𝗲𝗦𝘁 𝗦𝗼𝗨𝗥𝗰𝗲 𝗢𝗻 𝗧𝗲𝗟𝗲𝗚𝗿𝗔𝗺 ✧""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "✧ 𝗗𝗲𝘃 𝗦𝗼𝘂𝗿𝗰𝗲 ✧", url=f"https://t.me/COUDRA_1"),
                ],[
                    InlineKeyboardButton(
                        "✧ 𝗦𝗼𝗨𝗥𝗖𝗲 ✧", url=f"https://t.me/WU_SD"), 
                    InlineKeyboardButton(
                        "✧ 𝗚𝗿𝗼𝘂𝗽 ✧", url=f"https://t.me/HB_SW"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف البوت لمجموعتك ›", url=f"https://t.me/Sgvshbot?startgroup=true"),
            ]
        ]
         ),
     )
  
@app.on_message(
    command(["سورس","‹ السورس ›","كودرا","السورس","كودرا"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/09b8ec504336aada15ab7.png",
        caption=f"""✧ 𝗧𝗵𝗲 𝗕𝗲𝗦𝘁 𝗦𝗼𝗨𝗥𝗰𝗲 𝗢𝗻 𝗧𝗲𝗟𝗲𝗚𝗿𝗔𝗺 ✧""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "✧ 𝗗𝗲𝘃 𝗦𝗼𝘂𝗿𝗰𝗲 ✧", url=f"https://t.me/COUDRA_1"),
                ],[
                    InlineKeyboardButton(
                        "✧ 𝗦𝗼𝗨𝗥𝗖𝗲 ✧", url=f"https://t.me/WU_SD"), 
                    InlineKeyboardButton(
                        "✧ 𝗚𝗿𝗼𝘂𝗽 ✧", url=f"https://t.me/HB_SW"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف البوت لمجموعتك ›", url=f"https://t.me/Sgvshbot?startgroup=true"),
            ]
        ]
         ),
     )
