##|𐇮 𝑴𝑶𝑫𝒀 𖠮🚸𖠮 آلـۘهہؚيـٰـ‌ُـُ໋۠بـ໋ۘ۠ه 𐇮☬, [23/12/44 03:32 ص]
##|𐇮 𝑴𝑶𝑫𝒀 𖠮🚸𖠮 آلـۘهہؚيـٰـ‌ُـُ໋۠بـ໋ۘ۠ه 𐇮☬, [23/12/44 03:32 ص]
##|𐇮 𝑴𝑶𝑫𝒀 𖠮🚸𖠮 آلـۘهہؚيـٰـ‌ُـُ໋۠بـ໋ۘ۠ه 𐇮☬, [23/12/44 03:32 ص]

import asyncio
from config import OWNER_ID
from pyrogram import Client, filters
from ZeMusic import app
import random
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode, ChatMemberStatus

#       #             #  #####  #####      ####
#        #  كود الرتبه الوهميه برمجة ##|𐇮 𝑴𝑶𝑫𝒀 𖠮🚸𖠮 آلـۘهہؚيـٰـ‌ُـُ໋۠بـ໋ۘ۠ه 𐇮☬, [23/12/44 03:32 ص]         #  #         #            #     #
#          #        #  #####  #            #####    
#           #    #    #          #     ##   #     #
#              #      #####   ######   #     #

iddof = []

@app.on_message(filters.command(["المالك", "صاحب الخرابه", "المنشي"], ""), group=95)
async def ownner(client: Client, message: Message):
    x = []
    async for m in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
         if m.status == ChatMemberStatus.OWNER:
            x.append(m.user.id)
    if len(x) != 0:        
       m = await app.get_users(int(x[0]))
       if m.photo:
         async for photo in app.get_chat_photos(x[0],limit=1):
          await message.reply_photo(photo.file_id,caption=f"**المالك : {m.first_name}\nيوزر :@{m.username}\nايدي ᚐ:`{m.id}`\nشات {message.chat.title}\nايدي شات:`{message.chat.id}`",reply_markup=InlineKeyboardMarkup(
             [              
               [          
                 InlineKeyboardButton(m.first_name, url=f"https://t.me/{m.username}")
               ],             
             ]                 
            )                     
          )
       else:
        await message.reply_text(f"المالك : {m.first_name}\nيوزر :@{m.username}\nايدي ᚐ:`{m.id}`\nشات {message.chat.title}\nايدي شات:`{message.chat.id}`**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(m.first_name, url=f"https://t.me/{m.username}")],]))
    else:
        await message.reply_text("حجي هدا ساب الدنيا و مافيها\n༄")


                

iddof = []
@app.on_message(filters.command(["قفل الايدي", "تعطيل الايدي"], ""), group=509)
async def iddlock(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
      if message.chat.id in iddof:
        return await message.reply_text(" حجي انت تم معطل من قبل\n༄")
      iddof.append(message.chat.id)
      return await message.reply_text(" تم تعطيل الايدي بنجاح\n༄")
   else:
      return await message.reply_text("حجي هذا الامر ليس لك\n༄")

@app.on_message(filters.command(["فتح الايدي", "تفعيل الايدي"], ""), group=678)
async def iddopen(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
      if not message.chat.id in iddof:
        return await message.reply_text(" حجي انت الايدي مفعل من قبل\n༄ ")
      iddof.remove(message.chat.id)
      return await message.reply_text("تم فتح  الايدي بنجاح\n༄")
   else:
      return await message.reply_text("حجي هذا الامر ليس لك\n༄")




@app.on_message(filters.command(["ايدي","الايدي","ا"], ""), group=99)
async def iddd(client, message):
    if message.chat.id in iddof:
      return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"""✧ ɴᴀᴍᴇ : {message.from_user.mention}\n✧ ᴜsᴇʀ :  @{message.from_user.username}\n✧ ɪᴅ :{message.from_user.id}\n✧ ʙᴀʏᴜ : {usr.bio}\n✧ ɢʀᴏᴜᴘ : {message.chat.title}\n✧ ɪᴅ ɢʀᴏᴜᴘ : {message.chat.id}""", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )    


iddof = []
@app.on_message(
    command(["قفل صورتي","تعطيل صورتي"])
    & filters.group
)
async def lllock(client, message):
    dev = (OWNER_ID)
    ze = (5474971459)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if int(message.from_user.id) == ze:
         rotba= "مبرمج السورس" 

    elif message.from_user.id in dev:
         rotba = "مطور اساسي"
    elif get.status in [ChatMemberStatus.OWNER]:
         rotba = "المالك"

    elif get.status in [ChatMemberStatus.ADMINISTRATOR]:
         rotba = "الادمن"
  
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and  dev:
      if message.chat.id in iddof:
        return await message.reply_text(f"**يا {message.from_user.mention}\n صورتي مقفلها من قبل**")
      iddof.append(message.chat.id)
      return await message.reply_text(f"**تم قفل امر صورتي بنجاح\n\n بواسطة {rotba} ←{message.from_user.mention}**")
    
@app.on_message(
    command(["فتح صورتي","تفعيل صورتي"])
    & filters.group
)
async def idljjopen(client, message):
    dev = (OWNER_ID)
    ze = (5474971459)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if int(message.from_user.id) == ze:
       rotba= "مبرمج السورس"
    elif message.from_user.id in dev:
        rotba = "مطور اساسي"
    elif get.status in [ChatMemberStatus.ADMINISTRATOR]:
        rotba= "أدمن"
    elif get.status in [ChatMemberStatus.OWNER]:
        rotba= "المالك"
    else :
        await message.reply_text(f"**انت لست مشرفا هنا**")   
   
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and  dev:
      if not message.chat.id in iddof:
        return await message.reply_text(f"يا {message.from_user.mention} صورتي مقفلها من قبل")
      iddof.remove(message.chat.id)
      return await message.reply_text(f"**تم تفعيل امر صورتي بنجاح\n\n بواسطة {rotba} ←{message.from_user.mention}**")
 



@app.on_message(
    command(["صورتي"])
    & filters.group
)
async def idjjdd(client, message):
    if message.chat.id in iddof:
      return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    i = ["0","10", "15","20", "25","30","35", "40","45", "50","55", "60"," 66", "70","77", "80","85", "90","99", "100","1000" ]
    ik = random.choice(i)
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"نسبه جمالك يا طرف انت \n│ \n└ʙʏ: {ik} %😂❤️", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )
@app.on_message(
    command(["رتبتي"])
    & filters.group
)
async def rotba(client, message):
    dev = (OWNER_ID)
    ze = (5474971459)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if int(message.from_user.id) == ze:
       rotba= "مبرمج السورس"
    elif message.from_user.id in dev:
        rotba = "مطور اساسي"
    elif get.status in [ChatMemberStatus.ADMINISTRATOR]:
        rotba= "أدمن"
    elif get.status in [ChatMemberStatus.OWNER]:
        rotba= "المالك"
    else:
         rotba = "عضو جميل"
    await message.reply_text(f"رتبتك في هذه المجموعه \nهــي ← «{rotba}»")
       

bio = []

@app.on_message(
    command(["بايو"])
    & filters.group
)
async def idjjdd(client, message:Message):
    if message.chat.id in bio:
      return
    usr = await client.get_chat(message.from_user.id)
    await message.reply_text(f"**البايو هو\n│ \n└ʙʏ: {usr.bio}**")
