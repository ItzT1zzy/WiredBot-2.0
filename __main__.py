import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode

from pymongo.mongo_client import MongoClient

import config
from commands import router

bot = Bot(config.TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()


async def main():
    logging.basicConfig(level=logging.INFO)
    await bot.delete_webhook(True)

    cluster = MongoClient(config.MONGODB_URI)
    db = cluster.tgdb

    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit succesffuly!")
