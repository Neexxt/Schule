import sys
import os
import pygame
import random

screen_width = 1200
screen_height = 550
player_spaceship = pygame.image.load("spaceship.png")
game_background = pygame.image.load("space background.png")
laser_png = pygame.image.load("bullet.png")
game_background = pygame.transform.scale(game_background, (1200, 550))
laser_png = pygame.transform.scale(laser_png, (64, 64))


class space_ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_spaceship
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_width / 2
        self.rect.bottom = screen_height / 1.1
        self.pos = self.rect.centerx, self.rect.bottom
        self.speed_ship = 0
        self.shot = pygame.time.get_ticks()

    def update(self):
        self.speed_ship = 0
        cd = 250  # bullet speed // delay between shots
        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_LEFT]:
            self.speed_ship = -9
        if key_state[pygame.K_RIGHT]:
            self.speed_ship = 9
        self.rect.x += self.speed_ship
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.left < 0:
            self.rect.left = 0

        time_now = pygame.time.get_ticks()

        if key_state[pygame.K_SPACE] and time_now - self.shot > cd:
            bullet = laser(self.rect.centerx, self.rect.top)
            bullet_group.add(bullet)
            self.shot = time_now


bullet_group = pygame.sprite.Group()


class laser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = laser_png
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.y -= 5
        if self.rect.bottom < 0:
            self.kill()


class game_settings:
    pass


class aliens:
    def __init__(self):
        pass


def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Space Invaders")
    fps = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    spaceship = space_ship()

    all_sprites.add(spaceship)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        all_sprites.update()
        screen.blit(game_background, (0, 0))
        all_sprites.draw(screen)
        bullet_group.update()
        bullet_group.draw(screen)
        pygame.display.flip()
        fps.tick(60)


main()
