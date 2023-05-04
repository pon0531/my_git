# -*- coding: utf-8 -*-
"""
Created on Thu May  4 20:37:50 2023

@author: upon
"""

import pygame
bg_img = '../Data/bg.png'
data_1_img = '../Data/little_new_1.png'
data_2_img = '../Data/little_new_1.png'
data_3_img = '../Data/little_white.png'
data_4_img = '../Data/little_new_big_head.png'

class Bg(pygame.sprite.Sprite):
    def __init__(self):
        super(Bg, self).__init__()
        bg_small = pygame.image.load(bg_img).convert_alpha()
        grass_land = bg_small.subsurface((0, 0, 2046, 1367))
        self.surf = pygame.transform.scale(grass_land, (800, 600))
        self.rect = self.surf.get_rect(left=0, top=0)  # 左上角定位


class Pig(pygame.sprite.Sprite):
    def __init__(self):
        super(Pig, self).__init__()
        self.surf = pygame.image.load(data_1_img).convert_alpha()
        self.rect = self.surf.get_rect(center=(200, 200))  # 中心定位

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.move_ip((-1, 0))
        elif keys[pygame.K_RIGHT]:
            self.rect.move_ip((1, 0))
        elif keys[pygame.K_UP]:
            self.rect.move_ip((0, -1))
        elif keys[pygame.K_DOWN]:
            self.rect.move_ip((0, 1))

        # 防止小豬跑到屏幕外面
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 600:
            self.rect.bottom = 600


class Pig2(pygame.sprite.Sprite):
    def __init__(self):
        super(Pig2, self).__init__()
        self.surf = pygame.image.load(data_2_img).convert_alpha()
        self.rect = self.surf.get_rect(center=(100, 100))  # 中心定位

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.move_ip((1, 0))
        elif keys[pygame.K_RIGHT]:
            self.rect.move_ip((-1, 0))
        elif keys[pygame.K_UP]:
            self.rect.move_ip((0, 1))
        elif keys[pygame.K_DOWN]:
            self.rect.move_ip((0, -1))

        # 防止小豬跑到屏幕外面
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 600:
            self.rect.bottom = 600
def main():
    pygame.init()
    pygame.display.set_caption('Game Project：Felixs Game')  # 遊戲標題
    win = pygame.display.set_mode((800, 600))  # 窗口尺寸
    bg_small = pygame.image.load('../Data/bg.png').convert_alpha()
    bg_big = pygame.transform.scale(bg_small, (800, 600))
    little_new_1 = pygame.image.load(data_1_img).convert_alpha()
    little_new_2= pygame.image.load(data_3_img).convert_alpha()
    little_new_3= pygame.image.load(data_4_img).convert_alpha()
    running = True
    
    bg = Bg()
    pig2 = Pig2()
    pig = Pig()
   
    
    all_sprites = [bg, pig ,pig2] #決定哪個圖層在顯示在前面
    
    
    while running:
        pygame.time.delay(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 點擊左上角或者右上角的x關閉窗口時，停止程序
                running = False

        win.blit(bg_big, (0, 0))  # 背景圖最先加載，座標是(left, top)
        win.blit(little_new_1, (200, 300)) # 設定pig 1出現座標
        win.blit(little_new_2, (200+128, 300)) # 設定pig 2出現座標
        win.blit(little_new_3, (200+128+128, 300)) # 設定pig 2出現座標
        
        keys = pygame.key.get_pressed()
        pig.update(keys)
        pig2.update(keys)

        for sprite in all_sprites:
            win.blit(sprite.surf, sprite.rect)
        
        pygame.display.flip()
    
    
    pygame.quit() #python game 關閉，不做會卡住

if __name__ == '__main__':
    main()  # python main