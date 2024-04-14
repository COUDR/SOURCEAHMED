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
                
@app.on_message(filters.command(["كودرا ","المبرمج كودرا ","مبرمج السورس","المطور"],"")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/d313f089ede761bbad70a.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[ْ𝘀𝗼𝘂𝗿𝗰𝗲✘𝗰𝗼𝘂𝗱𝗿𝗮](https://t.me/G1_d_U)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @COUDRA_1 ❫
◉ 𝙸𝙳      : ❪ `5474971459` ❫
◉ 𝙱𝙸𝙾    : ❪ for me (@WU_SD)  ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ 𝘀𝗼𝘂𝗿𝗰𝗲✘𝗰𝗼𝘂𝗱𝗿𝗮 ›", url=f"https://t.me/WU_SD"), 
                 ],[
                   InlineKeyboardButton(
                        "‹ 𝘀𝗼𝘂𝗿𝗰𝗲✘𝗰𝗼𝘂𝗱𝗿𝗮 ›", url=f"https://t.me/WU_SD"),
                ],

            ]

        ),

    )
