import psychopy
from psychopy import core, visual, gui


myWin = visual.Window()
myClock = core.Clock()

counter = 0

while myClock.getTime() < 10:
    
    counter+=1

    myWin.flip()

print(f'counter: {counter}')

print(f'monitor FramePeriod = {myWin.monitorFramePeriod}')

