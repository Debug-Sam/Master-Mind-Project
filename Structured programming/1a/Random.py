
import random

def randoms_game():

    print("You need to guess the random number, between 0 and 10. ")
    print("Good luck \n")
    random_num = random.randint(0, 10)
    print(random_num)
    while True:
        answer = int(input("Make a guess: "))
        if answer == random_num:
            print("good job! ")
            break
        else:
            print("Try again! \n")

randoms_game()

