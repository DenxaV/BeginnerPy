import random

random_number = random.randint(1, 100)
number_of_guesses = 0

def input_validity(userinput):
    while True:
        try:
            if userinput < 1:
                print("Please enter a valid number greater than 0.")
                return False
            return True
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return False

def main():
    global number_of_guesses
    while True:
        try:
            number_guess = int(input("Guess the number chosen!"))
            number_of_guesses += 1
            if input_validity(number_guess):
                if number_guess < random_number:
                    print("Too low")
                elif number_guess > random_number:
                    print("Too high")
                else:
                    print(f"Congratulations! You found the number after {number_of_guesses} guesses!")
                    break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

main()





