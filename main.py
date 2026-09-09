import pygame
from config import *
from ball import Ball
def main():
    print("Hello from pong!")
    print("Let's build a wonderful pong game")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pong = Ball(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pong.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        pong.update(dt)


if __name__ == "__main__":
    main()
