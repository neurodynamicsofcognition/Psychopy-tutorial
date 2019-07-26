import random
import collections

#Variable Parameters
nTrials = 20
nOdds = 6
nGaps = nOdds; gf = 0 #plus funal gap gf = 0
gMin = 2 # odds cannot be closer than 3 appart
gMax = gMin + 5 #nor farther than 7 

#Compute gaps between odds
X = nTrials - nOdds*(1+gMin) - gf #gap s variable room
Gaps = [gMin for i in range(nGaps)] #filled with the gm
counter = X
while counter > 0: 
    i = random.randint(0,nGaps-1)
    if Gaps[i] < gMax:
        Gaps[i] += 1
        counter -= 1
    elif Gaps[i] >= gMax:
        continue

#Define the class Trial
class Trial():
    def __init__(self):
        self.type = "None" #standard or odd
    def __str__(self): #for print
        return(self.type)
    def __repr__(self): #for indirect prints
        return(self.type)

#Translate Gaps to Trials
Trials = [None]*nTrials
binTrials = [] #binary representation of the sequence of trials
for i in range(len(Gaps)):
    binTrials+= [0]*Gaps[i] + [1]

for i in range(len(binTrials)):
    thisTrial = Trial()
    if binTrials[i] == 0:
        thisTrial.type = 'standard'
    elif binTrials[i] == 1:
        thisTrial.type = 'odd'
    Trials[i] = thisTrial

print('Lista pseudoRandomizada',[Trials[i] for i in range(nTrials)])



