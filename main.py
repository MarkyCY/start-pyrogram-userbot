from pyrogram import Client, filters
from pyrogram.types import (ReplyKeyboardMarkup ,InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove)

#import asyncio
import time
import os

# Create a new Pyrogram client
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
bot_token = os.getenv('BOT_TOKEN')

app = Client(
    #"my_bot",
    "my_account",
    api_id=api_id, 
    api_hash=api_hash,
    #bot_token=bot_token,
)


@app.on_message(filters.photo & filters.group & filters.bot & filters.user(1733263647))
def handle_message(client, message):
    print(message)
    text = message.caption.split(' ')
    print("Mensaje recibido:", text)
    print("Mensaje 1:", text[1])

    if text[1] == "waifu":

        # Enviar un mensaje y esperar su finalización
        msg = message.reply_text(
            text="/protecc roxy"
        )

        # Esperar un breve tiempo (2 segundos)
        time.sleep(2)

        # Eliminar el mensaje enviado y esperar su finalización
        client.delete_messages(
            chat_id=msg.chat.id,
            message_ids=msg.id
        )

# Define a handler function for the /start command
#@app.on_message(filters.command("start"))
#async def start_command(client, message):
#    # Crear un objeto InlineKeyboardMarkup con los botones
#    reply_markup = ReplyKeyboardMarkup(
#                [
#                    ["A", "B", "C", "D"],  # First row
#                    ["E", "F", "G"],  # Second row
#                    ["H", "I"],  # Third row
#                    ["J"]  # Fourth row
#                ],
#                resize_keyboard=True  # Make the keyboard smaller
#            )
#    # Enviar un mensaje con los botones inline
#    await message.reply_text("Hello, World!", reply_markup=ReplyKeyboardRemove)
#    await message.reply_text(
#            "This is a InlineKeyboardMarkup example",
#            reply_markup=InlineKeyboardMarkup(
#                [
#                    [  # First row
#                        InlineKeyboardButton(  # Generates a callback query when pressed
#                            "Button",
#                            callback_data="data"
#                        ),
#                        InlineKeyboardButton(  # Opens a web URL
#                            "URL",
#                            url="https://docs.pyrogram.org"
#                        ),
#                    ],
#                    [  # Second row
#                        InlineKeyboardButton(  # Opens the inline interface
#                            "Choose chat",
#                            switch_inline_query="pyrogram"
#                        ),
#                        InlineKeyboardButton(  # Opens the inline interface in the current chat
#                            "Inline here",
#                            switch_inline_query_current_chat="pyrogram"
#                        )
#                    ]
#                ]
#            )
#        )
#
#@app.on_callback_query()
#async def answer(client, callback_query):
#    await callback_query.answer(
#        f"Button contains: '{callback_query.data}'",
#        show_alert=True)

# Define a handler function for polls



app.run()