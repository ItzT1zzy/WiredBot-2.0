from aiogram import Router, F
from aiogram.types import Message
from pymongo.mongo_client import MongoClient

import config

router = Router()
cluster = MongoClient(config.MONGODB_URI)
db = cluster.tgdb.users


@router.message(F.text.lower() == "админ панель 🛡️")
async def admin_panel(message: Message):
    await message.answer("В разработке...")
