from constants import *
import constants as C
from tools.collisions import *
from pygame.locals import *
from entities.entity import Entity
from tools.time import getSecondsElapsed
from entities.players.states.stateNormal import StateNormal
import pygame
class Player(Entity):

    def __init__(self,rect,inputConf,image,name):
        self.keyUp = inputConf['keyUp']
        self.keyDown = inputConf['keyDown']
        self.keyLeft = inputConf['keyLeft']
        self.keyRight = inputConf['keyRight']
        # self.keyPlaceBlock = inputConf['placeBlock']
        self.pCoolDown = 1
        self.placeCoolDownStartTick = None
        self.pCurrentCoolDown = 0

        self.type = C.TYPE_PLAYER
        self.name = name
        self.velocityX = 0
        self.velocityY = 0
        self.directionX = 1
        self.directionY = 1
        # self.maxXSpeed = 10
        # self.currentXSpeed = 0
        # self.maxYSpeed = 10
        # self.currentYSpeed = 0
        self.maxSpeed = 10
        self.currentSpeed = self.maxSpeed
        self.time_tagged = 0
        self.normalPicture = image
        self.state = StateNormal(self)

        # Tagged info
        self.taggedStartSecond = None
        super().__init__(rect,image)


    def move(self):
        entities = C.GAME.display.playArea.entities
        for target in entities:
            if hasattr(target,'name'):
                if target.name == self.name:
                    continue
            self.checkCollision(target)
            self.checkBoundary()
        self.rect = self.rect.move(self.velocityX,self.velocityY)
        return self.rect

# Collision Detection
    def checkCollision(self,target):
        self.state.checkCollision(target)
        rect = self.rect
        if checkTop(self,target): target.onCollision(self,C.SIDE_TOP)
        elif checkBottom(self,target): target.onCollision(self,C.SIDE_BOTTOM)
        elif checkLeft(self,target): target.onCollision(self,C.SIDE_LEFT)
        elif checkRight(self,target): target.onCollision(self,C.SIDE_RIGHT)

    def onCollision(self,collider,side):
        self.state.onCollision(collider,side)

    def handleInput(self):
        self.state.handleInput()

    def handleState(self):
        self.velocityX = self.currentXSpeed * self.directionX
        self.velocityY = self.currentYSpeed * self.directionY

        if self.placeCoolDownStartTick != None:
            self.placeCoolDown()
        self.state.tick()

    def tick(self):
        self.handleInput()
        self.handleState()
        self.move()
        if C.GAME.display.taggedPlayer == self:
            self.incrementTaggedTimer()
        return self.rect

    def tagged(self,tagger=None):
        from entities.players.states.stateInvincible import StateInvincible
        if self.tagged == None:
            self.taggedStartSecond = C.GAME.display.timer.currentLiveTime
        self.image = pygame.image.load('lib/players/tagged.png').convert()
        if tagger:
            tagger.taggedStartSecond = None
            tagger.image = tagger.normalPicture
            C.GAME.display.taggedPlayer = self
            self.state = StateNormal(self)
            tagger.state = StateInvincible(tagger,2)

    def placeCoolDown(self):
        if self.placeCoolDownStartTick == None:
            self.placeCoolDownStartTick = pygame.time.get_ticks()
            self.pCurrentCoolDown = self.pCoolDown
        else:
            elapsed = getSecondsElapsed(pygame.time.get_ticks(),self.placeCoolDownStartTick)
            self.pCurrentCoolDown = self.pCoolDown - elapsed
            if self.pCurrentCoolDown <= 0:
                self.placeCoolDownStartTick = None

    def placeBlock(self):
        return
        if self.placeCoolDownStartTick != None:
            return
        from entities.obstacles.wallStd import WallStd
        wallImg = pygame.image.load('lib/obstacles/wall.jpg').convert()
        obstacle = WallStd(wallImg,{'x':self.rect.x-self.rect.width,'y':self.rect.y-self.rect.height},moveableSides=[C.SIDE_RIGHT,C.SIDE_TOP,C.SIDE_LEFT,C.SIDE_BOTTOM])
        C.GAME.display.playArea.entities.append(obstacle)
        with open('test.txt','a') as f:
            f.write("obstacles.append(WallStd(wallImg,{'x':%i,'y':%i},moveableSides=[C.SIDE_RIGHT,C.SIDE_TOP,C.SIDE_LEFT,C.SIDE_BOTTOM]))\n" % (self.rect.x-self.rect.width,self.rect.y-self.rect.height))
        self.placeCoolDown()

    def incrementTaggedTimer(self):
        # Increment the total time every second
        currentTime = C.GAME.display.timer.currentLiveTime
        if self.taggedStartSecond == None:
            self.taggedStartSecond = currentTime
        if self.taggedStartSecond < currentTime:
            self.time_tagged += (currentTime-self.taggedStartSecond)
            self.taggedStartSecond = currentTime
