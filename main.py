from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import base, InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from decouple import config

TOKEN = config('TOKEN')
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)



#quiz v1
@dp.message_handler(commands=['quiz'])
async def quiz1(message: types.Message):
    question1 = "Зимой и летом одним цветом"
    answer = ['елка', "бабочка", "Дом", "Комп"]
    await bot.send_poll(message.chat.id,
                        question=question1,
                        options=answer,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=0,
                        explanation='Эх ты как ты не угадал детскую загадку',
                        explanation_parse_mode=ParseMode.MARKDOWN_V2
                        )

@dp.message_handler(commands=['game'])
async def game_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton('Next', callback_data='button_call_1')
    markup.add(button_call_1)
    question = 'Кто это?\nВывод: '
    answer = ['Лев', "Тигр", "Пума", "Медведь"]
    image = open("media/5. Белый тигренок.jpg", 'rb')
    await bot.send_photo(message.chat.id, photo=image)
    await bot.send_poll(
        message.chat.id,
        question=question,
        options=answer,
        correct_option_id=1,
        is_anonymous=False,
        type='quiz',
        reply_markup=markup


    )

@dp.callback_query_handler(lambda func: func.data == 'button_call_1')
async def game_1(call: types.CallbackQuery):
    question = 'Кто это?\nВывод: '
    answer = ['Лев', "Тигр", "Пума", "Медведь", "Леопард"]
    image = open("media/3. Леопард.jpg", 'rb')
    await bot.send_photo(call.message.chat.id, photo=image)
    await bot.send_poll(
        call.message.chat.id,
        question=question,
        options=answer,
        correct_option_id=4,
        is_anonymous=False,
        type='quiz'
    )







# #приветствие по никнейму
# @dp.message_handler(commands=['start'])
# async def hello(message: types.Message):
#     await bot.send_message(message.chat.id, f'Hello my Master: {message.from_user.full_name}')


# #Для вывода эхо сообщений
# @dp.message_handler()
# async def echo_message(message: types.Message):
#     await message.answer(message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)