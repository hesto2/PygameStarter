import pygame,time
class MainDisplay:
    def __init__(self,screen,entities,bg_color=(0,0,255)):
        self.screen = screen
        self.entities = entities
        self.bg_color = bg_color
        self.clock = pygame.time.Clock()

    def drawScreen(self):
        self.screen.fill(self.bg_color)
        for entity in entities:
            screen.blit(entity.image,entity.rect)
        pygame.display.flip()
