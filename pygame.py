import pygame
import sys
import hero
import monster
pygame.init()  # 初始化pygame
size = width, height = 640, 480  # 设置窗口大小
screen = pygame.display.set_mode(size)  # 显示窗口
color = (0, 0, 0)
NewHero =hero.Hero("神")
NewMonster=monster.Monster()
herorect = NewHero.hero.get_rect()
screen.blit(NewHero.hero,(150,260))
pygame.display.update()
clock = pygame.time.Clock()
speed = [5, 5]
while True:  # 死循环确保窗口一直显示
    clock.tick(60)
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.K_DOWN:
                print("向下")
                herorect = herorect.move([0,5])#向下移动



    #


    screen.fill(color)

    screen.blit(NewHero.hero, herorect)
    pygame.display.flip()
pygame.quit()
