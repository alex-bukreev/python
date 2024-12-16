import pgzrun
import random
WIDTH = 500
HEIGHT = 500

def dist(A,B):
	return ((A[0]-B[0])**2+(A[1]-B[1])**2)**0.5

class Ball():

	def __init__(self):
		if balls==[]:
			self.i = 1
		else:
			self.i = balls[-1].i + 1
		for _ in range(1000):
			self.center = [random.randint(50,450),random.randint(-250,-50)]
			for ball in balls:
				if dist(self.center,ball.center) < 2*r:
					break 
			else:
				break
		d = random.randint(1,10)
		if d==1:
			self.type = 'bomb'
			self.color = (250,50,50)
		elif d==2:
			self.type = 'freez'
			self.color = (50,50,250)
		elif d==3:
			self.type = 'bigger'
			self.color = (50,250,50)
		else:
			self.type = None
			self.color = (50,50,50)

	def update(self,dt):
		self.center[1] += v*dt

	def draw(self):
		screen.draw.filled_circle(self.center,r,self.color)
		screen.draw.text(str(self.i),center=self.center,fontsize=64,color=(250,250,250))

	def kill(self):
		global v,r
		if self.type=='bomb':
			balls.pop(0)
			balls.append(Ball())
			balls.pop(0)
			balls.append(Ball())
		elif self.type=='freez':
			v = v/2
		elif self.type=='bigger':
			r = r + 10
		balls.pop(0)
		balls.append(Ball())


restart()
pgzrun.go()
