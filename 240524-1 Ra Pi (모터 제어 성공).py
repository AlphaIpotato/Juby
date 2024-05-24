import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
AIN1 = 17
AIN2 = 18
BIN1 = 22
BIN2 = 23


# forward 기준 우측 R, 좌측 L / B는 역방향
GPIO.setwarnings(False)
GPIO.setup(AIN1, GPIO.OUT)
L_Motor = GPIO.PWM(AIN1, 50)
L_Motor.start(0)

GPIO.setup(AIN2, GPIO.OUT)
L_Motor_B = GPIO.PWM(AIN2, 50)
L_Motor_B.start(0)

GPIO.setup(BIN1, GPIO.OUT)
R_Motor_B = GPIO.PWM(BIN1, 50)
R_Motor_B.start(0)

GPIO.setup(BIN2, GPIO.OUT)
R_Motor = GPIO.PWM(BIN2, 50)
R_Motor.start(0)

def forward(time_sleep):
    L_Motor.start(20)
    L_Motor_B.start(0)
    R_Motor_B.start(0)
    R_Motor.start(25)
    time.sleep(time_sleep)

def backward(time_sleep):
    L_Motor.start(0)
    L_Motor_B.start(20)
    R_Motor_B.start(25)
    R_Motor.start(0)
    time.sleep(time_sleep)

def Right(time_sleep):
    L_Motor.start(25)
    L_Motor_B.start(0)
    R_Motor_B.start(0)
    R_Motor.start(20)
    time.sleep(time_sleep)

def Right(time_sleep):
    L_Motor.start(20)
    L_Motor_B.start(0)
    R_Motor_B.start(0)
    R_Motor.start(25)
    time.sleep(time_sleep)

def stop():
    L_Motor.start(0)
    L_Motor_B.start(0)
    R_Motor_B.start(0)
    R_Motor.start(0)

try:
    backward(5)
finally:
    stop()
