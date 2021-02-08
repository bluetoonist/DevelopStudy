#### Review

- MRO (Method Resolution Order) : 메소드 해석순서
  - 어떤 슈퍼클래스부터 초기화하는지를 정의함
  ```python
  class Example(ParentObject):
      pass
  print(Example.mro())
  ```
- Iterator Protocol(이터레이터 프로토콜)
  - Python의 for 루프와 관련된 표현식이 컨테이너 타입의 콘텐츠를 탐색하는 방법을 나타냄
  ```
  for x in foo 와 같은 문장을 만나면 실제로는 iter(foo)를 호출
  함수 iter()는 foo.__iter__를 호출 __iter__ 메서드는 이터레이터 객체를 반환
  ```

- MetaClass, 메타 클래스
  - 클래스가 정의될 때 마다 특별한 동작을 제공할 수 있음