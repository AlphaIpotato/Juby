"""
* 버전 관리 linetracer_ver3.py 변동사항
리니어액추에이터 동작 프로세스 변경, 각 높이에서 모든 지점을 돌고 최초 지점으로 돌아오면 높이 변경
DHT22 센서값을 서버로 전송하는 로직 추가
변수 area, temperature, humidity, height, member, farm, area_max, height_max, SERVER_URL 추가

이번 버전에서 조건문 보는 순서가 바뀌었음.
A: area < area_max
B: area == area_max and height == height_max
C: area == area_max
이유는 파이썬은 반복문 가장 상단부터 읽어오며 반복하기 때문
만약 C가 중간에 있다면 B 조건문은 height 값과 상관없이 실행되지 않고 우선 충족되는 C 조건문만 실행됨
이는 최대 높이, 최초 지점에 도착했을 때 문제가 발생하게 만듦

* 변수 목록
AIN1 - Pin 16 / 6핀 모터 드라이버 모듈 핀 AIN1 TO PIN 16 
AIN2 - Pin 26 / 6핀 모터 드라이버 모듈 핀 AIN2 TO PIN 26 
BIN1 - Pin 20 / 6핀 모터 드라이버 모듈 핀 BIN2 TO PIN 20 
BIN2 - Pin 21 / 6민 모터 드라이버 모듈 핀 BIN3 TO PIN 21 

IR_R - Pin 18 / 우측 IR센서의 DATA PIN TO PIN 16
IR_L - Pin 15 / 좌측 IR센서의 DATA PIN TO PIN 18

LONG - Pin 23 / 리니어 액추에이터를 제어하는 모터 드라이버 모듈 핀 IN2 TO PIN 23
SHORT - Pin 22 / 리니어 액추에이터를 제어하는 모터 드라이버 모듈 핀 IN1 TO PIN 22

speed / 라인트레이서가 동작 시 모터에 속도를 지정해주는 변수
PWM / 모터 제어 시 PWM 주기 값을 조절하는 변수
L_Motor / 좌측 모터 전진 핀 지정 변수 (AIN1)
R_Motor / 우측 모터 전진 핀 지정 변수 (BIN1)
L_Motor_B / 좌측 모터 후진 핀 지정 변수 (AIN2)
R_Motor_B / 우측 모터 후진 핀 지정 변수 (BIN2)

stop_count / 정지 지점에 도착한 횟수
start_time / 정지 지점에서 출발한 시간
last_stop_time / 마지막 정지 지점 도착 시간
current_stop_time / 가장 최근 정지 지점 도착 시간

SERVER_URL / 센서값 전송할 서버 주소 지정 변수

area / 현재 섹션 위치 (동시에 정지 횟수도 나타냄)
temperature / DHT22로 받은 주변 기온 지정 변수 
humidity / DHT22로 받은 주변 습도 지정 변수 
height / 액추에이터의 현재 높이 단계 지정 변수 
member / 테이블에 저장된 (회원가입 된) 유저 ID 지정 변수 
farm / 로봇이 운용중인 농장의 장소명 지정 변수
area_max / 정지 구간 전체 갯수 지정 변수
height_max / 최대 높이 구간 지정 변수
"""
import RPi.GPIO as GPIO
import time
import Adafruit_DHT
import requests
import json

# GPIO 설정
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)         # 경고문 생략

SERVER_URL = "http://192.168.0.2:8000/accountapp/robots/"

# DHT22 센서 설정
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 2

# 모터 핀 설정
AIN1 = 16       # 좌 정방향
AIN2 = 26       # 우 정방향
BIN1 = 20       # 좌 역방향
BIN2 = 21       # 우 역방향

# IR 센서 핀 설정
IR_R = 18
IR_L = 15

# 리니어 액추에이터 핀 설정
LONG = 23        # 늘어남  IN2
SHORT = 22       # 줄어듦  IN1

# 모터 핀을 출력으로 설정
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)

# IR 센서 핀을 입력으로 설정
GPIO.setup(IR_R, GPIO.IN)
GPIO.setup(IR_L, GPIO.IN)

# 리니어 액추에이터 핀을 출력으로 설정
GPIO.setup(LONG, GPIO.OUT)
GPIO.setup(SHORT, GPIO.OUT)

pwm = 18000         # PWM 값
# PWM 설정 (모터 제어)
L_Motor = GPIO.PWM(AIN1, pwm)
L_Motor.start(0)

L_Motor_B = GPIO.PWM(AIN2, pwm)
L_Motor_B.start(0)

R_Motor_B = GPIO.PWM(BIN1, pwm)
R_Motor_B.start(0)

R_Motor = GPIO.PWM(BIN2, pwm)
R_Motor.start(0)

# 서버에 전송할 변수(값)을 초기화
area = 0
area_max = 4
height = 1
height_max = 3     
member = "test@naver.com"
farm = "test1"

last_sensor_data_time = None
Speed = 30          # 모터 속도

# 출발할때 제자리에서 다시 인식함을 방지하기 위한 전진 함수
def Foward (T):          
    L_Motor.ChangeDutyCycle(Speed)
    L_Motor_B.ChangeDutyCycle(0)
    R_Motor_B.ChangeDutyCycle(0)
    R_Motor.ChangeDutyCycle(Speed)
    time.sleep(T)

