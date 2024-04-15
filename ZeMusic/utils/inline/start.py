from pyrogram.types import InlineKeyboardButton

import config
from ZeMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="❰ 𝗮𝗱𝗱 𝗺𝗲 𝘁𝗼 𝘆𝗼𝘂𝗿 𝗴𝗿𝗼𝘂𝗽 ❱",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="‹ الأوامر ›", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="‹ 𝗗𝗲𝘃 𝗖𝗼𝘂𝗱𝗿𝗮 ›", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="‹ 𝗖𝗵𝗮𝗻𝗻𝗲𝗹¹ ›", url=config.SUPPORT_CHANNEL),
        ],
        [
         
            InlineKeyboardButton(text="‹ 𝗗𝗲𝘃 𝗖𝗼𝘂𝗱𝗿𝗮 ›", url=f"https://t.me/COUDRA_1"),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="❰ 𝗮𝗱𝗱 𝗺𝗲 𝘁𝗼 𝘆𝗼𝘂𝗿 𝗴𝗿𝗼𝘂𝗽 ❱",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="‹ الأوامر ›", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="‹ 𝗗𝗲𝘃 𝗖𝗼𝘂𝗱𝗿𝗮 ›", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="‹ 𝗖𝗵𝗮𝗻𝗻𝗲𝗹¹ ›", url=config.SUPPORT_CHANNEL),
        ],
        [
         
            InlineKeyboardButton(text="‹ 𝗗𝗲𝘃 𝗖𝗼𝘂𝗱𝗿𝗮 ›", url=f"https://t.me/COUDRA_1"),
        ],
    ]
    return buttons
