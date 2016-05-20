from displays.levels.level import Level, LevelComponent
from entities.entity import Entity
from entities.obstacles.wallStd import WallStd
from entities.players.player import Player
from pygame.locals import *
import constants as C
import pygame
import json

class CustomLevel(Level):
    def __init__(self,data):
        self.data = data
        from tools.lists import loadList
        obstacles = []
        starts = []
        data = json.loads(data)
        for item in data['entities']:
            x = item['x']
            y = item['y']
            item = loadList[item['code']](position={"x":x,"y":y})
            if item.type == C.TYPE_PLAYER_START:
                starts.append(item)
            else:
                obstacles.append(item)


        self.initPlayers()
        for obstacle in obstacles:
            self.playAreaEntities.append(obstacle)

        super().__init__(C.GAME.SCREEN,self.playAreaEntities,self.hudEntities,starts)

    def reset(self):
        super().clear()
        self.__init__(self.data)
