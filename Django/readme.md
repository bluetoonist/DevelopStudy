# Django Cheet Sheet
TOC <br>
1. Create Project Command <br>
2. Running Project Server <br>
3. APP Create Command <br>
4. How to Configure DataBase <br>
5. How to append App <br>
<br>

# 1. Create Project Command
```
django-admin startproject {{PROJECT_NAME}}
```

# 2. Running Project Server
```
python manage.py runserver {PORT}
```
# 3. APP Create Command
```
python manage.py startapp {{APP_NAME}}
```

# 4. How to Configure DataBase
```
project/settings.py -> DATABASES의 'default' 항목을 
'django.db.backends.sqlite3',
'django.db.backends.postgresql',
'django.db.backends.mysql', 또는 'django.db.backends.oracle'
처럼 해당 Data Base 설정에 맞게 변경할 것
```
# 5. How to append App 
```
app 추가 경로 예제 : polls/app.py  -> class PollsConfig
setting.py : INSTALLED_APPS의 리스트에 -> polls.apps.PollsConfig

생성된 app을 추가
```