import pygame
from pygame import locals
from pygame.locals import *  # 导入pygame的静态模块locals

WINDOW_WIDTH = 512
WINDOW_HEIGHT = 768


def main():
    x = WINDOW_WIDTH // 2 - 50
    y = WINDOW_HEIGHT - 200
    # 开始
    pygame.init()
    # 窗口大小
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    # 加载内存
    image = pygame.image.load("res\\img_bg_level_1.jpg")

    # 飞机
    plane_main = pygame.image.load("res\\hero.png")

    while True:
        # 背景图
        window.blit(image, (0, 0))
        window.blit(plane_main, (x, y))
        pygame.display.update()

        # 获取新事件
        for event in pygame.event.get():
            # 1. 鼠标点击关闭窗口事件
            if event.type == QUIT:
                print("点击关闭窗口按钮")
                sys.exit()  # 关闭程序
                pygame.quit()  # 退出pygame，清理pygame占用资源

            # 3. 键盘长按事件
            # 获取当前键盘所有按键的状态（按下/没有按下），返回bool元组  (0, 0, 0, 0, 1, 0, 0, 0, 0)
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_a] or pressed_keys[K_LEFT]:
            x -= 2
        if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
            x += 2
        if pressed_keys[K_w] or pressed_keys[K_UP]:
            y -= 2
        if pressed_keys[K_s] or pressed_keys[K_DOWN]:
            y += 2


if __name__ == '__main__':
    main()
