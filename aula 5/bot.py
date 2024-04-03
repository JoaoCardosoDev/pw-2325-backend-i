import discord
import click


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"{client.user} is running.")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("ping"):
        await message.channel.send('Pong')

@click.group
def bot():
    """
    Discord bot that answer to a ping message.
    """

@bot.command()
def run():
    client.run('')