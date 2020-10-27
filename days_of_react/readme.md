# React Cheet Seet
```
# React?
: MVC 패턴 중 V(View)를 담당하는 라이브러리
: 프론트 프레임 워크 중 3대장 (React, Vue, Angular)
: 가상 DOM을 사용해 브라우저의 부담을 줄임 (DOM 조작은 브라우저에 무리를 줌)
: 가상이라는 특성을 활용해, 모바일, 데스크탑 애플리케이션에도 사용 가능

# Component 시스템
: 컴포넌트를 잘게 쪼개면 재사용성이 높아짐, 즉 해당 컴포넌트를 불러오기만 하면 됨
: 컴포넌트의 두 가지 핵심 원리
   1. 독립적으로 기능할 것
   2. 재사용 가능할 것
```

# Install
```
1. npm install -g create-react-app
-> npm은 프로그램을 설치함

2. npx create-react-app
-> "create-react-app"을 임시로 설치 뒤 지움
```

# React Command
```
1. create-react-app .
: 현재 디렉터리를 기점으로 리액트 환경을 구성해줌

2. npm run start

3. Deploy
Production of Application
--> npm run build
: build 폴더가 생성되며 최적화 됨
: 서비스를 올릴 때는 build 안의 파일들을 올리면 됨
```

# React Structure
```
1. public/  *.html 이 있는 부분 
2. src/ 
- index.js
- App.js
```
# Syntax Note
```
1. props : ./reactstudyproject/propsNote.txt
2. state : ./reactstudyproject/stateNote.txt
```