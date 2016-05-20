from displays.display import Display
from entities.entity import Entity
from entities.gui.timer import Timer
from pygame.locals import *
import constants as C
import pygame

class State:
    name = None
    def __init__(self,player):
        from entities.players.player import Player
        self.player = player

    def tick(self):
        pass

    # Default input
    def handleInput(self):
        keys = pygame.key.get_pressed()
        self.currentXSpeed = 0
        self.currentYSpeed = 0
        if keys[self.keyUp]:
                self.directionY = -1
                self.currentYSpeed = self.maxYSpeed
        if keys[self.keyDown]:
                self.directionY = 1
                self.currentYSpeed = self.maxYSpeed
        if keys[self.keyLeft]:
                self.directionX = -1
                self.currentXSpeed = self.maxXSpeed
        if keys[self.keyRight]:
                self.directionX = 1
                self.currentXSpeed = self.maxXSpeed
        if keys[self.keyPlaceBlock]:
            self.placeBlock()

    #Default on collision behavior
    def onCollision(self):
        pass

    #Default colliding behavior
    def checkCollision(self,target):
        pass
