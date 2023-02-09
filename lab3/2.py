import math
import itertools
from itertools import permutations
from random import randrange


#1st task
def conv(gramm):
    return gramm*28.3495231

# print(conv(1))

# ---------------------------------


#2nd task
def celsius(far):
    return (5/9)*(far-32)

# print(celsius(2))

# ---------------------------------

# 3rd task
"""
    3rd task
    r=rabits c=chicken
                           4r + 2c = numheads
    1*r+1*c=numlegs  == || 4r + 4c = 4numlegs
                           2c=4numlegs-2numheads 
                           r = numheads-c
"""
def solve(numheads,numlegs):
    c = (numlegs - 2*numheads) /2 
    r = numheads - c
    r=int(r)
    c=int(c)
    return r,",", c

# print(*solve(35,94))

# -------------------------------

# 4th task
def forik(x):
    if x%2==0 :
        return False
    else:
        for i in range(2,x):
            if x % i == 0:
                return False
    return True


def filter_prime(listik):
    b=[]
    for x in listik:
        if forik(x):
            b.append(x)
    return b   
    

# print(filter_prime(([1, 3, 8, 9, 15])))   

# ----------------------------------------------

# 5 th task
def perma(s):
    k = [''.join(p) for p in permutations(s)]
    return k

# b=str(input())
# print(perma(b))

# --------------------------------------------

# 6th task

def reverses(str):
    return str[::-1]

# b=input().split()
# print(*reverses(b))

# ----------------------------------

#7th task

def has_33(*nums):
    d=0
    k=1
    while nums and d!=len(nums) and k!=len(nums)+1:
        if nums[d]==3 and nums[k]==3:
            return True
        d=d+1
        k=k+1
    return False

# print(has_33(2, 3, 3, 4, 5))

# -----------------------------------------------------

#8th task
def spy_game(listik):
    for i in range(len(listik)):
        if i==len(listik)-1:
                return False
        if listik[i]==0:
            for x in range(i+1,len(listik)):
                if x==len(listik)-1:
                    return False
                if listik[x]==0:
                    for k in range(x+1,len(listik)):
                        if listik[k]==7:
                            return True
                        if k==len(listik)-1:
                            return False
# print(spy_game([1,2,4,0,0,7,5]))
# print(spy_game([1,0,2,4,0,5,7]))
# print(spy_game([1,7,2,0,4,5,0]))

# ----------------------------------------------------

#9th task          
def sphere(r):
    return (4/3)*3.1415*r

# --------------------------------------------------------

#10 task
def unique(listik):
    b=[]
    for i in listik:
        if i not in b:
            b.append(i)
    return b

# print(unique([1, 2, 3, 4, 3]))

# -------------------------------------

# 11 task
def palindrome(s):
    tigr=s[::-1]
    if tigr==s:
        return True
    else:
        return False

# print(palindrome(str(input())))

# ------------------------------------------

# 12 task
def histogram(list):
    for i in list:
        k=i
        for j in range(k):
            print('*',sep='',end='')
        print()

# histogram([4, 9, 7])

# ------------------------------
#13 task
def guess_the_number():
    gue=0
    name=str(input("Hello! What is your name?\n"))

    print("Well",name, ',',"I am thinking of a number between 1 and 20.")

    number=randrange(1,21)

    while True:
        print("Take a guess")
        guess=int(input())
        if number==guess:
            print("Good job, KBTU! You guessed my number",gue, "in guesses!")
        elif guess<number:
            gue+=1
            print("Your guess is too low.")
        else:
            gue+=1
            print("Your guess is too high.")

# print(guess_the_number())




    
