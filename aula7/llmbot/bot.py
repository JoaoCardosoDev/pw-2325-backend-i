import discord
from discord.message import Message
from llmbot.models import OllamaPrompt, OllamaResponse
from llmbot.clients import OllamaAPI
import requests

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

ollamaAPI = OllamaAPI()

@client.event
async def on_connect():
    print("Connecting...")

@client.event
async def on_ready():
    print("LLM bot connected")

@client.event
async def on_message(message: Message):
    
    assert message
    
    if message.author != client.user:
        if message.content.startswith("/prompt"):
            question=OllamaPrompt(
                prompt=message.content.split("/ask")[-1]
            )
            response: OllamaResponse = ollamaAPI.prompt(prompt=question)
    
    if not response.done:
        await message.channel.send(":poop oops!")
    else:
        await message.channel.send(response.response)


def start(token:str):
    client.run(token)

