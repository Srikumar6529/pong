import pygame
from config import *
from ball import Ball
from pad import Pad
def main():
    print("Hello from pong!")
    print("Let's build a wonderful pong game")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Ball.containers = (updatable,drawable)
    Pad.containers = (updatable,drawable)    
    #p1.containers = (updatable,drawable)
    pong = Ball(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    p1 = Pad(20, SCREEN_HEIGHT / 2, PLAYER_LENGTH, PLAYER_WIDTH)
    p2 = Pad(SCREEN_WIDTH - 20 - PLAYER_WIDTH, SCREEN_HEIGHT / 2, PLAYER_LENGTH, PLAYER_WIDTH)
   
    while True:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        
        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        for item in updatable:
            if isinstance(item,Ball):
                item.update(dt,[p1,p2])
            else:
                if keys[pygame.K_UP] or keys[pygame.K_DOWN]:
                    p2.update(dt)
                elif keys[pygame.K_w] or keys[pygame.K_s]:
                    p1.update(dt)
            


if __name__ == "__main__":
    main()
