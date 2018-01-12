import pygame

pygame.init()

#display (窗口)类

#set_mode（）方法初始化我们的游戏窗口

#update（）方法 刷新我们的屏幕

screen = pygame.display.set_mode((480,700))

#image.load

#步骤1加载图片数据

bg = pygame.image.load("/home/gao/图片/images/background.png")

#步骤2绘制图片数据

screen.blit(bg,(0,0))

#步骤一加载图片数据

hero_me = pygame.image.load("/home/gao/图片/images/life.png")

#步骤2绘制到屏幕上


#设置英雄初始位置

hero_rect = pygame.Rect(200,600,102,126)

screen.blit(hero_me,hero_rect)
#步骤三更新显示

pygame.display.update()

#游戏时钟

clock = pygame.time.Clock()

while True:

    #设置帧率

    clock.tick(60)
    #捕获事件
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print("退出游戏")
   # if hero_rect.y == 0:
    #    hero_rect.y = 600
    #else:
     #   hero_rect.y = hero_rect.y - 1
    #screen.blit(bg,(0,0))
    #screen.blit(hero_me,hero_rect)
    pyname.quit()
    exit()
