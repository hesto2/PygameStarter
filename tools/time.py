import math
def getSecondsElapsed(current,start):
    elapsed = current - start
    elapsed = elapsed/1000
    elapsed = math.modf(elapsed)
    return elapsed[1]
