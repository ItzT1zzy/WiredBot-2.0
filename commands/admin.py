from aiogram import Router, Bot
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from pymongo.mongo_client import MongoClient

import config

bot = Bot(config.TOKEN, parse_mode=ParseMode.HTML)
router = Router()
cluster = MongoClient(config.MONGODB_URI)
db = cluster.tgdb.users


@router.message(Command(commands=["bc"]))
async def broadcast_command(message: Message):
    msg = "Тестовое сообщение рассылки"
    users = db.find()
    if message.from_user.id in config.ADMIN_ID:
        for user in users:
            if not user.get("news", False):
                continue
            await bot.send_message(chat_id=user["_id"], text=msg)
    else:
        await message.answer("У вас нет прав для выполнения этого действия.")


@router.message(Command(commands=["list"]))
async def list_command(message: Message):
    if message.from_user.id in config.ADMIN_ID:
        users = db.find()
        user_list = ""
        for user in users:
            user_id = user['_id']
            user_name = user.get('name', 'Неизвестно')
            user_balance = user.get('bal', 'Неизвестно')
            user_friends = user.get('friends', 'Неизвестно')
            user_role = user.get('role', 'Неизвестно')
            user_news = user.get('news', 'Неизвестно')

            user_info = (f"<b>Имя:</b> {user_name}:\n"
                         f"  • <b>ID:</b> {user_id}\n"
                         f"  • <b>Баланс:</b> {user_balance}\n"
                         f"  • <b>Друзья:</b> {user_friends}\n"
                         f"  • <b>Роль:</b> {user_role}\n"
                         f"  • <b>Рассылка:</b> {user_news}\n\n")
            user_list += user_info
        await message.answer(f"<strong>Список пользователей:</strong>\n{user_list}")
    else:
        await message.answer("У вас нет прав для выполнения этого действия.")
