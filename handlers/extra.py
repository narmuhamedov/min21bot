from aiogram import types, Dispatcher
from bot_instanse import bot

async def secret_word1(message: types.Message):
    await message.reply('Привет Все хорошо как у тебя?')

async def secret_word2(message: types.Message):
    await message.reply('я сижу на паре а ты??')


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(secret_word1, lambda word: "бот" in word.text)
    dp.register_message_handler(secret_word2, lambda word: 'отлично' in word.text)