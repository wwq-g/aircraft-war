import pygame
from pygame import locals
from pygame.locals import *  # 导入pygame的静态模块locals


def main():
    # 开始
    pygame.init()
    # 窗口大小
    window = pygame.display.set_mode((512, 768))
    # 加载内存
    image = pygame.image.load("res\\img_bg_level_1.jpg")


    # 飞机
    plane_main=pygame.image.load("res\\app.ico")


    while True:
        window.blit(image, (0, 0))
        pygame.display.update()


        # 获取新事件
        for event in pygame.event.get():
            # 1. 鼠标点击关闭窗口事件
            if event.type == QUIT:
                print("点击关闭窗口按钮")
                sys.exit()  # 关闭程序
                pygame.quit()  # 退出pygame，清理pygame占用资源

            # 2. 键盘按下事件
            if event.type == KEYDOWN:
                # 判断用户按键
                if event.key == K_LEFT or event.key == K_a:
                    print("left")
                if event.key == K_RIGHT or event.key == K_d:
                    print("right")
                if event.key == K_UP or event.key == K_w:
                        print("up")
                if event.key == K_DOWN or event.key == K_s:
                            print("down")
                if event.key == K_SPACE:
                    print("space")
                if event.key == K_ESCAPE:
                    pygame.quit()


if __name__ == '__main__':
    main()
