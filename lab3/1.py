#1 task

class strr():
    def __init__(soz) :
        soz.s=""
    def getString(soz):
        soz.s=str(input())
    def printString(soz):
        print(soz.s.upper())
        

# word=strr()
# word.getString()
# word.printString()

# -----------------------------------

#2 task

class Square():
    def __init__(self,length):
        self.length=length

    def area(self,area=0):
        area=self.length*self.length
        print(area)

class Shape(Square):
    def __init__(self):
        pass
    def area(self,length):
        self.length=length
        area=self.length*self.length
        print(area)

# ----------------------------------

# 3 task

class rectangle(Shape):
    def __init__(self,width):
        self.width=width
    def area(self,w):
        print(self.length*w)

# -----------------------------------

# 4 task




 


