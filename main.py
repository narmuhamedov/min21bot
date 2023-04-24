import asyncio

from aiogram import executor
from bot_instanse import dp
from handlers import quiz, text, extra
from handlers import fsmadmin, notification
from database import bot_db
from handlers.notification import schleuder


async def on_startup(_):
    asyncio.create_task(schleuder())
    bot_db.sql_create()
    print('Bot online')


fsmadmin.register_handlers_fsmadmin(dp)
quiz.register_quiz_handlers(dp)
quiz.register_quiz_call(dp)
extra.register_handlers_extra(dp)
text.register_text_handlers(dp)
notification.register_handlers_notification(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)