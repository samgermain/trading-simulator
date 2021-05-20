import os, pygame
import pygame.midi
from settings import Settings
import json

class Game():
	def __init__(self):
		self.font = myfont = pygame.font.SysFont('Helvetica', 15)
		self.startTime = None
		self.state = "stopped"
		pygame.midi.init()

	def start(self, t):
		self.state='trading'
		if not self.startTime:
			self.startTime = t

	def restart(self):
		self.state = "stopped"
		self.startTime = None				

	def stop(self):
		self.state = "stopped"

	def save(self):
    	#TODO: Actually save something
		self.state = "stopped"
		print('saved')

	def drawToScreen(self, screen, dataFile):
		graphBottomY = Settings.height / 2 + 127/2
		screen.fill((0, 0, 0))
		text = self.font.render('.', False, (255, 255, 255))
		for signal in self.signals:
			t, h = signal
			x = t/10
			y = graphBottomY - h*2
			screen.blit(text, (x,y))

	def loop(self, screen):
    	
		fileName="assets/json/ada_usdt-15m.json"
		with open(fileName, "rb") as file:
			candleData = json.load(file)

		clock = pygame.time.Clock()
		signals = []

		r = lambda: None
		r.left = 50
		r.top = 50
		r.width = 50
		r.height = 100

		high = 10
		low = 10

		rect = pygame.Rect(r.left, r.top, r.width, r.height)
		#rect = pygame.Rect(50,50,50,100)
		pygame.draw.rect(screen, 'green', rect)
		pygame.draw.lines(screen, 'green', True, [(rect.x + r.width/2, rect.y - high ), (rect.x + r.width/2, rect.y + rect.height + low)])

		while True:

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return
			pygame.display.update()

	def quit(self):
		pass