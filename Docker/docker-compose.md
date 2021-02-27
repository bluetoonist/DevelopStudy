## Docker Compose

#### Compose?
 -  docker로 컨테이너를 실행할 떄 장황한 옵션을 일일히 적어주는 것을 방지하기 위해 사용

#### docker-compose.yml 파일
- `docker-compose.yml`에 docker images 실행에 관련한 옵션을 세부적으로 기재하고 이 파일을 통해 container를 실행할 수 있다

```yml
version: '3'

services:
  mydb:
    image: 43328f153adc
    environment:
      - MYSQL_ROOT_PASSWORD=1234
    ports:
      - "3306:3306"
    command: >
      bash -c "apt update && apt install unzip && tail -f /dev/null"
```
- `services` : 실행할 서비스들을 해당 block 안에 기재
  - `mydb` :  docker images를 기재해주는 곳
  - `environment`: 환경변수 설정을 기재
  - `ports`: 호스트 컴퓨터와 도커 컨테이너와의 포워딩을 시킬 포트를 지정
    - Ex. "호스트:컨테이너"
  - `command`: docker container에서 실행할 명령어를 기재

#### 실행 명령어
  - docker-compose up -d
    - docker-compose.yml에 있는 파일의 내용을 셋업시킨다 
  - docker-compose start 

#### Tips
 - `command`의 끝에 보면 `tail -f /dev/null`이 들어가 있는 게 보이는게 이 명령을 포함해 실행해 주지 않으면 docker-compose로 실행시킨 컨테이너는 금방 죽음
