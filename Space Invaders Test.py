import sys
import os
import pygame
import random

screen_width = 1200
screen_height = 550
player_spaceship = pygame.image.load("spaceship.png")
game_background = pygame.image.load("space background.png")
ani = 4


class space_ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_spaceship
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width / 2, screen_height / 2)
        self.move_x = 0
        self.move_y = 0
        self.frame = 0
        self.images = []
        self.img = self.images[0]

    def control(self, x, y):
        self.move_x += x
        self.move_y += y

    def update(self):
        self.rect.x = self.rect.x + self.move_x
        self.rect.y = self.rect.y + self.move_y
        # left
        if self.move_x > 0:
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
            self.img = self.images[self.frame // ani]
        # right
        if self.move_x < 0:
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
            self.img = self.images[self.frame // ani]


class laser:
    pass


class game_settings:
    pass


class aliens:
    def __init__(self):
        pass


def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Space Invaders")
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    spaceship = space_ship()
    all_sprites.add(spaceship)
    all_sprites.update()
    screen.blit(game_background, (0, 0))
    screen.blit(player_spaceship, spaceship.rect.center)
    pygame.display.flip()

    steps = 10
    spaceship.rect.x = 0
    spaceship.rect.y = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("links")
                    spaceship.control(-steps, 0)
                elif event.key == pygame.K_RIGHT:
                    print("rechts")
                    spaceship.control(steps, 0)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    spaceship.control(steps, 0)
                elif event.key == pygame.K_RIGHT:
                    spaceship.control(-steps, 0)

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        spaceship.update()
        pygame.display.flip()
        clock.tick(30)


main()
