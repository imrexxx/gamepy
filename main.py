import random
# number guessing game

# get a computer random number
computer = random.randint(1, 10)
print(computer)

# get a user input
# check if user input same as computer random number
for _ in range(3) :
    guess = int(input("Enter your guess : "))
    if guess == computer :
        print("Congratulations, you guess are correct!!!")
        break
