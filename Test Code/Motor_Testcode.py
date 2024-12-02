import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
AIN1 = 16       # 좌 정방향
AIN2 = 26       # 우 정방향
BIN1 = 20       # 좌 역방향
BIN2 = 21       # 우 역방향

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



def R_Rail(time_sleep):             # 우측 바퀴
    L_Motor.ChangeDutyCycle(0)
    L_Motor_B.ChangeDutyCycle(0)
    R_Motor_B.ChangeDutyCycle(50)
    R_Motor.ChangeDutyCycle(0)
    time.sleep(time_sleep)

def L_Rail(time_sleep):             # 좌측 바퀴
    L_Motor.ChangeDutyCycle(0)
    L_Motor_B.ChangeDutyCycle(50)
    R_Motor_B.ChangeDutyCycle(0)
    R_Motor.ChangeDutyCycle(0)
    time.sleep(time_sleep)

def forward(time_sleep):            # 전진
    L_Motor.ChangeDutyCycle(22)
    L_Motor_B.ChangeDutyCycle(0)
    R_Motor_B.ChangeDutyCycle(0)
    R_Motor.ChangeDutyCycle(22)
    time.sleep(time_sleep)

def backward(time_sleep):           # 후진
    L_Motor.ChangeDutyCycle(0)
    L_Motor_B.ChangeDutyCycle(50)
    R_Motor_B.ChangeDutyCycle(50)
    R_Motor.ChangeDutyCycle(0)
    time.sleep(time_sleep)

def Right(time_sleep):              # 우회전
    L_Motor.ChangeDutyCycle(50)
    L_Motor_B.ChangeDutyCycle(0)
    R_Motor_B.ChangeDutyCycle(0)
    R_Motor.ChangeDutyCycle(40)
    time.sleep(time_sleep)

def Right(time_sleep):              # 좌회전
    L_Motor.ChangeDutyCycle(40)
    L_Motor_B.ChangeDutyCycle(0)
    R_Motor_B.ChangeDutyCycle(0)
    R_Motor.ChangeDutyCycle(50)
    time.sleep(time_sleep)

def stop(time_sleep):                         # 정지
    L_Motor.ChangeDutyCycle(0)
    L_Motor_B.ChangeDutyCycle(0)
    R_Motor_B.ChangeDutyCycle(0)
    R_Motor.ChangeDutyCycle(0)
    time.sleep(time_sleep)

try:
    forward(5)
    time.sleep(2)
finally:
    stop(True)
