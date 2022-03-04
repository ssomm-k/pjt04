# Pjt04

평소와 다르게 README를 작성하려한다.

## 프로젝트를 완성하는 과정 일대기

1. 명시된대로 pjt04라는 프로젝트를 만들고, movies라는 앱을 만들며 Django의 시작을 알렸다.

   - settings.py에 movies를 추가해주고 소소한 것들을 변경했다.

     ```python
     # 변경사항 1
     # Application definition
     
     INSTALLED_APPS = [
         'movies',
         'django.contrib.admin',
         'django.contrib.auth',
         'django.contrib.contenttypes',
         'django.contrib.sessions',
         'django.contrib.messages',
         'django.contrib.staticfiles',
     ]
     
     # 변경사항 2
     # Internationalization
     # https://docs.djangoproject.com/en/3.2/topics/i18n/
     
     LANGUAGE_CODE = 'ko-kr'
     
     TIME_ZONE = 'Asia/Seoul'
     ```

     

2. 그 다음 명시된대로 URL을 작성하려고 했다.

   - 여기서부터 막혔다.

     | URL 패턴                 | 역할                             |
     | ------------------------ | -------------------------------- |
     | /movies                  | 메인 페이지 조회                 |
     | /movies/recommendations/ | API를 사용한 특정 추천 영화 조회 |

   - 해결방법 : 교수님 찬스를 사용했다.

     - 먼저, 프로젝트안에 있는 urls.py만 사용하는 것이 아니라는 것을 알아채야했다.

     - 수업시간에 배웠던 앱마다 urls.py를 만들고 include하는 방법을 사용해야한다.

       ```python
       # pjt04 urls.py
       from django.contrib import admin
       from django.urls import path , include
       
       
       urlpatterns = [
           path('admin/', admin.site.urls),
           path('movies/',include('movies.urls')),
       ]
       
       # movies urls.py
       from django.urls import path
       from movies import views
       
       
       urlpatterns = [
           path('',views.index,name='index'),
           path('recommendations/',views.recommendations,name='recommendations'),
       ]
       ```

