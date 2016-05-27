from entities.entity import Entity
from displays.levels.level import LevelComponent
import constants as C
import pygame

class ScoreBox(LevelComponent):
    def __init__(self,size,numPlayers):
        height = size[1]
        offsetX = 3
        entities = []
        for i in range(numPlayers):
            rankBox = RankBox(height)
            rankBox.rect.x = rankBox.rect.width*i + offsetX*i
            entities.append(rankBox)
        super().__init__(size,entities,C.WHITE)

    def tick(self):
        # Order players in new array by score
        orderedPlayers = self.orderPlayers()

        # Assign players to boxes
        for index, entity in enumerate(self.entities):
            entity.player = orderedPlayers[index]


    def orderPlayers(self):
        orderedPlayers = []
        unorderedPlayers = C.GAME.display.players
        for player in unorderedPlayers:
            if len(orderedPlayers) == 0:
                orderedPlayers.append(player)
                continue
            for index, p in enumerate(orderedPlayers):
                if player.time_tagged <= p.time_tagged:
                    orderedPlayers.insert(index,player)
                    break
                elif index == (len(orderedPlayers)-1) and player.time_tagged >= p.time_tagged:
                    orderedPlayers.append(player)
                    break
        return orderedPlayers

class RankBox(Entity):
    font = pygame.font.Font(None, 18)
    def __init__(self,height):
        image = pygame.Surface((40,height))
        rect = image.get_rect()
        image.fill(C.RED)
        self.player = None
        super().__init__(rect,image)

    def tick(self):
        playerImage = self.player.normalPicture
        playerImage = pygame.transform.scale(playerImage,(40,40))
        playerRect = playerImage.get_rect()
        playerRect.centerx = self.rect.width/2
        playerRect.centery = self.rect.height/2

        rankBox = pygame.Surface((38,10))
        rankBox.fill(C.WHITE)
        rankBox.set_alpha(200)
        rankBoxRect = rankBox.get_rect()
        rankBoxRect.centerx = playerRect.width / 2
        rankBoxRect.bottom = playerRect.height -2

        score = str(int(self.player.time_tagged))
        color = C.BLACK
        if C.GAME.display.taggedPlayer == self.player:
            color = C.RED
        scoreText = self.font.render(score, 1, color)
        scoreTextRect = scoreText.get_rect()
        scoreTextRect.centerx = rankBoxRect.width/2
        scoreTextRect.centery = rankBoxRect.height/2

        rankBox.blit(scoreText,scoreTextRect)
        playerImage.blit(rankBox,rankBoxRect)
        self.image.blit(playerImage,playerRect)
