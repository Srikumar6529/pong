import pygame
from config import *

def main():
    print("Hello from pong!")
    print("Let's build a wonderful pong game")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")


if __name__ == "__main__":
    main()
