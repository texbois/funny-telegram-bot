import sys
import os
import asyncio
from telegram import Bot
from telegram.constants import ParseMode

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _secrets import secrets_bot_token


async def main():
    if len(sys.argv) < 2:
        print("Provide chat ID as a command line argument")
        return

    print(f"Enter a message that will be sent to chat {sys.argv[1]}. Press Ctrl+D to send.")

    message = sys.stdin.read()
    if message != "":
        async with Bot(token=secrets_bot_token) as bot:
            await bot.send_message(chat_id=sys.argv[1], text=message, parse_mode=ParseMode.MARKDOWN)


if __name__ == '__main__':
    asyncio.run(main())
