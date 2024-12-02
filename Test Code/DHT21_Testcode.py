import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 2  # 센서가 연결된 GPIO 핀 번호로 수정하세요.

def read_sensor():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        return temperature, humidity
    else:
        print('Failed to read from DHT sensor')
        return None

try:
    while True:
        sensor_data = read_sensor()
        if sensor_data:
            temperature, humidity = sensor_data
            print(f'Temperature: {temperature:.1f}°C, Humidity: {humidity:.1f}%')
        time.sleep(2)  # DHT22 센서 권장 대기 시간

except KeyboardInterrupt:
    print("Program stopped")
