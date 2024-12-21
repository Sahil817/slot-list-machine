import random

def spin_reels():
    symbols = ["Cherry", "Lemon", "Orange", "Plum", "Bell", "Bar"]
    return [random.choice(symbols) for _ in range(3)]

def calculate_winnings(reels, bet):
    if reels[0] == reels[1] == reels[2]:  # All three symbols match
        payouts = {
            "Cherry": 5,
            "Lemon": 3,
            "Orange": 4,
            "Plum": 6,
            "Bell": 10,
            "Bar": 20
        }
        return bet * payouts[reels[0]]
    elif reels[0] == reels[1] or reels[1] == reels[2] or reels[0] == reels[2]:  # Two symbols match
        return bet * 2
    else:  # No match
        return 0

def display_reels(reels):
    print(f"Reels: {' | '.join(reels)}")

def slot_machine():
    balance = 100  # Starting balance
    print("Welcome to the Slot Machine!")
    print(f"Your starting balance is: ${balance}")

    while True:
        print(f"\nCurrent balance: ${balance}")
        bet = input("Enter your bet amount (or 'q' to quit): ")

        if bet.lower() == 'q':
            print(f"You are leaving with a balance of ${balance}. Thanks for playing!")
            break

        if not bet.isdigit() or int(bet) <= 0:
            print("Invalid bet amount. Please enter a positive number.")
            continue

        bet = int(bet)

        if bet > balance:
            print("You don't have enough balance to make that bet. Try a smaller amount.")
            continue

        balance -= bet
        reels = spin_reels()
        display_reels(reels)
        winnings = calculate_winnings(reels, bet)

        if winnings > 0:
            print(f"Congratulations! You won ${winnings}!")
            balance += winnings
        else:
            print("No winnings this time. Better luck next spin!")

        if balance <= 0:
            print("You have run out of balance. Game over!")
            break

if __name__ == "__main__":
    slot_machine()
