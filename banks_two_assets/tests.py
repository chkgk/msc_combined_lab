from . import *
import random


class PlayerBot(Bot):
    def play_round(self):
        # Decision
        # --------------------------------------------------------------------------------------------------------------
        asset_a = random.randrange(0, 100)
        asset_b = 100 - asset_a

        yield (Decision,
            {
                'asset_a': asset_a,
                'asset_b': asset_b
            }
        )
