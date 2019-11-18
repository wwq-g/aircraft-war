import pygame
from pygame.locals import *  # 导入pygame的静态模块locals

WINDOW_WIDTH = 512
WINDOW_HEIGHT = 768


# 子弹类
class HeroBullet(object):
    def __init__(self, img_path, x, y, window):
        self.img = pygame.image.load(img_path)
        self.x = x
        self.y = y
        self.window = window

    def display(self):
        self.window.blit(self.img, (self.x, self.y))

    def move(self):
        self.y -= 3




class HeroPlane(object):
    # 创建英雄飞机类
    def __init__(self, img_path, x, y, window):
        self.img = pygame.image.load(img_path)
        self.x = x
        self.y = y
        self.window = window
        self.bullets = []

    def dispaly(self):
        # 贴图
        self.window.blit(self.img, (self.x, self.y))

    def move_left(self):
        if self.x >= 3:
            self.x -= 3

    def move_right(self):
        if self.x <= 409:
            self.x += 3

    def move_up(self):
        if self.y >= 3:
            self.y -= 3

    def move_down(self):
        if self.y <= 699:
            self.y += 3

    def fire(self):
        bullet = HeroBullet("res\\bullet_1.png", self.x + 40, self.y - 31, self.window)
        self.bullets.append(bullet)

    def display_bullets(self):

        for bullet in self.bullets:
            bullet.display()
            bullet.move()



def main():
    # 开始
    pygame.init()
    # 窗口大小
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    # 加载内存
    image = pygame.image.load("res\\img_bg_level_1.jpg")

    # 飞机一
    plane_main = HeroPlane("res\\hero.png", WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT - 200, window)

    while True:
        # 背景图
        window.blit(image, (0, 0))
        # 贴飞机
        plane_main.dispaly()
        # 贴子弹
        plane_main.display_bullets()
        # 刷新
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
            plane_main.move_left()
        if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
            plane_main.move_right()
        if pressed_keys[K_w] or pressed_keys[K_UP]:
            plane_main.move_up()
        if pressed_keys[K_s] or pressed_keys[K_DOWN]:
            plane_main.move_down()
        if pressed_keys[K_SPACE]:
            plane_main.fire()


if __name__ == '__main__':
    main()
