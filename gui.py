import psychopy
from psychopy import gui, core, visual


guiDict = {'nombre': '', 'edad': ''}

myDialogGUI = gui.DlgFromDict(guiDict, title = "Mi Ventana de Dialogo") #labels, checkBoxes, defaultValues

if myDialogGUI.OK:
    print(guiDict)
else:
    print('Not Ok')


'''
myWin = visual.Window()
myClock = core.Clock()
while myClock.getTime() < 20:

    myDialogGUI = gui.DlgFromDict(guiDict) 
    
    if myDialogGUI.OK:
        print(guiDict)
    else:
        print('Not Ok')

    myWin.flip()
'''

