# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys
from game import *
from client import *

 
DEBUG = False


def main():
    # 初期化
    game = Game(DEBUG)
    pygame.init() 
    screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
    pygame.display.set_caption("ぷよぷよ?")
    clock = pygame.time.Clock()
    game.load_background_image()

    while(True):
        # 処理
        game.update()

        # 描写
        game.draw(screen)
        pygame.display.update()

        # 入力
        game.pushed_key(pygame.event.get())
        game.pressed_key(pygame.key.get_pressed())

        # 判定
        game.judge()

        clock.tick(game.fps)





if __name__ == "__main__":
    main()