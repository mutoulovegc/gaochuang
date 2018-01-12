import pygame
class GameSprite(pygame.sprite.Sprite):
    '''游戏精灵的基类'''
    def __init__(self,imaage_name,speed=1):
        #调用父类的初始方法
        super().__init__()
        #加载图像
        self.image = pygame.image.load(image_name)
        #设置尺寸
        self.rect = self.image.get_rect()
        #记录速度
        self.speed = speed
    def update(self,*args):
        #默认垂直方向移动
        self.rect.y += self.speed
