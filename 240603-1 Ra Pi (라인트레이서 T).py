import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
AIN1 = 17       # L_M
AIN2 = 18       # R_M
BIN1 = 22       # LB_M
BIN2 = 23       # RB_M

IR_R = 26
IR_L = 16


# forward 기준 우측 R, 좌측 L / B는 역방향
GPIO.setwarnings(False)
GPIO.setup(AIN1, GPIO.OUT)
L_Motor = GPIO.PWM(AIN1, 1000)
L_Motor.start(0)

GPIO.setup(AIN2, GPIO.OUT)
L_Motor_B = GPIO.PWM(AIN2, 1000)
L_Motor_B.start(0)

GPIO.setup(BIN1, GPIO.OUT)
R_Motor_B = GPIO.PWM(BIN1, 1000)
R_Motor_B.start(0)

GPIO.setup(BIN2, GPIO.OUT)
R_Motor = GPIO.PWM(BIN2, 1000)
R_Motor.start(0)

GPIO.setup(IR_R, GPIO.IN)


GPIO.setup(IR_L, GPIO.IN)




def R_Rail(time_sleep):             # 우측 바퀴
    L_Motor.start(0)
    L_Motor_B.start(0)
    R_Motor_B.start(0)
    R_Motor.start(20)
    time.sleep(time_sleep)

def R_Rail_B(time_sleep):             # 우측 바퀴 (Back)
    L_Motor.start(0)
    L_Motor_B.start(0)
    R_Motor_B.start(0)
    R_Motor.start(20)
    time.sleep(time_sleep)


def L_Rail(time_sleep):             # 좌측 바퀴
    L_Motor.start(20)
    L_Motor_B.start(0)
    R_Motor_B.start(0)
    R_Motor.start(0)
    time.sleep(time_sleep)

def L_Rail_B(time_sleep):             # 좌측 바퀴 (Back)
    L_Motor.start(20)
    L_Motor_B.start(0)
    R_Motor_B.start(0)
    R_Motor.start(0)
    time.sleep(time_sleep)

def forward(time_sleep):            # 전진
    L_Motor.start(20)
    L_Motor_B.start(0)
    R_Motor_B.start(0)
    R_Motor.start(20)
    time.sleep(time_sleep)

def backward(time_sleep):           # 후진
    L_Motor.start(0)
    L_Motor_B.start(20)
    R_Motor_B.start(20)
    R_Motor.start(0)
    time.sleep(time_sleep)

def RIGHT(time_sleep):              # 우회전
    L_Motor.start(20)
    L_Motor_B.start(0)
    R_Motor_B.start(0)
    R_Motor.start(20)
    time.sleep(time_sleep)

def LEFT(time_sleep):              # 좌회전
    L_Motor.start(20)
    L_Motor_B.start(0)
    R_Motor_B.start(0)
    R_Motor.start(20)
    time.sleep(time_sleep)

def stop(time_sleep):               # 정지
    L_Motor.start(0)
    L_Motor_B.start(0)
    R_Motor_B.start(0)
    R_Motor.start(0)
    time.sleep(time_sleep)


try:
    while True:        
        # 양쪽 센서 모두 검은색 라인을 감지하지 못한 경우 전진
        if not GPIO.input(IR_R) and not GPIO.input(IR_L):
            forward(True)
        
        # 왼쪽 센서만 라인을 감지한 경우 우회전
        elif not GPIO.input(IR_R) and GPIO.input(IR_L):
            R_Rail(True)
            L_Rail(False)

        # 오른쪽 센서만 라인을 감지한 경우 좌회전
        elif GPIO.input(IR_R) and not GPIO.input(IR_L):
            L_Rail(True)
            R_Rail(False)

        # 양쪽 센서 모두 라인을 감지한 경우 n초간 정지
        elif GPIO.input(IR_R) and GPIO.input(IR_L):
            backward(0.2)
            stop(5)


        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
