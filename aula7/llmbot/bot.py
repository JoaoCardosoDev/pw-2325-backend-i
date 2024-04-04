import discord
from discord.message import Message
from models import OllamaPrompt
import requests

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_connect():
    pass

@client.event
async def on_ready():
    pass

@client.event
async def on_message(message: Message):
    pass
