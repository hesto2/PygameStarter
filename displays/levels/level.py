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

        # Pickup Config
        self.pickupSpawned = True
        self.pickupFrequency = 2
        self.commonPickupChance = 60
        self.uncommonPickupChance = 30
        self.rarePickupChance = 10

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
            # Check if it is time to spawn a random pickup
            self.handlePickups()
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
        players = []



        p1Image = pygame.image.load('lib/players/player1.png').convert()
        p1Rect = p1Image.get_rect()
        p1Input = {
            "keyUp":K_w,
            "keyDown":K_s,
            "keyLeft":K_a,
            "keyRight":K_d,
            "placeBlock":K_e,
        }
        player1 = Player(p1Rect,p1Input,p1Image,'player1')
        players.append(player1)

        p2Image = pygame.image.load('lib/players/player2.png').convert()
        p2Rect = p2Image.get_rect()
        p2Input = {
            "keyUp":K_UP,
            "keyDown":K_DOWN,
            "keyLeft":K_LEFT,
            "keyRight":K_RIGHT,
            "placeBlock":K_m,
        }
        player2 = Player(p2Rect,p2Input,p2Image,'player2')
        players.append(player2)

        p3Image = pygame.image.load('lib/players/player3.png').convert()
        p3Rect = p3Image.get_rect()
        p3Input = {
            "keyUp":K_i,
            "keyDown":K_k,
            "keyLeft":K_j,
            "keyRight":K_l,
            "placeBlock":K_m,
        }
        player3 = Player(p3Rect,p3Input,p3Image,'player3')
        players.append(player3)

        # p4Image = pygame.image.load('lib/players/player4.png').convert()
        # p4Rect = masterBall.get_rect()
        # p4Input = {
        #     "keyUp":K_i,
        #     "keyDown":K_k,
        #     "keyLeft":K_j,
        #     "keyRight":K_l,
        #     "placeBlock":K_m,
        # }
        # player4 = Player(p4Rect,p4Input,p4Image,'player4')
        # players.append(player4)

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

    def handlePickups(self):
        from tools import lists
        if self.timer.currentLiveTime % self.pickupFrequency == 0 \
        and self.timer.currentLiveTime >= self.pickupFrequency:
            if self.pickupSpawned:
                return
            self.pickupSpawned = True
            randNum = random.randint(0,100)
            if randNum <= 100-self.commonPickupChance:
                pickups = lists.commonPickups
            elif randNum <= 100-self.uncommonPickupChance:
                pickups = lists.uncommonPickups
            else:
                pickups = lists.rarePickups
            pickup = random.choice(pickups)
            self.playArea.entities.append(pickup())
        else:
            self.pickupSpawned = False
