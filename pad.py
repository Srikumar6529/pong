import pygame
from config import *
from rectangleshape import RectangleShape

class Pad(RectangleShape):
    def __init__(self,x,y,l,w):
        super().__init__(x,y,l,w)

    def draw(self, screen):
        pygame.draw.rect(screen,"white", (self.position.x,self.position.y,self.width,self.length),LINE_WIDTH)
    def update(self,dt):
        pass
