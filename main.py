from aiogram import executor
from bot_instanse import dp
from handlers import quiz, text

quiz.register_quiz_handlers(dp)
quiz.register_quiz_call(dp)
text.register_text_handlers(dp)



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)