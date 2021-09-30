import sys
import os
import pygame

screen_width = 1200
screen_height = 550
player_spaceship = pygame.image.load("spaceship.png")
game_background = pygame.image.load("space background.png")


class space_ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_spaceship
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width / 2, screen_height / 2)

    def keybinding(self):
        pass



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
    clock.tick(10)
    all_sprites = pygame.sprite.Group()
    spaceship = space_ship()
    all_sprites.add(spaceship)
    all_sprites.update()
    screen.blit(game_background, (0, 0))
    screen.blit(player_spaceship, spaceship.rect.center)
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


main()
