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
