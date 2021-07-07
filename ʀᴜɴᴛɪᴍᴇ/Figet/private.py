import os
import asyncio
from pyrogram import Client as ɦʏքɛʋօɨɖֆօʊʟ, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message
)
from youtube_dl import YoutubeDL
import ffmpeg
from ᴅᴍᴇʀᴇ import *

SDEX = r"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:|soundcloud\.com|))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$"


@ɦʏքɛʋօɨɖֆօʊʟ.on_message(
filters.private
& filters.regex(SDEX))
async def music_downloader(
    _,
    scund: Message):
    await music_upldr(
    scund)
     
async def music_upldr(
    scund: Message):
    await scund.reply_chat_action(
    "playing")
    try:
        ydlfeeder = {
            'format': 
            'bestaudio',
            'outtmpl': 
            '%(title)s - %(extractor)s-%(id)s.%(ext)s',
            'writethumbnail': 
            True
            }
        ydlopts = YoutubeDL(ydlfeeder)
        VMft = ydlopts.extract_info(
        scund.text,
        download=True)
        if VMft['duration'] > 3600:
            JOIN_BUTTLOCK = InlineKeyboardMarkup([        
        [InlineKeyboardButton(
          "👓『 𝗬𝗼𝘂𝘁𝘂𝗯𝗲 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗿 』👓",
          url="https://t.me/YOUTUBELI_BOT")]])
            push = await scund.reply_photo(
            "https://telegra.ph/file/2752e78446fe4e63a7182.jpg",
            reply_markup=JOIN_BUTTLOCK,
            caption='''
`This won't be downloaded because its audio length is longer than the 2hour which is set by` {CB}
Please consider sending link of song with less then 2hour length


**Dҽʋ Mҽɳƚισɳ:**
    {CB}
一═デ🟠𝗦𝗼𝘂𝗻𝗱𝗖𝗹𝗼𝘂𝗱 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗿🟠デ═一''' )
            await delete_server(
            (push,
            scund),
            15)
            await push.delete()
            return
        d_status = await scund.reply_text(
        "⭕️Fetching Items....",
        quote=True,
        disable_notification=False)
        ydlopts.process_info(VMft)
        audio_file = ydlopts.prepare_filename(VMft)
        task = asyncio.create_task(audio_sender(scund, VMft,
                                                 audio_file))
        await scund.reply_chat_action(
        "record_video")
        await d_status.delete()
        while not task.done():
            await asyncio.sleep(1)
            await scund.reply_chat_action(
            "playing")
        await scund.reply_chat_action(
        "cancel")
        if scund.chat.type == "private":
            await scund.delete()
    except Exception as e:
        await scund.reply_text(repr(e))
        
async def audio_sender(
    scund: Message,
    VMft,
    audio_file):
    basename = audio_file.rsplit(".", 1)[-2]
    if VMft['ext'] == 'webm':
        audio_file_opus = basename + ".opus"
        ffmpeg.input(audio_file).output(audio_file_opus, codec="copy").run()
        os.remove(audio_file)
        audio_file = audio_file_opus
    thumbnail_url = VMft['thumbnail']
    if os.path.isfile(basename + ".jpg"):
        img_room = basename + ".jpg"
    else:
        img_room = basename + "." + \
            file_url(thumbnail_url)
    resized_img = basename + "_reshpedSQ.jpg"
    reshpSq(img_room, resized_img)
    webpage_url = VMft['webpage_url']
    title = VMft['title']
    duration = int(float(VMft['duration']))
    performer = VMft['uploader']
    if os.path.isfile(basename + ".jpg"):
        Simg_room = basename + ".jpg"
    else:
        Simg_room = basename + "." + \
            file_url(thumbnail_url)
    Sresized_img = basename + "_nonreshpedSQQ.jpg"
    reshpSq(Simg_room, Sresized_img)
    void = await scund.reply_photo(
        Sresized_img,
        caption=f'''✨🤩 𝙽𝚒𝚌𝚎 𝚌𝚑𝚘𝚒𝚌𝚎! 
🛒 **𝚈𝚘𝚞𝚛 𝙰𝚞𝚍𝚒𝚘 𝚏𝚒𝚕𝚎 𝚠𝚒𝚕𝚕 𝚋𝚎 𝚑𝚎𝚛𝚎 𝚜𝚑𝚘𝚛𝚝𝚕𝚢**
TITLE: `{title}`
WEBPAGE: {webpage_url}

一═デ🟠𝗦𝗼𝘂𝗻𝗱𝗖𝗹𝗼𝘂𝗱 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗿🟠デ═一
''',
        parse_mode='markdown',
        )
    JOIN_BUTTLOCK = InlineKeyboardMarkup([        
        [InlineKeyboardButton(
          "🟠『 ꜱᴏᴜɴᴅᴄʟᴏᴜᴅ_ᴅʟ 』",          
          url="https://t.me/SOUNDCLOUDLI_BOT")],
        [InlineKeyboardButton(
          "🍺『 ɢʀᴏᴜᴘ 』",          
          url="https://t.me/HYPEVOIDS")],
        [InlineKeyboardButton(
          "🔥『 ᴄʜᴀɴɴᴇʟ 』",          
          url="https://t.me/HYPEVOIDLAB")]        
        ])
    await scund.reply_audio(
        audio_file,
        reply_markup=JOIN_BUTTLOCK,
        caption=bbk,
        title=title,
        performer=performer,
        duration=duration,
        thumb=resized_img
        )
    os.remove(audio_file)
    os.remove(img_room)
    os.remove(resized_img)
    os.remove(Sresized_img)    


CB ='@HYPEVOIDBOT' 
bbk = f"""
ꜰɪʟᴇ ɴᴀᴍᴇ:☝🏻ꜰɪʟᴇ ᴛʏᴘᴇ: 🎧.๓p3
ꜱɪᴛᴇ:[🟠𝗦𝗼𝘂𝗻𝗱𝗖𝗹𝗼𝘂𝗱](https://soundcloud.com)

Dҽʋ Mҽɳƚισɳ:{CB}
一═デ🟠𝗦𝗼𝘂𝗻𝗱𝗖𝗹𝗼𝘂𝗱 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗿🟠デ═一
"""
