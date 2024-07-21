import sys
import pygame
from settngs import Settings
from ship import Ship
from character import Character
from bullet import Bullet

class AlienInvasion:
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width, self.settings.screen_height = (
            self.screen.get_rect().height, pygame.display.set_caption("Alien Invasion"))

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.character = Character(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 侦听键盘和⿏标事件
            self._check_events()
            self.ship.update()
            self.bullets.update()
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            # 每次循环时都重绘屏幕
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """响应按键和⿏标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """响应按下"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
            self.ship.image = pygame.image.load('images/shipright.bmp')
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
            self.ship.image = pygame.image.load('images/shipleft.bmp')
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """响应释放"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
            self.ship.image = pygame.image.load('images/ship.bmp')
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            self.ship.image = pygame.image.load('images/ship.bmp')

    def _fire_bullet(self):
        """创建⼀颗⼦弹，并将其加⼊编组 bullets """
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)


    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.character.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例并运⾏游戏
    ai = AlienInvasion()
    ai.run_game()
