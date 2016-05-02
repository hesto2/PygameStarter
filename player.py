class Player:
    top = False
    bottom = False
    left = False
    right = False

    def __init__(self,rect,keyUp,keyDown,keyLeft,keyRight,image,name):
        self.rect = rect
        self.keyUp = keyUp
        self.keyDown = keyDown
        self.keyLeft = keyLeft
        self.keyRight = keyRight
        self.image = image
        self.name = name
        self.velocityX = 0
        self.velocityY = 0
        self.directionX = 1
        self.directionY = 1


    def move(self,targets,boundary):
        for target in targets:
            if target.name == self.name:
                continue
            self.checkCollision(target)
            self.checkBoundary(boundary)
        self.rect = self.rect.move(self.velocityX,self.velocityY)
        return self.rect

# Collision Detection
    def checkBoundary(self,boundary):
        if self.rect.left + self.velocityX < 0: self.velocityX = 0
        if self.rect.right + self.velocityX > boundary['width'] : self.velocityX = 0
        if self.rect.top + self.velocityY < 0: self.velocityY = 0
        if self.rect.bottom + self.velocityY > boundary['height']: self.velocityY = 0

    def checkCollision(self,target):
        rect = self.rect
        if self.checkTop(target) or self.checkBottom(target): self.velocityY = 0
        if self.checkLeft(target) or self.checkRight(target): self.velocityX = 0


        # top = self.checkTop(target)
        # bottom =  self.checkBottom(target)
        # left =  self.checkLeft(target)
        # right =  self.checkRight(target)
        # if

        # return {"top":top,"bottom":bottom,"left":left,"right":right}


    def checkTop(self,target):
        rect = self.rect
        target = target.rect
        # since it is 2 pixels, it breaks when we get closer than 2 pixels on a given edge
        # Need to make it so that the code will move our object back if it will overlap,
        # Perhaps checking if top+1 will make us on top of another obejct
        if rect.top + self.velocityY < target.bottom and rect.top + self.velocityY > target.top:
            if (rect.left < target.right and rect.left > target.left) or\
                (rect.right > target.left and rect.right < target.right)or\
                (rect.left == target.left and rect.right == target.right):

                return  True

    def checkBottom(self,target):
        rect = self.rect
        target = target.rect
        # if self.name == 'hesto2':
        #     print(target.top)
        if rect.bottom + self.velocityY > target.top and rect.bottom + self.velocityY < target.bottom:
            if (rect.left < target.right and rect.left > target.left) or\
                (rect.right > target.left and rect.right < target.right)or\
                (rect.left == target.left and rect.right == target.right):

                return  True

    def checkLeft(self,target):
        rect = self.rect
        target = target.rect
        if rect.left + self.velocityX < target.right and rect.left + self.velocityX > target.left:
            if (rect.bottom > target.top and rect.bottom < target.bottom) or\
                (rect.top < target.bottom and rect.top > target.top)or\
                (rect.top == target.top and rect.bottom == target.bottom):

                return  True

    def checkRight(self,target):
        rect = self.rect
        target = target.rect
        if rect.right + self.velocityX > target.left and rect.right + self.velocityX < target.right:
            if (rect.bottom > target.top and rect.bottom < target.bottom) or\
                (rect.top < target.bottom and rect.top > target.top)or\
                (rect.top == target.top and rect.bottom == target.bottom):

                return  True




# if rect.top <= target.bottom and rect.top >= target.top:
#     if (rect.left <= target.right and rect.left >= target.left) or\
#         (rect.right >= target.left and rect.right <= target.right):
#         top = True
# if rect.bottom > target.top and rect.bottom < target.bottom:
#     if (rect.left <= target.right and rect.left >= target.left) or\
#         (rect.right >= target.left and rect.right <= target.right):
#         bottom = True
# if rect.left < target.right and rect.left > target.left:
#     if (rect.bottom >= target.top and rect.bottom <= target.bottom) or\
#         rect.top <= target.bottom and rect.top >= target.top:
#         left = True
# if rect.right > target.left and rect.right < target.right:
#     if (rect.bottom >= target.top and rect.bottom <= target.bottom) or\
#         rect.top <= target.bottom and rect.top >= target.top:
#         right = True
