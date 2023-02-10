# 5 task

def cate_imdb(category):
    sum=0
    count=0
    for i in movies:
        if i['category']==category:
            sum+=i['imdb']
            count+=1
    return sum/count

# print(cate_imdb('Romance'))