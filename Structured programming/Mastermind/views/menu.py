from controllers.datacontroller import DataController as DC
from controllers.simple import SimpleStratagy as SS
from controllers.worstcase import Worstcase as WC

class Menu():



    def __init__(self):
        self.var_DC = DC()
        self.var_SS = SS()
        self.var_WC = WC()

    def menu_codebreaker(self, code):

        guess = input("What is your guess: ")

        if guess == code:
            print("Congratulations you've cracked the code!")
            self.menu()
        else:
            print(f"Feedback: {self.var_DC.feedback(guess=guess, code=code)}")


    def menu_codemaker_simple(self):
        self.var_SS.simple_stratagy()

    def menu_codemaker_worstcase(self):
        self.var_WC.worstcase()

    def menu(self):
        string = """
        1: Play as CodeMaker
        2: Play as CodeBreaker
        """
        amount = 9
        print(string)
        option = input("Your choice: ")

        if option == "1":


                self.menu_codemaker_worstcase()

        elif option == "2":
            print("The computer has thought of a code")

            random_code = self.var_DC.random_code()

            while True:
                amount += -1
                if amount == 0:
                    break
                self.menu_codebreaker(random_code)

    @staticmethod
    def introduction():
        string = """    
        Welcome challanger.... In our game of MasterMind
        
        Gamerules: 
        The computer chooses a random code existing of A, B, C, D, E or F. 
        for example: AACD
        It is your job to crack the code. by using a max of 8 guesses if you haven't guessed the code untill then you've lost the game.
        The computer will give you a feedback existing of (A, B) 
        A stands for the amount of letters good and on the good spot.
        B stands for the amount of letters good but not on the good spot.
                        
        We wish you goodluck! you'll need it!
        """
        return string


