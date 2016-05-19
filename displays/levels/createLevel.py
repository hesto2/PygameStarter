from displays.display import Display
from entities.entity import Entity
from entities.gui.timer import Timer
from entities.players.player import Player
from displays.levels.level import LevelComponent
from tools.time import getSecondsElapsed
from tools.collisions import *
from pygame.locals import *
import constants as C
import random
import pygame


class CreateLevel(Display):
    playArea = LevelComponent((C.SCREEN_WIDTH,C.SCREEN_HEIGHT*.90))

    def __init__(self):
        from tools.lists import obstacleList
        self.playArea.entities = [obstacleList[1]()]
        self.playArea.rect.centerx = C.GAME.SCREEN.get_rect().centerx
        self.playArea.rect.bottom = C.SCREEN_HEIGHT - C.SCREEN_HEIGHT * .05
        self.hud = []
        self.state = C.STATE_IN_PROGRESS
        self.selectableBlocks = obstacleList
        self.selectedBlock = 0
        self.selectedItem = self.selectableBlocks[self.selectedBlock]()
        self.pCoolDown = .5
        self.placeCoolDownStartTick = None
        self.pCurrentCoolDown = 0
        self.mouseDown = False
        self.validPlacement = True
        self.keyLeft = K_a
        self.keyRight = K_d
        self.keyDown = False
        self.fileName = ''
        super().__init__(C.GAME.SCREEN,[])

    def tick(self):
        self.handleState()
        for entity in self.hud:
            entity.tick()
            for subEntity in entity.entities:
                subEntity.tick()


    def handlePausedInput(self):
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            if self.keyDown:
                return
            self.keyDown = True
            self.unpause()
        else:
            self.keyDown = False

    def handleNormalInput(self):
        # Handle Key Presses
        self.checkNormalKeys()
        self.selectedItem = self.selectableBlocks[self.selectedBlock]()

        # Handle Mouse Input
        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]
        self.selectedItem.rect.centerx = mouseX
        self.selectedItem.rect.centery = mouseY
        self.validPlacement = True
        self.checkSelectedItemBoundary()
        self.checkCollisions()
        if pygame.mouse.get_pressed()[0]:
            self.placeSelected()
        else:
            self.mouseDown = False
            if pygame.mouse.get_pressed()[2]:
                self.removeSelected()



    def handleState(self):
        if self.state == C.STATE_IN_PROGRESS:
            self.handleNormalInput()
        elif self.state == C.STATE_PAUSED:
            self.handlePausedInput()

    def draw(self):
        self.entities = []
        self.playArea.surface.fill(self.playArea.bg_color)
        for entity in self.playArea.entities:
            self.playArea.surface.blit(entity.image,entity.rect)
        playArea = Entity(self.playArea.rect,self.playArea.surface)
        self.entities.append(playArea)
        if self.selectedItem:
            self.drawBorder()
            self.entities.append(self.selectedItem)

        hudItems = []
        for hudEntity in self.hud:
            hudEntity.surface.fill(hudEntity.bg_color)
            for subEntity in hudEntity.entities:
                hudEntity.surface.blit(subEntity.image,subEntity.rect)
            hudItems.append(Entity(hudEntity.rect,hudEntity.surface))

        self.entities.extend(hudItems)
        super().draw()

    def reset(self):
        self.__init__()

    def placeSelected(self):
        # Force user to let off the mouse before they can place another, no dragging
        if self.mouseDown or self.validPlacement == False:
            return
        selectedX,selectedY = self.getAbsSelected()

        # Uncomment this line to disable being able to drag with the lmb for placing
        # self.mouseDown = True
        newItem = self.selectableBlocks[self.selectedBlock]()
        newItem.rect.x = selectedX
        newItem.rect.y = selectedY
        self.playArea.entities.append(newItem)

    def removeSelected(self):
        mouseX,mouseY = self.getAbsMouse()
        for entity in self.playArea.entities:
            if entity.rect.collidepoint((mouseX,mouseY)):
                self.playArea.entities.remove(entity)

    def drawBorder(self):
        if self.validPlacement:
            color = C.DARKGREEN
        else:
            color = C.RED
        width = self.selectedItem.rect.width+4
        height = self.selectedItem.rect.height+4
        border = pygame.Surface((width,height))
        border.fill(color)
        rect = border.get_rect()
        rect.centerx = self.selectedItem.rect.centerx
        rect.centery = self.selectedItem.rect.centery
        border = Entity(rect,border)
        self.entities.append(border)

    def checkSelectedItemBoundary(self):
        playArea = C.GAME.display.playArea.rect
        if self.selectedItem.rect.top  < playArea.top:
            self.selectedItem.rect.top = playArea.top
            # self.validPlacement = False
        if self.selectedItem.rect.bottom > playArea.bottom:
            self.selectedItem.rect.bottom = playArea.bottom
            # self.validPlacement = False
        if self.selectedItem.rect.left < playArea.left:
            self.selectedItem.rect.left = playArea.left
            # self.validPlacement = False
        if self.selectedItem.rect.right > playArea.right :
            self.selectedItem.rect.right = playArea.right
            # self.validPlacement = False

    def checkCollisions(self):
        selectedX,selectedY = self.getAbsSelected()
        newItem = self.selectableBlocks[self.selectedBlock]()
        newItem.rect.x = selectedX
        newItem.rect.y = selectedY
        for entity in self.playArea.entities:
            if newItem.rect.colliderect(entity):
                self.validPlacement = False
                break

    def checkNormalKeys(self):
        keys = pygame.key.get_pressed()
        if keys[self.keyLeft]:
            if self.keyDown == True:
                return
            self.keyDown = True
            self.selectedBlock += 1
            if self.selectedBlock > len(self.selectableBlocks)-1:
                self.selectedBlock = 0
        if keys[self.keyRight]:
            if self.keyDown == True:
                return
            self.keyDown = True
            self.selectedBlock -= 1
            if self.selectedBlock < 0:
                self.selectedBlock = len(self.selectableBlocks)-1

        if keys[K_ESCAPE]:
            if self.keyDown == True:
                return
            self.keyDown = True
            self.pause()

        if keys[self.keyRight]==False and keys[self.keyLeft] == False and keys[K_ESCAPE]==False:
            self.keyDown = False

        # Toggle Pause Menu

    def getAbsMouse(self):
        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]
        mouseX += self.playArea.rect.x
        mouseY -= self.playArea.rect.y
        return mouseX,mouseY

    def getAbsSelected(self):
        selectedX = self.selectedItem.rect.x
        selectedY = self.selectedItem.rect.y
        selectedX += self.playArea.rect.x
        selectedY -= self.playArea.rect.y
        return selectedX,selectedY

    def pause(self):
        from entities.gui import overlays,buttons
        from displays.menus.pauseCreateLevel import PauseCreateLevel
        screen = C.GAME.SCREEN.get_rect()
        overlay = overlays.black()
        self.hud.append(overlay)
        self.hud.append(PauseCreateLevel())
        self.state = C.STATE_PAUSED

    def unpause(self):
        self.hud = []
        self.state = C.STATE_IN_PROGRESS
