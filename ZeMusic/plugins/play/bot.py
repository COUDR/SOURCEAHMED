import asyncio
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters, Client
from ZeMusic import app
from config import OWNER_ID

@txt = [


"ها عايز اي 🙄",
"ايوااا جااااي 😂",
"عاوزني اشقطلك مين يروحي 🥺",
"ايوة قول عاوز اي 🤔",
"قلب البوت 🥺",
"يعم تعبتنا معاك 🙁",
"استنا يعم بشقط وجايبك علطول 😂",
"بس يا شخه 😂",
"انت اهطل ياض 😁",
"انا قولت حمار محدش صدقني 😎",
"احا في اي 🤬",
"است طيب 😏",

        ]


        


@app.on_message(filters.command(["بوت","يا بوت"], ""), group=1442)

async def khyrok(client: Client, message: Message):

      a = random.choice(txt)

      await message.reply(

        f"{a}")
