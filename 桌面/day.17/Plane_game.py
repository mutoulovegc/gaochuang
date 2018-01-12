import pygame
from plane_sprites import *
class PlayGame():
    def __init__(self):
        print("游戏初始化")
    
        #1.创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        #2.创建游戏时钟
        self.clock = pygame.time.Clock()
        #3.创建精灵组
        self.__creat_sprites()
        pygame.time.set_timer(SCREEN_EVENT,1000)
    def star_game(self):
        print("游戏开始")
        while True:
            #设置刷新帧率
            self.clock.tick(60)
            #事件监听
            self.__event_handler()
            #碰撞检测
            self.__check_collide()
           
            #更新绘制精灵组
            self.__update_sprites()
            #更新屏幕显示
            pygame.display.update()
    def __creat_sprites(self):
        #背景组
        bg1 = Backgroup("/home/gao/图片/images/background.png")
        bg2 = Backgroup("/home/gao/图片/images/background.png")
        bg2.rect.y = -bg2.rect.height
        self.back_group = pygame.sprite.Group(bg1,bg2)
        #敌机组
        
        self.enemy_group = pygame.sprite.Group()
        #英雄组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)
    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == SCREEN_EVENT:
                self.enemy_group.add(Enemy())
    def __check_collide(self):
        pass
    def __update_sprites(self):
        for group in [self.back_group,self.enemy_group,self.hero_group]:
            group.update()
            group.draw(self.screen)       




    @staticmethod
    def __game_over(self):
        print("游戏结束了")
        pygame.quit()
        exit()
if __name__ == "__main__":
    game = PlayGame()
    game.star_game()
