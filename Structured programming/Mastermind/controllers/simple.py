from controllers.datacontroller import DataController as DC
from itertools import product
import random

class SimpleStratagy():

    def __init__(self):
        global var_DC
        var_DC = DC()

    def simple_stratagy(self):
        lst = self.filter_lst()
        lst_lst = lst[0]

        while True:
            guess = self.guess(lst_lst)
            print("Computer guessed: " + guess)
            black = input("How many black pins: ")
            white = input("How many white pins: ")
            feedback = black + white
            lst_lst = self.feedback(feedback=feedback, guess=guess)


    def feedback(self, feedback, guess):

        filter_lst = self.filter_lst()
        filter_lst_letter_lst = filter_lst[1]
        filter_lst_lst = filter_lst[0]

        if feedback == 1:
            return filter_lst_lst
        elif feedback == 2:
            return filter_lst_lst
        elif feedback == 3:
            return filter_lst_lst
        elif feedback == 4:
            filter_lst = self.filter_lst(answer=guess)
            return filter_lst[0]
        elif feedback == 0:
            filter_lst = self.filter_lst(filter_lst_lst, filter_lst_letter_lst, guess)
            return filter_lst[0]


    def filter_lst(self, letter_lst=None, letters=None, answer=None):

        if answer != None:
            new_lst = []
            for j in answer:
                new_lst.append(j)
            combinations = list(product(new_lst, repeat=4))
            lst = []
            for i in combinations:
                b = list(i)
                lst.append(b)
            return lst, letter_lst

        if letter_lst == None:
            letter_lst = ['A', 'B', 'C', 'D', 'E', 'F']

        if letters != None:
            for i in letters:
                letter_lst.remove(i)
        combinations = list(product(letter_lst, repeat=4))
        lst = []
        for i in combinations:
            b = list(i)
            lst.append(b)
        return lst, letter_lst

    def guess(self, lst):
        random_seq = random.choice(lst)
        string = ""
        for j in random_seq:
            for m in j:
                string += m
        return string