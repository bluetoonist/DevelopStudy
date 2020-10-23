# Docker Note 
<h3>TOC</h3>
&nbsp;&nbsp;&nbsp; 1. Installing <br>
&nbsp;&nbsp;&nbsp; 2. Getting Start<br>

## Installing
```
TOPIC>> Docker 설치
도커는 리눅스 컨테이너 기술, 가상머신에 설치가 됨 
  1. curl -fsSL https://get.docker.com/ sudo sh

TOPIC>> Docker 기본적으로 root권한, root가 아닌 사용자가 사용하려면??
# 현재 접속중인 사용자에게 권한주기
  1. sudo usermod -aG docker $USER 
# your-user 사용자에게 권한주기
  2. sudo usermod -aG docker your-user 
```

## Getting Start
```
1. 컨테이너를 생성하고, 내부 진입
   : docker run ubunut:16.04
- run 명령어 사용 시 , 이미지 저장 확인 후 없으면 다운로드

2. 컨테이너 내부에 들어가기 위한 bash 쉘 실행
   : docker run --rm -it ubuntu:16.04 /bin/bash
- '--rm' -> 프로세스 종료시 컨테이너 자동 삭제
```

## Docker Container Delete
```
# 컨테이너 전부 삭제
docker rm $(docker ps -qa)
```

## Docker Container EXEC
```
# 도커 컨테이너 실행
docker run -d -it {{docker-name}} /bin/bash
```

## Container Connect
```
# 도커 컨테이너 연결
docker attach {{Container-ID}}
```

## Container Save
```
# 도커 컨테이너 백업
sudo docker commit -p {Container-ID} {build-machine}
```

## ALL Image Delete
```
# 도커 이미지 전부 삭제
docker rmi $(docker images -q) -f
```