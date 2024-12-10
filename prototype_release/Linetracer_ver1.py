"""
* 버전 관리 linetracer_ver1.py
라인트레이서 구현 최초 버전, 우회전시 좌측 모터 전진 동작, 우측 모터 동작 정지
Rinidoractuator 동작 구현 X

* 변수 목록
AIN1 - Pin 16 / 6핀 모터 드라이버 모듈 핀 AIN1 TO PIN 16 
AIN2 - Pin 26 / 6핀 모터 드라이버 모듈 핀 AIN2 TO PIN 26 
BIN1 - Pin 20 / 6핀 모터 드라이버 모듈 핀 BIN2 TO PIN 20 
BIN2 - Pin 21 / 6민 모터 드라이버 모듈 핀 BIN3 TO PIN 21 

IR_R - Pin 18 / 우측 IR센서의 DATA PIN TO PIN 16
IR_L - Pin 15 / 좌측 IR센서의 DATA PIN TO PIN 18

LONG - Pin 23 / 리니어 액추에이터를 제어하는 모터 드라이버 모듈 핀 IN2 TO PIN 23
SHORT - Pin 22 / 리니어 액추에이터를 제어하는 모터 드라이버 모듈 핀 IN1 TO PIN 22

L_Motor / 좌측 모터 전진 핀 지정 변수
R_Motor / 우측 모터 전진 핀 지정 변수
L_Motor_B / 좌측 모터 후진 핀 지정 변수
R_Motor_B / 우측 모터 후진 핀 지정 변수

stop_count / 정지 지점에 도착한 횟수
start_time / 정지 지점에서 출발한 시간
last_stop_time / 마지막 정지 지점 도착 시간
"""
import RPi.GPIO as GPIO
import time

# GPIO 설정
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# 모터 핀 설정
AIN1 = 16       # 좌 정방향
AIN2 = 26       # 우 정방향
BIN1 = 20       # 좌 역방향
BIN2 = 21       # 우 역방향

# IR 센서 핀 설정
IR_R = 18
IR_L = 15

# 모터 핀을 출력으로 설정
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)

# IR 센서 핀을 입력으로 설정
GPIO.setup(IR_R, GPIO.IN)
GPIO.setup(IR_L, GPIO.IN)

# PWM 설정 (모터 제어)
L_Motor = GPIO.PWM(AIN1, 1000)
L_Motor.start(0)

L_Motor_B = GPIO.PWM(AIN2, 1000)
L_Motor_B.start(0)

R_Motor_B = GPIO.PWM(BIN1, 1000)
R_Motor_B.start(0)

R_Motor = GPIO.PWM(BIN2, 1000)
R_Motor.start(0)

try:
    while True:
        # IR 센서 입력값 읽기
        R_IR = GPIO.input(IR_R)
        L_IR = GPIO.input(IR_L)
        print(f"L_IR: {L_IR}, R_IR: {R_IR}")  # 디버깅을 위한 출력

        # 양쪽 센서 모두 검은색 라인을 감지하지 못한 경우 전진 (1 = 검정, 0 = 바닥)
        if L_IR == 0 and R_IR == 0:
            L_Motor.ChangeDutyCycle(22)
            L_Motor_B.ChangeDutyCycle(0)
            R_Motor_B.ChangeDutyCycle(0)
            R_Motor.ChangeDutyCycle(22)
            print("감지 안됨: 전진")

        # 왼쪽 검은색 감지 (좌회전)
        elif L_IR == 1 and R_IR == 0:
            L_Motor.ChangeDutyCycle(0)
            L_Motor_B.ChangeDutyCycle(0)
            R_Motor_B.ChangeDutyCycle(0)
            R_Motor.ChangeDutyCycle(22)
            print("왼쪽 감지: 좌회전")

        # 오른쪽 검은색 감지 (우회전)
        elif L_IR == 0 and R_IR == 1:
            L_Motor.ChangeDutyCycle(22)
            L_Motor_B.ChangeDutyCycle(0)
            R_Motor_B.ChangeDutyCycle(0)
            R_Motor.ChangeDutyCycle(0)
            print("오른쪽 감지: 우회전")

        # 양쪽 센서 모두 라인을 감지한 경우 정지
        elif L_IR == 1 and R_IR == 1:
            L_Motor.ChangeDutyCycle(0)
            L_Motor_B.ChangeDutyCycle(0)
            R_Motor_B.ChangeDutyCycle(0)
            R_Motor.ChangeDutyCycle(0)
            print("둘 다 검정 감지: 정지")

        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
