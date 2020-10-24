# Sample Data Generator Guide

## 데이터 셋 and 가이드 링크
```
https://docs.timescale.com/latest/tutorials/other-sample-datasets
```

## 샘플 데이터 생성 키노트
```
-샘플 데이터는 위의 링크에서 구할 수 있음
-가이드 대로 따라 가자면 아래의 절차로 샘플 데이터를 생성할 수 있음

Sample Data zip File :  device_small.tar.gz
SampleData_path.csv  : /home/user1/file1.csv 와 같은 경로

1. 샘플 데이터 압축 해제
  : tar xvfz device_small.tar.gz

2. 샘플 데이터 *.sql 초기화 
  : psql -U postgres -d device_small < devices.sql

3. 샘플 데이터 불러오기
  : psql -U postgres -d devices_small -c "\COPY readings FROM SampleData_path.csv CSV"
  : psql -U postgres -d devices_small -c "\COPY device_info FROM SampleData_path.csv CSV"
```

## Feature?
```
먄악 위와 같은 과정에서 데이터가 제대로 생성되어 있지 않다면 데이터베이스를 생성(create)해줘야 됨
```

## How to Create DataBase in psql
```
1. 관리자로 권한 변경
- su

2. psql로 접속
- psql -U postgres -h 127.0.0.1

3 psql 쉘에서 데이터 베이스 생성
- postgres=# create database_small;
```
