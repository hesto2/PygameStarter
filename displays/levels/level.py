from displays.display import Display
from entities.entity import Entity
import constants as C
import pygame

class LevelComponent():
    def __init__(self,size=(50,50),entities=[],color=(0,0,0)):
        self.surface = pygame.Surface(size)
        self.rect = self.surface.get_rect()
        self.entities = entities
        self.bg_color = color

class Level(Display):
    playArea = LevelComponent((C.SCREEN_WIDTH,C.SCREEN_HEIGHT*.90))
    hud = LevelComponent()
    paused = False
    def __init__(self,screen,playAreaEntities,hudEntities):
        self.playArea.entities = playAreaEntities
        self.playArea.rect.centerx = C.GAME.SCREEN.get_rect().centerx
        self.playArea.rect.bottom = C.SCREEN_HEIGHT - C.SCREEN_HEIGHT * .05
        # self.hudEntities = hudEntities
        super().__init__(screen,[])

    def togglePause(self):
        pass

    def tick(self):
        for entity in self.playArea.entities:
            entity.tick()
        for entity in self.hud.entities:
            entity.tick()

    def draw(self):
        self.playArea.surface.fill(self.playArea.bg_color)
        for entity in self.playArea.entities:
            self.playArea.surface.blit(entity.image,entity.rect)
        playArea = Entity(self.playArea.rect,self.playArea.surface)

        # for entity in self.hud.entities:
        #     self.hud.surface.blit(entity.rect,entity.image)
        # hud = Entity(self.hud.rect,self.hud.surface
        self.entities = [playArea]
        super().draw()
