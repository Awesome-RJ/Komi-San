from pyrogram import filters
from pyrogram.types.bots_and_keyboards import callback_game
from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup 
from nksama import bot ,help_message
from typing import List , Any



@bot.on_message(filters.command('help'))
def bothelp(_,message):
    keyboard = [
        [
            InlineKeyboardButton(
                f"{x['Module_Name']}", callback_data=f"help:{x['Module_Name']}"
            )
        ]
        for x in help_message
    ]

    bot.send_message(message.chat.id , "Commands and help" , reply_markup=InlineKeyboardMarkup(keyboard))
