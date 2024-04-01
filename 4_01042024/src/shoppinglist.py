import click


@click.group()
@click.pass_context
def slist(list):
    """
    Welcome to your shopping list
    Please use --help for further instruction.
    """
    list.ensure_object(dict)

@slist.command()
@click.pass_context
def show(list):
    """
    Shows your current shopping list.
    """
    click.echo(f"{list}")

@slist.command()
@click.pass_context
@click.option('--item', prompt="Add an item to your list\n[Item]: ", help="Input an item to be added to the list.")
def add(list, item):
    """
    Adds an item to your list.
    """
    list.obj.append(item)
    option = input("Would you like to add more items?\n[Y|N]: ")
    if option == "Y":
        add()
    elif option == "N":
        return
    else:
        click.echo("Invalid input")

@click.command()
@click.pass_context
@click.option('--item', prompt="Which item would you like to remove from the list\n[Item to remove]")
def remove(list, item):
    """
    Removes an item from your list.
    """
    list.remove(item)
    click.echo(f"{item} removed from the list")
        
if __name__ == "__main__":
    slist()