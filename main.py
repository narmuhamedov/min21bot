
from aiogram import executor
from bot_instanse import dp
from handlers import quiz, text, extra
from handlers import fsmadmin
from database import bot_db

async def on_startup(_):
    bot_db.sql_create()

fsmadmin.register_handlers_fsmadmin(dp)

quiz.register_quiz_handlers(dp)
quiz.register_quiz_call(dp)
extra.register_handlers_extra(dp)
text.register_text_handlers(dp)




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)