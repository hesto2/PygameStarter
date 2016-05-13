import constants as c
import pygame
class Entity:

    def __init__(self,rect,image):
        self.rect = rect
        self.image = image
        self.mouseHover = False
        self.leftMouseDown = False
        self.rightMouseDown = False
        self.id = self.getGuid()

    def onCollision(self,collider,side):
        pass

    def getGuid(self):
        self.id = c.GUID
        c.GUID = c.GUID + 1

    def onLeftMouseDown(self):
        pass

    def onRightMouseDown(self):
        pass

    def onLeftMouseUp(self):
        pass

    def onRightMouseUp(self):
        pass

    def onMouseHover(self):
        pass

    def tick(self):
        self.checkMouseEvents()

    def checkMouseEvents(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.onMouseHover()
            if pygame.mouse.get_pressed()[0]:
                self.onLeftMouseDown()
            if pygame.mouse.get_pressed()[2]:
                self.onRightMouseDown()
