import random
from aiogram import Bot, Dispatcher, executor, types
import requests
import json

def info_get():
    page=random.randrange(0, 20)
    data = requests.get(f'https://rickandmortyapi.com/api/character?page={page}')
    char_rick = data.json()
    i = int(random.randrange(0, 20))
    data1=(f"стр {page}, номер {i}\nИмя {char_rick['results'][i]['name']}\nВид {char_rick['results'][i]['species']}\nСтатус {char_rick['results'][i]['status']}\nАватар {char_rick['results'][i]['image']}")
    return data1


import logging
from aiogram import Bot, Dispatcher, executor, types
# Объект бота
bot = Bot(token="5335063016:AAGc67oOlL9b72Y97GFmEiZZJqbAQDxBGiA")
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Хэндлер на команду /start
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Следующий"]
    keyboard.add(*buttons)
    await message.answer("Персонажи Rick and Morty?", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Следующий")
async def without_puree(message: types.Message):
    await message.reply(info_get())

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
