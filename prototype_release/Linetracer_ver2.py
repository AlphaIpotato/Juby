"""
* 버전 관리 linetracer_ver2.py 변동사항
Rinioractuator 기능 구현, 지점 도착시 stopcount를 확인하여 4까지 증가, 4 이상인 상태에서 액추에이터 상승 명령시 14초간 하강 진행
우회전시 좌측 모터는 전진, 우측 모터는 후진 동작으로 기동성 증가
모터 동작 속도 제어 편의성을 위한 "speed" 변수 추가
모터 동작 시 낮은 펄스 주기때문에 높은 모터값을 지정해줘도 본래 출력이 나오지 않았음, 이를 위해 PWM 값을 지정해 줄 수 있는 PWM 변수 추가

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

def Foward (T):
    L_Motor.ChangeDutyCycle(Speed)
    L_Motor_B.ChangeDutyCycle(0)
    R_Motor_B.ChangeDutyCycle(0)
    R_Motor.ChangeDutyCycle(Speed)
    time.sleep(T)


start_time = 0  # start_time 초기화
stop_count = 0  # stop_count 초기화
last_stop_time = time.time()  # last_stop_time 초기화

Speed = 20          # 모터 속도

try:
    while True:
        # IR 센서 입력값 읽기
        R_IR = GPIO.input(IR_R)
        L_IR = GPIO.input(IR_L)

        # 양쪽 센서 모두 검은색 라인을 감지하지 못한 경우 전진 (1 = 검정, 0 = 바닥)
        if L_IR == 0 and R_IR == 0:
            start_time = time.time()  # start_time 업데이트
            if time.time() - start_time >= 4:  # 4초간 직진일시 라인이탈 판정으로 정지
                L_Motor.ChangeDutyCycle(0)
                L_Motor_B.ChangeDutyCycle(0)
                R_Motor_B.ChangeDutyCycle(0)
                R_Motor.ChangeDutyCycle(0)
                start_time = time.time()  # start_time 업데이트
                print(f"좌: {L_IR} 우: {R_IR} / 라인이탈, 정지")
            else :
                L_Motor.ChangeDutyCycle(Speed)
                L_Motor_B.ChangeDutyCycle(0)
                R_Motor_B.ChangeDutyCycle(0)
                R_Motor.ChangeDutyCycle(Speed)
                print(f"좌: {L_IR} 우: {R_IR} / 전진")

        # 왼쪽 검은색 감지 (좌회전)
        elif L_IR == 1 and R_IR == 0:
            L_Motor.ChangeDutyCycle(0)
            L_Motor_B.ChangeDutyCycle(Speed)
            R_Motor_B.ChangeDutyCycle(0)
            R_Motor.ChangeDutyCycle(Speed)
            print(f"좌: {L_IR} 우: {R_IR} / 좌회전")

        # 오른쪽 검은색 감지 (우회전)
        elif L_IR == 0 and R_IR == 1:
            L_Motor.ChangeDutyCycle(Speed)
            L_Motor_B.ChangeDutyCycle(0)
            R_Motor_B.ChangeDutyCycle(Speed)
            R_Motor.ChangeDutyCycle(0)
            print(f"좌: {L_IR} 우: {R_IR} / 우회전")

        # 양쪽 검은색 감지 (정지)
        elif L_IR == 1 and R_IR == 1:             
            L_Motor.ChangeDutyCycle(0)
            L_Motor_B.ChangeDutyCycle(0)
            R_Motor_B.ChangeDutyCycle(0)
            R_Motor.ChangeDutyCycle(0)
            print(f"좌: {L_IR} 우: {R_IR} / 정지")
            
            # 마지막 정지 후 N초 이상 지남 + 정지횟수 N회
            if time.time() - last_stop_time >= 4 and stop_count < 4:  
                print("stop count: ", stop_count)
                GPIO.output(LONG, GPIO.HIGH)
                time.sleep(4)
                GPIO.output(LONG, GPIO.LOW)
                stop_count += 1  # 정지 횟수 증가
                print("stop count: ", stop_count)
                last_stop_time = time.time()  # 마지막 실행 시간 업데이트

            # 마지막 정지 후 N초 이상 지남 + 정지횟수 N회
            elif time.time() - last_stop_time >= 4 and stop_count == 4:     
                print("stop count: ", stop_count)
                print("최대높이 도달, 높이 초기화")
                GPIO.output(SHORT, GPIO.HIGH)
                time.sleep(14)
                GPIO.output(SHORT, GPIO.LOW)
                stop_count = 0  # stop_count 초기화
                last_stop_time = time.time()  # 마지막 실행 시간 업데이트

            # 4초 이내로 다시 시작
            elif time.time() - last_stop_time < 4:
                print("실행 후 경과시간: ",time.time() - last_stop_time)
                Foward(0.01)

        time.sleep(0.01)

except KeyboardInterrupt:
    GPIO.cleanup()