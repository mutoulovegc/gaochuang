import pygame
from plane_sprites import *

class PlaneGame():
	"""飞机大战主游戏类"""

	def __init__(self):
		"""初始化游戏"""
		#1.窗口
		self.screen = pygame.display.set_mode((SCREEN_RECT.size))
		#2.创建游戏时中
		self.clock = pygame.time.Clock()
		#3.背景敌机精灵英雄
		self.__creat_sprites()

	def start_game(self):
		"""开始游戏"""
		print('开始游戏')

		while True:
			#1.设置帧率
			self.clock.tick(60)
			#2.事件监听
			self.__event_handler()
			#3.碰撞检测
			self.__check_collide()
			#4.更新精灵组
			self.__update_sprites()
			#5.更新屏幕		
			pygame.display.update()
	def __event_handler(self):
		"""监听事件"""
		for event in pygame.event.get():

			if event.type == pygame. QUIT:
				PlaneGame.__game_over()



	@staticmethod
	def __game_over(self):
		pygame.quit()
		exit()

	def __check_collide(self):
		"""碰撞检测"""
		pass
	def __update_sprites(self):
		"""更新精灵组"""
		pass


	def __creat_sprites(self):
		pass

if __name__ == '__main__':
	#创建游戏对象
	game = PlaneGame()
	#开始游戏
	game.start.game()



