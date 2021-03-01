## Django Row Query
- Table of Contents
  -  1.connection

#### connection
- Refer
  - https://docs.djangoproject.com/en/3.1/topics/db/sql/
- Summary
  - module import
    ```python
    from django.db import connection
    ```
  - CASE 01: DB conneciton && cusor
    ```python
    with connections['my_db_alias'].cursor() as cursor:
    ```
  - CASE 02: Column with Keys
    ```python
    def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
    ``` 