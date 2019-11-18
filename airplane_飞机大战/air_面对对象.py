import pygame
from pygame import locals
from pygame.locals import *  # 导入pygame的静态模块locals

WINDOW_WIDTH = 512
WINDOW_HEIGHT = 768


class Hero(object):
    # 创建英雄飞机类
    def __init__(self, img_path, x, y, window):
        self.img = pygame.image.load(img_path)
        self.x = x
        self.y = y
        self.window = window

    def dispaly(self):
        # 贴图
        self.window.blit(self.img, (self.x, self.y))


def main():
    # 开始
    pygame.init()
    # 窗口大小
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    # 加载内存
    image = pygame.image.load("res\\img_bg_level_1.jpg")

    # 飞机一
    plane_main = Hero("res\\hero.png", WINDOW_WIDTH // 2 - 150, WINDOW_HEIGHT - 200, window)
    # 飞机二
    plane_main2 = Hero("res\\hero2.png", WINDOW_WIDTH // 2 + 50, WINDOW_HEIGHT - 200, window)
    while True:
        # 背景图
        window.blit(image, (0, 0))
        # 贴飞机图
        plane_main.dispaly()
        plane_main2.dispaly()
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

        if pressed_keys[K_a]:
            plane_main.x -= 2
        if pressed_keys[K_LEFT]:
            plane_main2.x -= 2
        if pressed_keys[K_d]:
            plane_main.x += 2
        if pressed_keys[K_RIGHT]:
            plane_main2.x += 2
        if pressed_keys[K_w]:
            plane_main.y -= 2
        if pressed_keys[K_UP]:
            plane_main2.y -= 2
        if pressed_keys[K_s]:
            plane_main.y += 2
        if pressed_keys[K_DOWN]:
            plane_main2.y += 2

        # 加载背景音乐
        pygame.mixer.music.load("./res/bg2.ogg")


if __name__ == '__main__':
    main()
