from dartssim.match import Match
from dartssim.player import Player

#### Todays 1st match
vandebergh = Player(name = 'Van de Bergh', treble_pct=0.385, single_pct=0.538, big_miss_pct=0.034,small_miss_pct=0.043,
                    bull_pct=0.35,outer_pct=0.6,double_pct=0.354)

sulijovic = Player(name = 'Sulijovic', treble_pct=0.407, single_pct=0.521, big_miss_pct=0.023,small_miss_pct=0.049,
                    bull_pct=0.35,outer_pct=0.6,double_pct=0.395)

#### 2nd match
whitlock = Player(name = 'Whitlock', treble_pct=0.379, single_pct=0.542, big_miss_pct=0.03,small_miss_pct=0.049,
                 bull_pct=0.35,outer_pct=0.6,double_pct=0.373)

unterbuchner = Player(name = 'Unterbuchner',treble_pct=0.397, single_pct=0.507, big_miss_pct=0.037,small_miss_pct=0.058,
                    bull_pct=0.35,outer_pct=0.6,double_pct=0.371)




match1 = Match(clayton,ratajski, first_to = 16)
match2 = Match(wade, unterbuchner,first_to = 16)


match1.simulate(num_sims = 100000)
match2.simulate(num_sims = 100000)


