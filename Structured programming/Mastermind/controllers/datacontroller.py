from itertools import product
import random


class DataController():

    def __init__(self):
        pass

    @staticmethod
    def list_comb():
        combinations = list(product(["A", "B", "C", "D", "E", "F"], repeat=4))
        lst = []
        for i in combinations:
            b = list(i)
            lst.append(b)
        return lst

    def random_code(self):
        random_seq = random.choice(self.list_comb())
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