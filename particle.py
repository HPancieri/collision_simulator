import pygame
from random import choice, uniform

MAX_VELOCITY = 5
COLORS: list[str] = ['blue', 'brown', 'cyan', 'green', 'orange', 'pink', 'red', 'white', 'yellow']


class Particle:
	id: int
	color: str
	position: list[float]
	velocity: list[float]
	radius: float = 15
	surf: pygame.Surface
	rect: pygame.Rect

	def __init__(self, id: int) -> None:
		self.id = id
		self.color = choice(COLORS)
		self.velocity = [uniform(-MAX_VELOCITY, MAX_VELOCITY) for _ in range(2)]
		# self.position = [uniform(200, 900), uniform(100, 700)]

		self.surf = pygame.image.load(f'./images/{self.color}.png').convert_alpha()
		# self.rect = self.surf.get_rect(center=(self.position[0], self.position[1]))

	def invertXSpeed(self) -> None:
		self.velocity[0] = -self.velocity[0]

	def invertYSpeed(self) -> None:
		self.velocity[1] = -self.velocity[1]

	def invertSpeed(self) -> None:
		for i in range(2):
			self.velocity[i] *= -1

	def getDistance(self, particle) -> float:
		distance: float = 0.0
		for pos1, pos2 in zip(self.position, particle.position):
			distance += (pos1 - pos2) ** 2
		distance **= 0.5
		return distance

	@staticmethod
	def getModule(vector: list[float]) -> float:
		module: float = 0.0
		for i in vector:
			module += i ** 2
		module **= 0.5
		return module

	@staticmethod
	def normalize(vector: list[float]) -> list[float]:
		normalized_vector: list[float] = []
		vector_module = Particle.getModule(vector)

		for i in vector:
			normalized_vector.append(i / vector_module)
		return normalized_vector

	@staticmethod
	def productByScalar(vector: list[float], scalar: float) -> list[float]:
		product: list[float] = []
		for i in vector:
			product.append(scalar * i)
		return product

	@staticmethod
	def dotProduct(vector1: list[float], vector2: list[float]) -> float:
		product: float = 0.0
		for i, j in zip(vector1, vector2):
			product += i * j
		return product
