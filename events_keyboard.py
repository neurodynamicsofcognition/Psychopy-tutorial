import psychopy
from psychopy import core, visual, event

myWin = visual.Window()
myClock = core.Clock()

nFrame = 0
while myClock.getTime() < 10:
    nFrame+=1

    
    if 'k' in event.getKeys() :
        print(f'key "K" pressed at frame: {nFrame} at time: {myClock.getTime()}')

    '''
    if len(event.getKeys()) != 0:
        print(event.getKeys())
    
    
    pressedKeys = event.getKeys()
    if len(pressedKeys) != 0:
        print(pressedKeys)
    '''

    myWin.flip()
#print("total number of frames and time elapsed: ", nFrame, myClock.getTime())