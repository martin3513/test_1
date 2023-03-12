# 청송대학교 OJ 프론트 엔드 (VER 0.2)


## 개발자

+ 팀원 구성: 나동빈, 장승훈, 김세아, 강경민, 이상수
+ 팀 매니저: 안득하

## 특징

+ 웹팩3(Webkpack3)를 활용한 다중 페이지
+ 쉽게 사용할 수 있는 코드 에디터
+ E-Charts를 활용한 시각화 모듈
+ 사용자 친화적인 명령어 기능

## 설치 방법

노드 JS **v6.11** 버전이 설치가 되어 있어야 합니다.

```
# NPM을 이용해 인스톨을 수행합니다.
sudo npm install

# 웹팩3 DLL 레퍼런스를 이용해 빌드 시간을 절약합니다.
# 기본적으로 이 명령어는 build/webpack.dll.conf.js 내부의 패키지를 업그레이드하지 않았다면 한 번만 수행하면 됩니다. (매 번 실행할 필요가 없음.)
NODE_ENV=development sudo npm run build:dll

# 개발 서버에서 백 엔드 서버에 프록시 테이블을 설정합니다.

```
실행 이후의 Host의 80번 포트 혹은 443번 포트와 본 서버의 8080 포트와 포트 포워딩을 해주어야 합니다.

## 실행 화면

![image](https://user-images.githubusercontent.com/16822641/45494171-78df7080-b7ab-11e8-80b9-2e42509b099a.png)

![image](https://user-images.githubusercontent.com/16822641/45494216-8f85c780-b7ab-11e8-9736-2872e7dc4ddf.png)

## 데모

[교원대 OJ](http://117.17.205.70/)

## 브라우저 지원

+ 인터넷 익스플로러 10 이상 버전을 포함한 다양한 모던 브라우저

## 향후 개발 방향
+ 향후 본 서버에서 추출된 사용자 채점 정보를 이용해 학생들의 수준을 판별하고 분류합니다.
60
+ REST API를 활용한 Micro Service 원칙을 철저하게 따릅니다.
61
​
62
## 오픈소스 라이센스
63
​
64
[MIT](http://opensource.org/licenses/MIT)
