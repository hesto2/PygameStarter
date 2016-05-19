from entities.obstacles.wallStd import WallStd
from entities.obstacles.wallSolid import WallSolid
obstacleList = [WallStd,WallSolid]
loadList = {}
for obstacle in obstacleList:
    loadList[obstacle().keyCode] = obstacle
