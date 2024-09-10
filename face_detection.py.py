import time
import multiprocessing
import requests
import cv2
import os
from datetime import datetime

LAPTOP_ID = 'laptop1'
SERVER_URL = 'http://192.168.34.113:5000/update'
IMAGE_FOLDER = 'static/images'
if not os.path.exists(IMAGE_FOLDER):
    os.makedirs(IMAGE_FOLDER)

def run_face_detection(queue):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)  # Replace with the appropriate camera index

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error reading frame from camera")
            continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        if len(faces) > 0:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            image_filename = f"{LAPTOP_ID}_{timestamp}.jpg"
            image_path = os.path.join(IMAGE_FOLDER, image_filename)
            cv2.imwrite(image_path, frame)
            queue.put(('Person detected', image_filename))
        else:
            queue.put(('No person detected', ''))

    cap.release()
    cv2.destroyAllWindows()

def send_updates(queue):
    while True:
        try:
            # Only send updates when there's something new in the queue
            while not queue.empty():
                status, image_filename = queue.get()
                response = requests.post(SERVER_URL, data={'laptop_id': LAPTOP_ID, 'status': status, 'image_filename': image_filename})
                print(f"Request sent successfully: laptop_id={LAPTOP_ID}, status={status}, image_filename={image_filename}, response={response.status_code}, response_text={response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Error sending request: {e}")
        time.sleep(5)  # Adjust the interval as needed

if __name__ == '__main__':
    queue = multiprocessing.Queue()

    # Start the face detection process
    detection_process = multiprocessing.Process(target=run_face_detection, args=(queue,))
    detection_process.start()

    # Run the update sending function in the main process
    send_updates(queue)
