import pygame
from config import PADDLE_LENGTH,PADDLE_WIDTH,SCREEN_WIDTH,SCREEN_HEIGHT
from ball import Ball
from pad import Pad
def main():
    print("Hello from pong!")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Ball.containers = (updatable,drawable)
    Pad.containers = (updatable,drawable)    
    
    pong = Ball(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    paddle1 = Pad(
            0, 
            SCREEN_HEIGHT//2 - PADDLE_LENGTH//2, 
            PADDLE_LENGTH, 
            PADDLE_WIDTH,
            {
                "up":pygame.K_w,
                "down": pygame.K_s
            }
        )
    paddle2 = Pad(
            SCREEN_WIDTH-0 - PADDLE_WIDTH, 
            SCREEN_HEIGHT//2 - PADDLE_LENGTH//2, 
            PADDLE_LENGTH, 
            PADDLE_WIDTH,
            {
                "up":pygame.K_UP,
                "down":pygame.K_DOWN
            }
        )
   
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
                item.update(dt,[paddle1,paddle2])
            else:
                item.update(dt)


if __name__ == "__main__":
    main()
