from entities.entity import Entity
import constants as C
import pygame
import math
from tools.time import getSecondsElapsed
class Timer(Entity):
    font = pygame.font.Font(None, 36)

    def __init__(self):
        text = self.font.render("0:00", 1, C.WHITE)
        textpos = text.get_rect()
        self.pausedStartTick = None
        # Time in seconds the game has been in progress
        self.currentLiveTime = 0
        self.minutes = 0
        self.seconds = 0
        super().__init__(textpos,text)

    def tick(self):
        current_time = pygame.time.get_ticks()
        color = C.BLACK

        # Fix for weird time bug
        if current_time < C.GAME.display.start_time:
            C.GAME.display.start_time = current_time

        if C.GAME.display.state == C.STATE_PAUSED and self.pausedStartTick == None:
            self.pausedStartTick = pygame.time.get_ticks()
        elif C.GAME.display.state != C.STATE_PAUSED and self.pausedStartTick:
            C.GAME.display.start_time = C.GAME.display.start_time + (pygame.time.get_ticks()-self.pausedStartTick)
            self.pausedStartTick = None

        if C.GAME.display.state == C.STATE_PRE_START:
            current_time -= C.GAME.display.start_time
            countdown = C.GAME.display.start_countdown
            timeElapsed = getSecondsElapsed(current_time,countdown)
            self.minutes = 0
            self.seconds = countdown - timeElapsed
            color = C.RED
            if self.seconds <= 0:
                C.GAME.display.state = C.STATE_IN_PROGRESS
                C.GAME.display.start_time = pygame.time.get_ticks()
                color = C.BLACK

        if C.GAME.display.state == C.STATE_IN_PROGRESS:
            start_time = C.GAME.display.start_time
            current_time -= start_time
            time_limit = C.GAME.display.time_limit
            timeElapsed = getSecondsElapsed(current_time,time_limit)
            self.currentLiveTime = timeElapsed
            timeLeft = time_limit - timeElapsed
            self.minutes = math.modf(timeLeft/60)[1]
            self.seconds = (self.minutes * 60) - timeLeft
            self.seconds *= -1


            if timeLeft <= 15:
                color = C.RED
                if timeLeft <= 0:
                    C.GAME.display.state = C.STATE_FINISHED


        time = '%i:%02d' % (self.minutes,self.seconds)
        self.image = self.font.render(time,1,color)
