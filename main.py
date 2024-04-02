from pyrogram import Client, filters
from PIL import Image
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

def comparar_imagenes(imagen1, imagen2):
    # Abrir las imágenes
    img1 = Image.open(imagen1)
    img2 = Image.open(imagen2)

    # Verificar si las dimensiones de las imágenes son iguales
    if img1.size != img2.size:
        return False

    # Comparar los píxeles de ambas imágenes
    diferencia = 0
    for i in range(img1.size[0]):  # Ancho
        for j in range(img1.size[1]):  # Alto
            pixel_img1 = img1.getpixel((i, j))
            pixel_img2 = img2.getpixel((i, j))
            if pixel_img1 != pixel_img2:
                diferencia += 1

    # Calcular el porcentaje de similitud
    porcentaje_similitud = (1 - (diferencia / (img1.size[0] * img1.size[1]))) * 100

    # Definir un umbral de similitud (puedes ajustarlo según tus necesidades)
    umbral_similitud = 90

    # Devolver True si el porcentaje de similitud supera el umbral, False en caso contrario
    print("Similaridad en porciento: ",porcentaje_similitud)
    
    if porcentaje_similitud >= umbral_similitud:
        return True
    else:
        return False


#@app.on_message(filters.photo & filters.private & filters.bot & filters.user(1161908115)) #Megu PV
@app.on_message(filters.photo & filters.group & filters.bot & filters.user(1733263647))
def handle_message(client, message):
    print(message)
    text = message.caption.split(' ')

    if text[1] == "waifu":

        app.download_media(message, file_name="./new.jpg")

        if comparar_imagenes("original.jpg", "new.jpg") is False:
            return

        # Enviar un mensaje y esperar su finalización
        message.reply_text(
            text="/protecc roxy"
        )

        # Esperar un breve tiempo (2 segundos)
        #time.sleep(2)

        # Eliminar el mensaje enviado y esperar su finalización
        #client.delete_messages(
        #    chat_id=msg.chat.id,
        #    message_ids=msg.id
        #)

app.run()