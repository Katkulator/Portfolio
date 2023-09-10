# def colorize(text, color):
#     colors = ("cyan", "blue", "magenta", "yellow", "blue", "red", "green")
#     if type(text) is not str:
#         raise ValueError("Please type in a string")
#     if color not in colors:
#         raise ValueError("Pleasy type in a valid color")
#     print(f"Printed {text} in {color}")

# colorize("blablabla", "red")
# colorize(658, "red")
# colorize("blablabla", "gray")

from datetime import datetime
start_time = datetime.now()
def max_balloon_moves(S):
    required_letters = {"B": 1, "A": 1, "L": 2, "O": 2, "N": 1}
    letter_counts = {letter: S.count(letter) for letter in required_letters}
    
    max_moves = 10**9  # A large number as a placeholder for infinity
    
    for letter, count in required_letters.items():
        if letter_counts[letter] < count:
            return 0
        max_moves = min(max_moves, letter_counts[letter] // count)
    
    return max_moves

# Example usage
from string import ascii_uppercase
import random

s = ''.join(random.choice(ascii_uppercase) for _ in range(1, 200001))
result = max_balloon_moves(s)
print(result)

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))