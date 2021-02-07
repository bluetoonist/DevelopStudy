### defaultConnectionProxy 
```python
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View

from django.db import DefaultConnectionProxy
from django.db import connection as django_connection

from MySQLdb.connections import Connection
from MySQLdb.cursors import Cursor


class MySqlCursor(object):
    def __init__(self, connection, cursor: Cursor):
        self.conneciton = connection
        self.cursor = cursor

    def execute(self, *args, **kwargs):
        res = self.cursor.execute(*args, **kwargs)
        res_sql = self.cursor.fetchone()
        print(res_sql)
        return res


class MysSqlConnection(object):
    def __init__(self, connection: DefaultConnectionProxy):
        self.con: Connection = connection

    def cursor(self):
        return MySqlCursor(self, self.con.cursor())


class SimpleRead(View):
    def __init__(self):
        self.dbcon =  MysSqlConnection(django_connection)

    def get(self, request):
        sql = "SELECT * FROM customers WHERE customerNumber ='121';"

        print(self.dbcon.cursor().execute(sql))

        return HttpResponse("result")

```

### Task LIST
```
1. django MySQL 접속 정보 설정
2. library 폴더를 만들어 db 커넥션 핸들링
``` 