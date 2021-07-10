from . import *

GLUU = dict(
    root="ʀᴜɴᴛɪᴍᴇ"
)

Client(
    "ɦʏքɛʋօɨɖֆօʊʟ",
    api_id=AP,
    api_hash=AH,
    bot_token=AB,
    workers=12,
    plugins=GLUU
)
Client.start()
LOGS.info('🍁🎷一═デ🟠𝗦𝗼𝘂𝗻𝗱𝗖𝗹𝗼𝘂𝗱 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗿🟠デ═一\nONLINE🍁🎷\n')
idle()
Client.stop()  
try:
    shutil.rmtree(K)
    shutil.rmtree(P)
    shutil.rmtree(V)
    shutil.rmtree(Y)
    shutil.rmtree(M)
except:
    pass
LOGS.info('🍁⚰️一═デ🟠𝗦𝗼𝘂𝗻𝗱𝗖𝗹𝗼𝘂𝗱 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗿🟠デ═一\nOFFLINE ⚰️🍁\n')
