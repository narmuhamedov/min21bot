from aiogram import types, Dispatcher
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from bot_instanse import dp, bot
from parser_app import tv_show
from database  import bot_db

#quiz v1
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


#Викторина с картинками

async def game_start(message: types.Message):
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


#for parser
async def parser_manas_film(message: types.Message):
    data = tv_show.parser()
    for i in data:
        await bot.send_message(message.chat.id, i)
    #await bot.send_message(message.chat.id, data)


#Для вызова просмотра из бд результаты
async def show_min_command(message: types.Message):
    await bot_db.sql_command_select(message)

def register_quiz_handlers(dp: Dispatcher):
    dp.register_message_handler(quiz1, commands=['quiz'])
    dp.register_message_handler(game_start, commands=['game'])
    dp.register_message_handler(parser_manas_film, commands=['parser'])
    dp.register_message_handler(show_min_command, commands=['show_all'])


def register_quiz_call(dp: Dispatcher):
    dp.register_callback_query_handler(game_1,lambda func: func.data == 'button_call_1')