3. base.html을 통해서 nav와 footer를 만들고 골격을 잡기위해 pjt04와 같은 위치에 templates 폴더를 만들고 그 안에 base.html을 작성하였다.

   - 그 과정해서 settings.py가 한번 더 수정된다.

     ```python
     TEMPLATES = [
         {
             'BACKEND': 'django.template.backends.django.DjangoTemplates',
             # 수정된 부분
             'DIRS': [BASE_DIR / 'templates'],
             'APP_DIRS': True,
             'OPTIONS': {
                 'context_processors': [
                     'django.template.context_processors.debug',
                     'django.template.context_processors.request',
                     'django.contrib.auth.context_processors.auth',
                     'django.contrib.messages.context_processors.messages',
                 ],
             },
         },
     ]
     ```

   - 작성한 base.html을 다음 코드와 같다.

     ```python
     <!DOCTYPE html>
     <html lang="en">
     <head>
       <meta charset="UTF-8">
       <meta http-equiv="X-UA-Compatible" content="IE=edge">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       # 부트스트랩 css
       <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
       {% block style %}{% endblock style %}
       <title>Document</title>
     </head>
     <body>
     # 네브바 햄버거 버전으로 만들기
       <nav class="navbar navbar-expand-lg sticky-top navbar-dark bg-dark">
         <div class="container-fluid">
           <a class="navbar-brand" href="#">SSAFY MOVIE</a>
           <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
             <span class="navbar-toggler-icon"></span>
           </button>
           <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
             <ul class="navbar-nav">
               <li class="nav-item">
                 <a class="nav-link active" aria-current="page" href="{% url 'index' %}">Home</a>
               </li>
               <li class="nav-item">
                 <a class="nav-link" href="{% url 'recommendations' %}">영화추천받기</a>
               </li>
             </ul>
           </div>
         </div>
       </nav>
     # base.html을 상속받는 html이 만드는 것이 작성되는 부분
       <div class='container'>
         {% block content %}
         {% endblock content %}
       </div>
     # 푸터
       <footer class="fixed-bottom bg-secondary d-flex justify-content-around align-items-center"  style="--bs-bg-opacity: .5; height: 40px;">
           <div class="text-light text-center"> @SSAFY</div>
           # href="#"을 통해 아이콘을 누르면 페이지 제일 위로 올라가게 한다.
           <a href="#">
             <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="text-light bi bi-arrow-up-circle-fill" viewBox="0 0 16 16">
               <path d="M16 8A8 8 0 1 0 0 8a8 8 0 0 0 16 0zm-7.5 3.5a.5.5 0 0 1-1 0V5.707L5.354 7.854a.5.5 0 1 1-.708-.708l3-3a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1-.708.708L8.5 5.707V11.5z"/>
             </svg>
           </a>
       </footer>
       # 부트스트랩 js
       <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
     </body>
     </html>

4. View에서 index와recommendations를 선언만한 다음 templates에 index.html을 만들고 recommendations폴더를 생성해 그 안에 recommendations.html를 만들었다.



5. 다시 View로 돌아가 index는 건너뛰고 recommendations부터 만들어 주었다.

   - 여기서부터 pjt02를 하던 과거의 나를 소환해야했다.

     - 우선 pjt02에서 API를 불러오는 코드를 복사해왔다.

     - 그 코드를 한참동안 바라보고 이것 저것 만져보다가 원하는 결과를 만들었다.

       ```python
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
       ```

       굳이 함수를 두개 만들어서 할 필요는 없는데 내가 코드를 볼 때 헷갈려서 따로 만들어서 호출하는 방식을 선택했다. 

     - 위 코드를 통해 쇼생크 탈출과 비슷한 영화를 추천하고 화면에 카드로 만들어 보여줄때 사용할 값들만 넘겨주었다.



6. 다음으로 원하는 화면을 만들기 위해 recommendations.html을 수정하려고 했다.

   - 먼저 base.html을 상속 받고 부트스트랩 카드 종류 중 수평이라는 카드를 사용하여 화면을 작성했다.

     ```python
     {% extends 'base.html' %}
     
     {% block content %}
     <h1 class='text text-center'>쇼생크 탈출과 비슷한 영화 추천 페이지</h1>
     <div class="card mb-3" >
       <div class="row g-0">
         <div class="col-md-4 ">
           <img src="https://image.tmdb.org/t/p/w500/{{poster_path}}" class="img-fluid rounded-start" alt="image">
         </div>
         <div class="col-md-8">
           <div class="card-body">
             <h4 class="card-title">{{ title }}
               <button type="button" class="btn btn-success">{{ vote_average }}</button> 
             </h4>
             <p class="card-text">{{ overview }}</p>
             <p class="card-text"><small class="text-muted"> 개봉일 : {{ release_date }}</small></p>
             <div class="d-grid">
               <button class="btn bg-info" type="button">
                 <a href="https://www.themoviedb.org/movie/{{ movie_id }}" class="text-white text-decoration-none"> 상세정보 </a>
               </button>
             </div>
           </div>
         </div>
       </div>
     </div>
     {% endblock content %}
     ```

     - 상세정보 버튼을 누르면 tmdp에서 해당 영화페이지로 넘어가게 하는 것이 이 html에 핵심이었다.



7. 이제 View에서 index에 대한 부분을 만들 차례이다.

   - 처음에 pjt03에서 사용했던 코드를 그대로 가져와서 코드를 채워놨다.

   - 이후 선택사항이였던 것에 욕심이 생겨서 tmdp에 top_rated를 불러와 사용했다.

     ```python
     def top_rated(title):
     # top_rated URL을 불러옴
         BASE_URL = 'https://api.themoviedb.org/3'
         path = '/movie/top_rated'
         parmas = {
             'api_key' : '2d80cdc7b6bf40261c314f32486b4784',
             'language': 'ko',
         }
         response = requests.get(BASE_URL+path,params=parmas)
         data = response.json()
     
         top_movie = []
         # main page에 6개의 카드만 두려고 6개만 불러온다.
         for i in range(6):
             top_movie.append(data['results'][i])
         return top_movie
     
     
     def index(request):
         top_movie_list = top_rated('영화')
         context = {
             'top_movie_list' : top_movie_list,
         }
     
         return render(request,'index.html',context)
     ```



8. index.html만 작성하면 이제 완성인줄 알았다.

   - 먼저 base.html을 상속받는다.

   - 그다음 header로 사용할 이미지를 static 폴더를 생성하여 저장한다.

   - static을 사용하기 위해 load를 해주고 헤더를 채워준다.

   - for문을 통해 영화목록을 반응형으로 만들어준다.

   - 그 for문 안에 modal도 넣어준다. 여기가 내 마지막 비극의 시작이다.

     - modal에서 가장 중요하다고 했던 것이 modal에 선언한 id의 이름과 modal을 사용하려고 하는 부분에 작성한 id의 명이 같아야한다고 배웠다.

       ```python
       # 초기에 작성한 코드
       # 모달을 사용하는 부분
       <div class="card" data-bs-toggle="modal" data-bs-target="#stillcut">
       # 모달에 선언하는 부분
       <div class="modal" id="stillcut" tabindex="-1">
       ```

       위 코드처럼 작성을 하여 만들어지 페이지에서 제일 처음 카드의 모달이 잘 나왔다. 성공인줄 알았다. 그것은 나의 착각이였다. 모든 카드가 다 같은 모달이 나왔다.

   - 자 여기서 한참 허우적 거리다 이 문제를 먼저 해결한 분께 도움을 받았다.

     - 첫째, modal에 id값에는 숫자가 들어오면 안되고 띄어쓰기가 있어서도 안된다.

     - 둘째, 해서 기존에 가지고있는 것들 중엔 활용을 할 수 있는 값이 없다.

     - 그래서 다시 View에 있는 index를 수정한다.

       ```python
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
       ```

     - 새로운 modal_id를 만들어서 모달 id에 사용하였다.

9. 드디어 완성된 index.html!!!!

   ```python
   {% extends 'base.html' %}
   {% load static %}
   
   {% block content %}
   <header >
     <img src="{% static 'header1.jpg' %}" class="d-block w-100" alt="...">
   </header>
   
   <section class="container">
     <h1 class="text-center my-3">영화목록</h1>
     <div class="row mb-5">
   	# for문을 사용하면 하나하나 만들지 않아도 된다!!!!
       {% for i in top_movie_list %}
       # 이 부분이 카드 만드는 부분
       <article class="col-md-6 col-lg-4 col-xl-3 my-1">
         <div class="card" data-bs-toggle="modal" data-bs-target="#{{ i.modal_id }}">
           <img src="https://image.tmdb.org/t/p/w500/{{ i.poster_path }}" class="card-img-top" alt="...">
           <div class="card-body">
             <h5 class="card-title">{{i.title}}</h5>
             <p class="card-text">{{ i.overview }}</p>
           </div>
           <div class="card-footer text-start">
             {{ i.release_date }}
           </div>
         </div>
       </article>
       # 이 부분이 모달을 만드는 부분
       <div class="modal" id="{{ i.modal_id }}" tabindex="-1">
         <div class="modal-dialog">
           <div class="modal-content">
             <div class="modal-header">
               <h5 class="modal-title">{{i.title}}</h5>
               <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
             </div>
             <div class="modal-body">
               <img src="https://image.tmdb.org/t/p/w500/{{ i.poster_path }}" class="card-img-top" alt="...">
             </div>
             <div class="modal-footer">
               <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
             </div>
           </div>
         </div>
       </div>
       {% endfor %}
     </div>
   </section>
   
   {% endblock content %}
   ```

10. 끝이다!



## pjt04를 하고 난 후기

처음엔 css적인 디테일 말고도 html에 대한 부분도 많이 놓치고 넘어갔다. 뭐 물론 한번에 다 완벽하게 하면 좋겠지만 그럼 너무 오래걸린다는걸 나는 이미 알았던 것 같다. 덕분에 큰틀은 먼저 다 만들어놔서 내가 미리 했던 부분에서 막혀있는 팀원들을 도와줄 수 있었다. 저녁도 포기한채 장장 8시간에 걸쳐 완성한 프로젝트였다. 또 README를 제대로 작성해 두지 않으면 머지않은 미래에 내가 고생할 것 같아서 이번 README는 약 1시간에 걸쳐 작성하였다. 부디 공들여 작성한 README가 미래에 나에게 도움이 되길,,,