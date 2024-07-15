# NOTE: while loop also has an else statement, look at to the code bellow:
import random

print("\nNumber Guessing Game!\n")
print("Guess a number between 1 to 10")

secret_number = random.randint(1, 11)
guess_counter = 0
attempts = 3

while guess_counter < attempts:
    guess = int(input("Guess the number : "))
    guess_counter += 1
    if guess == secret_number:
        print(f"You won! the number is {secret_number}")
        break

else:
    print("Sorry, you failed!")