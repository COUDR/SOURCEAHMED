from pyrogram.types import InlineKeyboardButton

import config
from ZeMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="✧ 𝗮𝗗𝗗 𝗠𝗲 𝗧𝗼 َ𝗬𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽𝘀 ✧",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="✧ 𝗛𝗮𝗜𝗽 ✧", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="✧ 𝗕𝗼𝗧 𝗢𝗪𝗡𝗘𝗥 ✧", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="✧ 𝗦𝗼𝗨𝗥𝗖𝗲 ✧", url=config.SUPPORT_CHANNEL),
        ],
        [
         
            InlineKeyboardButton(text="✧ 𝗗𝗲𝘃 𝗦𝗼𝘂𝗿𝗰𝗲 ✧", url=f"https://t.me/COUDRA_1"),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="✧ 𝗮𝗗𝗗 𝗠𝗲 𝗧𝗼 َ𝗬𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽𝘀 ✧",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="✧ 𝗛𝗮𝗜𝗽 ✧", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="✧ 𝗕𝗼𝗧 𝗢𝗪𝗡𝗘𝗥 ✧", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="✧ 𝗦𝗼𝗨𝗥𝗖𝗲 ✧", url=config.SUPPORT_CHANNEL),
        ],
        [
         
            InlineKeyboardButton(text="✧ 𝗗𝗲𝘃 𝗦𝗼𝘂𝗿𝗰𝗲 ✧", url=f"https://t.me/COUDRA_1"),
        ],
    ]
    return buttons
