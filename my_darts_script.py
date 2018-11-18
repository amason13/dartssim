from dartssim.match import Match
from dartssim.player import Player

#### Todays 1st match
price = Player(name = 'Price',treble_pct=0.406, single_pct=0.492, big_miss_pct=0.041,small_miss_pct=0.062,
                    bull_pct=0.35,outer_pct=0.6,double_pct=0.365)

suljovic = Player(name = 'Sujovic', treble_pct=0.403, single_pct=0.528, big_miss_pct=0.023,small_miss_pct=0.045,
                    bull_pct=0.35,outer_pct=0.6,double_pct=0.395)
'''
#### 2nd match
whitlock = Player(name = 'Whitlock', treble_pct=0.379, single_pct=0.542, big_miss_pct=0.03,small_miss_pct=0.049,
                 bull_pct=0.35,outer_pct=0.6,double_pct=0.373)
                 
clayton = Player(name = 'Clayton', treble_pct=0.385, single_pct=0.515, big_miss_pct=0.038,small_miss_pct=0.062,
                    bull_pct=0.35,outer_pct=0.6,double_pct=0.386)

'''



match1 = Match(price, sujovic, first_to = 16)
#match2 = Match(whitlock, price,first_to = 16)


match1.simulate(num_sims = 100000)
#match2.simulate(num_sims = 100000)


