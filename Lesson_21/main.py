from aiogram import Bot
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from materials import available_commands
from handlers import *
import keyboards
import logging


logging.basicConfig(level=logging.INFO)
bot = Bot(token="PUT_YOU_TOKEN_HERE")
dp = Dispatcher(bot)


@dp.message_handler(commands="info")
async def show_info(message: types.Message):
    await message.answer(available_commands, reply_markup=keyboards.info)


@dp.message_handler(commands=["start", "menu"])
async def start(message: types.Message):
    await message.answer(text="BOT MENU:",
                         reply_markup=keyboards.launch)


@dp.callback_query_handler(text=["menu", "info", "websites", "books", "start"])
async def process_callback(call: types.CallbackQuery):
    await {
        "start": start,
        "menu": show_menu,
        "info": show_info,
        "books": show_books,
        "websites": show_websites,
    }[call.data](message=call.message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
