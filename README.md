## **Project explanation**
해당 프로젝트 **JUBY**는 1차 산업 중 농업의 인력 부족 해결과 생산량, 효율성 증가와 객관적이고 최적의 생장 환경데이터를 수집하기 위해 기획되었다.

## **Specification**

|보드| NVIDIA Jetson nano 4GB RAM|
|:--:|:---:|
|환경| Jetson nano Devlopment kit 4.6.1 ( Jetpack 4.6.4 )|
|OS| ubuntu (18.6.04 LTS)|

## **Installed (version)**
**Yolov5**
|프로그램명|버전|
|:---:|:---:|
|SSH|any|
|jtop|any|
|ufw|any|
|Python|3.9.1|
|OpenCV|4.5.5|
|CUDA|10.2.300|
|CUDA Toolkit|10.2|
|PyTorch|1.8.0|
|TorchVision|0.9.0|
|Cython|0.29.36|


## **How to use**
1. 이동 경로대로 라인트레이서가 따라갈 수 있도록 바닥에 적절한 두께로 검은색 테이프를 테이핑한다.
2. 초기 위치와 정지 위치를 위해 검은색 테이프를 양쪽 IR 센서가 한번에 닿을만큼 두껍게 설치한다. 이때 IR센서에 인식되는 시간이 약 1초 이상 유지되도록 두께를 알맞게 정한다.
3. 테이핑을 마치면 적절한 위치에서 IR 센서가 알맞게 위치하도록 로봇의 몸체를 조정을 해준 뒤 [모니터링 모드] OR [수확 모드] 를 실행한다.
4. 적절한 시기마다 원격 또는 직접 조정으로 수확 모드를 실행해준다.



## **WARING**
1. 해당 제품이 라인 이탈하게 될 경우 15초 후에 정지되도록 설정되어 있으므로, [모니터링 모드]에서 해당 상황이 발생시 변동이 거의 없는 데이터를 계속 수집하게 되므로 해당 현상을 통해 상황 인식 후 적절한 위치로 이동시켜 다시 재가동 시켜줄 것.
2. 해당 제품은 라인트레이서에 테이핑된 정지 구간에서 약 4초간 온습도 센서의 높낮이를 조절 후 4회 주기마다 최하단 높이로 초기화 되는게 정상 작동 상태. 만약 초기화되지 않는다면 제작자에게 문의 바람
3. 해당 제품을 재현하기에 앞서 설치 권장중인 버전 외에는 호환성 체크를 하고 진행할 수 있길 바람

## Parts
Rasberry pi 3 model +B
<br/>DC motor drive Board [AT8236 module compact version], [L298N motor driver]
<br/>
<br/>SMPS - [LRS-350-12]
<br/>WHEELTEC DC reduction motor 12V
<br/>Arduino Actuator 150mm 12V
<br/>Level converter 3.3V to 5V
<br/>TCRT5000 IR sensor
<br/>NEXT 208PB-UPS portable batttery
<br/>


## CODE interpret
- 코드 전달인자, 반환값 등 정리


## **LICENSE**
JUNGBU Univercity Student ID Number 20 한승준

## **Status**
**Free**


+회로도, 부품 제원, 기능 구조도




