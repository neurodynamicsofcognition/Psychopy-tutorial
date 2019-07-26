class Trial():
    """Data container"""
    def __init__(self):
        self.type = "None" #standard or odd

#Definir la estructura trials
#"relleando desde trials vacíos"
nTrials = 100
n_odds = 25
Trials = []

for trialIdx in range(nTrials):
    thisTrial = Trial()
    if trialIdx < n_odds:
        thisTrial.type = 'odd'
    else:
        thisTrial.type = 'standard'
    Trials.append(thisTrial)

print('Lista recien creada: ')
print([Trials[i].type for i in range(nTrials)])

#aleatorizar secuencia
#   sin requisitos
import random
random.shuffle(Trials)
print('\nLista aleatorizada base: ')
print([Trials[i].type for i in range(nTrials)])

#   con distancia minima entre odds = 2
#   	fuerza bruta
import random
for i in range(1000):
    random.shuffle(Trials)

    #guarda el indice de todos los odds
    oddIdxs = []
    for trialIdx, trial in enumerate(Trials):
        if trial.type == 'odd':
            oddIdxs.append(trialIdx)

    #checkea distancia
    dmin = min([oddIdxs[i+1] - oddIdxs[i] for i in range(len(oddIdxs)-1)]) #n_odds -1
    if dmin > 10:
        break


print('\nLista aleatorizada fuerza bruta: ')
print([Trials[i].type for i in range(nTrials)])		


