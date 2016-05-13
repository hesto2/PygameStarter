import pygame,time
class Display:
    def __init__(self,screen,entities,bg_color=(0,0,255)):
        self.screen = screen
        self.entities = entities
        self.bg_color = bg_color

    def draw(self):
        self.screen.fill(self.bg_color)
        for entity in self.entities:
            self.screen.blit(entity.image,entity.rect)
        pygame.display.flip()

    def tick(self):
        for entity in self.entities:
            entity.tick()
