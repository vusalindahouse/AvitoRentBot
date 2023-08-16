from callback import *
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import schedule
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from time import sleep
from loader import dp
from bot import *
import callback
from aiogram.utils.callback_data import CallbackData



async def avtovo_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
                if news_dict[k]['метро'] == "Автово":
                    sleep(3)
                    news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                           f"Стоимость: {hbold(v['цена'])} руб\n" \
                           f"Метро : {hbold(v['метро'])} \n" \

                    await bot.send_message(message.chat.id, news, disable_notification=True)



async def akadem_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Академическая":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

            elif news_dict[k]['метро'] == "Академическая":
                  sleep(3)
                  news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                         f"Стоимость: {hbold(v['цена'])} руб\n" \
                         f"Метро : {hbold(v['метро'])} \n" \

                  await bot.send_message(message.chat.id, news, disable_notification=True)


async def admir_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Адмиралтейская":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)

async def baltiy_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Балтийская":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def nevskiy_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Невский проспект":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def buxar_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Бухаресткая":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def vlad_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Владимирская":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def vaska_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Василеостровская":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def volk_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Волковская":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)



async def viborg_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Выборгская":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)



async def gork_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Горьковская":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)



async def graj_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Гражданский проспект":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def gost_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Гостиный двор":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)

async def devat_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Девяткино":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)

async def dost_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Достоевская":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def eliz_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Елизаровская":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def zvezda_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Звёздная":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def zveni_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Звенигородская":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \


                await bot.send_message(message.chat.id, news, disable_notification=True)


async def kirov_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Кировский завод":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def komenda_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Комендантский проспект":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def krest_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Крестовский остров":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def kupcino_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Купчино":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def ladoj_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Ладожская":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def lenin_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Ленинский проспект":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def les_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Лесная":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def liga_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Лиговский проспект":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def lomo_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Ломоносовская":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def mayak_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Маяковская":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def mejdu_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Международная":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def moscow_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Московская":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def mosc_gate_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Московские ворота":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def narv_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Нарвская":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)

async def novo_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Новочеркасская":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)



async def obvod_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Обводный канал":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)



async def obux_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Обухово":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)



async def ozerki_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Озерки":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def pp_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Парк Победы":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)

async def parnas_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Парнас":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)

async def petro_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Петроградская":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def pioner_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Пионерская":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def pan_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Площадь Александра Невского I":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def pv_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Площадь Восстания":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \


                await bot.send_message(message.chat.id, news, disable_notification=True)


async def pl_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Площадь Ленина":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def pm_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Площадь Мужества":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def polit_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Политехническая":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def primor_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Приморская":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def proletar_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Пролетарская":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def pb_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Проспект Большевиков":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def veteran_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Проспект Ветеранов":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def prosvet_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Проспект Просвещения":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def puskin_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Пушкинская":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def riba_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Рыбацкое":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def sport_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Спортивная":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def sd_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Старая Деревня":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def ti_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Технологический институт":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def udel_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Удельная":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)

async def ud_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Улица Дыбенко":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def sport_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Спортивная":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def frun_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Фрунзенская":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def cr_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Чёрная речка":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def cern_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Чернышевская":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)

async def ckal_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Чкаловская":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


async def electro_all_flats(message: types.Message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)
        for k, v in sorted(news_dict.items()):
            if news_dict[k]['метро'] == "Электросила":
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)





