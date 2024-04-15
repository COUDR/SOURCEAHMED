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
        caption=f"""❰ 𝘁𝗵𝗲 𝗯𝗲𝘀𝘁 𝘀𝗼𝘂𝗿𝗰𝗲 𝗼𝗻 𝘁𝗲𝗹𝗲𝗴𝗿𝗮𝗺 ❱""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "‹ 𝗗𝗲𝘃 𝗖𝗼𝘂𝗱𝗿𝗮 ›", url=f"https://t.me/COUDRA_1"),
                ],[
                    InlineKeyboardButton(
                        "‹ 𝗖𝗵𝗮𝗻𝗻𝗲𝗹¹ ›", url=f"https://t.me/WU_SD"), 
                    InlineKeyboardButton(
                        "‹ 𝗚𝗿𝗼𝘂𝗽² ›", url=f"https://t.me/HB_SW"),
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
        caption=f"""❰ 𝘁𝗵𝗲 𝗯𝗲𝘀𝘁 𝘀𝗼𝘂𝗿𝗰𝗲 𝗼𝗻 𝘁𝗲𝗹𝗲𝗴𝗿𝗮𝗺 ❱""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "‹ 𝗗𝗲𝘃 𝗖𝗼𝘂𝗱𝗿𝗮 ›", url=f"https://t.me/COUDRA_1"),
                ],[
                    InlineKeyboardButton(
                        "‹ 𝗖𝗵𝗮𝗻𝗻𝗲𝗹¹ ›", url=f"https://t.me/WU_SD"), 
                    InlineKeyboardButton(
                        "‹ 𝗚𝗿𝗼𝘂𝗽² ›", url=f"https://t.me/HB_SW"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف البوت لمجموعتك ›", url=f"https://t.me/Sgvshbot?startgroup=true"),
            ]
        ]
         ),
     )
