# Window-Plus
## 목차
### [1. 개요](#i-개요)
+ 1. 작품소개
+ 2. 개발배경
### [2. 하드웨어 구성](#ii-하드웨어-구성)
### [3. 기능](#iii-기능)
+ 1. 어플
+ 2. 실내모드
+ 3. 실외모드
+ 4. 원격제어
### [4. 결과](#iiii-결과)
### [5. 기대효과](#iiiii-기대효과)
#### i. 개요
+ 작품소개


Window Plus는 실내의 가스, 온/습도 미세먼지 농도, 빗물 감지를 센서들로부터 값을 받아와 각 값들로부터 조건을 만들어 쾌적한 환경을 위해

창문을 개폐한다. 좀 더 편리하게 실내 환경을 조성하기 위해 실내/실외모드를 두어 각각의 상황에 맞게 창문을 자동으로 제어할 수 있도록 한다.


윈도우 플러스와 스마트폰 어플리케이션을 연결하여  센서에서 받아오는 각종 값들을 실시간으로 스마트폰 어플리케이션 인터페이스에 

표기하여 현재 실내의 상태를 확인할 수 있다. 
또한 Telegram을 이용하여 외부에서도 실내의 환경을 확인할 수 있고, 창문을 제어할 수 있다.


![KakaoTalk_20221028_045309978](https://user-images.githubusercontent.com/116808851/198393074-54d45d61-5b3c-4b5a-985c-aa14d4d4d650.jpg)

+  개발배경


현대인이 실내에 거주하는 시간은 90% 이상이며, 최근에는 코로나19로 인해 재택근무와 비대면 수업도 증가하고 있다.

이에 실내 환경은 매우 중요하다. 실내에는 건강을 해치는 요소들이 있다. 미세먼지, 일/이산화탄소, 라돈등

이러한 요소들은 간단한 방법으로 개선할 수 있다. 그 방법은 바로 환기이다.

![image](https://user-images.githubusercontent.com/116808851/198395599-0d370b0c-2600-4dd4-89f3-c29cfb0ddf50.png)


한국건설기술연구원 연구 자료에 의하면 시간당 10분 환기로 오염물질이 약 40% 정도 제거되는 것으로 분석되었다.


또한 현대사회에는 1인 가구가 급격하게 증가하고있다. 1인 가구가 증가함에 따라 기존 핵가족으로 구성된 실내환경과 다르게 

실내를 관리하는 시간이 줄어듬에 따라 외부 침입 또는 실내 대기 환경 관리해야 할 필요성이 증가하였다.

<img src="https://user-images.githubusercontent.com/116808851/198397869-b79225a3-ff9e-46cd-b170-01a6f1e26539.png" width="800" height="400"/>

#### ii. 하드웨어 구성

<img src="https://user-images.githubusercontent.com/116808851/198398792-a1f81e91-4ac6-44fc-9c43-bb7312e660a0.png" width="800" height="400"/>


<img src="https://user-images.githubusercontent.com/116808851/198399275-62dbc63e-fee9-43e0-aa68-05bc1ebf5ad2.png" width="400" height="400"/><img src="https://user-images.githubusercontent.com/116808851/198399417-48652d68-c4ca-45af-b186-d72e8172866f.png" width="400" height="400"/>

#### iii. 기능
+ 어플
![image](https://user-images.githubusercontent.com/116808851/198402778-e8d208dc-8ef1-4d7b-95e5-b28ad5a2d3b3.png)

+ 실내모드
![image](https://user-images.githubusercontent.com/116808851/198403267-3e0549b6-e9a2-49fb-b63d-95c493c9f5ee.png)
+ 실외모드
![image](https://user-images.githubusercontent.com/116808851/198403337-010f1d63-c89d-4c3b-b465-7e1eb398f333.png)


실내와 실외모드의 차이점은 실외모드에는 실내모드의 기능 + 침입자 감지기능이 추가되었다.
또한 실내모드는 사용자가 직접 실내에서 

사용하기 때문에 센서 수치들을 더 예민하게 두어 쾌적한 실내환경을 유지하도록 하였다.
+ 원격제어

<img src="https://user-images.githubusercontent.com/116808851/198403870-788274e5-b331-4d9c-89f2-c14ad19077aa.png" width="300" height="500"/><img src="https://user-images.githubusercontent.com/116808851/198404025-c6b04a6d-695f-4f08-9e4f-6d64f9cb0892.png" width="300" height="500"/><img src="https://user-images.githubusercontent.com/116808851/198404112-8ac97a98-d7d3-47c0-be53-1bb606bde13b.png" width="300" height="500"/>

gate, open, close, indoor, outdoor, status 6가지 명령어로 원격제어가 가능하고, 침입자나 화재 감지시 사용자에게 실내 상황을 알리게된다.

#### iiii. 결과
https://www.youtube.com/watch?v=CZ8GNtdD36g

실내에서는 Window Plus 전용 앱을 통해 창문을 제어하고, 실외에서는 Telegram bot을 이용하여 원격제어가 가능하다.

실내환경에 변화가 있을 시 즉시 대처한다. ex) 미세먼지 수치가 설정한 수치보다 높아질 경우 외부 미세먼지와 비교해서 더 안 좋을 때 환기 진행,

침입자나 화재 감지 시 사용자에게 실내 사진을 보낸다.

환기가 진행 중에도 시스템이 계속 작동하기 때문에 변화는 환경에 반응하여 대처가 가능하다. ex) 환기 진행 시 비가 오게 된다면, 환기를 중단하고 창문을 닫는다.

외부에서도 간단한 명령어로 실내환경을 확인할 수 있고, 제어할 수 있다. 

ex) gate(창문 개폐 여부), status(실내 환경), open,clsoe(창문 제어), indoor,outdoor(모드 변경)

#### iiiii. 기대효과


편의성 증가 - Window Plus의 환기 시스템과 상황에 맞는 실내/실외모드, 수동 제어 기능을 통해 바쁜 현대사회인들과 몸이 불편하신 어르신이나 장애인분들도 쉽게

실내환경을 관리하고 창문을 제어할 수 있다.

사고 예방 및 보안 향상 - 1인 가구가 증가하고 있는 현재 특히 여성가구도 증가함에 Window Plus를 통해 실내환경을 실시간으로 확인하여 빠르게 대처할 수 있다.
