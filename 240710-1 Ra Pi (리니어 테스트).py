import RPi.GPIO as GPIO
import time

# GPIO 모드 설정
GPIO.setmode(GPIO.BCM)

# GPIO 핀 설정
GPIO_22 = 22        # 늘어남
GPIO_27 = 27        # 줄어듦

# GPIO 핀을 출력 모드로 설정
GPIO.setup(GPIO_22, GPIO.OUT)
GPIO.setup(GPIO_27, GPIO.OUT)


# GPIO 핀을 HIGH 상태로 설정        / 완전히 늘어나고 줄어드는데 약 13~14초
GPIO.output(GPIO_22, GPIO.HIGH)
print("GPIO_22 핀이 HIGH 상태입니다.")
time.sleep(15)  # 2초 동안 대기

# GPIO 핀을 LOW 상태로 설정
GPIO.output(GPIO_22, GPIO.LOW)
print("GPIO_22 핀이 LOW 상태입니다.")
time.sleep(2)  # 2초 동안 대기



# GPIO 핀을 HIGH 상태로 설정
GPIO.output(GPIO_27, GPIO.HIGH)
print("GPIO_27 핀이 HIGH 상태입니다.")
time.sleep(15)  # 2초 동안 대기

# GPIO 핀을 LOW 상태로 설정
GPIO.output(GPIO_27, GPIO.LOW)
print("GPIO_27 핀이 LOW 상태입니다.")
time.sleep(2)  # 2초 동안 대기




# GPIO 정리
GPIO.cleanup()
