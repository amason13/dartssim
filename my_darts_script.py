from dartssim.match import Match
from dartssim.player import Player

#### Todays 1st match
clayton = Player(name = 'Clayton', treble_pct=0.385, single_pct=0.515, big_miss_pct=0.038,small_miss_pct=0.062,
                    bull_pct=0.35,outer_pct=0.6,double_pct=0.41)

gerwen = Player(name = 'Van Gerwen', treble_pct=0.469, single_pct=0.474, big_miss_pct=0.026,small_miss_pct=0.03,
                    bull_pct=0.35,outer_pct=0.6,double_pct=0.455)
'''
#### 2nd match
whitlock = Player(name = 'Whitlock', treble_pct=0.379, single_pct=0.542, big_miss_pct=0.03,small_miss_pct=0.049,
                 bull_pct=0.35,outer_pct=0.6,double_pct=0.373)

price = Player(name = 'Price',treble_pct=0.397, single_pct=0.507, big_miss_pct=0.037,small_miss_pct=0.058,
                    bull_pct=0.35,outer_pct=0.6,double_pct=0.371)
'''



match1 = Match(clayton, gerwen, first_to = 16)
#match2 = Match(whitlock, price,first_to = 16)


match1.simulate(num_sims = 100000)
#match2.simulate(num_sims = 100000)


