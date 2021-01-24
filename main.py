# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import cv2
from deepface import DeepFace

emotions = {
    "angry": 0,
    "disgust": 0,
    "fear": 0,
    "happy": 0,
    "sad": 0,
    "surprise": 0,
    "neutral": 0
}


def start_analyzing_mimic():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise IOError("No camera detected")

    while True:
        ret, frame = cap.read()
        result_analyzer = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_PLAIN
        print('Dominant Facial Expression {0}'.format(result_analyzer['dominant_emotion']))
        analyze_expressions(result_analyzer['emotion'])

        cv2.putText(frame, result_analyzer['dominant_emotion'], (50, 50), font, 3, (0, 0, 255), 2, cv2.LINE_4)
        cv2.imshow('Original video', frame)

        if cv2.waitKey(2) & 0xFF == ord('q'):
            report_expressions()
            break

    cap.release()
    cv2.destroyAllWindows()


def analyze_expressions(emotion):
    for key in emotion:
        emotions[key] = emotions[key] + emotion[key];

def report_expressions():
    total = 0;
    print("Facial Expression Report")
    print(emotions)
    for key in emotions:
        total += emotions[key];
    for key in emotions:
        percentage = emotions[key] * 100 / total;
        #print(key)
        #print(percentage)
        print('{0} => % {1}'.format(key, round(percentage, 2)))


if __name__ == '__main__':
    start_analyzing_mimic()
