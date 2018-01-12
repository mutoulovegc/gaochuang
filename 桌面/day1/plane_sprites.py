import pygame


#游戏屏幕的大小
SCREEN.RECT = pygame.Rect(0,0,480,700)

class GameSprite(pygame.sprite.Sprite):
	'''基类'''
	def __init__(self,imaga_name,speed=1):
		super().__init__()

		self.image_name = pygame.image.load(image_name)
		self.speed = speed
		self.rect = self.image_name.get_rect()

	def update(self):
		self.rect.y += self.speed


class Hero(GameSprite):
	'''英雄类'''
	def __init__(self,image_name,speed=0):
		super().__init__(image_name,speed)

	def update(self):
		pass

class Background(GameSprite):
	'''背景类'''
	def __init__(self,image_name,speed=1):
		super().__init__(image_name)

	def update(self):
		pass
