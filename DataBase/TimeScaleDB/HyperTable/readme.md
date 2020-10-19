# Hyper Table
<h2>TOC</h2>
&nbsp;&nbsp; - What is HyperTable? <br>
&nbsp;&nbsp; - Hyper Table Create <br>
&nbsp;&nbsp; - Hyper Table Modify <br>
&nbsp;&nbsp; - Hyper Table Delete <br>
<br>

## What is Hyper Table?
```
What is Hyper Table> >>
: http://wiki.hash.kr/index.php/%ED%95%98%EC%9D%B4%ED%8D%BC%ED%85%8C%EC%9D%B4%EB%B8%94
: 하이퍼테이블의 테이블은 단일 기본 키인 행 키로 정렬 된 방대한 데이터 테이블로 생각할 수 있다

Point >>
: 구글의 빅테이블을 모델로 한, 확장 가능한 고성능 오픈 소스 데이터베이스이다. 하이퍼테이블은 기존 관계형 데이터베이스 관리 시스템(RDBMS)에서 잘 처리되지 않는 확장성 문제를 해결하기 위한 목적으로 설계되었다
: 하이퍼테이블은 타임 스탬프를 추가하여 기존의 2차원 테이블 모델을 확장한다. 이 타임 스탬프 차원은 각 테이블 셀의 서로 다른 버전을 나타내는 것으로 생각할 수 있다.
```

## Hyper Table Create
```
다음과 같이 테이블 만드는 SQL 있다. time 이라는 레코드는 HyperTable의 장점인 시계열 기반의 타임 스탬프 자료형을 가지는 걸 알 수 있다.
 CREATE TABLE conditions (
   time        TIMESTAMPTZ       NOT NULL,
   location    TEXT              NOT NULL,
   temperature DOUBLE PRECISION  NULL,
   humidity    DOUBLE PRECISION  NULL
 );

위와 같이 생성하게 되면 그냥 "테이블", TimeScaleDB에서는 아래와 같이 HyperTable로 지정해주는 쿼리를 해줘야 한다.
SELECT create_hypertable('conditions', 'time');
```

## Hyper Table Modify
```
기존의 "alter"를 이용하여 Hyper Table의 내용 변경 가능
ALTER TABLE conditions ADD COLUMN humidity DOUBLE PRECISION NULL;
```

## Hyper Table Delete
```
삭제도 마찬가지로 "DROP"을 이용
DROP TABLE conditions;
```