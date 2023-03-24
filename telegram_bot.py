# Код телеграмм бота:

import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'Ваш токен' #токен бота от @BotFather

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
   await message.reply('Start')

@dp.message_handler(commands=['help'])
async def echo(message: types.Message):
   await message.reply('Вы обратились к справке бота')

if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)

# Дата вебинара: 24.03.2023
# Преподаватель: Дуплей Максим Игоревич