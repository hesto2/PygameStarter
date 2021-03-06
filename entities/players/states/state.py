from displays.display import Display
from entities.entity import Entity
from entities.gui.timer import Timer
from tools.collisions import *
from pygame.locals import *
import constants as C
import pygame

class State:
    name = None
    def __init__(self,player,duration=0):
        from entities.players.player import Player
        self.player = player
        self.duration = duration
        self.coolDownStartSecond = None

    def tick(self):
        # Revert state after duration is filled
        currentSecond = C.GAME.display.timer.currentLiveTime
        if self.duration > 0:
            if self.coolDownStartSecond == None:
                self.coolDownStartSecond = currentSecond
            if currentSecond >= (self.coolDownStartSecond+self.duration):
                from entities.players.states.stateNormal import StateNormal
                self.player.state = StateNormal(self.player)

    # Default input
    def handleInput(self):
        keys = pygame.key.get_pressed()
        self.player.currentXSpeed = 0
        self.player.currentYSpeed = 0
        if keys[self.player.keyUp]:
                self.player.directionY = -1
                self.player.currentYSpeed = self.player.currentSpeed
        if keys[self.player.keyDown]:
                self.player.directionY = 1
                self.player.currentYSpeed = self.player.currentSpeed
        if keys[self.player.keyLeft]:
                self.player.directionX = -1
                self.player.currentXSpeed = self.player.currentSpeed
        if keys[self.player.keyRight]:
                self.player.directionX = 1
                self.player.currentXSpeed = self.player.currentSpeed
        # if keys[self.player.keyPlaceBlock]:
        #     self.player.placeBlock()

    #Default on collision behavior
    def onCollision(self,collider,side):
        from entities.players.states.stateInvincible import StateInvincible
        # Allow players to move through one another if invincible
        if collider.type == C.TYPE_PLAYER:
            if collider.state.name == C.P_STATE_INVINCIBLE:
                return
            elif C.GAME.display.taggedPlayer == self.player:
                print(1)
                collider.tagged(self.player)
            elif C.GAME.display.taggedPlayer == collider:
                self.player.tagged(collider)

        moveToEdge(self.player,collider,side)

        # if C.GAME.display.taggedPlayer == self.player:
        #     collider.tagged(self.player)

    #Default colliding behavior
    def checkCollision(self,target):
        rect = self.player.rect
        if checkTop(self.player,target): target.onCollision(self.player,C.SIDE_TOP)
        elif checkBottom(self.player,target): target.onCollision(self.player,C.SIDE_BOTTOM)
        elif checkLeft(self.player,target): target.onCollision(self.player,C.SIDE_LEFT)
        elif checkRight(self.player,target): target.onCollision(self.player,C.SIDE_RIGHT)
