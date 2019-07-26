

class Trial():
    """Data container for each trial storing data related to
    for presenting thing durin the trial and stornig info 
    about subject's responses during the trial"""
    def __init__(self, tipo = 'standard' ):
        self.type = tipo #'standard' #vs odd
        self.response = None #correct /incorrect
        self.rt = None
        self.duration = 3.2 #segundos


t1 = Trial(tipo ='training')
print(t1.rt)
t1.rt = 1.14
print(t1.rt)
