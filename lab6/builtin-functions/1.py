def multip(listik):
    # listik=list(map(int, input().split()))
    sum=1
    for i in listik:
        sum*=i
    return sum

print(multip([1,2,3,4]))
# import math
# print(math.prod(listik))