## Server
### lib
<br/>absl-py==2.1.0
<br/>asgiref==3.8.1
<br/>astunparse==1.6.3
<br/>awscli==1.35.19
<br/>boto3==1.35.53
<br/>botocore==1.35.53
<br/>certifi==2024.7.4
<br/>chardet==5.2.0
<br/>charset-normalizer==3.3.2
<br/>click==8.1.7
<br/>colorama==0.4.6
<br/>contourpy==1.3.0
<br/>cycler==0.12.1
<br/>Django==5.0.7
<br/>django-cors-headers==4.4.0
<br/>django-request-logging==0.7.5
<br/>djangorestframework==3.15.2
<br/>docker==7.1.0
<br/>docutils==0.16
<br/>et-xmlfile==1.1.0
<br/>filelock==3.16.1
<br/>flatbuffers==24.3.25
<br/>fonttools==4.54.1
<br/>fsspec==2024.10.0
<br/>gast==0.6.0
<br/>google-pasta==0.2.0
<br/>grpcio==1.64.1
<br/>h5py==3.11.0
<br/>idna==3.7
<br/>jaraco.classes==3.4.0
<br/>jaraco.context==6.0.1
<br/>Jinja2==3.1.4
<br/>jmespath==1.0.1
<br/>keras==3.4.1
<br/>keyring==8.7
<br/>keyrings.alt==5.0.2
<br/>kiwisolver==1.4.7
<br/>libclang==18.1.1
<br/>Markdown==3.6
<br/>markdown-it-py==3.0.0
<br/>MarkupSafe==2.1.5
<br/>matplotlib==3.9.2
<br/>mdurl==0.1.2
<br/>ml-dtypes==0.4.0
<br/>more-itertools==10.5.0
<br/>mpmath==1.3.0
<br/>mysqlclient==2.2.4
<br/>namex==0.0.8
<br/>networkx==3.4.2
<br/>numpy==1.26.4
<br/>opencv-python==4.10.0.84
<br/>openpyxl==3.1.5
<br/>opt-einsum==3.3.0
<br/>optree==0.12.1
<br/>packaging==24.1
<br/>pandas==2.2.2
<br/>pillow==11.0.0
<br/>protobuf==4.25.3
<br/>psutil==6.1.0
<br/>py-cpuinfo==9.0.0
<br/>pyasn1==0.6.1
<br/>Pygments==2.18.0
<br/>pyparsing==3.2.0
<br/>python-dateutil==2.9.0.post0
<br/>pytz==2024.1
<br/>pywin32==308
<br/>pywin32-ctypes==0.2.3
<br/>PyYAML==6.0.2
<br/>requests==2.32.3
<br/>rich==13.7.1
<br/>rsa==4.7.2
<br/>ruamel.yaml==0.18.6
<br/>ruamel.yaml.clib==0.2.12
<br/>s3transfer==0.10.3
<br/>scipy==1.14.1
<br/>seaborn==0.13.2
<br/>setuptools==70.3.0
<br/>six==1.16.0
<br/>sqlparse==0.5.1
<br/>sympy==1.13.1
<br/>tabulate==0.9.0
<br/>tensorboard==2.17.0
<br/>tensorboard-data-server==0.7.2
<br/>tensorflow==2.17.0
<br/>tensorflow-intel==2.17.0
<br/>termcolor==2.4.0
<br/>torch==2.5.1
<br/>torchvision==0.20.1
<br/>tqdm==4.66.6
<br/>typing_extensions==4.12.2
<br/>tzdata==2024.1
<br/>ultralytics==8.3.27
<br/>ultralytics-thop==2.0.10
<br/>urllib3==2.2.2
<br/>voluptuous==0.15.2
<br/>Werkzeug==3.0.3
<br/>wheel==0.43.0
<br/>wrapt==1.16.0
<br/>yolo==0.3.1


# API Documentation

<br/>## Member
<br/>Method: POST  
<br/>URL: /create_member/  
<br/>Description: 회원 생성  
<br/>Request Body:  

<br/>json
<br/>{
<br/>    "member_ID": "user@example.com",
<br/>    "password": "securepassword"
<br/>}

<br/>## SmartFarm
<br/>Method: POST
<br/>URL: /create_smart_farm/
<br/>Description: 스마트 농장 생성
<br/>Request Body:

<br/>json
<br/>{
<br/>    "farm_name": "Farm1",
<br/>    "member": 1,
<br/>    "robot_id": "1234",
<br/>    "crop": "Tomatoes"
<br/>}


<br/>##JubyAdministrator
<br/>Method: POST
<br/>URL: /create_admin/
<br/>Description: 관리자 생성
<br/>Request Body:

<br/>json
<br/>{
<br/>    "admin_ID": "admin@example.com",
<br/>    "admin_password": "adminpassword"
<br/>}


<br/>##Robot
<br/>Method: POST
<br/>URL: /create_robot/
<br/>Description: 로봇 생성
<br/>Request Body:

<br/>json
<br/>{
<br/>    "member": 1,
<br/>    "farm": 1,
<br/>    "area": "Area1",
<br/>    "height": "1.5m",
<br/>    "temperature": "25C",
<br/>    "humidity": "60%",
<br/>    "soil_temperature": "20C",
<br/>    "soil_humidity": "55%"
<br/>}


<br/>##Harvest
<br/>Method: POST
<br/>URL: /create_harvest/
<br/>Description: 수확 정보 생성 및 이미지 기반 성숙도 예측
<br/>Request Body:

<br/>json
<br/>{
<br/>    "image": "<파일>",
<br/>    "robot_id": 1,
<br/>    "farm_name": "Farm1",
<br/>    "member_id": "user@example.com"
<br/>}
