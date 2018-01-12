#使用python 我们先导入这个包
import pygame
from plane_sprites import *
class PlaneGame():
    def __init__(self):
        """游戏初始化"""
        #1.创建游戏窗口pygame.display.set_mode 创建游戏窗口需要宽和高
        #.size取宽高 x取x轴的值 y取y轴的值
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        #2.创建游戏时钟pygame.time.Clock()会返回给我们一个时钟对象
        self.clock = pygame.time.Clock()
        #3.调用私有方法 里面的创建精灵和精灵组
        self.__create_sprites()
        #4.设置定时器事件 每秒创建一架敌机
        pygame.time.set_timer(SCREEN_RECT1,1000)
        #5.每隔0.5秒发射一个豆豆
        pygame.time.set_timer(HERO_FIRE_EVENT,500)
    def start_game(self):
        print("开始游戏")
        while True:
            #1.设置帧率
            self.clock.tick(60)
            #2.事件监听
            self.__event_handler()
            #3.碰撞检测
            self.__check_collide()
            #4.更新精灵组
            self.__update_sprites()
            #5.更新屏幕显示
            pygame.display.update()

    def __create_sprites(self):
        """创建精灵和精灵组"""
        #pygame.sprute.Group()可以创建一个精灵组
        #创建背景精灵组
        bg1 = Backgroup("/home/gao/图片/images/background.png")
        bg2 = Backgroup("/home/gao/图片/images/background.png")
        bg2.rect.y = -bg2.rect.height
        #1.背景组
        self.back_group = pygame.sprite.Group(bg1,bg2)
        #2.敌机组self.enemy_group = []
        self.enemy_group = pygame.sprite.Group()
        #3.英雄组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)
        #创建子弹精灵
        self.bullets = pygame.sprite.Group()
    def __event_handler(self):
        """事件监听的方法"""
        for event in pygame.event.get():
            #当列表里面有pygame.QUIT这个值的时候说明用户
            if event.type == pygame.QUIT:
                #调用静态私有方法
                PlaneGame.__game_over()
            elif event.type == SCREEN_RECT1:
                self.enemy_group.add(Enemy())
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            #获取用户按键
            #elif event.type == pygame.KEYDOWN and event.key == pygame.KEYDOWN
            #    print ("向右面移动")
            #另外一个方案  返回所有按键的元祖 如果某个按键按下对应的值
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_RIGHT]:
                print("向右面移动")
                self.hero.speed = 2
            elif keys_pressed[pygame.K_LEFT]:
                self.hero.speed = -2
                print("像左面移动")
            else:
                self.hero.speed = 0

    def __check_collide(self):
        """碰撞检测的方法"""
        #1.子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)
        #2.英雄撞到敌机
        enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
        #判断是否有内容
        if len(enemies)>0:
            #让英雄牺牲
            self.hero.kill()
            #结束游戏
            self.__game_over()
    def __update_sprites(self):
        """更新精灵组"""
        for group in [self.back_group,self.enemy_group,self.hero_group,self.hero.bullets]:
            #更新精灵组里面所有精灵的位置
            group.update()
            group.draw(self.screen)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)
    @staticmethod
    def __game_over(self):
        """游戏结束了"""
        print("游戏结束了")
        pygame,quit()
        exit()
#一般情况下 比如有一个场景 测试
if __name__ == "__main__":
    #1.创建游戏
    game = PlaneGame()
    #开始游戏
    game.start_game()
