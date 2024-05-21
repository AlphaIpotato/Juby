# status error 404


# _*_ coding: utf-8 _*_

import Adafruit_DHT
import requests # 보내고자 하는 ip로 전송하기 위해 라이브러리
import json # python data 형식을 json 형식으로 변환하기 위한 라이브러리
import time


# DHT 센서의 핀 번호 설정
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 2  # 센서가 연결된 GPIO 핀 번호로 수정해주세요.

# URL(Pulic IP)
SERVER_URL = "http://192.168.226.45:8000/appacountapp/Juby/"

def read_sensor():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        return temperature, humidity

                                            # 좌: Key / 우: data
def send_to_server(temperature, humidity):
    data = {'temperature': temperature, 'humidity': humidity}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(SERVER_URL, data=json.dumps(data), headers=headers)
    if response.status_code == 200:
        print("Data sent successfully to server.")
    else:
        print("Failed to send data to server. Status code:", response.status_code)

def main():
    while True:
        sensor_data = read_sensor()
        if sensor_data:
            temperature, humidity = sensor_data
            send_to_server(temperature, humidity)
        else:
            print("Failed to read sensor data.")
        time.sleep(1)  # 60초마다 센서를 읽고 서버로 데이터를 전송합니다.


if __name__ == "__main__":
    main()