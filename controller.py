import pygame
from sys import exit
from particle import Particle
from random import uniform


class Controller:
	particle_list: list[Particle]
	numberOfParticles: int

	# Game initialization
	def __init__(self) -> None:
		pygame.init()

		self.particle_list = []

		# Number of particles definition
		self.numberOfParticles = 10

		# Clock initialization
		self.clock = pygame.time.Clock()

		# Screen settings
		self.screen = pygame.display.set_mode((1100, 800))
		pygame.display.set_caption('Collision Simulator')

		# for i in range(self.numberOfParticles):
		# 	self.particle_list.append(Particle(i))

		# Spawning particles
		self.spawnParticles()

	def update(self) -> None:
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()

			# Screen redefinition
			self.screen.fill((0, 0, 0))

			# Collision detection
			self.particleCollision()

			# Object moving
			self.object_moving()

			pygame.display.update()
			self.clock.tick(60)

	def spawnParticles(self) -> None:
		for i in range(self.numberOfParticles):
			new_particle = Particle(i)
			new_particle.position = [uniform(200, 900), uniform(100, 700)]

			if self.particle_list:
				for j in self.particle_list:
					distance = new_particle.getDistance(j)
					while distance <= new_particle.radius + j.radius:
						new_particle.position = [uniform(200, 900), uniform(100, 700)]

			self.particle_list.append(new_particle)
			new_particle.rect = new_particle.surf.get_rect(center=(new_particle.position[0], new_particle.position[1]))

	def object_moving(self) -> None:
		if self.particle_list:
			for particle in self.particle_list:
				if particle.rect.top < 0: particle.invertYSpeed()
				if particle.rect.bottom > 800: particle.invertYSpeed()
				if particle.rect.left < 0: particle.invertXSpeed()
				if particle.rect.right > 1100: particle.invertXSpeed()

				for i in range(2):
					particle.position[i] += particle.velocity[i]

				particle.rect.x = particle.position[0]
				particle.rect.y = particle.position[1]

				self.screen.blit(particle.surf, particle.rect)

	def particleCollision(self) -> None:
		for i, particle1 in enumerate(self.particle_list):
			for particle2 in self.particle_list[i+1:]:
				distance = particle1.getDistance(particle2)
				if distance <= particle1.radius + particle2.radius:
					particle1.invertSpeed()
					particle2.invertSpeed()
