import pygame,random
from circleshape import CircleShape
from config import *
class Ball(CircleShape):

    def __init__(self, x: float, y: float):
        super().__init__(x,y,BALL_RADIUS)
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)
    def update(self,dt):
        self.velocity = pygame.Vector2(BALL_SPEED,BALL_SPEED)
        self.velocity.rotate(random.randint(-30, 30))
        self.position += dt * self.velocity
