# Blackjack Win Percentage Simulator

This Python program simulates multiple rounds of a simple Blackjack game to calculate the player's win percentage against a dealer. The simulation allows you to specify the number of rounds to be played and uses basic strategies for both the player and the dealer.

## Features

- **Card and Deck Classes**: The program includes `Card` and `Deck` classes to represent the cards and manage the deck.
- **Hand Class**: Manages the cards in hand and calculates the hand's value, including logic to handle Aces (counted as 1 or 11).
- **BlackjackGame Class**: Manages the game logic, including drawing cards, determining the winner, and tracking player wins.
- **Simulation**: Run the simulation for a specified number of rounds to calculate the win percentage of the player.

## How It Works

1. **Deck Creation**: A standard deck of 52 cards is created and shuffled.
2. **Initial Draw**: Both the player and the dealer are dealt two cards each.
3. **Player's Turn**: The player will keep hitting (drawing cards) until their hand value is 17 or more. If the player's hand exceeds 21, the player busts and loses the round.
4. **Dealer's Turn**: The dealer will hit until their hand value is 17 or more. If the dealer busts, the player wins the round.
5. **Comparison**: If neither the player nor the dealer busts, their hand values are compared. The player wins if their hand value is higher than the dealer's.
6. **Win Tracking**: The number of rounds won by the player is tracked and used to calculate the win percentage.

## Usage

To run the simulation:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ThomasCaneday/BlackJack-Win-Percentage-Simulator.git
   cd BlackJack-Win-Percentage-Simulator
   ```

2. **Run the Simulation**:
   ```bash
   python BlackJack-Win-Percentage-Simulator.py
   ```

3. **Input the Number of Rounds**: When prompted, input the number of rounds you want to simulate. For example, entering `1000` will simulate 1000 rounds of Blackjack.

4. **View Results**: The program will output the player's win percentage after all rounds have been played.

Example:
```python
Rounds: 1000
Win %: 0.421
```

## Customization

- **Player Strategy**: The player currently hits until their hand value is 17 or more. You can modify this strategy in the `play_round` method of the `BlackjackGame` class.
- **Dealer Strategy**: The dealer's strategy of hitting until their hand value is 17 or more is standard. You can modify this if desired.
