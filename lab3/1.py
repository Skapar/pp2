import math
#1 task

class strr:
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

class Square:
    def __init__(self, length ):
        self.length  = length

    def area (self):
        print(self.length * self.length == 0)  

class Shape(Square):
    def __init__(self, length = 0 ):
        self.length  = length
    
    def area (self) :
        print(self.length * self.length) 

# ----------------------------------

# 3 task

class Rectangle(Shape):

    def __init__(self,  width):
        self.width = width

    def area (self, w):
        print( self.length  * w)  

# -----------------------------------

x=Rectangle()
x.area()

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

class bank:
    def __init__(self,name:str,balance=0):
        self.name=name
        self.balance=balance
    def deposit(self,add):
        self.balance+=add
    def withdraw(self,vivod):
        if self.balance < vivod:
            print("Not enough money in balance")
        else:
            self.balance-=vivod
            print(self.name,'on your account left',self.balance)
# x=bank('Dauren',500)
# x.deposit(500)
# x.withdraw(200)

def prime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True

def fillt(listik):
    print(list(filter(lambda x : all( x % i !=0  
                                     for i in range(2,x)),listik)))
    
# fillt([3, 5, 8, 15, 7])







 


