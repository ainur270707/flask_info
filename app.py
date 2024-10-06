from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import cv2
import base64
import numpy as np
from ultralytics import YOLO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Замените на ваш секретный ключ
socketio = SocketIO(app, cors_allowed_origins="*")

# Загрузка модели YOLO один раз при старте сервера
model = YOLO('yolov8n.pt')

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('frame')
def handle_frame(data):
    try:
        # Декодирование изображения из base64
        header, encoded = data.split(',', 1)
        nparr = np.frombuffer(base64.b64decode(encoded), np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Обработка кадра моделью YOLO
        results = model(frame)
        annotated_frame = results[0].plot()

        # Кодирование аннотированного кадра обратно в JPEG
        _, buffer = cv2.imencode('.jpg', annotated_frame)
        jpg_as_text = base64.b64encode(buffer).decode('utf-8')
        jpg_full = 'data:image/jpeg;base64,' + jpg_as_text

        # Отправка аннотированного кадра обратно клиенту
        emit('processed_frame', jpg_full)
    except Exception as e:
        print(f"Ошибка при обработке кадра: {e}")
        emit('processed_frame', None)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
