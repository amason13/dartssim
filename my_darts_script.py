from dartssim.match import Match
from dartssim.player import Player

#### Todays 1st match
clayton = Player(name = 'Clayton', treble_pct=0.38, single_pct=0.522, big_miss_pct=0.038,small_miss_pct=0.061,
                    bull_pct=0.35,outer_pct=0.6,double_pct=0.328)

ratajski = Player(name = 'Ratajski', treble_pct=0.371, single_pct=0.544, big_miss_pct=0.034,small_miss_pct=0.051,
                    bull_pct=0.35,outer_pct=0.6,double_pct=0.354)

#### 2nd match
wade = Player(name = 'Wade', treble_pct=0.393, single_pct=0.545, big_miss_pct=0.024,small_miss_pct=0.038,
                 bull_pct=0.35,outer_pct=0.6,double_pct=0.398)

unterbuchner = Player(name = 'Unterbuchner')#,treble_pct=0.408, single_pct=0.521, big_miss_pct=0.026,small_miss_pct=0.045,
                    #bull_pct=0.35,outer_pct=0.6,double_pct=0.362)

#### 3rd match
anderson = Player(name = 'Anderson', treble_pct=0.444, single_pct=0.471, big_miss_pct=0.035,small_miss_pct=0.05,
                    bull_pct=0.35,outer_pct=0.6,double_pct=0.385)

harms = Player(name = 'Harms')#, treble_pct=0.356, single_pct=0.56, big_miss_pct=0.03,small_miss_pct=0.055,
                    #bull_pct=0.35,outer_pct=0.6,double_pct=0.344)

#### 4th match
smith = Player(name = 'Smith', treble_pct=0.419, single_pct=0.518, big_miss_pct=0.026,small_miss_pct=0.036,
                    bull_pct=0.35,outer_pct=0.6,double_pct=0.371)

vangerwen = Player(name = 'Van Gerwen', treble_pct=0.469, single_pct=0.474, big_miss_pct=0.026,small_miss_pct=0.03,
                    bull_pct=0.35,outer_pct=0.6,double_pct=0.428)




match1 = Match(clayton,ratajski)
match2 = Match(wade, unterbuchner)
match3 = Match(anderson, harms)
match4 = Match(smith, vangerwen)

match1.simulate(num_sims = 10000)
#match2.simulate(num_sims = 10000)
#match3.simulate(num_sims = 10000)
match4.simulate(num_sims = 10000)
