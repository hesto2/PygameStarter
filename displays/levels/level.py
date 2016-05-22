from displays.display import Display
from entities.entity import Entity
from entities.gui.timer import Timer
from entities.players.player import Player
from pygame.locals import *
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
    players = []
    def __init__(self,screen,playAreaEntities,hudEntities,starts=None):
        self.playArea = LevelComponent((C.SCREEN_WIDTH,C.SCREEN_HEIGHT*.90))
        self.hud = []
        self.paused = False
        self.started = False
        self.state = C.STATE_PRE_START
        self.time_limit = 60 #In seconds
        self.start_time = None
        self.start_countdown = 0
        self.taggedPlayer = None
        self.keyPause = False
        self.playArea.entities = playAreaEntities
        self.playArea.rect.centerx = C.GAME.SCREEN.get_rect().centerx
        self.playArea.rect.bottom = C.SCREEN_HEIGHT - C.SCREEN_HEIGHT * .05
        self.gameMode = C.MODE_NORMAL
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
        self.timer = timer

        if starts:
            for player in self.players:
                start = random.choice(starts)
                starts.remove(start)
                player.rect.x = start.rect.x
                player.rect.y = start.rect.y
        else:
            self.players[1].rect.right = self.playArea.rect.width
            self.players[1].rect.bottom = self.playArea.rect.height



        self.hud.extend([timerBox])

        self.start_time = pygame.time.get_ticks()
        super().__init__(screen,[])
    def togglePause(self):
        pass

    def tick(self):
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE] and self.keyPause == False:
            if self.state != C.STATE_PAUSED:
                self.keyPause = True
                self.pause()
        else:
            if keys[K_ESCAPE] == False:self.keyPause = False

        if self.state == C.STATE_IN_PROGRESS:
            for entity in self.playArea.entities:
                entity.tick()

        if self.state == C.STATE_PAUSED:
            if keys[K_ESCAPE] and self.keyPause == False:
                self.keyPause = True
                self.unpause()
            else:
                if keys[K_ESCAPE] == False:self.keyPause = False

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

        for hudEntity in self.hud:
            hudEntity.surface.fill(hudEntity.bg_color)
            for subEntity in hudEntity.entities:
                hudEntity.surface.blit(subEntity.image,subEntity.rect)
            hudItems.append(Entity(hudEntity.rect,hudEntity.surface))

        self.entities = [playArea]
        self.entities.extend(hudItems)
        super().draw()

    def endRound(self):
        from entities.gui import overlays,buttons
        from displays.menus.endRound import EndRoundMenu
        screen = C.GAME.SCREEN.get_rect()
        overlay = overlays.black()
        self.hud.append(overlay)
        self.hud.append(EndRoundMenu())
        self.state = C.STATE_END_ROUND

    def clear(self):
        self.playArea.entities = []
        self.hud = []
        self.state = C.STATE_PRE_START
        self.paused = False
        self.started = False
        self.taggedPlayer = None
        self.players = []

    def initPlayers(self):
        self.players = []
        ball = pygame.image.load('ball.png').convert()
        masterBall = pygame.image.load('masterBall.png').convert()

        ballrect = ball.get_rect()

        ballrect2 = masterBall.get_rect()

        p1Input = {
            "keyUp":K_w,
            "keyDown":K_s,
            "keyLeft":K_a,
            "keyRight":K_d,
            "placeBlock":K_e,
        }
        p2Input = {
            "keyUp":K_UP,
            "keyDown":K_DOWN,
            "keyLeft":K_LEFT,
            "keyRight":K_RIGHT,
            "placeBlock":K_m,
        }
        player1 = Player(ballrect,p1Input,ball,'billums123')
        player2 = Player(ballrect2,p2Input,masterBall,'hesto2')
        players = [player1,player2]
        self.playAreaEntities = []
        self.hudEntities = []
        for player in players:
            self.playAreaEntities.append(player)
            self.players.append(player)

    def pause(self):
        from entities.gui import overlays,buttons
        from displays.menus.pauseLevel import PauseLevel
        screen = C.GAME.SCREEN.get_rect()
        overlay = overlays.black()
        self.hud.append(overlay)
        self.hud.append(PauseLevel())
        self.state = C.STATE_PAUSED

    def unpause(self):
        self.hud = self.hud[:-2]
        self.state = C.STATE_IN_PROGRESS
