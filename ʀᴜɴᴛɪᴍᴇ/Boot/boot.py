from pyrogram import Client as ɦʏքɛʋօɨɖֆօʊʟ, filters
from pyrogram import StopPropagation
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message
)
from ᴅᴍᴇʀᴇ import *

@ɦʏքɛʋօɨɖֆօʊʟ.on_message(
filters.command(
"start",
prefixes="/")) 
async def starts(
    self,
    ytrgx: Message):
    JoinButtlock = InlineKeyboardMarkup([
        [InlineKeyboardButton(
          "☕️『 𝐆𝐫𝐨𝐮𝐩 』",
          url="https://t.me/hypevoids")],
        [InlineKeyboardButton(
          "⛱『 𝐖𝐚𝐥𝐥𝐩𝐚𝐩𝐞𝐫𝐬 』",
          url="https://t.me/vrtxwalls")],
        [InlineKeyboardButton(
          "🍺『 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 』👓",
          url="https://t.me/hypevoidlab")],
        ])
    await ytrgx.reply_photo(
    "https://telegra.ph/file/2752e78446fe4e63a7182.jpg",
    reply_markup=JoinButtlock,
    caption=f"""
📌I Am 𝗦𝗼𝘂𝗻𝗱𝗖𝗹𝗼𝘂𝗱 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗿 that can take any 𝗦𝗼𝘂𝗻𝗱𝗖𝗹𝗼𝘂𝗱 link and send you its music in mere seconds.
📌Just send me the 𝗦𝗼𝘂𝗻𝗱𝗖𝗹𝗼𝘂𝗱 Link and wait.


📜 LICΣПSΣ
- 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝗦𝗼𝘂𝗻𝗱𝗖𝗹𝗼𝘂𝗱 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗿 𝘪𝘴 𝘭𝘪𝘤𝘦𝘯𝘴𝘦𝘥 𝘶𝘯𝘥𝘦𝘳 𝘵𝘩𝘦 
[𝘎𝘕𝘜 𝘎𝘦𝘯𝘦𝘳𝘢𝘭 𝘗𝘶𝘣𝘭𝘪𝘤 𝘓𝘪𝘤𝘦𝘯𝘴𝘦 𝘷3.0](https://github.com/HypeVoidSoul/Telegram-SoundCloud-Downloader/blob/Vrtx/LICENSE)

DΣV MΣNƬIӨN:
    @HYPEVOIDSOUL
一═デ🟠𝗦𝗼𝘂𝗻𝗱𝗖𝗹𝗼𝘂𝗱 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗿🟠デ═一""")
    return StopPropagation
