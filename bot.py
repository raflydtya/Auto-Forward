# File ini bagian dari Repositori: github.com/raflydtya/Auto-Forward Akun: @raflydtya
# Nama: bot.py | Python Telegram Bot
# Copyright 2022. All Right Reserved.

import time, asyncio, sys, random

from telethon import TelegramClient, events, utils, Button

api_id = isi api id milikmu 
api_hash = 'isi api hash milikmu'
sesi_file = 'Forwarder'
client = TelegramClient(sesi_file, api_id, api_hash)

usr = 'isi username pengguna spesifik'
grup = 'isi username grup/tujuan pesan'

@client.on(events.NewMessage(from_users=usr))
async def handler(event):
        pesan = event.raw_text
        
        if 'a' in pesan:
            time.sleep(1)
            await event.message.forward_to(grup)
            time.sleep(1)
            print('Berhasil')
            return

with client:
    client.run_until_disconnected()
