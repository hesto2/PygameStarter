import constants as c
class Entity:

    def __init__(self,rect,image):
        self.rect = rect
        self.image = image
        self.id = self.getGuid()

    def onCollision(self,collider,side):
        pass

    def getGuid(self):
        self.id = c.GUID
        c.GUID = c.GUID + 1
