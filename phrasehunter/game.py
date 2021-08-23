
import random

from phrase import Phrase

class Game:

    phrases = ["Close But No Cigar", "Cry Over Spilled Milk",
               "Curiosity Killed The Cat", "Cut To The Chase",
               "Back to Square One"]

    def __init__(self):
        #self.____ = ___
        self.missed = 0
        # this is used to track no. of incorrect guesses / initial value = 0
        self.active_phrase = None
        # initial value = None. within the start() method, this is set to phrase object
        # returned from call to the get_random_phrase() method
        self.guesses = [" "]
        # list contains all guesses made. 


    def get_random_phrase(self):
        # Method get_random_phrase() for getting a random phrase from phrases
        # stored in the phrases list and returns
        pass



    

    def start(self):
        pass

    


# Method start() for starting the game
# - calls welcome method: welcome(): at start of game
# - creates game loop
# calls get_guess() method: add's user's guess to guesses attribute
# incrememnts no. of missed for incorrect
# calls game_over method if over: method displays win or loss message and ends game

# Method for handling interactions



# Method for checking for a win/loss state

# adding to the numbers missed

