import pygame


class Ship:
    """管理⻜船的类"""

    def __init__(self, ai_game):
        """初始化⻜船并设置其初始位置"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # 加载⻜船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.image_left = pygame.image.load('images/shipleft.bmp')
        self.image_right = pygame.image.load('images/shipright.bmp')
        self.rect = self.image.get_rect()
        # 每艘新⻜船都放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom

        # 在⻜船的属性 x 中存储⼀个浮点数
        self.x = float(self.rect.x)

        # 移动标志（⻜船⼀开始不移动）
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整⻜船的位置"""
        # 更新⻜船的属性 x 的值，⽽不是其外接矩形的属性 x 的值

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # 根据 self.x 更新 rect 对象
        self.rect.x = self.x

    def blitme(self):
        """在指定位置绘制⻜船"""
        self.screen.blit(self.image, self.rect)



