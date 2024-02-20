from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_kb_buttons = [[KeyboardButton(text="Профиль 👤"), KeyboardButton(text="Помощь ❓")],
                    [KeyboardButton(text="Поддержка 🤝"), KeyboardButton(text="Другое 🌟")]]
start_keyboard = ReplyKeyboardMarkup(keyboard=start_kb_buttons, resize_keyboard=True,
                                     input_field_placeholder="Выберите пункт меню")

admin_start_kb_buttons = [[KeyboardButton(text="Профиль 👤"), KeyboardButton(text="Помощь ❓")],
                          [KeyboardButton(text="Поддержка 🤝"), KeyboardButton(text="Другое 🌟")],
                          [KeyboardButton(text="Админ панель 🛡️")]]
admin_start_keyboard = ReplyKeyboardMarkup(keyboard=admin_start_kb_buttons, resize_keyboard=True,
                                           input_field_placeholder="Выберите пункт меню")

other_kb_buttons = [[KeyboardButton(text="Настройки ⚙️"), KeyboardButton(text="О нас ℹ️")],
                    [KeyboardButton(text="О создателе 👤"), KeyboardButton(text="Назад 🔙")]]
other_keyboard = ReplyKeyboardMarkup(keyboard=other_kb_buttons, resize_keyboard=True,
                                     input_field_placeholder="Выберите пункт меню")
