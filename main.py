import random
# number guessing game

# get a computer random number
computer = random.randint(1, 10)
print(computer)
# get a user input
guess = int(input("Enter your guess"))
print(guess)

# check if user input same as computer random number
