import pygame

class CircleShape(pygame.sprite.Sprite):
    container: tuple[pygame.sprite.Group, ...]

    def __init__(self, x: float, y: float, radius: float) -> None:

        if hasattr(self,"container"):
            super().__init__(*self,containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity: pygame.Vector2 = pygame.Vector2(0,0)
        self.radius: float = radius
    def draw(self, screen: pygame.Surface) -> None:
        pass
    def update(self, df: float) -> None:
        pass

