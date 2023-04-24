import asyncio
import aioschedule
from aiogram import types, Dispatcher
from bot_instanse import bot

async def alarm(message: types.Message):
    global chat_id
    chat_id = message.chat.id
    if message.text == 'разбуди':
        await message.reply('ОК')

async def wake_up():
    await bot.send_message(chat_id=chat_id, text="Проснись хозяин, а то опоздаешь на работу!")


async def schleuder():
    aioschedule.every().day.at("10:35").do(wake_up)

        # aioschedule.cancel_job(wake_up())
    while 1:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
def register_handlers_notification(db: Dispatcher):
    db.register_message_handler(alarm)