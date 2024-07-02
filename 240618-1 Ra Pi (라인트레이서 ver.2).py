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
IR_R = 15
IR_L = 18

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
            L_Motor.ChangeDutyCycle(25)
            L_Motor_B.ChangeDutyCycle(0)
            R_Motor_B.ChangeDutyCycle(0)
            R_Motor.ChangeDutyCycle(25)
            print("감지 안됨: 전진")

        # 왼쪽 검은색 감지 (좌회전)
        elif L_IR == 1 and R_IR == 0:
            L_Motor.ChangeDutyCycle(0)
            L_Motor_B.ChangeDutyCycle(0)
            R_Motor_B.ChangeDutyCycle(0)
            R_Motor.ChangeDutyCycle(25)
            print("왼쪽 감지: 좌회전")

        # 오른쪽 검은색 감지 (우회전)
        elif L_IR == 0 and R_IR == 1:
            L_Motor.ChangeDutyCycle(25)
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
