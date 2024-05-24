import asyncio
from pyrogram import Client, types

import os

# Create a new Pyrogram client
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
bot_token = os.getenv('BOT_TOKEN')

async def progress(current, total):
    print(f"{current * 100 / total:.1f}%")

async def main():
    #my_account
    #my_bot
    #Aki
    async with Client("Aki", api_id=api_id, api_hash=api_hash, bot_token="6275121584:AAEhFMJXAsQSOcnX2K84p3Uck0AGsdCu-bI") as app:

        await app.send_photo(-1001485529816, "2.png", """
Nuevo video en YouTube de Otaku Senpai!
                             
Título: Suicide Squad Isekai (Escuadrón suicida)
Descripción: ¿Qué debes saber sobre el Suicide Squad Isekai? ¡Te lo contamos!
""", reply_markup=types.InlineKeyboardMarkup(
            [
                [types.InlineKeyboardButton(
                    "📺 Ir a Ver",
                    url="https://www.youtube.com/watch?v=9KfuXg3y3H4"
                )]
            ]
        ),
            message_thread_id=251766,
            progress=progress)


asyncio.run(main())
