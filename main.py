from telethon import TelegramClient
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()

API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
PHONE_NUMBER = os.getenv('PHONE_NUMBER')

client = TelegramClient('session_name', API_ID, API_HASH)

async def keep_online():
    await client.connect()
    if not await client.is_user_authorized():
        await client.send_code_request(PHONE_NUMBER)
        await client.sign_in(PHONE_NUMBER, input('Enter the code: '))
    
    print("[INFO] Client is running...")
    while True:
        await client.send_read_acknowledge('me')  
        await asyncio.sleep(300)  

if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(keep_online())
