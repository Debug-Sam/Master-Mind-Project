from controllers.datacontroller import DataController as DC
from itertools import product
import random


class SimpleStratagy():

    def __init__(self):
        global var_DC
        var_DC = DC()

    def simple_stratagy(self):

        print("You have to make a code existing of: A, B, C, D, E or F")
        print("For example: AABC")
        code = input("Make your code: ")
        print("your code: " + code)


        list_combinations = self.make_lst()
        guess = self.guess(list_combinations)
        while True:
            feedback = self.feedback(guess, code)
            new_lst = self.filter_lst(list_combinations, guess, feedback)
            guess = self.guess(new_lst)
            print("The computer guessed: " + guess)
            answer = input("Did the computer get it right? yes or no: ")
            if answer == "yes":
                break


    def make_lst(self):
        combinations = list(product(['A', 'B', 'C', 'D', 'E', 'F'], repeat=4))
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