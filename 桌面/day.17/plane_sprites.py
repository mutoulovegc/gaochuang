import random
import pygame
SCREEN_RECT = pygame.Rect(0,0,480,700)
SCREEN_EVENT = pygame.USEREVENT
class GameSprite(pygame.sprite.Sprite):
    def __int__(self,image_name,speed=1):
        #调用父类的方法
        super().__int__()
        #加载图像
        self.image = pygame.image.load(image_name)
        #设置尺寸
        self.rect = pygame.image.get_rect()
        #记录速度
        self.speed = speed
    def update():
        self.rect.y += self.speed
class Backgroup(GameSprite):
    def update(self):
        super().update()
        if self.rect.y >= SCREEN.RECT.height:
            self.rect.y = -SCREEN.RECT.height
class Enemy(GameSprite):
    def __init__(self):
        super().__init__("/home/gao/图片/images/enemy1.png")
        #设置敌机得初始速度
        self.speed = random.randint(1,3)
        #设置敌机的基础初始位置
        self.rect.x = random.randint(0,SCREEN.RECT.width - self.rect.width)
        def update(self):
            super().update()
            #判断是否飞出屏幕
            if self.rect.y >= SCREEN.RECT.height:
                self.kill()
class Hero(GameSprite):
    def __init__(self):
        super().__init__("/home/gao/图片/images/me1.png")
        #设置初始位置
        self.centerx = SCREEN.RECT.center.x
        self.bottom = SCREEN.RECT.bottom - 120
    def update(self):
        self.rect.x += self.speed
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN.RECT.right:
            self.rect.right = SCREEN.RECT.right
