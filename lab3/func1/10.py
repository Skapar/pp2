#10 task
def unique(listik):
    b=[]
    for i in listik:
        if i not in b:
            b.append(i)
    return b

# print(unique([1, 2, 3, 4, 3]))

# -------------------------------------