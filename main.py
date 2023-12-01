import random
# number guessing game

# get a user input
# check if user input same as computer random number

while True :

    # get a computer random number
    computer = random.randint(1, 10)
    print(computer)

    for _ in range(3) :
        guess = int(input("Enter your guess : "))
        if guess == computer :
            print("Congratulations, you guess are correct!!!")
            break
    
    ask = input("Play again? (enter 'y' or 'n') :")
    if ask != "y" :
        break