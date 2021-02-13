import discord
import asyncio
import random
import json
import os
import os.path
from discord.ext import commands
from discord.voice_client import VoiceClient

client=discord.Client()
    
@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('Coded by: TheRealCed')
	print('~~~~~~~~~~~~~~~~~~~~~~')
    
    python level_system.py

@client.event
async def on_message(message):

    if message.content.lower().startswith('c!help'):
        await client.send_message(message.author, "test")

        

client.run('token')
