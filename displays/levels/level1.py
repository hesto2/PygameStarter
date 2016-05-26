from displays.levels.level import Level, LevelComponent
from entities.entity import Entity
from entities.obstacles.wallStd import WallStd
from entities.players.player import Player
from entities.players.playerStart import PlayerStart
from pygame.locals import *
from entities.pickups.pickupInvincible import PickupInvincible
import constants as C
import pygame
class Level1(Level):

    def __init__(self):
        obstacles = []
        wallImg = pygame.image.load('lib/obstacles/wall.jpg').convert()
        obstacles.append(WallStd(wallImg,{'x':50,'y':200},moveableSides=[C.SIDE_RIGHT,C.SIDE_TOP,C.SIDE_LEFT,C.SIDE_BOTTOM]))
        obstacles.append(WallStd(wallImg,{'x':550,'y':50},moveableSides=[C.SIDE_RIGHT,C.SIDE_TOP,C.SIDE_LEFT,C.SIDE_BOTTOM]))
        obstacles.append(WallStd(wallImg,{'x':300,'y':150},moveableSides=[C.SIDE_RIGHT,C.SIDE_TOP,C.SIDE_LEFT,C.SIDE_BOTTOM]))
        obstacles.append(WallStd(wallImg,{'x':150,'y':350},moveableSides=[C.SIDE_RIGHT,C.SIDE_TOP,C.SIDE_LEFT,C.SIDE_BOTTOM]))
        obstacles.append(WallStd(wallImg,{'x':620,'y':224},moveableSides=[C.SIDE_RIGHT,C.SIDE_TOP,C.SIDE_LEFT,C.SIDE_BOTTOM]))
        obstacles.append(WallStd(wallImg,{'x':740,'y':160},moveableSides=[C.SIDE_RIGHT,C.SIDE_TOP,C.SIDE_LEFT,C.SIDE_BOTTOM]))
        obstacles.append(WallStd(wallImg,{'x':870,'y':464},moveableSides=[C.SIDE_RIGHT,C.SIDE_TOP,C.SIDE_LEFT,C.SIDE_BOTTOM]))
        obstacles.append(WallStd(wallImg,{'x':700,'y':568},moveableSides=[C.SIDE_RIGHT,C.SIDE_TOP,C.SIDE_LEFT,C.SIDE_BOTTOM]))
        obstacles.append(WallStd(wallImg,{'x':440,'y':544},moveableSides=[C.SIDE_RIGHT,C.SIDE_TOP,C.SIDE_LEFT,C.SIDE_BOTTOM]))
        obstacles.append(WallStd(wallImg,{'x':350,'y':350},moveableSides=[C.SIDE_RIGHT,C.SIDE_TOP,C.SIDE_LEFT,C.SIDE_BOTTOM]))
        obstacles.append(WallStd(wallImg,{'x':700,'y':312},moveableSides=[C.SIDE_RIGHT,C.SIDE_TOP,C.SIDE_LEFT,C.SIDE_BOTTOM]))
        obstacles.append(WallStd(wallImg,{'x':970,'y':216},moveableSides=[C.SIDE_RIGHT,C.SIDE_TOP,C.SIDE_LEFT,C.SIDE_BOTTOM]))
        obstacles.append(WallStd(wallImg,{'x':142,'y':64},moveableSides=[C.SIDE_RIGHT,C.SIDE_TOP,C.SIDE_LEFT,C.SIDE_BOTTOM]))
        obstacles.append(WallStd(wallImg,{'x':412,'y':168},moveableSides=[C.SIDE_RIGHT,C.SIDE_TOP,C.SIDE_LEFT,C.SIDE_BOTTOM]))
        obstacles.append(WallStd(wallImg,{'x':812,'y':48},moveableSides=[C.SIDE_RIGHT,C.SIDE_TOP,C.SIDE_LEFT,C.SIDE_BOTTOM]))
        obstacles.append(WallStd(wallImg,{'x':922,'y':112},moveableSides=[C.SIDE_RIGHT,C.SIDE_TOP,C.SIDE_LEFT,C.SIDE_BOTTOM]))
        obstacles.append(WallStd(wallImg,{'x':1028,'y':326},moveableSides=[C.SIDE_RIGHT,C.SIDE_TOP,C.SIDE_LEFT,C.SIDE_BOTTOM]))
        obstacles.append(WallStd(wallImg,{'x':1088,'y':174},moveableSides=[C.SIDE_RIGHT,C.SIDE_TOP,C.SIDE_LEFT,C.SIDE_BOTTOM]))
        obstacles.append(WallStd(wallImg,{'x':1008,'y':14},moveableSides=[C.SIDE_RIGHT,C.SIDE_TOP,C.SIDE_LEFT,C.SIDE_BOTTOM]))
        obstacles.append(WallStd(wallImg,{'x':994,'y':574},moveableSides=[C.SIDE_RIGHT,C.SIDE_TOP,C.SIDE_LEFT,C.SIDE_BOTTOM]))
        obstacles.append(WallStd(wallImg,{'x':824,'y':600},moveableSides=[C.SIDE_RIGHT,C.SIDE_TOP,C.SIDE_LEFT,C.SIDE_BOTTOM]))
        obstacles.append(WallStd(wallImg,{'x':534,'y':624},moveableSides=[C.SIDE_RIGHT,C.SIDE_TOP,C.SIDE_LEFT,C.SIDE_BOTTOM]))
        obstacles.append(WallStd(wallImg,{'x':204,'y':504},moveableSides=[C.SIDE_RIGHT,C.SIDE_TOP,C.SIDE_LEFT,C.SIDE_BOTTOM]))
        obstacles.append(WallStd(wallImg,{'x':332,'y':480},moveableSides=[C.SIDE_RIGHT,C.SIDE_TOP,C.SIDE_LEFT,C.SIDE_BOTTOM]))
        obstacles.append(WallStd(wallImg,{'x':510,'y':360},moveableSides=[C.SIDE_RIGHT,C.SIDE_TOP,C.SIDE_LEFT,C.SIDE_BOTTOM]))
        obstacles.append(WallStd(wallImg,{'x':80,'y':592},moveableSides=[C.SIDE_RIGHT,C.SIDE_TOP,C.SIDE_LEFT,C.SIDE_BOTTOM]))

        self.initPlayers()
        for obstacle in obstacles:
            self.playAreaEntities.append(obstacle)

        self.start_countdown = 0
        super().__init__(C.GAME.SCREEN,self.playAreaEntities,self.hudEntities)
    def reset(self):
        super().clear()
        self.__init__()
