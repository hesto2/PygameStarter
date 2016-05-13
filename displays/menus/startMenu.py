from displays.display import Display
import pygame
import constants as C
from entities.entity import Entity
class StartMenu(Display):
    def __init__(self):
        font = pygame.font.Font(None, 36)
        text = font.render("Start Game", 1, (255,255,255),(200,200,200))
        textpos = text.get_rect()
        textpos.centerx = C.GAME.SCREEN.get_rect().centerx
        textpos.centery = C.GAME.SCREEN.get_rect().centery *.25
        text = Entity(textpos,text)
        
        entities = [text]
        super().__init__(C.GAME.SCREEN,entities)
