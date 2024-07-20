import pygame


class Character:
    """管理角色的类"""
    def __init__(self, ai_game):
        """初始化角色并设置其初始位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # 加载角色图像并获取其外接矩形
        self.image = pygame.image.load('images/chargespot_person_01.bmp')
        self.rect = self.image.get_rect()
        # 每个角色都放在屏幕底部的中央
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """在指定位置绘制⻜船"""
        self.screen.blit(self.image, self.rect)