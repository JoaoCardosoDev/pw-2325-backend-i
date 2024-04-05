import click
from llmbot.bot import *

@click.group()
def llm():
    pass


@llm.command()
#@click.option('--token', show_envvar="BOT_TOKEN")
def run():
    start('')

if __name__=="__main__":
    run()