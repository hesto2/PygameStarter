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

# Collision Detection

    def checkCollsion(self,target):
        rect = self.rect

        top = self.checkTop(target)
        bottom =  self.checkBottom(target)
        left =  self.checkLeft(target)
        right =  self.checkRight(target)

        return {"top":top,"bottom":bottom,"left":left,"right":right}


    def checkTop(self,target):
        rect = self.rect

        # since it is 2 pixels, it breaks when we get closer than 2 pixels on a given edge
        # Need to make it so that the code will move our object back if it will overlap,
        # Perhaps checking if top+1 will make us on top of another obejct

        if rect.top <= target.bottom and rect.top >= target.top:
            if (rect.left <= target.right-2 and rect.left >= target.left+2) or\
                (rect.right >= target.left+2 and rect.right <= target.right-2)or\
                (rect.left == target.left and rect.right == target.right):
                return  True

    def checkBottom(self,target):
        rect = self.rect
        if rect.bottom > target.top and rect.bottom < target.bottom:
            if (rect.left <= target.right-2 and rect.left >= target.left+2) or\
                (rect.right >= target.left+2 and rect.right <= target.right-2)or\
                (rect.left == target.left and rect.right == target.right):
                return  True

    def checkLeft(self,target):
        rect = self.rect
        if rect.left < target.right and rect.left > target.left:
            if (rect.bottom >= target.top+2 and rect.bottom <= target.bottom-2) or\
                (rect.top <= target.bottom-2 and rect.top >= target.top+2)or\
                (rect.top == target.top and rect.bottom == target.bottom):
                return  True

    def checkRight(self,target):
        rect = self.rect
        if rect.right > target.left and rect.right < target.right:
            if (rect.bottom >= target.top+2 and rect.bottom <= target.bottom-2) or\
                (rect.top <= target.bottom-2 and rect.top >= target.top+2)or\
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
