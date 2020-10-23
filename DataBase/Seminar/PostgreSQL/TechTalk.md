# 발표자 Peter Geoghegan (피터 게이건)

## B-Tree deduplication in PostgreSQL13 - design and background
```
*B-Tree 중복제거 (키를 한번만 저장)
```
## 키를 한번만 저장
```
동일한 키를 처음부터 저장한 것이 아니라, 요청이 들어올 떄 기다린 다음
예전에 저장한 키를 찾고 값을 추가함

-> 오라클 인덱싱과는 다름
: 오라클 같은 경우, 락킹이 강력한 형태이기 떄문에 동시에 데이터를 수정하는 것이 불가능
```

## Index Size Reductions
```
중복제거를 통해 저장 공간의 사이즈를 절약함, 의료 부분의 데이터베이스에 사용되고 있음
```
## Design goals for deduplication
```
기본적으로 중복제거를 할 수 있게 되었음
```

## The Chanllenge of write amplication
```
: 중복 제거를 하는 이유는 데이터웨어하우스를 위한 인덱싱 작업을 하는 것
: MVCC (Multi-Version Concurency Contorl)를 위한 작업
```
## Right Amplicatoon 문제
```
: 여러 번 물리적으로 인덱싱이 있을 떄 직면하는 문제
```

## A Solution : B-Tree "deletion deduplication"

## Conclusion
```
- 동시 제어 도움이 되었음.
- 유연한 설계를 통해 혁신이 가능하다라는 장점
```