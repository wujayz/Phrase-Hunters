# Import your Game class
from phrasehunter.game import Game
from phrasehunter.phrase import Phrase


if __name__ == "__main__":
    game = Game()
#    phrase = Phrase()

    for phrase in game.phrases:
        print(phrase.phrase)


# Create your Dunder Main statement.

# Inside Dunder Main:
## Create an instance of your Game class
## Start your game by calling the instance method that starts the game loop


# # import Game class from phrasehunter package

# create a new instance of Game class and store this instance in a game variable

# call start() 

# ensure you place your instance creation and method calls inside dunder main
