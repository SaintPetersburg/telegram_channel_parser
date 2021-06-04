from telethon import TelegramClient, events
import asyncio

api_id =  #api id // hash брать - https://my.telegram.org/
api_hash = ''

my_channel_id = '' #id нашего канала
channels = [-]  #id каналов, откуда будем брать материал.

client = TelegramClient('myGrab', api_id, api_hash)
print("MARI_FUCK - Started")


@client.on(events.NewMessage(chats=channels))
async def my_event_handler(event):
    if event.message:
        await client.send_message(my_channel_id, event.message)
        
client.start()
client.run_until_disconnected()
