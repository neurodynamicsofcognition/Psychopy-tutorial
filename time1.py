
#import psychopy
from psychopy import core, visual

myClock = core.Clock()
myWin = visual.Window()
print(f'clock time: {myClock.getTime()}')
counter = 0

while myClock.getTime() < 10: 
    
    counter += 1

    #stim.draw()

    myWin.flip()

print('Resultado')
print(f'counter: {counter}')
print(f'clock time: {myClock.getTime()}')
print(f'monitor FramePeriod = {myWin.monitorFramePeriod}')


'''
class auto(object):
	def __init__(self, nRuedas, color):
		self.nRuedas = nRuedas
		self.color = color
	def pintar(self, colorFinal):
		self.colorViejo = self.color
		self.color = colorFinal
	def nEjes(self, nRuedas):
		self.nEjes = nRuedas/2
	def printea():
		print('hola')



a = auto(4,'rojo')
print(a)
print(a.color, a.nRuedas)

a.pintar('negro')
print(' ')
print(a.color, a.nRuedas)

auto.printea()

'''
