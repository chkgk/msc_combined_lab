from . import *
import numpy as np


class PlayerBot(Bot):
    def play_round(self):

        # Decision
        # --------------------------------------------------------------------------------------------------------------
        p = np.random.dirichlet(np.ones(5), size=1)
        a = np.random.multinomial(100, p[0], size=1)

        asset_a = a[0][0]
        asset_b = a[0][1]
        asset_c = a[0][2]
        asset_d = a[0][3]
        asset_e = a[0][4]

        yield (Decision,
            {
                'asset_a': asset_a,
                'asset_b': asset_b,
                'asset_c': asset_c,
                'asset_d': asset_d,
                'asset_e': asset_e
            }
        )