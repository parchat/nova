import random
def guessTheNumber():

    num = random.randint(1,10)
    print("The system picked {}".format(num))

    while True:
        guess = int(input("Please guess a number between 1 to 10: "))
        print("Your guess is {}".format(guess))

        if guess == num:
            print("Your guess was correct.")
            break
        elif guess < num:
            print("Your guess was too low. Try again.")
        elif guess > num:
            print("Your guess was too high. Try again.")



if __name__ == "__main__":
    guessTheNumber();