from displays.display import Display
from entities.entity import Entity
import constants as C
from entities.players.player import Player
from pygame.locals import *
import pygame

class LevelComponent():
    def __init__(self,size=(50,50),entities=[],color=(0,0,0)):
        self.surface = pygame.Surface(size)
        self.rect = self.surface.get_rect()
        self.entities = entities
        self.bg_color = color

class Level(Display):
    playArea = LevelComponent((C.SCREEN_WIDTH*.95,C.SCREEN_HEIGHT*.92))
    hud = LevelComponent()
    paused = False
    def __init__(self,screen,playAreaEntities,hudEntities):
        self.initPlayers()
        self.playArea.entities.extend(playAreaEntities)
        self.playArea.rect.centerx = C.GAME.SCREEN.get_rect().centerx
        self.playArea.rect.centery = C.GAME.SCREEN.get_rect().centery
        # self.hudEntities = hudEntities
        super().__init__(screen,[])

    def togglePause(self):
        pass

    def tick(self):
        for entity in self.playArea.entities:
            entity.tick()
        for entity in self.hud.entities:
            entity.tick()

    def draw(self):
        self.playArea.surface.fill(self.playArea.bg_color)
        for entity in self.playArea.entities:
            self.playArea.surface.blit(entity.image,entity.rect)
        playArea = Entity(self.playArea.rect,self.playArea.surface)

        # for entity in self.hud.entities:
        #     self.hud.surface.blit(entity.rect,entity.image)
        # hud = Entity(self.hud.rect,self.hud.surface
        self.entities = [playArea]
        super().draw()

    def initPlayers(self):
        p1Input = {
            "keyUp":K_w,
            "keyDown":K_s,
            "keyLeft":K_a,
            "keyRight":K_d,
        }
        p2Input = {
            "keyUp":K_UP,
            "keyDown":K_DOWN,
            "keyLeft":K_LEFT,
            "keyRight":K_RIGHT,
        }

        ball = pygame.image.load('ball.png')
        masterBall = pygame.image.load('masterBall.png')

        ballrect = ball.get_rect()

        ballrect2 = masterBall.get_rect()
        ballrect2.right = self.playArea.rect.right
        ballrect2.bottom = self.playArea.rect.bottom

        player1 = Player(ballrect,p1Input,ball,'billums123')
        player2 = Player(ballrect2,p2Input,masterBall,'hesto2')
        players = [player1,player2]
        self.playArea.entities.extend(players)
