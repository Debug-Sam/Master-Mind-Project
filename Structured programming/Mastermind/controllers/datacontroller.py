from itertools import permutations
from itertools import combinations_with_replacement
import random


class DataController():

    @staticmethod
    def random_code():
        combinations = combinations_with_replacement(["A", "B", "C", "D", "E", "F"], 4)
        lst = []
        for i in list(combinations):
            lst.append(i)
        random_seq = random.choice(lst)
        string = ""
        for j in random_seq:
            string += j
        return string

    @staticmethod
    def feedback(guess, code):

        if guess == code:
            pass
        goodindex = 0
        good = 0

        for i in range(len(code)):
            if guess[i] == code[i]:
                goodindex += 1
                guess.replace(guess[i], "")

        for j in guess:
            if j in code:
                good += 1

        feedback = goodindex, good
        return feedback





