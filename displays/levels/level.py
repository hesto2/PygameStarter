from displays.display import Display
from entities.entity import Entity
from entities.gui.timer import Timer
from entities.players.player import Player
from pygame.locals import *
import constants as C
import random
import json
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
        from entities.gui.scoreBox import ScoreBox
        topBarHeight = C.SCREEN_HEIGHT*.045
        topBarOffset = 2
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
        self.taggedPlayer.taggedStartSecond = 0

        # Pickup Config
        self.pickupSpawned = True
        self.pickupFrequency = 2
        self.commonPickupChance = 60
        self.uncommonPickupChance = 30
        self.rarePickupChance = 10

        # Hud Items
        # Timer
        timerBox = LevelComponent((200,topBarHeight),color=(255,255,255))
        timerBox.rect.centerx = C.GAME.SCREEN.get_rect().centerx
        timerBox.rect.y = topBarOffset
        timer = Timer()

        timer.rect.centerx = timerBox.rect.width/2
        timer.rect.centery = timerBox.rect.centery
        timerBox.entities.append(timer)
        self.timer = timer

        # Score Box
        scoreBox = ScoreBox((43*len(self.players)-3,topBarHeight),len(self.players))
        scoreBox.rect.centerx = C.GAME.SCREEN.get_rect().centerx
        scoreBox.rect.bottom = C.SCREEN_HEIGHT - topBarOffset



        if starts:
            for player in self.players:
                start = random.choice(starts)
                starts.remove(start)
                player.rect.x = start.rect.x
                player.rect.y = start.rect.y
        else:
            self.players[1].rect.right = self.playArea.rect.width
            self.players[1].rect.bottom = self.playArea.rect.height



        self.hud.extend([timerBox,scoreBox])
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
        # Load settings
        with open(C.SETTINGS_FILE,'r') as f:
            data = f.read()
        self.settings = json.loads(data)

        if self.settings['player1']:
            p1Image = pygame.image.load('lib/players/player1.png').convert()
            p1Rect = p1Image.get_rect()
            with open(C.P1_CONF_FILE,'r') as f:
                data = f.read()
            p1Conf = json.loads(data)
            p1Input = {
                "keyUp":globals()["K_"+p1Conf['up']],
                "keyDown":globals()["K_"+p1Conf['down']],
                "keyLeft":globals()["K_"+p1Conf['left']],
                "keyRight":globals()["K_"+p1Conf['right']],
                # "placeBlock":K_e,
            }
            player1 = Player(p1Rect,p1Input,p1Image,'player1')
            players.append(player1)

        if self.settings['player2']:
            p2Image = pygame.image.load('lib/players/player2.png').convert()
            p2Rect = p2Image.get_rect()
            with open(C.P2_CONF_FILE,'r') as f:
                data = f.read()
            p2Conf = json.loads(data)
            p2Input = {
                "keyUp":globals()["K_"+p2Conf['up']],
                "keyDown":globals()["K_"+p2Conf['down']],
                "keyLeft":globals()["K_"+p2Conf['left']],
                "keyRight":globals()["K_"+p2Conf['right']],
                # "placeBlock":K_e,
            }
            player2 = Player(p2Rect,p2Input,p2Image,'player2')
            players.append(player2)

        if self.settings['player3']:
            p3Image = pygame.image.load('lib/players/player3.png').convert()
            p3Rect = p3Image.get_rect()
            with open(C.P3_CONF_FILE,'r') as f:
                data = f.read()
            p3Conf = json.loads(data)
            p3Input = {
                "keyUp":globals()["K_"+p3Conf['up']],
                "keyDown":globals()["K_"+p3Conf['down']],
                "keyLeft":globals()["K_"+p3Conf['left']],
                "keyRight":globals()["K_"+p3Conf['right']],
                # "placeBlock":K_e,
            }
            player3 = Player(p3Rect,p3Input,p3Image,'player3')
            players.append(player3)

        if self.settings['player4']:
            p4Image = pygame.image.load('lib/players/player4.png').convert()
            p4Rect = p4Image.get_rect()
            with open(C.P4_CONF_FILE,'r') as f:
                data = f.read()
            p4Conf = json.loads(data)
            p4Input = {
                "keyUp":globals()["K_"+p4Conf['up']],
                "keyDown":globals()["K_"+p4Conf['down']],
                "keyLeft":globals()["K_"+p4Conf['left']],
                "keyRight":globals()["K_"+p4Conf['right']],
                # "placeBlock":K_e,
            }
            player4 = Player(p4Rect,p4Input,p4Image,'player4')
            players.append(player4)

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
