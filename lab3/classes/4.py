import math
# 4 task

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        print(self.x,self.y)
    def move(self,x,y):
        self.x=x
        self.y=y
    def dist(self,x,y):
        d=math.sqrt(pow((self.x-x),2) + pow((self.y-y),2))
        print(d)

# x=Point(10,8)
# x.dist(2,2)
