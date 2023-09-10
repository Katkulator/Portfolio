import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def value(self):
        if self.rank in ["J", "Q", "K"]:
            return 10
        elif self.rank == "A":
            return 11
        else:
            return int(self.rank)
        
    def __repr__(self):
        return f"{self.rank} of {self.suit}"
    
class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K"]
                      for suit in ["Hearts", "Clubs", "Spades", "Diamonds"]]
        random.shuffle(self.cards)
    
    def deal(self):
        return self.cards.pop()
    
class Player:
    def __init__(self):
        self.hand = []
        self.total_value = 0
    
    def add_card(self, card):
        self.hand.append(card)
        self.calculate_total_value()
    
    def calculate_total_value(self):
        card_sum = 0
        for card in [card.value() for card in self.hand]:
            if card == 11 and card_sum >= 11:
                card_sum += 1
            else:
                card_sum += card
        self.total_value = card_sum

class Blackjack:
    def __init__(self):
        self.set_initial_values()
        
    def set_initial_values(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Player()

    def deal_initial_cards(self):
            self.player.add_card(self.deck.deal())
            self.dealer.add_card(self.deck.deal())
            self.player.add_card(self.deck.deal())
            self.dealer.add_card(self.deck.deal())
    
    def player_turn(self):
        while self.player.total_value < 21 and self.dealer.total_value < 21:
            choice = input("Would you like to hit(H) or stand(S)?: ").lower()
            if choice == "h":
                self.player.add_card(self.deck.deal())
                print(f"Players hand:{self.player.hand} | Value: {self.player.total_value}")
                print(f"Dealers hand:{self.dealer.hand} | Value: {self.dealer.total_value}")
            elif choice == "s":
                break
            else:
                print("Invalid choice! Please type H or S")

    def dealer_turn(self):
        while self.dealer.total_value < 17:
            self.dealer.add_card(self.deck.deal())
            print(f"Dealers hand:{self.dealer.hand} | Value:{self.dealer.total_value}")

    def determine_winner(self):
        if self.player.total_value > 21: 
            print(f"Dealer Wins: {self.dealer.hand} - {self.dealer.total_value}")
        elif self.dealer.total_value > 21:
            print(f"Player Wins: {self.player.hand} - {self.player.total_value}")
        elif self.player.total_value == self.dealer.total_value:
            print("It's a TIE!")
        elif self.player.total_value > self.dealer.total_value:
            print(f"Player Wins: {self.player.hand} - {self.player.total_value}")
        else:
            print(f"Dealer Wins: {self.dealer.hand} - {self.dealer.total_value}")
    
    def play(self):
        print("Welcome to Blackjack!")
        while True:
            self.deal_initial_cards()
            print(f"Player's hand: {self.player.hand} - Value: {self.player.total_value}")
            print(f"Dealer's hand: {self.dealer.hand[0]}, Unknown")

            self.player_turn()
            if self.player.total_value < 21:
                self.dealer_turn()
            self.determine_winner()
            
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again != "y":
                break
            self.set_initial_values()


if __name__ == "__main__":
    blackjack_game = Blackjack()
    blackjack_game.play()

print("Thank you for playing!")








        


    


