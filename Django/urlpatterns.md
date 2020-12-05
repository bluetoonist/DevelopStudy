# urlpatterns 로 라우팅
```
프로젝트 최상단에 templates 폴더를 추가하고 경로를 설정하는 법

[template] 등록 /url.py
1. 루트 urls.py에 밑의 라인 추가
import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

2. TEMPLATES 변수의 중간 'DIRS' 부분에 TEMPLATE_DIR 추가
TEMPLATES = [
    {
      ...
        'DIRS': [
            TEMPLATE_DIR
        ],
      ...
]
```

## app/views.py를 urls.py에 추가
```
생성된 app에 라우팅 추가하기
[views.py]
from django.shortcuts import render,redirect
# Create your views herefrom .
def helloworld(request):
    return render(request,"test/index.html")

[urls.py]에 경로 추가
from django.urls import path
from . import views
urlpatterns = [
    path('', views.helloworld, name="helloworld")
]
```

## /urls.py에 라우팅 추가
```
urlpatterns = [
    # path('',include(router.urls)),
    path('/hello',include("auth.urls")),
    url(r"^admin/", admin.site.urls),
]
```
