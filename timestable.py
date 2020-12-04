import pygame
import math
import os


#Edit these variables
lines = 5
multiplicator = 1
#Edit these variables


#Code

#Sets the window pos to x,y
os.environ["SDL_VIDEO_WINDOW_POS"] = "580,28"

global width,widht,height,white,black
white,black = (255,255,255),(0,0,0)
widht,width,height = 1000,1000,1000

pygame.init()

screen = pygame.display.set_mode((width,height))

#Vector class
class Vector:
	def __init__(self,x,y,rot = 0,ox = width//2, oy = height//2):
		self.rot = rot
		self.x = x
		self.y = y
		self.aAcc = 0
		self.len = math.sqrt(abs((0-self.x))**2+abs((0-self.y))**2)
		self.update()

	def update(self):
		self.rotate(self.aAcc)
		self.len = math.sqrt(abs((0-self.x))**2+abs((0-self.y))**2)

	def rotate(self,deg):
		self.rot += deg
		self.y = -math.sin(-self.rot)*self.len
		self.x = -math.cos(-self.rot)*self.len

def getlines(m,size):
	vectors = []
	lines_ = []
	size = size
	vectors.append(Vector(size,0,0))

	for n in range(m-1):
		n+=1
		vectors.append(Vector(size,0,math.radians(360/m*n)))
	for vec in vectors:
		lines_.append([vec.x+width//2,vec.y+height//2])
	return lines_


def main(lines,times,size = 400):
	clock = pygame.time.Clock()
	m,k = lines,times
	lines_ = getlines(m,size)
	rang = len(lines_)
	while True:
		mx,my = pygame.mouse.get_pos()
		screen.fill(black)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_1:
					k+=1
				if event.key == pygame.K_2 and k != 1:
					k-=1
				if event.key == pygame.K_3:
					m+=1
					lines_ = getlines(m,size)
					rang = len(lines_)
				if event.key == pygame.K_4:
					m-=1
					lines_ = getlines(m,size)
					rang = len(lines_)
				if event.key == pygame.K_l:
					print(lines_)
					print(k)
					print(m)
		lines = lines_*(k*2)
		for n in range(rang):
			n+=1
			pygame.draw.line(screen,(255,0,255),(lines[n][0],lines[n][1]),(lines[n*k][0],lines[n*k][1]))
		#pygame.draw.line(screen,(255,0,255),(lines[0][0],lines[0][1]),(lines[-1][0],lines[-1][1]))


		pygame.display.update()
		clock.tick(30)

main(lines,multiplicator)
