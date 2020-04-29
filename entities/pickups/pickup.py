from displays.display import Display
from entities.entity import Entity
from entities.gui.timer import Timer
from tools.collisions import *
from pygame.locals import *
import constants as C
from random import randint
import pygame

class Pickup(Entity):
    def __init__(self,rect,image,name,rarity,statusEffect,duration=5,ttl=15,roam=False):
        self.tolerance = 200
        super().__init__(rect,image)
        self.name = name
        self.duration = duration
        self.rarity = rarity
        self.ttl = ttl
        self.statusEffect = statusEffect
        self.roam = roam
        self.velocityX = 0
        self.velocityY = 0
        self.mass = 0
        self.type = C.TYPE_PICKUP
        self.spawnSecond = C.GAME.display.timer.currentLiveTime
        self.spawnRandomly()
        # how many tries it should randomly try to find a spot before it gives up
    def tick(self):
        if C.GAME.display.timer.currentLiveTime - self.spawnSecond >= self.ttl:
            self.removeFromGame()

    def onCollision(self,collider,side):
        if collider.type == C.TYPE_PLAYER:
            self.affectPlayer(collider)
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
        if self in C.GAME.display.playArea.entities:
            C.GAME.display.playArea.entities.remove(self)

    def affectPlayer(self,collider):
        collider.state = self.statusEffect(collider,duration=self.duration)


    def spawnRandomly(self):
        entities = C.GAME.display.playArea.entities
        colliding = True
        tries = 0
        while colliding or tries <= self.tolerance:
            tries += 1
            colliding = False
            self.rect.x = randint(0,C.GAME.display.playArea.rect.width)
            self.rect.y = randint(0,C.GAME.display.playArea.rect.height)
            if self.isInBoundary() == False:
                colliding = True
            for entity in entities:
                if self.rect.colliderect(entity):
                    colliding = True
                    break
