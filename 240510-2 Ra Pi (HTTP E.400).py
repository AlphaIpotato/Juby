# status error 400

# _*_ coding: utf-8 _*_

import Adafruit_DHT
import requests
import json
import time

# DHT 센서의 핀 번호 설정
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 2  # 센서가 연결된 GPIO 핀 번호로 수정해주세요.

# 서버 URL
SERVER_URL = "http://192.168.226.45:8000/accountapp/Juby/"

def read_sensor():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        return temperature, humidity
    else:
        return None


def send_to_server(temperature, humidity):
    data = {
#    "JUBY": "2",
#    "area": "13",
#    "height": "3.00",
    "temperature": "11",
    "humidity": "22",
#    "soil_ph": "13.00",
#    "soil_ec": "13.00"
    }
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(SERVER_URL, json=data, headers=headers)
        if response.status_code == 200:
            print("Data sent successfully to server.")
        else:
            print("Failed to send data to server. Status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

def main():
    while True:
        sensor_data = read_sensor()
        if sensor_data:
            temperature, humidity = sensor_data
            send_to_server(temperature, humidity)
        else:
            print("Failed to read sensor data.")
            print(DHT_SENSOR)
            print(DHT_PIN)
        time.sleep(1)  # 1초마다 센서를 읽고 서버로 데이터를 전송합니다.



if __name__ == "__main__":
    main()
