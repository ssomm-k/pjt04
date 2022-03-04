from django.shortcuts import render
import requests
import random

# Create your views here.
def top_rated(title):
# 추천 영화 URL을 불러옴
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/top_rated'
    parmas = {
        'api_key' : '2d80cdc7b6bf40261c314f32486b4784',
        'language': 'ko',
    }
    response = requests.get(BASE_URL+path,params=parmas)
    data = response.json()

    top_movie = []
    for i in range(6):
        top_movie.append(data['results'][i])
    return top_movie


def index(request):
    top_movie_list = top_rated('영화')
    ls = ['a','b','c','d','e','f']
    cnt =0
    for i in top_movie_list:
        i['modal_id'] = ls[cnt]
        cnt += 1
    
    context = {
        'top_movie_list' : top_movie_list,
    }

    return render(request,'index.html',context)


# 쇼생크 탈출과 비슷한 영화 추천 받기
def recommendation(title):
        # 추천 영화 URL을 불러옴
        BASE_URL = 'https://api.themoviedb.org/3'
        path = '/movie/278/recommendations'
        parmas = {
            'api_key' : '2d80cdc7b6bf40261c314f32486b4784',
            'language': 'ko',
        }
        response = requests.get(BASE_URL+path,params=parmas)
        data = response.json()
        # 원하는 결과가 나오도록 조건문 생성
        movie_list = data.get('results')
        return movie_list

def recommendations(request):
    movielist = recommendation('쇼생크 탈출')
    choice_movie = random.choice(movielist)
    title = choice_movie['title']
    overview = choice_movie['overview']
    release_date =choice_movie['release_date']
    vote_average = round(choice_movie['vote_average'],1)
    poster_path = choice_movie['poster_path']
    movie_id = choice_movie['id']
    
    context = {
        'movielist' : movielist,
        'choice_movie' : choice_movie,
        'title' : title,
        'overview' : overview,
        'release_date' :release_date,
        'vote_average' : vote_average,
        'poster_path' : poster_path,
        'movie_id' : movie_id,

    }
    return render(request,'recommendations/recommendations.html',context)