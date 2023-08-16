from callback import *
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import schedule
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from time import sleep
from loader import dp
import callback
import callback_underground
from callback_underground import *
from aiogram.utils.callback_data import CallbackData
from markups import *


"""Меню, которое поялвяется после команды 'start' """
def get_keyboard() -> ReplyKeyboardMarkup:
    start_button = ["1-комнатные", "2-комнатные", "3-комнатные", "квартира-студия", "метро"]
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(*start_button)
    return kb


@dp.message_handler(commands='start')
async def start(message: types.Message) -> None:
    await message.answer('Выберите тип квартиры',
                         reply_markup=get_keyboard())


@dp.message_handler(commands='stop')
async def stop(message: types.Message):
    await message.answer('Выберите тип квартиры',
                        reply_markup=get_keyboard())
    callback.schedule_state = False
    print("Job Is Canceled")
    return schedule.CancelJob

@dp.message_handler(Text(equals="1-комнатные"))
async def start_parsing(message: types.Message):
    all_flats = KeyboardButton('Показать все однокомнатные квартиры')
    new_flats = KeyboardButton('Отправлять только новые однокомнатные квартиры')

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(all_flats, new_flats)

    await message.answer('Выберите способ получения новых предложений', reply_markup=markup)


@dp.message_handler(Text(equals="2-комнатные"))
async def start_parsing(message: types.Message):
    all_flats = KeyboardButton('Показать все двухкомнатные квартиры')
    new_flats = KeyboardButton('Отправлять только новые двухкомнатные квартиры')

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(all_flats, new_flats)

    await message.answer('Выберите способ получения новых предложений', reply_markup=markup)


@dp.message_handler(Text(equals="3-комнатные"))
async def start_parsing(message: types.Message):
    all_flats = KeyboardButton('Показать все трекхомнатные квартиры')
    new_flats = KeyboardButton('Отправлять только новые трехкомнатые квартиры')

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(all_flats, new_flats)

    await message.answer('Выберите способ получения новых предложений', reply_markup=markup)


@dp.message_handler(Text(equals="квартира-студия"))
async def start_parsing(message: types.Message):
    all_flats = KeyboardButton('Показать все квартиры-студии')
    new_flats = KeyboardButton('Отправлять только новые квартиры-студии')

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(all_flats, new_flats)

    await message.answer('Выберите способ получения новых предложений', reply_markup=markup)





@dp.message_handler(Text(equals="метро"))
async def inline_keyboard(message: types.Message):
    await message.answer(
        'Спиксок метростанций', reply_markup=markup)




@dp.message_handler()
async def sending_method(message: types.Message):
    user_msg = message.text
    if user_msg == 'Отправлять только новые однокомнатные квартиры':
        callback.schedule_state = True
        await one_appartment(message)
    elif user_msg == 'Показать все однокомнатные квартиры':
        callback.schedule_state = True
        await all_news_one_room(message)
    if user_msg == 'Отправлять только новые двухкомнатные квартиры':
        callback.schedule_state = True
        await two_rooms(message)
    elif user_msg == 'Показать все двухкомнатные квартиры':
        callback.schedule_state = True
        await all_news_two_rooms(message)
    if user_msg == 'Отправлять только новые трехкомнатые квартиры':
        callback.schedule_state = True
        await three_rooms(message)
    elif user_msg == 'Показать все трекхомнатные квартиры':
        callback.schedule_state = True
        await all_news_three_rooms(message)
    if user_msg == 'Отправлять только новые квартиры-студии':
        callback.schedule_state = True
        await studio_appartment(message)
    elif user_msg == 'Показать все квартиры-студии':
        callback.schedule_state = True
        await all_news_studio(message)



if __name__ == '__main__':
    executor.start_polling(dp)

    """Запуск функций по парсингу каждые 5 минут"""
    schedule.every(5).minutes.do(one_room_flats)
    schedule.every(5).minutes.do(two_room_flats)
    schedule.every(5).minutes.do(three_room_flats)
    schedule.every(5).minutes.do(appartment_room_flats)

    while callback.schedule_state:
        schedule.run_pending()
        sleep(1)
