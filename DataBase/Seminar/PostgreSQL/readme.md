# PostgreSQL : 인젠스 세미나(Summary)
```
Link : https://www.youtube.com/watch?v=Kvq9yHoU3GE&feature=youtu.be
```

# Opening
## 인젠트 엑스퍼 DB가 "플랫폼"이라 불리는 이유
```
DBMS를 사용하기 위해선
- DBMS 상태 체크를 위한 모니터링
- 장애상황에서 서비스를 계속해야되는 이중화 솔루션
- 매니지먼팅 솔루션 
등이 필요함, 위의 것들이 인젠트 엑스퍼에서 제공하기 떄문에 "플랫폼"이라는 용어를 사용 중
```
## 기존의 오픈소스 DBMS에서 "플랫폼"이라는 단어로 제공되는 서비스가 있나
```
*AWS : Postgre Service를 제공하고 인젠트 엑스퍼 DB를 사용중임
차이점은?
1. AWS : 전 세계적으로 제공되다보니 고객의 니즈에 맞게 해결 불가
2. 엑스퍼 디비 : 고객의 니즈에 맞게 솔루션을 제공
```
<hr>

# 발표자 : Peter Eisentraut ( 피터 아이젠트러시)
## Waht is PosgreSQL?
```
# PostgreSQL?
- 관계형 데이터 베이스 관리 시스템으로 SQL 데이터 베이스
```
## Why PostgreSQL?
```
: 오픈 소스DBMS -> 경제적인 효과
: GPL 라이선스를 따르지만 코드 및 변경 사항을 공유할 필요가 없음
: PostgreSQL 사용하는 것은 완전 무료이 추가 제약없이 원하는 대로 수정할 수 있음
```

## BEST SQL
```
1. SQL 의 177개 특징 170개가 반영됨

2. PostgreSQL
: SQL의 레펀스로서 보여지고 있음
```

## Do relational databases still matter?
```
NoSQL은 No-SQL 이었지만 그 다음으로는 Not-SQL이 되었으며 현재 흐름은 다시 SQL로 가고 있음
```

## PostgreSQL is multi-paradigm
```
PostgreSQL이 지원하는 데이터 모델들
- Relational (관계형)
- object-relational (객체 관계형)
- XML 
- JSON
- graph (그래프)
```

## Who Makes PostgreSQL?
```
// PostgreSQL은 매년 Major Release를 발표 (9월~10월)
// 400명의 Contributor가 참여
// Commiter(29명)는 사람들이 제출한 코드를 리뷰하고 확정하는 역할을 함
// Commiter는 5명의 코어 팀으로 구성되어 있음
```

# Extensions
```
높은 확장성을 가진 DB이므로 다음과 같은 것들이 사용자가 개발해추가할 수 있음
- 데이터 타입
- 사용자 정의 함수 
- 인덱스 타입 정의 (index type)
- 저장 엔진 (Store Engine)

```
