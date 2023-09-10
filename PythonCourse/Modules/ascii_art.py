from pyfiglet import figlet_format
from termcolor import colored


def print_art(message, color):
    colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")
    if color not in colors:
        color = "green"

    ascii_art = figlet_format(message)
    colored_ascii = colored(ascii_art, color)
    print(colored_ascii)


message = input("What message do you want to print?: ")
color = input("In what color?: ")

print_art(message, color)
