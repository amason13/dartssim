from dartssim.match import Match
from dartssim.player import Player

#### Todays 1st match
price = Player(name = 'Price',treble_pct=0.406, single_pct=0.492, big_miss_pct=0.041,small_miss_pct=0.062,
                    bull_pct=0.35,outer_pct=0.6,double_pct=0.365)

suljovic = Player(name = 'Suljovic', treble_pct=0.403, single_pct=0.528, big_miss_pct=0.023,small_miss_pct=0.045,
                    bull_pct=0.35,outer_pct=0.6,double_pct=0.395)

#### 2nd match
gerwen = Player(name = 'van Gerwen', treble_pct=0.466, single_pct=0.478, big_miss_pct=0.026,small_miss_pct=0.029,
                 bull_pct=0.35,outer_pct=0.6,double_pct=0.428)
                 
anderson = Player(name = 'Anderson', treble_pct=0.449, single_pct=0.464, big_miss_pct=0.036,small_miss_pct=0.05,
                    bull_pct=0.35,outer_pct=0.6,double_pct=0.423)





#match1 = Match(price, suljovic, first_to = 16)
match2 = Match(gerwen, anderson, first_to = 16)


#match1.simulate(num_sims = 100000)
match2.simulate(num_sims = 100000)


