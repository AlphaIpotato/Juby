import cv2
import socket
import time
import os

# 웹캠 열기
cap = cv2.VideoCapture(0, cv2.CAP_V4L2)

# 서버 연결
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect(('http://192.168.0.2:8000/accountapp/harvest/', 8000))
    server_connected = True
except Exception as e:
    print("서버 연결 실패:", e)
    server_connected = False

# 이미지 저장 경로
image_save_path = '/home/juby/Desktop/test/image/'

# 최초 1회 이미지를 저장하기 위한 플래그
first_frame_saved = False

while True:
    # 웹캠에서 프레임 읽기
    ret, frame = cap.read()
    if not ret:
        print("프레임을 읽을 수 없습니다.")
        break

    # 프레임을 JPEG 형식으로 인코딩
    _, img_encoded = cv2.imencode('.jpg', frame)
    data = img_encoded.tobytes()

    # 최초 1회 이미지를 저장
    if not first_frame_saved:
        cv2.imwrite(os.path.join(image_save_path, 'first_frame.jpg'), frame)
        first_frame_saved = True
        print("첫 번째 이미지를 저장했습니다.")

    # 서버로 데이터 전송
    if server_connected:
        try:
            s.sendall(data)
        except Exception as e:
            print("서버로 데이터 전송 실패:", e)
            server_connected = False  # 이후 전송이 실패하면 서버 연결 상태를 업데이트

    # 0.1초 대기
    time.sleep(1)

# 자원 해제
cap.release()
s.close()