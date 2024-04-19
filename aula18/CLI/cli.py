import secrets
import string
import click

@click.command()
@click.option('--lenght', '-l', default=8, help="Size of your password")
@click.option('--upper', '-u', default=True, help="Define if the password has uppercase.")
@click.option('--digits', '-d', default=True, help="Define the inclusion of digits.")
@click.option('--special', '-s', default=True, help="Define the inclusion of special characters.")
def PassGen(lenght:int, upper:bool, digits:bool, special:bool):
    """
    This CLI will generate a strong password depending on your preferences.
    """
    alphabet = string.ascii_letters
    digitslist = string.digits
    specialchars = string.punctuation
    password = "".join(secrets.choice(alphabet+digitslist+specialchars) for _ in range(lenght))
    if not upper:
        password.lower()
    if not digits:
        password = "".join(secrets.choice(alphabet+specialchars) for _ in range(lenght))
    if not special:
        password = "".join(secrets.choice(alphabet+digitslist) for _ in range(lenght))
    
    click.echo(password)


if __name__ == '__main__':
    PassGen()