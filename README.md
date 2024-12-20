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
