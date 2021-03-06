from itertools import permutations
from itertools import product
from itertools import combinations_with_replacement
import random


class Worstcase():

    def __init__(self):
        pass

    def worstcase(self):
        # Hoofdfuncite, hier komt alles samen
        print("You've to make a code existing of: [ A, B, C, D, E, F ]")
        code = input("Make your code: ")
        print("your code: " + code)
        lst_combinations = self.list_combinations()
        sorted_lst = self.split_lst(lst_combinations)
        guess = self.random_guess(sorted_lst)
        print("The computer guessed: " + guess)
        while True:

            feedback = self.feedback(guess, code)
            new_lst = self.filter_lst(lst_combinations, guess, feedback)
            guess = self.new_guess(new_lst)
            print("The computer guessed: " + guess)
            if guess == code:
                victory = "The code was: " + guess
                return print(victory)

    def list_combinations(self):
        combinations = list(product(['A', 'B', 'C', 'D', 'E', 'F'], repeat=4))
        lst = []
        for i in combinations:
            b = list(i)
            lst.append(b)
        return lst

    def split_lst(self, lst):
        lst_aabb = []
        for i in lst:
            if i[0] == i[1] and i[1] != i[2] and i[2] == i[3] or\
                    i[0] == i[2] and i[1] == i[3] and i[1] != i[2] or\
                    i[0] == i[3] and i[1] == i[2] and i[0] != i[1]:
                lst_aabb.append(i)
        return lst_aabb

    def feedbackoptions(self):
        # maak een lijst met alle mogelijke feedback
        permutations = list(permutations([0, 1, 2, 3, 4], 2))
        combinations = list(combinations_with_replacement([0, 1, 2, 3, 4], 2))
        lst = []
        for i in permutations:
            sum = i[0] + i[1]
            if sum <= 4:
                lst.append(i)

        for j in combinations:
            sum = j[0] + j[1]
            if sum <= 4:
                lst.append(j)
        lst = list(dict.fromkeys(lst))
        lst.remove((3, 1))
        return lst

    def combinationvariations(self):
        # maak een lijst met de 4 verschillende combinaties lst = [AAAA, AAAB, AABB, ABCD]
        lst = ['AAAA', 'AAAB', 'AABB', 'AABC' ,'ABCD']
        return lst

    def feedback(self, guess, code):
        # maak een feedback functie
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

    def random_guess(self, lst):
        # maak een random gok functie
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

    def worst_case_guess(self, lst):

        random_seq = random.choice(lst)
        string = ""
        for j in random_seq:
            for m in j:
                string += m
        return string

    def filter_lst(self, lst, guess, feedback):
        # maak een functie die de mogelijke lijsten berekent
        new_lst = []
        for i in lst:
            if feedback == self.feedback(guess, i):
                new_lst.append(i)
        return new_lst

    def possible_lst_length(self, lst, lst_guesses, lst_feedback):
        # maak een functie die een nieuwe lijst terug geeft met de verschillende lengtes tegen de bijbehorende feedback
        dict_length = {}
        for guess, feedback in lst_guesses, lst_feedback:
            filter = self.filter_lst(lst,guess,feedback)
            length = len(filter)
            dict_length[length] = filter
        return dict_length

    def choose_lst(self, dict):
        # maak een functie die uit een dictionary de juiste lijst zoekt waar de computer zijn volgende gok mee moet doen.
        pass
