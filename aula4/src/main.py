import click

@click.command()
@click.argument("name")
def hello(name):

    click.secho(f"Hello {name} !", fg="black", blink=True, underline=True, bold=True, bg="white")

if __name__ == "__main__":
    hello()