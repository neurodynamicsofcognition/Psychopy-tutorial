from psychopy import core, visual, event

class Trial():
	def __init__(self, tipo):
		self.type = tipo
		self.duration = 2
	def __str__(self):
		return(f'Trial tipo: {self.type}')

nTrials = 10
Trials = [Trial('standard')]*2 + [Trial('odd')] + [Trial('standard')]*4 + [Trial('odd')] + [Trial('standard')]


ventana = visual.Window()
stim_odd = visual.ShapeStim(ventana, vertices = ((-0.3,-0.3),(0.3,-0.3),(-0.3,0.3),(0.3,0.3)), fillColor = (0,1,0) )
stim_std = visual.ShapeStim(ventana, vertices = ((-0.3,-0.3),(0.3,-0.3),(-0.3,0.3),(0.3,0.3)), fillColor = (0.2,0.2,0.2) )
reloj = core.Clock()
respuestas = [None]*nTrials

trialIdx = 0
for trial in Trials:
	
	relojTrial = core.Clock()
	while relojTrial.getTime() < trial.duration:

		if trial.type == 'odd' and relojTrial.getTime() > trial.duration*0.3:
			stim_odd.draw()
		elif trial.type == 'standard' and relojTrial.getTime() > trial.duration*0.3:
			stim_std.draw()

		keys = event.getKeys()
		if trial.type == 'standard' and 'o' in keys:
			respuestas[trialIdx] = 'incorrecta'
		elif trial.type == 'odd' and 'p' in keys:
			respuestas[trialIdx] = 'incorrecta'
		elif trial.type == 'standard' and 'p' in keys:
			respuestas[trialIdx] = 'correcta'
		elif trial.type == 'odd' and 'o' in keys:
			respuestas[trialIdx] = 'correcta'


		if 'q' in keys:
			core.quit()
			quit()

		
		ventana.flip()
	trialIdx += 1
print(f'Respuestas: {respuestas}')
