from flask import Flask, render_template, Response
import cv2
from ultralytics import YOLO

app = Flask(__name__)

camera = cv2.VideoCapture(0)

model = YOLO('yolov8n.pt')

def gen_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            results = model(frame)
            annotated_frame = results[0].plot()
            ret, buffer = cv2.imencode('.jpg', annotated_frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
