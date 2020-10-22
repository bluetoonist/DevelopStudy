# TIME SCALE DB 
- Public Document
- Access SetUp
- Sample Data
- Getting Start
- Cloud Service
- TimescaleDB with Docker
- About Hyper table 


## Public Document
```
https://docs.timescale.com/latest/getting-started
```

## Access Setup
```
[CentOS 7.x]
- pgAdmin4
  - pgadmin4.sh 실행에 앞서 먼저 httpd 서비스가 실행되어야함
  - systemctl start httpd

- 로컬 환경에서 관리자 페이지(pgadmin4)에 접근할 경우 막히는 문제가 있음
  - iptables -F
  - firewall-cmd --permanent --add-servce=http
```

## Sample Data
```
https://docs.timescale.com/latest/tutorials/other-sample-datasets
Location : SampleGenExample\readme.md
```

## Getting Start
```
What is TimeScaleDB?
: PostgreSQL에서 확장가능한 시계열 기반 데이터베이스

Installation
: OS 마다 설치 방법이 다르니 설치는 아래의 링크를 참고할 것
: https://docs.timescale.com/latest/getting-started/installation/ubuntu/installation-apt-ubuntu
```

## Cloud Service
```
Cloud Link : https://www.timescale.com/cloud-signup
위 링크에서 클라우드를 통해 TimeScaleDB를 운용할 수 있지만 가격이 붙음 (월 단위)
```

## TimescaleDB with Docker
```
1. Docker를 이용해 TimeScaleDB 컨테이너를 빠르게 생성 가능
Link : https://docs.timescale.com/latest/getting-started/installation/docker/installation-docker

2. Docker Install
docker run -d --name timescaledb -p 5432:5432 -e POSTGRES_PASSWORD=password timescale/timescaledb:1.7.4-pg12

3. Access Shell
docker exec -it timescaledb psql -U postgres

4. Remote Connection
- docker로 구성한 TimScaleDB에 원격으로 접속
  - 운영체제에 맞는 방화벽 설정 or 포트 개방 후 아래와 같이 테스팅
  - psql -U postgres -h {{remote_ip}} -p 5432
  - Password is "password"  (비밀번호는 "password")
```

## About Hyper Table
```
Location : HpyerTable/readme.md
```
