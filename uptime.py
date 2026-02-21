from telegram import Update
from telegram.ext import Updater, CommandHandler
from utils import in_whitelist
import logging
from _secrets import lucky_numbers
import time

logger = logging.getLogger(__name__)
start_time = time.time()

async def uptime(update: Update, context):
    if (not in_whitelist(update)):
        return
    now = time.time()
    diff_seconds = now - start_time
    hours = int(diff_seconds // 3600)
    minutes = int((diff_seconds % 3600) // 60)
    seconds = int((diff_seconds % 3600) % 60)

    message = f"{hours:02}:{minutes:02}:{seconds:02}  {lucky_numbers.get(hours, '')}"

    await update.message.reply_text(message, do_quote=False)


def subscribe(u: Updater):
    u.dispatcher.add_handler(CommandHandler(("uptime"), uptime))