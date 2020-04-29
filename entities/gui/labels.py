from entities.entity import Entity
import constants as C
import pygame


class Label(Entity):
    def __init__(self,text,color=(C.WHITE),size=30,x=None,y=None,centerx=None,centery=None):
        self.font = pygame.font.Font(None, size)
        self.text = text
        self.color = color
        text = self.font.render(self.text, 1, self.color)
        textpos = text.get_rect()

        if x:
            textpos.x = x
        elif centerx:
            textpos.centerx = centerx

        if y:
            textpos.y = y
        elif centery:
            textpos.centery = centery

        super().__init__(textpos,text)

    def tick(self):
        self.image = self.font.render(self.text, 1, self.color)
        super().tick()
