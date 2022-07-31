from aiogram import types
import keyboards


async def show_menu(message: types.Message):
    await message.answer(text="What are you looking for: books or websites?",
                         reply_markup=keyboards.menu)


async def show_books(message: types.Message):
    await message.answer(text=f"Some good books on Python programming:",
                         reply_markup=keyboards.books)


async def show_websites(message: types.Message):
    await message.answer(text=f"Some good websites on Python programming:",
                         reply_markup=keyboards.websites)
