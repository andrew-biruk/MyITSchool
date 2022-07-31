from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from materials import books_storage, websites_storage


launch = InlineKeyboardMarkup(row_width=1)
launch.add(InlineKeyboardButton(text="Information", callback_data="info"),
           InlineKeyboardButton(text="Resources", callback_data="menu"),
           )

info = InlineKeyboardMarkup()
info.add(InlineKeyboardButton(text="Back", callback_data="start"))

menu = InlineKeyboardMarkup(row_width=2)
menu.add(InlineKeyboardButton(text="Books", callback_data="books"),
         InlineKeyboardButton(text="Websites", callback_data="websites"),
         InlineKeyboardButton(text="Back", callback_data="start"),
         )

books = InlineKeyboardMarkup(row_width=1)
buttons = [InlineKeyboardButton(text=k, url=v) for k, v in books_storage.items()]
buttons.append(InlineKeyboardButton(text="Back", callback_data="menu"))
books.add(*buttons)

websites = InlineKeyboardMarkup(row_width=2)
buttons = [InlineKeyboardButton(text=k, url=v) for k, v in websites_storage.items()]
buttons.append(InlineKeyboardButton(text="Back", callback_data="menu"))
websites.add(*buttons)