import warnings
try:
    import simulation_model_1 as model
except ImportError as e:
    warnings.warn(e)
if 'model' not in globals():
    try:
        import simulation_model_2 as model
    except ImportError as e:
        warnings.warn(e)
if 'model' not in globals():
    # raise ImportError( "Missing simulation_model_1 and simulation_model_2" )
    pass


class Player:

    __version__ = "2.1"

    def bet(self):
        warnings.warn("bet is deprecated, use place_bet",
                      DeprecationWarning, stacklevel=2)
        pass


warnings.simplefilter("always", category=DeprecationWarning)
p2 = Player()
p2.bet()
