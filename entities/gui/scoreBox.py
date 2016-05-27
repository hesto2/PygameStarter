from entities.entity import Entity
import constants as C
import pygame

class ScoreBox(Entity):
    font = pygame.font.Font(None, 36)
    def __init__(self):
        size = (200,C.SCREEN_HEIGHT*.90)

        image = pygame.Surface(size)
        super().__init__(rect,image)

    def tick(self):
        pass

class RankBox(Entity):
    def __init__(self):

        super().__init__(rect,image)

    def tick(self):
        pass
