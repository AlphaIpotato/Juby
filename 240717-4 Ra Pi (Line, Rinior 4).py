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

Speed = 1          # 모터 속도

try:
    while True:
        # IR 센서 입력값 읽기
        R_IR = GPIO.input(IR_R)
        L_IR = GPIO.input(IR_L)
        # print(f"L_IR: {L_IR}, R_IR: {R_IR}")  # 디버깅을 위한 출력

        # 양쪽 센서 모두 검은색 라인을 감지하지 못한 경우 전진 (1 = 검정, 0 = 바닥)
        if L_IR == 0 and R_IR == 0:
            start_time = time.time()  # start_time 업데이트
            if time.time() - start_time >= 5:  # 5초간 직진일시 라인이탈 판정으로 정지
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
            L_Motor_B.ChangeDutyCycle(0)
            R_Motor_B.ChangeDutyCycle(0)
            R_Motor.ChangeDutyCycle(Speed)
            print(f"좌: {L_IR} 우: {R_IR} / 좌회전")

        # 오른쪽 검은색 감지 (우회전)
        elif L_IR == 0 and R_IR == 1:
            L_Motor.ChangeDutyCycle(Speed)
            L_Motor_B.ChangeDutyCycle(0)
            R_Motor_B.ChangeDutyCycle(0)
            R_Motor.ChangeDutyCycle(0)
            print(f"좌: {L_IR} 우: {R_IR} / 우회전")

        elif L_IR == 1 and R_IR == 1:
            L_Motor.ChangeDutyCycle(0)
            L_Motor_B.ChangeDutyCycle(0)
            R_Motor_B.ChangeDutyCycle(0)
            R_Motor.ChangeDutyCycle(0)
            print(f"좌: {L_IR} 우: {R_IR} / 정지")
            

            if time.time() - last_stop_time >= 10 and stop_count < 3:
                print("stop count: ", stop_count)
                GPIO.output(LONG, GPIO.HIGH)
                time.sleep(4)
                GPIO.output(LONG, GPIO.LOW)
                stop_count += 1  # 정지 횟수 증가
                print("stop count: ", stop_count)
                last_stop_time = time.time()  # 마지막 실행 시간 업데이트


            elif time.time() - last_stop_time >= 10 and stop_count == 3:
                print("stop count: ", stop_count)
                print("최대높이 도달, 높이 초기화")
                GPIO.output(SHORT, GPIO.HIGH)
                time.sleep(14)
                GPIO.output(SHORT, GPIO.LOW)
                stop_count = 0  # stop_count 초기화
                last_stop_time = time.time()  # 마지막 실행 시간 업데이트


            elif time.time() - last_stop_time < 10:
                print("실행 후 경과시간: ",time.time() - last_stop_time)
                Foward(0.1)

        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()