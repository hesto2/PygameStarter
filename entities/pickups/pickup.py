from displays.display import Display
from entities.entity import Entity
from entities.gui.timer import Timer
from tools.collisions import *
from pygame.locals import *
import constants as C
import pygame

class Pickup(Entity):
    def __init__(self,rect,image,name,rarity,ttl,statusEffect,roam=False):
        super().__init__(rect,image)
        self.name = name
        self.rarity = rarity
        self.ttl = ttl
        self.statusEffect = statusEffect
        self.roam = roam
        self.velocityX = 0
        self.velocityY = 0
        self.mass = 0
        self.type = C.TYPE_PICKUP
        self.rect.x = 100
        self.rect.y = 50

    def tick(self):
        pass

    def onCollision(self,collider,side):
        if collider.type == C.TYPE_PLAYER:
            collider.state = self.statusEffect(collider)
            self.removeFromGame()
        else:
            self.velocityX = 0
            self.velocityY = 0
            if side == C.SIDE_TOP:
                collider.velocityY = collider.velocityY + self.mass
                if collider.velocityY > 0:
                    collider.velocityY = 0
                self.velocityY = collider.velocityY
            elif side == C.SIDE_BOTTOM:
                collider.velocityY = collider.velocityY - self.mass
                if collider.velocityY < 0:
                    collider.velocityY = 0
                self.velocityY = collider.velocityY
            elif side == C.SIDE_LEFT:
                collider.velocityX = collider.velocityX + self.mass
                if collider.velocityX > 0:
                    collider.velocityX = 0
                self.velocityX = collider.velocityX
            elif side == C.SIDE_RIGHT:
                collider.velocityX = collider.velocityX - self.mass
                if collider.velocityX < 0:
                    collider.velocityX = 0
                self.velocityX = collider.velocityX

            self.rect = self.move(collider,side)

    def move(self,collider,side):
        entities = C.GAME.display.playArea.entities
        for target in entities:
            if target == self or target == collider:
                continue
            self.checkCollision(target)
            self.checkBoundary()

        self.rect = self.rect.move(self.velocityX,self.velocityY)

        if side in [C.SIDE_TOP,C.SIDE_BOTTOM]:
            collider.velocityY = self.velocityY
        else:
            collider.velocityX = self.velocityX
        return self.rect

    def removeFromGame(self):
        print(self)
        # C.GAME.display.playArea.entities.remove(self)
