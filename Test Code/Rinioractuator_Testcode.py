import RPi.GPIO as GPIO
import time

# GPIO 모드 설정
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# GPIO 핀 설정
LONG = 23         # 늘어남  IN2
SHORT = 22        # 줄어듦  IN1

# GPIO 핀을 출력 모드로 설정
GPIO.setup(LONG, GPIO.OUT)
GPIO.setup(SHORT, GPIO.OUT)

# 액추에이터를 늘리는 함수
def long(time_sleep):          
    GPIO.output(LONG, GPIO.HIGH)
    print("LONG 핀이 HIGH 상태입니다.")
    time.sleep(time_sleep)  # N초동안 높이 높아짐
    GPIO.output(LONG, GPIO.LOW)
    print("LONG 핀이 LOW 상태입니다.")

# 액추에이터를 줄이는 함수
def short(time_sleep):          
    GPIO.output(SHORT, GPIO.HIGH)
    print("SHORT 핀이 HIGH 상태입니다.")
    time.sleep(time_sleep)  # N초동안 높이 낮아짐
    GPIO.output(SHORT, GPIO.LOW)
    print("SHORT 핀이 LOW 상태입니다.")

try:
    while True:
        user_input = input("1: 늘리기, 2: 줄이기, q: 종료 (입력): ")
        if user_input == '1':
            long(14)  # 14초동안 늘림
        elif user_input == '2':
            short(14)  # 14초동안 줄임
        elif user_input.lower() == 'q':
            break
        else:
            print("잘못된 입력입니다. 1, 2 또는 q를 입력하세요.")

except KeyboardInterrupt:
    print("프로그램이 중단되었습니다.")

finally:
    # GPIO 정리
    GPIO.cleanup()
    print("GPIO 정리 완료.")
