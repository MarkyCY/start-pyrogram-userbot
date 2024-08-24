from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from PIL import Image
from dotenv import load_dotenv
load_dotenv()

import asyncio
import aiohttp
import json
import os

# Create a new Pyrogram client
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
bot_token = os.getenv('BOT_TOKEN')
SAUCENAO = os.getenv('SAUCENAO')

from logging import basicConfig, INFO
basicConfig(format="*%(levelname)s %(message)s", level=INFO, force=True)

app = Client(
    #"my_bot",
    "my_account",
    api_id=api_id, 
    api_hash=api_hash,
    #bot_token=bot_token,
)

async def async_post_image(url, params, image_path):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, params=params, data={'file': open(image_path, 'rb')}) as response:
            return await response.text()

async def comparar_imagenes(imagen1, imagen2):
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

async def search_sauce(downloaded_file, app, message):
    url = "https://saucenao.com/search.php"
    params = {
        "api_key": SAUCENAO,
        "output_type": "2",
        "testmode": "0"
    }
    result = await async_post_image(url, params, downloaded_file)
    
    res = json.loads(result)

    if 'results' in res:
        characters = None

        for i, result in enumerate(res['results']):
            if 'characters' in result['data']:
                characters = result['data']['characters']
                chars = characters.split(' ')
                for i, char in enumerate(chars):
                    
                    if char == "" or char == " ":
                        continue

                    await message.reply_text(f"/protecc {char}")
                    break
                break

@app.on_message(filters.photo & filters.group & filters.bot & filters.user(1733263647))
async def handle_message(app, message: Message):
    #text = message.caption.split(' ')
    chat_id = message.chat.id

    #if text[1] != "waifu":
    #    return

    downloaded_file = await app.download_media(message, file_name="./photo/new.jpg")

    await search_sauce(downloaded_file, app, message)

    directorio = './photo'

    archivos_jpg = [archivo for archivo in os.listdir(directorio) if archivo.lower().endswith('.jpg')]

    for archivo in archivos_jpg:
        # Verificar si el archivo es el nuevo archivo   
        if archivo == "new.jpg":
            continue

        name, ext = os.path.splitext(archivo)

        origin = f"{directorio}/{name}{ext}"
        compara = await comparar_imagenes(origin, f"{directorio}/new.jpg")

        if compara is False:
            continue
        else:
            # Enviar un mensaje y esperar su finalización
            await message.reply_text(
                text=f"/protecc {name}"
            )
            break
     
    # Esperar un breve tiempo (2 segundos)
    #await asyncio.sleep(2)
     
    # Eliminar el mensaje enviado y esperar su finalización
    #await client.delete_messages(
    #    chat_id=msg.chat.id,
    #    message_ids=msg.id
    #)

async def main():
    await app.start()
    print('*Bot Online.')

print("Bot Starting")
loop: asyncio.AbstractEventLoop = asyncio.get_event_loop_policy().get_event_loop()
loop.create_task(main())
loop.run_forever()