import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def choose(self):
        return input(f"{self.name}, enter your choice (rock/paper/scissors): ").lower()

    def win_round(self):
        self.score += 1

class Game:
    def __init__(self,):
        self.winning_score = 3
        self.players = [Player("Player"), Player("Computer")]

    def get_computer_choice(self):
        return random.choice(["rock", "paper", "scissors"])

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "It's a tie!"
        elif (
            (player_choice == "rock" and computer_choice == "scissors")
            or (player_choice == "paper" and computer_choice == "rock")
            or (player_choice == "scissors" and computer_choice == "paper")
        ):
            return "You win!"
        else:
            return "Computer wins :("

    def play(self):
        while True:
            player_choice = self.players[0].choose()

            if player_choice == "quit" or player_choice == "q":
                break

            computer_choice = self.get_computer_choice()
            print(f"Computer plays: {computer_choice}")

            result = self.determine_winner(player_choice, computer_choice)
            print(result)

            if result == "You win!":
                self.players[0].win_round()
            elif result == "Computer wins :(":
                self.players[1].win_round()

            print(f"Player: {self.players[0].score} Computer: {self.players[1].score}\n")

            if any(player.score >= self.winning_score for player in self.players):
                break

        if self.players[0].score > self.players[1].score:
            print("Player won the game!")
        elif self.players[0].score == self.players[1].score:
            print("It's a tie!")
        else:
            print("Computer won the game!")

if __name__ == "__main__":
    game = Game()
    game.play()