def Actuator_up () :                # 액추에이터 상승
    GPIO.output(LONG,GPIO.HIGH)
    time.sleep(4.5)
    GPIO.output(LONG,GPIO.LOW)

def Actuator_Heigh_Reset () :       # 액추에이터 높이 초기화 (최소 높이)
    GPIO.output(SHORT, GPIO.HIGH)
    time.sleep(14)
    GPIO.output(SHORT, GPIO.LOW)


def read_sensor():                  # 센서값 읽어오기
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        return round(temperature,1), round(humidity,1)
    else:
        print('Failed to read from DHT sensor')
        return None

def send_to_server(area,temperature,humidity,height,member,farm):
    data = {
    "area": area,
    "temperature": temperature,
    "humidity": humidity,
    "height": height,
    "member": member,
    "farm": farm,
    }
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(SERVER_URL, json=data, headers=headers)
        if response.status_code == 200:
            print("Data sent successfully to server.")
            print(f"Temp: {temperature:.1f}°C  Humi: {humidity:.1f}%  area: {area}  height: {height}")
        else:
            print("Failed to send data to server. Status code:", response.status_code)
            print(f"Temp: {temperature:.1f}°C  Humi: {humidity:.1f}%  area: {area}  height: {height}")
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

# 반복 메인 구간
try:
    while True:
        # IR 센서 입력값 읽기
        R_IR = GPIO.input(IR_R)
        L_IR = GPIO.input(IR_L)

        # 양쪽 센서 모두 검은색 라인을 감지하지 못한 경우 전진 (1 = 검정, 0 = 바닥)
        if L_IR == 0 and R_IR == 0:
            start_time = time.time()  # start_time 업데이트
            if time.time() - start_time >= 6:  # N초간 직진일시 라인이탈 판정으로 정지
                L_Motor.ChangeDutyCycle(0)
                L_Motor_B.ChangeDutyCycle(0)
                R_Motor_B.ChangeDutyCycle(0)
                R_Motor.ChangeDutyCycle(0)
                print(f"좌: {L_IR} 우: {R_IR} / 라인이탈, 정지")
            else:
                L_Motor.ChangeDutyCycle(Speed)
                L_Motor_B.ChangeDutyCycle(0)
                R_Motor_B.ChangeDutyCycle(0)
                R_Motor.ChangeDutyCycle(Speed)
                # print(f"좌: {L_IR} 우: {R_IR} / 전진")

        # 왼쪽 검은색 감지 (좌회전)
        elif L_IR == 1 and R_IR == 0:
            L_Motor.ChangeDutyCycle(0)
            L_Motor_B.ChangeDutyCycle(Speed)
            R_Motor_B.ChangeDutyCycle(0)
            R_Motor.ChangeDutyCycle(Speed)
            # print(f"좌: {L_IR} 우: {R_IR} / 좌회전")

        # 오른쪽 검은색 감지 (우회전)
        elif L_IR == 0 and R_IR == 1:
            L_Motor.ChangeDutyCycle(Speed)
            L_Motor_B.ChangeDutyCycle(0)
            R_Motor_B.ChangeDutyCycle(Speed)
            R_Motor.ChangeDutyCycle(0)
            # print(f"좌: {L_IR} 우: {R_IR} / 우회전")

        # 양쪽 검은색 감지 (정지)
        elif L_IR == 1 and R_IR == 1:

            current_time = time.time()      # 이전에 센서 데이터를 전송했는지 확인
            if last_sensor_data_time and current_time - last_sensor_data_time <= 2:
                print("2초 내에 다시 정지 상태 탐지. 전진 수행.")
                Foward(0.3)  # 전진
                continue  # 이후 동작을 건너뜀

            L_Motor.ChangeDutyCycle(0)
            L_Motor_B.ChangeDutyCycle(0)
            R_Motor_B.ChangeDutyCycle(0)
            R_Motor.ChangeDutyCycle(0)
            print(f"좌: {L_IR} 우: {R_IR} / 정지")
            
            sensor_data = read_sensor()
            if sensor_data is not None:
                temperature, humidity = sensor_data  # 데이터 분리
                
                if area < area_max:                                     # 정해진 구간의 갯수 미만일 경우 측정, 전송
                    area += 1
                    print("4초간 센서 안정화")
                    time.sleep(4)
                    send_to_server(area, temperature, humidity, height, member, farm)
                    
                elif area == area_max and height == height_max:         # 최초 출발 지점에서 높이가 최대치일 경우 액추에이터 높이 초기화
                    print(f"height: {height} , area: {area} / 높이, 구역 초기화")
                    area = 1
                    height = 1
                    Actuator_Heigh_Reset()
                    print("4초간 센서 안정화")
                    time.sleep(4)
                    send_to_server(area, temperature, humidity, height, member, farm)
                    
                elif area == area_max:                                  # 최초 출발 지점에 도착시 액추에이터 높이 1단계 상승
                    area = 1
                    print(f"area: {area} / 출발 지점 도착, 높이 증가, 구역 초기화")
                    Actuator_up()
                    height += 1
                    print("4초간 센서 안정화")
                    time.sleep(4)
                    send_to_server(area, temperature, humidity, height, member, farm)
                    
                last_sensor_data_time = time.time()
            else:
                print("Failed to read from DHT sensor")
            Foward(0.3)
        time.sleep(0.01)
            


except KeyboardInterrupt:
    GPIO.cleanup()

finally:
    GPIO.cleanup()
    print("GPIO 핀 초기화 완료.")