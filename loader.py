from aiogram import Bot, Dispatcher, executor, types
import config
bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot=bot)