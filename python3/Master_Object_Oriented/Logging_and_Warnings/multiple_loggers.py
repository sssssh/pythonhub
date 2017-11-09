import logging


def demo():
    # expanded decorator
    def log_to(*names):
        if len(names) == 0:
            names = ['logger']

        def concrete_log_to(class_):
            for log_name in names:
                setattr(class_, log_name, logging.getLogger(
                    log_name + "." + class_.__qualname__))
            return class_
        return concrete_log_to

    # sample class
    @log_to("audit", "verbose")
    class Player:
        def __init__(self, bet, strategy, stake):
            self.audit.info("Initial {0:d}".format(stake))
            self.verbose.info("Init bet={bet:s} strategy={strategy:s} stake={stake:d}".format(
                bet=bet, strategy=strategy, stake=stake))

    @log_to("security")
    class Table:
        def add_player(self, player):
            self.security.info("Adding {0}".format(player))

    # demo output
    print("Create Player 2")
    p3 = Player("Bet3", "Strategy3", 3)
    t = Table()
    t.add_player(p3)

    logging.shutdown()
