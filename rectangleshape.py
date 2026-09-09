import pygame

class RectangleShape(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Groups, ...]
    
    def __init__(self,x: float, y: float, length: float, width: float) -> None:
        if hasattr(self,"containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x,y)
        self.length = length
        self.width = width
    def draw(self, screen: pygame.Surface) -> None:
        pass
    def update(seld, df: float) -> None:
        pass

