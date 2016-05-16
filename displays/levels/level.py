from displays.display import Display
from entities.entity import Entity
from entities.gui.timer import Timer


import constants as C
import random
import pygame

class LevelComponent():
    def __init__(self,size=(50,50),entities=[],color=(0,0,0)):
        self.surface = pygame.Surface(size)
        self.rect = self.surface.get_rect()
        self.entities = entities
        self.bg_color = color
    def tick(self):
        pass

class Level(Display):
    playArea = LevelComponent((C.SCREEN_WIDTH,C.SCREEN_HEIGHT*.90))
    hud = []
    paused = False
    started = False
    state = C.STATE_PRE_START
    time_limit = 3 #In seconds
    start_time = None
    start_countdown = 0
    taggedPlayer = None
    players = []

    def __init__(self,screen,playAreaEntities,hudEntities):
        self.playArea.entities = playAreaEntities
        self.playArea.rect.centerx = C.GAME.SCREEN.get_rect().centerx
        self.playArea.rect.bottom = C.SCREEN_HEIGHT - C.SCREEN_HEIGHT * .05

        # Select Tagged Player
        self.taggedPlayer = random.choice(self.players)
        self.taggedPlayer.tagged()

        # Hud Items
        # Timer
        timerBox = LevelComponent((200,50),color=(255,255,255))
        timerBox.rect.centerx = C.GAME.SCREEN.get_rect().centerx
        timer = Timer()

        timer.rect.centerx = timerBox.rect.width/2
        timer.rect.centery = timerBox.rect.centery
        timerBox.entities.append(timer)
        self.players[1].rect.right = self.playArea.rect.width
        self.players[1].rect.bottom = self.playArea.rect.height



        self.hud.extend([timerBox])
        super().__init__(screen,[])

    def togglePause(self):
        pass

    def tick(self):
        if self.state == C.STATE_IN_PROGRESS:
            for entity in self.playArea.entities:
                entity.tick()
        if self.state == C.STATE_FINISHED:
            self.endRound()

        for entity in self.hud:
            entity.tick()
            for subEntity in entity.entities:
                subEntity.tick()

    def draw(self):
        self.playArea.surface.fill(self.playArea.bg_color)
        for entity in self.playArea.entities:
            self.playArea.surface.blit(entity.image,entity.rect)
        playArea = Entity(self.playArea.rect,self.playArea.surface)

        hudItems = []
        for entity in self.hud:
            entity.surface.fill(entity.bg_color)
            for subEntity in entity.entities:
                entity.surface.blit(subEntity.image,subEntity.rect)
            hudItems.append(Entity(entity.rect,entity.surface))

        self.entities = [playArea]
        self.entities.extend(hudItems)
        super().draw()

    def endRound(self):
        from entities.gui import overlays
        from displays.menus.endRound import EndRoundMenu
        screen = C.GAME.SCREEN.get_rect()
        overlay = overlays.black()
        self.hud.append(overlay)
        # self.hud.append(EndRoundMenu())
        self.state = C.STATE_END_ROUND
