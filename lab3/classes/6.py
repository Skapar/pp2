class filter:
    def __init__(self):
        pass
    def fillt(listik):
        print(list(filter(lambda x : all( x % i !=0  
                                     for i in range(2,x)),listik)))  
# fillt([3, 5, 8, 15, 7])