import time
from contextlib import suppress

from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.types import KeyboardButton
from pymongo.errors import DuplicateKeyError
from pymongo.mongo_client import MongoClient

import config
from keyboards.reply import start_keyboard, admin_start_keyboard

router = Router()
cluster = MongoClient(config.MONGODB_URI)
db = cluster.tgdb


@router.message(CommandStart())
async def start(message: types.Message):
    with suppress(DuplicateKeyError):
        db.users.insert_one(
            dict(
                _id=message.from_user.id,
                name=str(message.from_user.full_name),
                bal=300,
                friends=0,
                role="Пользователь",
                news=True
            )
        )
    if message.from_user.id in config.ADMIN_ID:
        await message.answer_sticker("CAACAgUAAxkBAAELaURlzlWNWIyn-2JVeTecMZ-o9hJY_wAC5gEAApHbgFWkJ7qbgopTnzQE")
        admin_welcome_message = ("👋 Приветствую, уважаемый администратор!\n\n"
                                 "Вы вошли в режим администратора бота WiredBot. Здесь вы можете управлять различными аспектами бота и следить за его работой.\n"
                                 "Не забудьте быть внимательным при внесении изменений в настройки и функционал бота.\n"
                                 "Если у вас есть какие-либо вопросы или предложения, не стесняйтесь обращаться к нам.\n"
                                 "Спасибо за вашу работу и поддержку! 🙏")
        await message.answer(admin_welcome_message, reply_markup=admin_start_keyboard)
    else:
        welcome_message = ("🤖 <b>WiredBot</b> - ваш надежный помощник в мире возможностей! 🚀\n\n"
                           "🎉 Что я могу предложить: \n"
                           "• 👥 <b>Добавление в друзья:</b> Позвольте мне помочь вам расширить ваш круг общения, добавляйте новых друзей и находите единомышленников.\n"
                           "• 👀 <b>Многое другое:</b> Это только начало! Мой функционал постоянно обновляется, и я готов предложить вам еще больше возможностей. 💡\n\n"
                           "🤝 Поддержка и обратная связь: \n"
                           "Если у вас есть вопросы, предложения или проблемы, не стесняйтесь обращаться к нам. Мы всегда готовы помочь вам и улучшить нашего бота для вашего удобства.\nДля связи вы можете написать создателю: @ItzT1zzy.\nА также можете посетить наш телеграм канал: <i>Скоро...</i>\n\n"
                           "Просто воспользуйтесь доступными командами или задайте мне вопрос, и я с удовольствием помогу вам. Вместе мы сделаем ваше время в Telegram более увлекательным и продуктивным! 🌟\n\n"
                           "Не стесняйтесь исследовать, общаться и наслаждаться этим опытом! 🌈\n\n"
                           "Приятного общения! 🚀")
        await message.answer_sticker("CAACAgUAAxkBAAELaURlzlWNWIyn-2JVeTecMZ-o9hJY_wAC5gEAApHbgFWkJ7qbgopTnzQE")
        time.sleep(0.5)
        await message.answer(welcome_message, reply_markup=start_keyboard)
