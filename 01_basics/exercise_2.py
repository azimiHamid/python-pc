import random

print("\nNumber Guessing Game!\n")

secret_number = random.randint(1, 10)
# print(secret_number)
guess_counter = 0
attempts = 3

while guess_counter < attempts:
    guess = int(input("Guess the number : "))
    guess_counter += 1
    if guess == secret_number:
        print(f"You won! the number is {secret_number}")
    else:
        print(f"Try again!")