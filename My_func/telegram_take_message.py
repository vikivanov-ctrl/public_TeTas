import time
from telethon import TelegramClient

#Функция сбора сообщений
async def take_message(limit, canals, all_messages,phone_number,client) -> list:  
    #Запускаем клиент 
    await client.start(phone=phone_number)
    #Берём все диалоги (каналы и чаты)
    dialogs= await client.get_dialogs()
    #Ищем нужные
    for dialog in dialogs:
        if dialog.title in canals:
            #Берём сообщения из канала
            messages=client.iter_messages(entity=dialog)
            async for message in messages:
                #Забираем, если оно не пустое
                if message.text!='':
                    all_messages.append([message.text])
                    #Останавливаемся после добавления нужного количества сообщений
                    if len(all_messages)%limit==0:
                        break
                #Ждём, чтобы не приняли за спам
                time.sleep(1)
    await client.disconnect()              
    return(all_messages)

#Запуск клиента
def start_client(api_id, api_hash,api_name):
    #Подключаемся к клиенту / TeTas название из Api
    client=TelegramClient(api_name, api_id, api_hash, system_version='4.16.30-vxCUSTOM')
    return client
