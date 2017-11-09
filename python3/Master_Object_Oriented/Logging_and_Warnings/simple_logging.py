import logging
import sys


def logged(class_):
    class_.logger = logging.getLogger(class_.__qualname__)
    return class_


def demo():
    # add a level
    logging.addLevelName(15, "VERBOSE")
    logging.VERBOSE = 15

    # sample class
    @logged
    class Player:
        def __init__(self, bet, strategy, stake):
            self.logger.debug("init bet {0}, strategy {1}, stake {2}".format(
                bet, strategy, stake))

    # no configuration -- no output
    print("Create Player 1")
    p1 = Player("Bet1", "Strategey1", 1)

    # configuration changed -- now there's output
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    print("Create Player 2")
    p2 = Player("Bet2", "Strategey2", 2)

    logging.shutdown()
