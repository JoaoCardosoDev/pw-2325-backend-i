from click.testing import CliRunner
from shoppinglist import *

def test_show():
    runner = CliRunner()
    result = runner.invoke(show)
    assert result.exit_code == 0
    assert "shopping list" in result.output

def test_add():
    runner = CliRunner()
    result = runner.invoke(add, ['banana'], ['n'])
    assert result.exit_code == 0
    with open("list.txt", "r") as list_file:
        lines = list_file.readlines()
        assert "banana\n" in lines

def test_remove():
    runner = CliRunner()
    result = runner.invoke(remove, ['banana'])
    assert result.exit_code == 0
    assert "banana removed from the list" in result.output