import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

#          
                
@app.on_message(filters.command(["جودزلا ","المبرمج جودزلا ","مبرمج السورس","المطور"],"")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/8c6b3160f70e64270e880.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[ْ𓌹𝚂𝙾𝚄𝚁𝙲𝙴 𝙶𝙾𝙳𝚉𝙸𝙻𝙻𝙰𓌺](https://t.me/G1_d_U)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @G1_d_U ❫
◉ 𝙸𝙳      : ❪ `6910087582` ❫
◉ 𝙱𝙸𝙾    : ❪ for me (@El_Godzy)  ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ْ𓌹𝚂𝙾𝚄𝚁𝙲𝙴 𝙶𝙾𝙳𝚉𝙸𝙻𝙻𝙰𓌺", url=f"https://t.me/G1_d_U"), 
                 ],[
                   InlineKeyboardButton(
                        "𓌹𝚂𝙾𝚄𝚁𝙲𝙴 𝙶𝙾𝙳𝚉𝙸𝙻𝙻𝙰𓌺", url=f"https://t.me/G1_d_U"),
                ],

            ]

        ),

    )
