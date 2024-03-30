import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {'A': 3, 'B': 3, 'C': 3, 'D': 3, 'E': 3}
symbol_value = {'A': 5, 'B': 10, 'C': 15, 'D': 20, 'E': 25}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

def get_number_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount

def retract_amount(balance):
    while True:
        retract = input("Would you like to retract the amount? (y/n): ").lower()
        if retract == 'y':
            amount_to_retract = int(input("Enter the amount to retract: $"))
            if amount_to_retract <= balance:
                balance -= amount_to_retract
                print(f"${amount_to_retract} retracted successfully.")
                break
            else:
                print("Insufficient balance to retract that amount.")
        elif retract == 'n':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def spin(balance, user_name):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)

    if all(column[0] == slots[0][0] for column in slots):
        multiplier = 3 if slots[0][0] == 1 else 2 if slots[0][0] == 2 else 1.5
        winnings *= multiplier
        print(f"Congratulations {user_name}! You got three equal numbers in a row! Your winnings are multiplied by {multiplier}.")
    else:
        print("No three equal numbers in a row.")

    return winnings - total_bet

def main():
    user_name = input("Enter your name: ")
    balance = deposit()
    while True:
        print(f"Current balance for {user_name} is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        retract_amount(balance)
        balance += spin(balance, user_name)

    print(f"{user_name}, you left with ${balance}")

main()
