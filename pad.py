import pygame
from config import *
from rectangleshape import RectangleShape

class Pad(RectangleShape):
    def __init__(self,x,y,l,w):
        super().__init__(x,y,l,w)

    def draw(self, screen):
        pygame.draw.rect(screen,"white", (self.position.x,self.position.y,self.width,self.length),LINE_WIDTH)
    
    def update(self,dt):
        x,y = self.position.x + self.width//2 , self.position.y + self.length //2
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            if not y + self.length//2 >= SCREEN_HEIGHT-10:
                self.position += pygame.Vector2(0,1) * dt * PLAYER_SPEED
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            if not y + self.length//2  <= PLAYER_LENGTH + 10:
                self.position += pygame.Vector2(0,1) * -dt * PLAYER_SPEED
