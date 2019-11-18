import pygame
from pygame.locals import *  # 导入pygame的静态模块locals
import sys
import random

WINDOW_WIDTH = 512
WINDOW_HEIGHT = 768
enplanes = []
grade = 0


# 基础基类
class Base(object):
    def __init__(self, img_path, x, y, window):
        self.img = pygame.image.load(img_path)
        self.x = x
        self.y = y
        self.window = window

    def display(self):
        self.window.blit(self.img, (self.x, self.y))


# 飞机基类
class PlaneBase(Base):
    pass


# 定义一个地图类
class Map(object):
    def __init__(self, img_path, window):
        self.x = 0
        self.bg2_y = 0
        self.bg1_y = -WINDOW_HEIGHT
        self.bg_img1 = pygame.image.load(img_path)
        self.bg_img2 = pygame.image.load(img_path)
        self.window = window

    def move(self):
        if self.bg1_y == 0:
            self.bg2_y = -WINDOW_HEIGHT
        if self.bg2_y == 0:
            self.bg1_y = -WINDOW_HEIGHT
        self.bg1_y += 3
        self.bg2_y += 3

    def display(self):
        self.window.blit(self.bg_img1, (self.x, self.bg1_y))
        self.window.blit(self.bg_img2, (self.x, self.bg2_y))


# 敌方飞机类
class EnemyPlane(PlaneBase):
    def __init__(self, img_path, x, y, window):
        super().__init__(img_path, x, y, window)
        self.carsh_plane = False  # 用来标记敌机是否被击中

    def move(self):
        self.y += 4
        if self.y >= WINDOW_HEIGHT:
            self.x = random.randint(0, WINDOW_WIDTH - 68)
            self.y = random.randint(-768, 0)

    def display(self):
        """贴图"""
        if self.carsh_plane:
            self.x = random.randint(0, 412)
            self.y = random.randint(-100, 0)
            self.carsh_plane = False
        self.window.blit(self.img, (self.x, self.y))


# 子弹类
class HeroBullet(Base):
    def move(self):
        self.y -= 3

    def carsh_plane(self, enemy):
        bullet_rect = Rect(self.x, self.y, 20, 29)
        enemy_rect = Rect(enemy.x, enemy.y, 100, 68)
        if pygame.Rect.colliderect(bullet_rect, enemy_rect):
            return True
        else:
            return False

    def __del__(self):
        pass


class HeroPlane(PlaneBase):

    # 创建英雄飞机类
    def __init__(self, img_path, x, y, window):
        super().__init__(img_path, x, y, window)
        self.bullets = []

    def card_enemyplane(self, enemy):
        if pygame.Rect.colliderect(Rect(self.x, self.y, 100, 68), Rect(enemy.x, enemy.y, 100, 68)):
            return True
        else:
            return False

    def display(self):
        for enemy in enplanes:
            if self.card_enemyplane(enemy):
                enemy.carsh_plane = True
                print("点击关闭窗口按钮")
                pygame.quit()  # 退出pygame，清理pygame占用资源
                sys.exit()  # 关闭程序

        self.window.blit(self.img, (self.x, self.y))

    def move_left(self):
        if self.x >= 3:
            self.x -= 5

    def move_right(self):
        if self.x <= 409:
            self.x += 5

    def move_up(self):
        if self.y >= 3:
            self.y -= 5

    def move_down(self):
        if self.y <= 699:
            self.y += 5

    def fire(self):
        bullet = HeroBullet("res\\bullet_12.png", self.x + 40, self.y - 31, self.window)
        self.bullets.append(bullet)

    def display_bullets(self):
        deleted_bullets = []
        for bullet in self.bullets:
            if bullet.y <= -31:
                deleted_bullets.append(bullet)
            else:
                bullet.display()
                bullet.move()
            for enemy in enplanes:
                if bullet.carsh_plane(enemy):
                    enemy.carsh_plane = True
                    deleted_bullets.append(bullet)
                    global grade
                    grade+=10
                    break
        for deleted_bullet in deleted_bullets:
            self.bullets.remove(deleted_bullet)


def main():
    # 开始
    pygame.init()
    # 窗口大小
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    # 地图
    map_ditu = Map("res\\img_bg_level_%d.jpg" % random.randint(1, 5), window)
    # 我方飞机
    plane_main = HeroPlane("res\\hero.png", WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT - 200, window)
    # 背景音乐
    pygame.mixer.music.load("./res/bg2.ogg")
    # 敌方飞机
    for i in range(10):
        plane_enemy = EnemyPlane("res\\img-plane_%d.png" % random.randint(1, 7), random.randint(0, WINDOW_WIDTH - 68),
                                 random.randint(-768, 0), window)
        enplanes.append(plane_enemy)

    # 加载自定义字体，返回字体对象
    font_obj = pygame.font.Font("res/SIMHEI.TTF", 30)

    while True:
        # 背景图
        map_ditu.display( )
        map_ditu.move()
        # 贴飞机
        plane_main.display()
        # 贴敌方飞机
        for emplane in enplanes:
            emplane.display()
            emplane.move()
        # 设置文本，返回文本对象   render(文本内容， 抗锯齿，颜色)
        text_obj = font_obj.render("分数:%d" % grade, 1, (255, 255, 255))
        window.blit(text_obj,(0,0))


        # 贴子弹
        plane_main.display_bullets()
        # 刷新
        pygame.display.update()

        # 获取新事件
        for event in pygame.event.get():
            # 1. 鼠标点击关闭窗口事件
            if event.type == QUIT:
                print("点击关闭窗口按钮")
                # 停止背景音乐
                pygame.mixer.music.stop()
                pygame.quit()  # 退出pygame，清理pygame占用资源
                sys.exit()  # 关闭程序
            else:
                # 循环播放背景音乐
                pygame.mixer.music.play(-1)

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
