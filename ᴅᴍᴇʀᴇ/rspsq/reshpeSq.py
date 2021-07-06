from PIL import Image
from ᴅᴍᴇʀᴇ.rp import *

def reshpSq(thumbnail, output):
    nonreshpedSQ = Image.open(thumbnail)
    reshpedSQ = reshp(nonreshpedSQ)
    reshpedSQ.thumbnail((
    320,320),Image.LANCZOS)
    reshpedSQ.save(output)

def reshpSq(thumbnail, output):
    nonreshpedSQQ = Image.open(thumbnail)
    nonreshpedSQQ.save(output)