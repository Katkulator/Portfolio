from pyfiglet import figlet_format
from termcolor import colored
import requests
from random import choice

header = figlet_format("\nDadJokes3000")
print(colored(header, color="magenta"))

while True:
    user_input = input("Write a theme for a dad joke: ")
    url = "https://icanhazdadjoke.com/search"
    response = requests.get(
        url,
        headers={"Accept": "Application/json"},
        params={"term": user_input}

    ).json()

    total_jokes = response["total_jokes"]
    results = response["results"]

    if total_jokes > 1:
        print(
            f"There are {total_jokes} jokes about {user_input}. Here's one: ")
        print(choice(results)["joke"])
    elif total_jokes == 1:
        print(f"There is only one joke about {user_input}: ")
        print(results[0]['joke'])
    else:
        print(f"There are no jokes about {user_input} :(")

    again = input("Do you want another joke? y/n")
    if again != "y":
        break
