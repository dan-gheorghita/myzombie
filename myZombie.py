import zombiedice
import random

class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break
            
class BotRandom:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        while random.randint(0,1) != 0:
            zombiedice.roll()

class BotFour:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        rolls = 1
        shotguns = 0
        shotguns += diceRollResults['shotgun']
        while rolls < 5 and shotguns < 2 and diceRollResults is not None:
            shotguns += diceRollResults['shotgun']
            diceRollResults = zombiedice.roll()
            rolls += 1
            
class MoreBrains:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        brains = 0
        shotguns = 0
        brains += diceRollResults['brains']
        shotguns += diceRollResults['shotgun']
        while brains >= shotguns and diceRollResults is not None:
            shotguns += diceRollResults['shotgun']
            brains += diceRollResults['brains']
            diceRollResults = zombiedice.roll()

zombies = (
    #zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    #zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    #zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
    #zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    MyZombie(name='My Zombie Bot'),
    BotRandom(name='This is random'),
    MyZombie(name='Stop at 2 brains'),
    BotFour(name='Try 4 times or 2 shotguns'),
    MoreBrains(name='Brains over shotgun'),
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)
