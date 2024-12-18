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
			self.center = [random.randint(50,450),random.randint(-150,-50)]
			for ball in balls:
				if dist(self.center,ball.center) < 2*r:
					break 
			else:
				break
		d = random.randint(1,20) # бросаем кость
		if d==1:
			self.type = 'bomb'
			self.color = (250,50,50)
		elif d==2:
			self.type = 'freez'
			self.color = (50,50,250)
		elif d==3:
			self.type = 'bigger'
			self.color = (50,250,50)
		elif d==4:
			self.type = 'downup'
			self.color = (150,150,50)
			self.center[1] = 550
		else:
			self.type = None
			self.color = (50,50,50)

	def update(self,dt):
		self.center[1] += v*dt
		if self.type=='downup':
			self.center[1] -= 1.5*v*dt


	def draw(self):
		screen.draw.filled_circle(self.center,r,self.color)
		screen.draw.text(str(chr(self.i%27+64)),center=self.center,fontsize=64,color=(250,250,250))

	def kill(self):
		global v,r
		if self.type=='bomb':
			balls.pop(0)
			balls.append(Ball())
			balls.pop(0)
			balls.append(Ball())
			for ball in balls:
				ball.i -= 2
		elif self.type=='freez':
			v = v/2
		elif self.type=='bigger':
			if r<100:
				r += 20
		balls.pop(0)
		balls.append(Ball())

def draw():
	screen.fill((10,20,30))
	for ball in reversed(balls):
		ball.draw()

def update(dt):
	global v,r
	v = v + 5*dt
	if r>20:
		r -= 1*dt 
	for ball in balls:
		ball.update(dt)
	# d = random.randint(1,50)
	# if d==1:
	# 	balls[0].change()

def on_mouse_down(pos):
	ball = balls[0]
	if dist(ball.center, pos) < r:
		ball.kill()


def restart():
	global r,v,balls
	r = 50
	v = 100
	balls = []
	for _ in range(5):  # повтори пять раз
		balls.append(Ball())

restart()
pgzrun.go()
