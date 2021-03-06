from controllers.datacontroller import DataController as DC
from itertools import product
import random


class SimpleStratagy():

    def __init__(self):
        self.var_DC = DC()


    def simple_stratagy(self):

        string2 = """
        1: Average
        2: Play vs Computer
        """
        print(string2)
        option2 = input("Your choice: ")
        if option2 == "1":
            count = int(input("Sample size: "))
            count_amount = 0
            sample_size = count
            while count != 0:
                count += -1
                list_combinations = self.make_lst()
                guess = self.guess(list_combinations)
                code = self.guess(list_combinations)
                while True:
                    count_amount += 1
                    feedback = self.feedback(guess, code)
                    new_lst = self.filter_lst(list_combinations, guess, feedback)
                    guess = self.new_guess(new_lst)
                    if guess == code:
                        victory = "The code was: " + guess
                        print(victory)
                        break
            average = round(count_amount/sample_size)
            return print(f"Average amount of guesses: {average}" )

        elif option2 == "2":
            letter_amount = input("How many letter options should the code have: ")
            letter_lst = []
            for l in letter_amount:
                letter_lst.append(l)
            print(letter_lst)
            length = int(input("How long should the code be: "))
            print("You have to make a code existing of: " + letter_amount)
            code = input("Make your code: ")
            print("your code: " + code)

            list_combinations = self.make_lst_letters(letters=letter_lst, length=length)
            guess = self.guess(list_combinations)
            while True:
                feedback = self.feedback(guess, code)
                new_lst = self.filter_lst(list_combinations, guess, feedback)
                guess = self.new_guess(new_lst)
                print("The computer guessed: " + guess)
                if guess == code:
                    victory = "The code was: " + guess
                    return print(victory)


    def make_lst(self):
        combinations = list(product(['A', 'B', 'C', 'D', 'E', 'F'], repeat=4))
        lst = []
        for i in combinations:
            b = list(i)
            lst.append(b)
        return lst

    def make_lst_letters(self, letters, length):
        combinations = list(product(letters, repeat=length))
        lst = []
        for i in combinations:
            b = list(i)
            lst.append(b)
        return lst

    def guess(self, lst):
        random_seq = random.choice(lst)
        string = ""
        for j in random_seq:
            for m in j:
                string += m
        return string

    def new_guess(self, lst):
        random_seq = random.choice(lst)
        string = ""
        for j in random_seq:
            for m in j:
                string += m
        return string

    def feedback(self, guess, code):
        guess = list(guess)
        code = list(code)
        temp_guess = guess.copy()

        black = 0
        white = 0

        for i in range(len(code)):
            if guess[i] == code[i]:
                black += 1
                temp_guess[i] = "X"

        for j in temp_guess:
            if j in code:
                white += 1

        feedback = black, white
        return feedback

    def filter_lst(self, lst, guess, feedback):
        new_lst = []

        for i in lst:
            if feedback == self.feedback(guess, i):
                new_lst.append(i)

        return new_lst