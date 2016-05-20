from entities.obstacles.wallStd import WallStd
from entities.obstacles.wallSolid import WallSolid
from entities.players.playerStart import PlayerStart
obstacleList = [PlayerStart,WallStd,WallSolid]
loadList = {}
for obstacle in obstacleList:
    loadList[obstacle().keyCode] = obstacle
