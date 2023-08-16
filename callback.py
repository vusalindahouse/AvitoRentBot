import asyncio
from scrap import one_room_flats, two_room_flats, three_room_flats, appartment_room_flats
from aiogram.utils.markdown import hbold, hlink
import json
from time import sleep
from loader import bot


schedule_state = True

"""Все предложения по однокомнатным квартирам"""


async def all_news_one_room(message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)

    for k, v in sorted(news_dict.items()):
        if schedule_state:
            if k.startswith('1-k'):
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


"""Отправка только нововыствленных однокомнатных квартир"""


async def one_appartment(message):
    while schedule_state:
        fresh_flats = one_room_flats()
        if len(fresh_flats) >= 1:
            for k, v in sorted(fresh_flats.items()):
                sleep(2)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)
        else:
            await bot.send_message(message.chat.id, "Пока нет новых предложений по однакомнатным квартирам. Для остановки загрузки и перехода в основное меню нажмите /stop ",
                                   disable_notification=True)

        await asyncio.sleep(1800)


"""Все предложения по двухкомнатным квартирам"""


async def all_news_two_rooms(message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)

    for k, v in sorted(news_dict.items()):
        if schedule_state:
            if k.startswith('2-k'):
                sleep(2)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


"""Отправка только нововыствленных двухкомнатных квартир"""


async def two_rooms(message):
    while schedule_state:
        fresh_flats = two_room_flats()

        if len(fresh_flats) >= 1:

            for k, v in sorted(fresh_flats.items()):
                sleep(2)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)
        else:
            await bot.send_message(message.chat.id, "Пока нет новых предложений по двухкомнатным квартирам. Для остановки загрузки и перехода в основное меню нажмите /stop ",
                                   disable_notification=True)

        await asyncio.sleep(1800)


"""Все предложения по трехкомнатным квартирам"""


async def all_news_three_rooms(message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)

    for k, v in sorted(news_dict.items()):
        if schedule_state:
            if k.startswith('3-k'):
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


"""Отправка только нововыствленных трехкомнатных квартир"""

async def three_rooms(message):
    while schedule_state:
        fresh_flats = three_room_flats()

        if len(fresh_flats) >= 1:
            for k, v in sorted(fresh_flats.items()):
                sleep(2)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)
        else:
            await bot.send_message(message.chat.id, "Пока нет новых предложений по трехкомнатным квартирам. Для остановки загрузки и перехода в основное меню нажмите /stop ",
                                   disable_notification=True)

        await asyncio.sleep(1800)


"""Все предложения по квартирам-студиям квартирам"""
async def all_news_studio(message):
    with open('items.json', encoding='utf-8') as f:
        news_dict = json.load(f)

    for k, v in sorted(news_dict.items()):
        if schedule_state:
            if k.startswith('kvartira-studiya'):
                sleep(3)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)


"""Отправка только нововыствленных квартир-студий"""
async def studio_appartment(message):
    while schedule_state:
        fresh_flats = appartment_room_flats()

        if len(fresh_flats) >= 1:
            for k, v in sorted(fresh_flats.items()):
                sleep(2)
                news = f"{hlink(v['наименование'], v['ссылка'])}\n" \
                       f"Стоимость: {hbold(v['цена'])} руб\n" \
                       f"Метро : {hbold(v['метро'])} \n" \

                await bot.send_message(message.chat.id, news, disable_notification=True)

        else:
            await bot.send_message(message.chat.id, "Пока нет новых предложений  по квартирам-студиям. Для остановки загрузки и перехода в основное меню нажмите /stop ",
                                   disable_notification=True)

        await asyncio.sleep(1800)





