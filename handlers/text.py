from aiogram import types, Dispatcher
from keyboards.keyboard import keyboard_stat
from bot_instanse import dp, bot


async def dice_echo_and_ban_and_pin(message: types.Message):
    if message.text.lower() == 'dice':
        await bot.send_dice(message.chat.id, emoji='🎲')
    elif message.text.startswith('pin'):
        await bot.pin_chat_message(message.chat.id, message.message_id)

    ban_world = ['java', 'slut', 'bitch', 'niga', 'python is bad']
    for i in ban_world:
        if i.replace(" ", '') in message.text.lower().replace(" ", ""):
            await message.delete()
            await bot.send_message(message.chat.id, "Бот удалил сообщение за "
                                                    "ненормативную лексику!")

    # else:
    #     await message.answer(message.text)




# #Для вывода эхо сообщений
# @dp.message_handler()
# async def echo_message(message: types.Message):
#     await message.answer(message.text)
# #приветствие по никнеймуx

async def hello(message: types.Message):
    await bot.send_message(message.chat.id,
                           f'Hello my Master: {message.from_user.full_name}',
                           reply_markup=keyboard_stat)


def register_text_handlers(dp: Dispatcher):
    dp.register_message_handler(dice_echo_and_ban_and_pin, content_types=['text'])
    dp.register_message_handler(hello, commands=['start'])