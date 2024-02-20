from aiogram import F, Bot
from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from pymongo.mongo_client import MongoClient

import config
from keyboards import reply

bot = Bot(config.TOKEN, parse_mode=ParseMode.HTML)
router = Router()
cluster = MongoClient(config.MONGODB_URI)
db = cluster.tgdb.users


@router.message(Command(commands=["help"]))
async def help_command(message: Message):
    help_text = ("Я поддерживаю множество команд и функций.\n\n"
                 "Вот некоторые из команд, которые я поддерживаю:\n"
                 "• /start - Начать взаимодействие со мной\n"
                 "• /help - Получить список доступных команд и их описания\n"
                 "• /profile - Ваш профиль\n\n"
                 "Это только начало! Не стесняйтесь исследовать все возможности, которые я предлагаю.\n\n"
                 "Если у вас возникли вопросы или вы нуждаетесь в помощи, обратитесь к разделу поддержки.\n\n"
                 "Список не окончательный и будет обновлться.\n\n"
                 "Удачи и приятного общения! ✨")
    await message.answer(help_text)


@router.message(F.text.lower() == "помощь ❓")
async def help_command(message: Message):
    help_text = ("Я поддерживаю множество команд и функций.\n\n"
                 "Вот некоторые из команд, которые я поддерживаю:\n"
                 "• /start - Начать взаимодействие со мной\n"
                 "• /help - Получить список доступных команд и их описания\n"
                 "• /profile - Ваш профиль\n\n"
                 "Это только начало! Не стесняйтесь исследовать все возможности, которые я предлагаю.\n\n"
                 "Если у вас возникли вопросы или вы нуждаетесь в помощи, обратитесь к разделу поддержки.\n\n"
                 "Список не окончательный и будет обновлться.\n\n"
                 "Удачи и приятного общения! ✨")
    await message.answer(help_text)


@router.message(Command(commands=["profile"]))
async def profile_command(message: Message):
    user = db.find_one({"_id": message.from_user.id})
    user_id = message.from_user.id
    photos = await bot.get_user_profile_photos(user_id=user_id, limit=1)
    if photos.total_count > 0:
        photo = photos.photos[0][-1].file_id
        msg = (f" 🌟 Профиль {message.from_user.full_name} 🌟\n\n"
               f"👤 Имя: {message.from_user.first_name}\n"
               f"🆔 ID: {message.from_user.id}\n"
               f"💰 Баланс: {user['bal']}\n"
               f"👥 Друзья: {user['friends']}\n"
               f"🔖 Роль: {user['role']}")
        await message.answer_photo(photo=photo, caption=msg)
    else:
        msg = (f"<blockquote>У вас нету аватарки</blockquote>\n\n"
               f" 🌟 Профиль {message.from_user.full_name} 🌟\n\n"
               f"👤 Имя: {message.from_user.first_name}\n"
               f"🆔 ID: {message.from_user.id}\n"
               f"💰 Баланс: {user['bal']}\n"
               f"👥 Друзья: {user['friends']}\n"
               f"🔖 Роль: {user['role']}")
        await message.answer(msg)


@router.message(F.text.lower() == "профиль 👤")
async def profile_command(message: Message):
    user = db.find_one({"_id": message.from_user.id})
    user_id = message.from_user.id
    photos = await bot.get_user_profile_photos(user_id=user_id, limit=1)
    if photos.total_count > 0:
        photo = photos.photos[0][-1].file_id
        msg = (f" 🌟 Профиль {message.from_user.full_name} 🌟\n\n"
               f"👤 Имя: {message.from_user.first_name}\n"
               f"🆔 ID: {message.from_user.id}\n"
               f"💰 Баланс: {user['bal']}\n"
               f"👥 Друзья: {user['friends']}\n"
               f"🔖 Роль: {user['role']}")
        await message.answer_photo(photo=photo, caption=msg)
    else:
        msg = (f"<blockquote>У вас нету аватарки</blockquote>\n\n"
               f" 🌟 Профиль {message.from_user.full_name} 🌟\n\n"
               f"👤 Имя: {message.from_user.first_name}\n"
               f"🆔 ID: {message.from_user.id}\n"
               f"💰 Баланс: {user['bal']}\n"
               f"👥 Друзья: {user['friends']}\n"
               f"🔖 Роль: {user['role']}")
        await message.answer(msg)


@router.message(F.text.lower() == "поддержка 🤝")
async def support_command(message: Message):
    await message.answer("В разработке...", quote=True, show_alert=True)


@router.message(F.text.lower() == "другое 🌟")
async def support_command(message: Message):
    await message.answer("Выберите действие", reply_markup=reply.other_keyboard)


@router.message(F.text.lower() == "назад 🔙")
async def support_command(message: Message):
    await message.answer("Выберите действие", reply_markup=reply.start_keyboard)
