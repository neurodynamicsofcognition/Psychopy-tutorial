import psychopy
from psychopy import core, visual, event

myWin = visual.Window((200,200), units = 'norm')
myClock = core.Clock()

myMouse = event.Mouse()

nFrame = 0
while myClock.getTime() < 17:
    nFrame+=1

    '''
    if nFrame in [100,200,300,400,500, 600, 700, 800, 900, 1000, 'hola']:
        print(f'Mouse was at pos {myMouse.getPos()} at frame {nFrame}')

    frameClock = core.Clock()
    while frameClock.getTime() < refreshRate-deltaT:
        mouse.getPos()
        
    '''
    buttons = myMouse.getPressed()
    if 1 in buttons:
        print(buttons)

    
    if myMouse.getPressed():
        print(f'Mouse Clicked with buttons')
    '''
    '''    
    myWin.flip()
#print()