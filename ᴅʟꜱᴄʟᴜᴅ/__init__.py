from pyrogram import Client
from pyrogram.methods.utilities import idle
import shutil
from logging import INFO, basicConfig, getLogger
basicConfig(
format="%(levelname)s - %(message)s",
level=INFO)
LOGS = getLogger(__name__)
