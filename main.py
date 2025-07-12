import os
from telethon import TelegramClient, events

api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')
session_name = os.getenv('SESSION_NAME', 'pushkod_session')

client = TelegramClient(session_name, api_id, api_hash)

source_channels = [
    'KODTIMEDUYURU',
    'bonusuzmanikod',
    'bonusprimeduyuru'
]

target_channel = 'PushKod'

@client.on(events.NewMessage(chats=source_channels))
async def handler(event):
    await client.send_message(target_channel, event.message)
    print(f"➡ Mesaj iletildi: {event.message.message[:30]}...")

print("🚀 Bot başlatılıyor...")
client.start()
client.run_until_disconnected()