@dp.callback_query_handler()
async def underground_handler(call) -> None:
    if call.data == "avtovo":
        await akadem_all_flats(call.message)
    elif call.data == "akademiceskaya":
        await akadem_all_flats(call.message)
    elif call.data == "vaska":
        await vaska_all_flats(call.message)
    elif call.data == "admiralteyskaya":
        await admir_all_flats(call.message)
    elif call.data == "baltiyskaya":
        await baltiy_all_flats(call.message)
    elif call.data == "buxarestkaya":
        await buxar_all_flats(call.message)
    elif call.data == "vladimir":
        await vlad_all_flats(call.message)
    elif call.data == "viborg":
        await viborg_all_flats(call.message)
    elif call.data == "gork":
        await gork_all_flats(call.message)
    elif call.data == "gost_dvor":
        await gost_all_flats(call.message)
    elif call.data == "grajdan":
        await graj_all_flats(call.message)
    elif call.data == "devat":
        await devat_all_flats(call.message)
    elif call.data == "dost":
        await dost_all_flats(call.message)
    elif call.data == "elizar":
        await eliz_all_flats(call.message)
    elif call.data == "zvezdnaya":
        await zvezda_all_flats(call.message)
    elif call.data == "nevskiy":
        await nevskiy_all_flats(call.message)
    elif call.data == "zveni":
        await zveni_all_flats(call.message)
    elif call.data == "narv":
        await narv_all_flats(call.message)
    elif call.data == "kupcino":
        await kupcino_all_flats(call.message)
    elif call.data == "zveni":
        await zveni_all_flats(call.message)
    elif call.data == "ok":
        await obvod_all_flats(call.message)
    elif call.data == "petro":
        await petro_all_flats(call.message)
    elif call.data == "krest":
        await krest_all_flats(call.message)
    elif call.data == "lenin":
        await lenin_all_flats(call.message)
    elif call.data == "mayak":
        await mayak_all_flats(call.message)
    elif call.data == "kirov":
        await kirov_all_flats(call.message)
    elif call.data == "mej":
        await mejdu_all_flats(call.message)
    elif call.data == "komenda":
        await komenda_all_flats(call.message)
    elif call.data == "obux":
        await obux_all_flats(call.message)
    elif call.data == "pioner":
        await pioner_all_flats(call.message)
    elif call.data == "parnas":
        await parnas_all_flats(call.message)
    elif call.data == "lomo":
        await lomo_all_flats(call.message)
    elif call.data == "lado":
        await ladoj_all_flats(call.message)
    elif call.data == "les":
        await les_all_flats(call.message)
    elif call.data == "novo":
        await novo_all_flats(call.message)
    elif call.data == "ozerki":
        await ozerki_all_flats(call.message)
    elif call.data == "pb":
        await pb_all_flats(call.message)
    elif call.data == "moscow":
        await moscow_all_flats(call.message)
    elif call.data == "mosc_gate":
        await mosc_gate_all_flats(call.message)
    elif call.data == "liga":
        await liga_all_flats(call.message)
    elif call.data == "pan":
        await pan_all_flats(call.message)
    elif call.data == "pv":
        await pv_all_flats(call.message)
    elif call.data == "pl":
        await pl_all_flats(call.message)
    elif call.data == "pm":
        await pm_all_flats(call.message)
    elif call.data == "pol":
        await polit_all_flats(call.message)
    elif call.data == "prim":
        await primor_all_flats(call.message)
    elif call.data == "proletar":
        await proletar_all_flats(call.message)
    elif call.data == "pros_bol":
        await pb_all_flats(call.message)
    elif call.data == "vet":
        await veteran_all_flats(call.message)
    elif call.data == "pp":
        await pp_all_flats(call.message)
    elif call.data == "riba":
        await riba_all_flats(call.message)
    elif call.data == "saport":
        await sport_all_flats(call.message)
    elif call.data == "sd":
        await sd_all_flats(call.message)
    elif call.data == "ti":
        await ti_all_flats(call.message)
    elif call.data == "udel":
        await udel_all_flats(call.message)
    elif call.data == "ud":
        await ud_all_flats(call.message)
    elif call.data == "frun":
        await frun_all_flats(call.message)
    elif call.data == "cr":
        await cr_all_flats(call.message)
    elif call.data == "electro":
        await electro_all_flats(call.message)
    elif call.data == "chkal":
        await ckal_all_flats(call.message)
    elif call.data == "cher":
        await cr_all_flats(call.message)
    elif call.data == "right_arrow":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup2)
    elif call.data == "left_arrow":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)
    elif call.data == "right_arrow2":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup3)
    elif call.data == "left_arrow2":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup2)
    elif call.data == "right_arrow3":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup4)
    elif call.data == "left_arrow3":
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup3)

