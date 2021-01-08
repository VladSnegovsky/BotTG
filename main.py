from aiogram import Bot, Dispatcher, executor, types
import telebot
import logging

import config

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.API_TG_BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer("Hi!")

@dp.message_handler(content_types=["text"])
async def answered(message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)