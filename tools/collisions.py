import constants as C
def checkTop(host,target):
    rect = host.rect
    target = target.rect
    # since it is 2 pixels, it breaks when we get closer than 2 pixels on a given edge
    # Need to make it so that the code will move our object back if it will overlap,
    # Perhaps checking if top+1 will make us on top of another obejct
    if rect.top + host.velocityY < target.bottom and rect.top + host.velocityY > target.top:
        if (rect.left < target.right and rect.left > target.left) or\
            (rect.right > target.left and rect.right < target.right)or\
            (rect.left == target.left and rect.right == target.right):

            return  True

def checkBottom(host,target):
    rect = host.rect
    target = target.rect
    # if host.name == 'hesto2':
    #     print(target.top)
    if rect.bottom + host.velocityY > target.top and rect.bottom + host.velocityY < target.bottom:
        if (rect.left < target.right and rect.left > target.left) or\
            (rect.right > target.left and rect.right < target.right)or\
            (rect.left == target.left and rect.right == target.right):

            return  True

def checkLeft(host,target):
    rect = host.rect
    target = target.rect
    if rect.left + host.velocityX < target.right and rect.left + host.velocityX > target.left:
        if (rect.bottom > target.top and rect.bottom < target.bottom) or\
            (rect.top < target.bottom and rect.top > target.top)or\
            (rect.top == target.top and rect.bottom == target.bottom):

            return  True

def checkRight(host,target):
    rect = host.rect
    target = target.rect
    if rect.right + host.velocityX > target.left and rect.right + host.velocityX < target.right:
        if (rect.bottom > target.top and rect.bottom < target.bottom) or\
            (rect.top < target.bottom and rect.top > target.top)or\
            (rect.top == target.top and rect.bottom == target.bottom):

            return  True

def moveToEdge(host,target,side):
    if side == C.SIDE_TOP:
        target.velocityY = host.rect.bottom - target.rect.top
    elif side == C.SIDE_BOTTOM:
        target.velocityY = host.rect.top - target.rect.bottom
    elif side == C.SIDE_LEFT:
        target.velocityX = host.rect.right - target.rect.left
    elif side == C.SIDE_RIGHT:
        target.velocityX = host.rect.left - target.rect.right
