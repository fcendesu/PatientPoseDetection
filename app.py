from flask import Flask, render_template
import cv2
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_video')
def process_video():
    cap = cv2.VideoCapture(0) 
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        if len(faces) > 0:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open('head_movements.log', 'a') as log_file:
                log_file.write(f"{current_time}: Head movement detected\n")

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow('Head Movement Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return "Head movement detection completed."

if __name__ == '__main__':
    app.run(debug=True)