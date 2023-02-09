movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1 task

def single_movie(name):
    for i in movies:
        if i['name']==name and float(i['imdb']>5.5):
            return True
    return False
        



# print(single_movie('Exam'))
# -------------------------------------------------------
# 2 task
def sublist_movies(dict):
    b=[]
    for i in dict:
        if i['imdb']>5.5:
            b.append(i['name'])
    return b


# sublist_movies(movies)
# print(sublist_movies(movies))
#---------------------------------------------

# 3 task
def category_movies(name):
    b=[]
    for i in movies:
        if i['category']==name:
            b.append(i['name'])
    return b

# print(category_movies('Romance'))

# -------------------------------------------------

# 4 task
def list_movies(listik):
    sum=0
    for i in listik:
        sum+=i['imdb']

    return sum/len(listik)
    
# print(list_movies(movies))

# ---------------------------------------------------

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


