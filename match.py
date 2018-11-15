import numpy as np

class Match:
    
    def __init__(self,player1,player2,first_to=10):
        
        self.player1 = player1
        self.player2 = player2
        self.playerDict = {0:self.player1, 1:self.player2}
        self.first_to = first_to
        self.score = (0,0)
        self.TOT_LEGS1 = 0
        self.WINNER1 = 0
        self.SCORES1 = []
        self.LEGS_LIST1 = []
        self.TOT_LEGS2 = 0
        self.WINNER2 = 0
        self.SCORES2 = []
        self.LEGS_LIST2 = []
    
    def reset(self):
        self.player1.reset()
        self.player2.reset()
        self.score = (0,0)
        
    def playLeg(self, p=0):
        
        while not self.legEnded():
            #print(self.player1.score, self.player2.score)
            self.playerDict[p%2].throw()
            p +=1 
            
        self.updateScore()
        
    def legEnded(self):
        
        if (self.player1.score==0) or (self.player2.score==0):
            return 1
        else:
            return 0
        
    def updateScore(self):
        (a,b) = self.score
        if self.player1.score == 0:
            a +=1
        if self.player2.score == 0:
            b +=1
        self.score = (a,b)
        #print(self.score)
            
            
    def playMatch(self, q=0):
        
        while not self.matchEnded():
            #print('\n Leg ', q+1, '\n')
            self.playLeg(p=q%2)
            self.player1.reset()
            self.player2.reset()
            q+=1
        
    
    def matchEnded(self):
        if max(self.score) == self.first_to:
            return 1
        else:
            return 0
    
    def update_statistics1(self):
        # update stats for if player 1 throws 1st in 1st leg
        if self.matchEnded()==1:
            
            # evaluate match winner and record if p1 wins
            if self.score[0] == self.first_to:
                self.WINNER1 += 1
                
            # record number of legs in this iteration    
            tot_legs = self.score[0]+self.score[1]
            self.LEGS_LIST1.append(tot_legs)
            
            # update total legs in iterations completed so far
            self.TOT_LEGS1 += tot_legs
            
            # record final score of this iteration
            self.SCORES1.append(self.final_score())
    
    def update_statistics2(self):
        # update stats for if player 2 throws 1st in 1st leg
        if self.matchEnded()==1:
            
            # evaluate match winner and record if p1 wins
            if self.score[0] == self.first_to:
                self.WINNER2 += 1
                
            # record number of legs in this iteration    
            tot_legs = self.score[0]+self.score[1]
            self.LEGS_LIST2.append(tot_legs)
            
            # update total legs in iterations completed so far
            self.TOT_LEGS2 += tot_legs
            
            # record final score of this iteration
            self.SCORES2.append(self.final_score())
        
            
    def final_score(self):
        return str(self.score)
            
    def odds(self,prob): 
        # converts probability to decimal odds
        if prob == 0:
            return 1000000
        else:
            return 1/prob
        
    def simulate(self, num_sims = 10000):
        
        for i in range(int(num_sims/2)):
            if i%1000 == 0: # to track progress of simulation
                print('Iteration: ', i+1)
                
            # simulate with p1 to throw first in 1st leg
            self.playMatch()
            self.update_statistics1()
            self.reset()
        
        for i in range(int(num_sims/2)):
            if i%1000 == 0: # to track progress of simulation
                print('Iteration: ', int(num_sims/2+i+1))
            
            # simulate with p2 to throw first in 1st leg
            self.playMatch(q=1) 
            self.update_statistics2()
            self.reset()
            
        ### For player1 to throw 1st in 1st leg   
        # Display win odds           
        print('\n',self.player1.name,' TO THROW FIRST: \n')
        print(self.player1.name,' win odds: ',  "{0:.4f}".format(self.odds(2*self.WINNER1/num_sims)))
        print(self.player2.name,' win odds: ',  "{0:.4f}".format(self.odds((num_sims-2*self.WINNER1)/num_sims)))
        print('Average no. of legs: ', "{0:.4f}".format(2*self.TOT_LEGS1/num_sims))
        
        # Display correct score odds
        unique_scores1 = list(set(self.SCORES1))
        unique_scores1.sort()
        for el in unique_scores1:
            print(el, ' odds: ', "{0:.4f}".format(self.odds(self.SCORES1.count(el)/len(self.SCORES1))))
            
        # Display Over/under no of legs odds
        unique_legs1 = list(set(self.LEGS_LIST1))
        unique_legs1.sort()
        leg_freq = []
        for el in unique_legs1:
            leg_freq.append(self.LEGS_LIST1.count(el)/len(self.LEGS_LIST1))    
        cum_leg_freq = np.cumsum(leg_freq)
        for i in range(len(unique_legs1)-1):
            line = (unique_legs1[i]+unique_legs1[i+1])/2
            unders = cum_leg_freq[i]
            overs = 1-unders
            print('Under/Over', line,':', "{0:.4f}".format(self.odds(unders)),'/',"{0:.4f}".format(self.odds(overs)))
        
        ### For player2 to throw 1st in 1st leg   
        # Display win odds
        print('\n',self.player2.name,' TO THROW FIRST: \n')
        print(self.player1.name,' win odds: ',  "{0:.4f}".format(self.odds(2*self.WINNER2/num_sims)))
        print(self.player2.name,' win odds: ',  "{0:.4f}".format(self.odds((num_sims-2*self.WINNER2)/num_sims)))
        print('Average no. of legs: ', "{0:.4f}".format(2*self.TOT_LEGS2/num_sims))

        # Display correct score odds
        unique_scores2 = list(set(self.SCORES2))
        unique_scores2.sort()
        for el in unique_scores2:
            print(el, ' odds: ', "{0:.4f}".format(self.odds(self.SCORES2.count(el)/len(self.SCORES2))))
        
        # Display Over/under no of legs odds
        unique_legs2 = list(set(self.LEGS_LIST2))
        unique_legs2.sort()
        leg_freq = []
        for el in unique_legs2:
            leg_freq.append(self.LEGS_LIST2.count(el)/len(self.LEGS_LIST2))    
        cum_leg_freq = np.cumsum(leg_freq)
        for i in range(len(unique_legs2)-1):
            line = (unique_legs2[i]+unique_legs2[i+1])/2
            unders = cum_leg_freq[i]
            overs = 1-unders
            print('Under/Over', line,':', "{0:.4f}".format(self.odds(unders)),'/',"{0:.4f}".format(self.odds(overs)))
        
        ### Overall with each player throwing 1st leg equal amount           
        WINNER = self.WINNER1 + self.WINNER2
        SCORES = self.SCORES1 + self.SCORES2
        LEGS_LIST = self.LEGS_LIST1 + self.LEGS_LIST2
        
        # Display win odds
        print('\n OVERALL: \n')
        print(self.player1.name,' win odds: ',  "{0:.4f}".format(self.odds(WINNER/num_sims)))
        print(self.player2.name,' win odds: ',  "{0:.4f}".format(self.odds((num_sims-WINNER)/num_sims)))
        print('Average no. of legs: ', "{0:.4f}".format((self.TOT_LEGS1+self.TOT_LEGS2)/num_sims))

        # Display correct score odds
        unique_scores = list(set(SCORES))
        unique_scores.sort()
        for el in unique_scores:
            print(el, ' odds: ', "{0:.4f}".format(self.odds(SCORES.count(el)/len(SCORES))))
            
        # Display Over/under no of legs odds
        unique_legs = list(set(LEGS_LIST))
        unique_legs.sort()
        leg_freq = []
        for el in unique_legs:
            leg_freq.append(LEGS_LIST.count(el)/len(LEGS_LIST))    
        cum_leg_freq = np.cumsum(leg_freq)
        for i in range(len(unique_legs)-1):
            line = (unique_legs[i]+unique_legs[i+1])/2
            unders = cum_leg_freq[i]
            overs = 1-unders
            print('Under/Over', line,':', "{0:.4f}".format(self.odds(unders)),'/',"{0:.4f}".format(self.odds(overs)))

        
        