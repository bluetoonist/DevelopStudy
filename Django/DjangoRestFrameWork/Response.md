## Response Renderere
- Table of Contents
  - 1.Brower Renderer
  - 2.Json Renderer 


#### Beowser Render
- DRF에서 제공해주는 응답 방식 중 Browser를 통해 응답 결과를 반환해주는 방식
  - `settings.py`에 추가
    ```python
    REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
    }
    ```
  - `View` 에서는 다음과 같은 방식으로 리턴
    ```python
    from rest_framework.response import Response
    class MemberView(APIView):
        def get():
        """ Something Task"""
            return Response(data.get())
    ```
    - 위의 data.get()의 데이터 타입은 `Json`

#### Json Renderer
- DRF에서 제공해주는 응답 방식 Json을 통해 응답결과를 반환해주는 방식
  - `settings.py`
    ```
    REST_FRAMEWORK = {
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
        ),
        'DEFAULT_PARSER_CLASSES': (
            'rest_framework.parsers.JSONParser',
        )
    }
    ```
  - `View`에서는 다음과 같은 방식으로 리턴
    ```python
    from rest_framework.views import APIView
        def get():
            """ Something Task"""
            return HttpResponse(json.dumps(data.get()))
    ```
    - 위의 data.get()의 데이터 타입은 `Json`
