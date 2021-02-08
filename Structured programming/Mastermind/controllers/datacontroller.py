from itertools import product
import random


class DataController():

    def __init__(self):
        pass

    @staticmethod
    def random_code():
        combinations = list(product(["A", "B", "C", "D", "E", "F"], repeat=4))
        lst = []
        for i in combinations:
            b = list(i)
            lst.append(b)
        random_seq = random.choice(lst)
        string = ""
        for j in random_seq:
            for m in j:
                string += m
        return string

    @staticmethod
    def feedback(guess, code):
        guess = list(guess)
        code = list(code)
        temp_guess = guess.copy()

        goodindex = 0
        good = 0

        for i in range(len(code)):
            if guess[i] == code[i]:
                goodindex += 1
                temp_guess[i] = "X"

        for j in temp_guess:
            if j in code:
                good += 1

        feedback = goodindex, good
        return feedback

    def simple_stratagy(self, guess, feedback):
        return



    def first_guess(self):
        combinations = list(product(["A", "B", "C", "D", "E", "F"], repeat=4))
        lst = []
        for i in combinations:
            b = list(i)
            lst.append(b)
        random_seq = random.choice(lst)
        return random_seq