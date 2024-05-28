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
                
@app.on_message(filters.command(["كودرا","المبرمج كودرا","مبرمج السورس","المطور"],"")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/d313f089ede761bbad70a.jpg",
        caption=f"""
        ✧ ɴᴀᴍᴇ : 𝗖َِ𝗢َِ𝗨َِ𝗗َِ𝗥َِ𝗔 
✧ ᴜsᴇʀ :  @COUDRA_1 
✧ ɪᴅ   : 5474971459""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "مـطـور الـبـوت", url=f"https://t.me/COUDRA_1"), 
                 ],[
                   InlineKeyboardButton(
                        "سـورس", url=f"https://t.me/WU_SD"),
                ],

            ]

        ),

    )
