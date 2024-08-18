import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    @property
    def value(self):
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return 11
        else:
            return int(self.rank)

class Deck:
    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    @property
    def value(self):
        total = sum(card.value for card in self.cards)
        aces = sum(card.rank == 'A' for card in self.cards)
        # Adjust Ace value from 11 to 1 as needed to avoid busting
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total

    @property
    def is_busted(self):
        return self.value > 21

    @property
    def is_blackjack(self):
        return self.value == 21 and len(self.cards) == 2

class BlackjackGame:
    def __init__(self):
        self.player_wins = 0

    def play_round(self):
        deck = Deck()
        player_hand = Hand()
        dealer_hand = Hand()

        # Initial draw
        player_hand.add_card(deck.draw())
        player_hand.add_card(deck.draw())
        dealer_hand.add_card(deck.draw())
        dealer_hand.add_card(deck.draw())

        # Player turn (simple logic: hit until value >= 17)
        # Manipulate this conditional variable
        # Findings: Less than 12 = 0.420049
        # Findings: Less than 14 = 0.420169
        while player_hand.value < 17:
            player_hand.add_card(deck.draw())
            if player_hand.is_busted:
                return  # Player loses, no win increment

        # Dealer turn (dealer hits until value >= 17)
        while dealer_hand.value < 17:
            dealer_hand.add_card(deck.draw())
            if dealer_hand.is_busted:
                self.player_wins += 1  # Dealer busts, player wins
                return

        # Compare hands
        if player_hand.value > dealer_hand.value:
            self.player_wins += 1  # Player wins

# Example usage:
game = BlackjackGame()
rounds = input("Rounds: ")
rounds = int(rounds)
for _ in range(rounds):  # Play 100 rounds
    game.play_round()

# Now `game.player_wins` contains the number of rounds the player won.
win_percentage = game.player_wins / rounds
print("Win %: " + str(win_percentage))