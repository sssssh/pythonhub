class BettingStrategy:
    def __init__(self):
        self.win = 0
        self.loss = 0

    def __call__(self):
        return 1


bet = BettingStrategy()
bet()
bet.win += 1
bet()
bet.loss += 1
bet()


# a stateful betting strategy. Property-based
class BettingMartingale(BettingStrategy):
    def __init__(self):
        self._win = 0
        self._loss = 0
        self.stage = 1

    @property
    def win(self):
        return self._win

    @win.setter
    def win(self, value):
        self._win = value
        self.stage = 1

    @property
    def loss(self):
        return self._loss

    @loss.setter
    def loss(self, value):
        self._loss = value
        self.stage *= 2

    def __call__(self):
        return self.stage


bet = BettingMartingale()
bet()
bet.win += 1
bet()
bet.loss += 1
bet()


# using ``__setattr__()`` instead if properties
class BettingMartingale2(BettingStrategy):
    def __init__(self):
        self.win = 0
        self.loss = 0
        self.stage = 1

    def __setattr__( self, name, value):
        if name == 'win':
            self.stage = 1

        elif name == 'loss':
            self.stage *= 2

        super().__setattr__(name, value)

    def __call__(self):
        return self.stage


bet= BettingMartingale2()
bet()
bet.win += 1
bet()
bet.loss += 1
bet()
