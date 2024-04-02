import click

@click.group()
def slist():
    """
    Welcome to your shopping list
    Please use --help for further instruction.
    """

@slist.command()
def show():
    """
    Shows your current shopping list.
    """
    try:
        with open("list.txt", 'r') as list:
            click.secho("Your Shopping List:", fg='cyan')
            for line in list:
                click.echo(f"- {line.strip()}")
    except FileNotFoundError:
        click.secho("Your shopping list is empty.", fg='cyan')

@slist.command()
@click.option('--item', prompt=click.style("Add an item to your list\n[Item]", fg='yellow'), help="Input an item to be added to the list.")
def add(item):
    """
    Adds an item to your list.
    """

    with open('list.txt', 'a') as list:
        list.write(f"{item}\n")
    option = click.prompt(click.style("Would you like to add more items?\n[y|n]", fg='yellow')).lower()
    if option == "y":
        add(click.prompt(click.style("Add an item to your list\n[Item]", fg='yellow')))
    elif option == "n":
        return
    else:
        click.secho("Invalid input", fg='bright_red')

@slist.command()
@click.option('--item', prompt="Which item would you like to remove from the list\n[Item to remove]: ", help="Input an item to be removed from the list.")
def remove(item):
    """
    Removes an item from your list.
    """
    try:
        with open("list.txt", 'r') as list:
            lines = list.readlines()
        with open("list.txt", "w") as list:
            for line in lines:
                if line.strip() != item:
                    list.write(line)
        click.secho(f"{item} removed from the list", fg="bright_red")
    except FileNotFoundError:
        click.secho("Your list is empty.", fg='cyan')
    

if __name__ == "__main__":
    slist()
