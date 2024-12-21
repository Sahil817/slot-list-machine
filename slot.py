import random

class SlotMachine:
    def __init__(self):
        # Initialize the balance
        self.balance = 100  # Starting balance for the player
    
    def spin_reels(self):
        # Define the symbols
        symbols = ['🍒', '🍋', '🍊', '🍉', '🍇', '🍀']
        
        # Spin the reels (randomly select symbols for each reel)
        reel1 = random.choice(symbols)
        reel2 = random.choice(symbols)
        reel3 = random.choice(symbols)
        
        # Display the reels
        print(f"|| {reel1} {reel2} {reel3} ||")
        
        return reel1, reel2, reel3
    
    def calculate_winnings(self, reels, bet):
        # Calculate the winnings based on matching symbols
        reel1, reel2, reel3 = reels
        
        if reel1 == reel2 == reel3:
            if reel1 == '🍒':
                winnings = bet * 10  # Special case for 🍒 symbols
            else:
                winnings = bet * 5   # Standard case for matching symbols
            print(f"🎉 You won {winnings}! 🎉")
            return winnings
        else:
            print("Sorry, you lose. Try again!")
            return -bet  # If no match, you lose your bet
    
    def play_game(self):
        print("Welcome to the Slot Machine!")
        
        while True:
            print(f"Your current balance is: ${self.balance}")
            
            # Ask the player to place a bet
            bet = float(input("Place your bet: $"))
            
            if bet <= 0:
                print("Bet must be greater than 0. Try again.")
                continue
            elif bet > self.balance:
                print("You don't have enough balance. Try a lower amount.")
                continue
            
            # Spin the reels
            reels = self.spin_reels()
            
            # Calculate winnings or losses
            winnings = self.calculate_winnings(reels, bet)
            
            # Update balance
            self.balance += winnings
            
            # Check if the user wants to continue
            if self.balance <= 0:
                print("You ran out of money! Game over.")
                break
            
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again != 'y':
                print(f"Thanks for playing! Your final balance is: ${self.balance}")
                break


# Create a SlotMachine object and start the game
game = SlotMachine()
game.play_game()
