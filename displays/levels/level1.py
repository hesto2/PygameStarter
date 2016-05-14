from displays.levels.level import Level, LevelComponent
from entities.entity import Entity
from entities.obstacles.wallStd import WallStd
from entities.players.player import Player
from pygame.locals import *
import constants as C
import pygame
class Level1(Level):

    def __init__(self):
        self.test1Level()
        super().__init__(C.GAME.SCREEN,self.playAreaEntities,self.hudEntities)

    def test1Level(self):
        self.testLevel = 1
        screenRect = self.playArea.rect
        obstacles = []
        wallImg = pygame.image.load('lib/obstacles/wall.jpg').convert()
        obstacles.append(WallStd(wallImg,{'x':50,'y':200},moveableSides=[C.SIDE_RIGHT,C.SIDE_TOP,C.SIDE_LEFT,C.SIDE_BOTTOM]))
        obstacles.append(WallStd(wallImg,{'x':550,'y':50},moveableSides=[C.SIDE_RIGHT,C.SIDE_TOP,C.SIDE_LEFT,C.SIDE_BOTTOM]))
        obstacles.append(WallStd(wallImg,{'x':300,'y':150},))
        obstacles.append(WallStd(wallImg,{'x':150,'y':350}))
        obstacles.append(WallStd(wallImg,{'x':350,'y':350}))
        self.playAreaEntities = []
        self.hudEntities = []
        for obstacle in obstacles:
            self.playAreaEntities.append(obstacle)


    def test2Level(self):
        self.testLevel = 2
        obstacles = []
        wallImg = pygame.image.load('lib/obstacles/wall.jpg').convert()
        obstacles.append(WallStd(wallImg,{'x':50,'y':200},moveableSides=[C.SIDE_RIGHT,C.SIDE_TOP,C.SIDE_LEFT,C.SIDE_BOTTOM]))
        obstacles.append(WallStd(wallImg,{'x':550,'y':50},moveableSides=[C.SIDE_RIGHT,C.SIDE_TOP,C.SIDE_LEFT,C.SIDE_BOTTOM]))
        obstacles.append(WallStd(wallImg,{'x':300,'y':150},))
        obstacles.append(WallStd(wallImg,{'x':150,'y':350}))
        obstacles.append(WallStd(wallImg,{'x':350,'y':350}))
        testSurface = pygame.Surface((800,400))
        testSurface.fill((50,255,50))
        testPos = testSurface.get_rect()
        testPos.centerx = C.GAME.SCREEN.get_rect().centerx
        testPos.centery = C.GAME.SCREEN.get_rect().centery
        self.playArea['surface'] = testSurface.convert()
        self.playArea['rect'] = testPos
        for entity in obstacles:
            self.subEntities.append(entity)

    def draw(self):
        if self.testLevel == 2:
            for entity in self.subEntities:
                self.playArea['surface'].blit(entity.image,entity.rect)
            playArea = Entity(self.playArea['rect'],self.playArea['surface'])
            self.entities = [playArea]
        super().draw()
