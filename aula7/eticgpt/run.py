import click
from eticgpt import bot as chat_bot


@click.group()
def bot():
    pass


@bot.command()
@click.option('--token', envvar="BOT_TOKEN",show_envvar=True, type=str)
def run(token:str):
    chat_bot.client.run(token)


if __name__ == "__main__":
    bot()
