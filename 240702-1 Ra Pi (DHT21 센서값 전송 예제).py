# 주기적으로 전송되는 data들의 PK 중복과 자료형이 맞지 않아서 안됬던 것
# _*_ coding: utf-8 _*_

import Adafruit_DHT
import time
import requests
import json

# DHT 센서의 핀 번호 설정
DHT_SENSOR = Adafruit_DHT.DHT22         # DHT21 = DHT22 
DHT_PIN = 2  # 센서가 연결된 GPIO 핀 번호로 수정해주세요.

Time = time.strftime('%c')

SERVER_URL = "http://192.168.0.2:8000/"

def read_sensor():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        return round(temperature, 1), round(humidity, 1)
    else:
        return None


def send_to_server(temperature, humidity):
    data = {
    "robot" : "1",
    "area" : "Hi",
    "height" :"23.2",
    "temperature": temperature,
    "humidity": humidity,
    "soil_ph" : "22.2",
    "soil_ec" : "33.3",
    "soil_temp" : "30.1",
    "soil_humi" :"32.1",
    "N" : "0.1111",
    "P": "0.1111",
    "K": "0.1111"

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
            print(Time)
            print(f'Temperature: {temperature}°C, Humidity: {humidity}%')
            send_to_server(temperature, humidity)
        else:
            print("Failed to read sensor data.")
        time.sleep(2)  # 2초마다 센서를 읽습니다.

if __name__ == "__main__":
    main()