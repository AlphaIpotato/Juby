import RPi.GPIO as GPIO
import time

# GPIO 핀 설정
IR_R = 18  # TCRT5000 센서 연결 핀
IR_L = 15

# GPIO 초기화
GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_R, GPIO.IN)
GPIO.setup(IR_L, GPIO.IN)

try:
    while True:
        # TCRT5000 센서 값 읽기
        IR_R_value = GPIO.input(IR_R)
        IR_L_value = GPIO.input(IR_L)

        
        # 센서 값 출력
        if IR_R_value == 0 and IR_L_value == 0:
            print("감지된 검은색 없음")
        elif IR_R_value == 1 and IR_L_value == 0:
            print("오른쪽 검은색 감지")
        elif IR_R_value == 0 and IR_L_value == 1:
            print("왼쪽 검은색 감지")
        else:
            print("둘 다 검정감지")
        
        time.sleep(0.5)  # 0.5초 간격으로 센서 값 확인

except KeyboardInterrupt:
    # 프로그램 종료 시 GPIO 정리
    GPIO.cleanup()
    print("Program stopped")
