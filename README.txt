Face Detection Web Application
==============================

This is a web application built using Flask that detects faces in real-time from a webcam feed. It captures images when a face is detected and sends the image and detection status to a server. The server stores the images and updates the detection status for each laptop.

Prerequisites
-------------
- Python 3.x
- Flask
- OpenCV
- requests

Installation
------------
1. Clone the repository or download the source code.
2. Install the required Python packages by running the following command:

   pip install flask opencv-python requests

Usage
-----
1. Run the Flask application:

   python app.py

   This will start the server at http://0.0.0.0:5000.

2. Open a web browser and navigate to http://localhost:5000 to see the face detection status.

3. The application will continuously capture frames from the webcam and detect faces. When a face is detected, it will save the captured image and update the detection status on the server.

4. The web page will automatically refresh and display the updated detection status and the captured images.

Code Structure
--------------
- app.py: This file contains the Flask application code, including routes for handling the web page, updating the detection status, and serving the captured images.
- face_detection.py: This file contains the code for running the face detection process using OpenCV and sending updates to the server.
- templates/index.html: This HTML file contains the web page template for displaying the face detection status and captured images.

Customization
-------------
You can customize the application by modifying the following variables in face_detection.py:
- LAPTOP_ID: The unique identifier for the laptop running the face detection process.
- SERVER_URL: The URL of the Flask server where the detection status and images will be sent.
- IMAGE_FOLDER: The folder where the captured images will be stored.

Additionally, you can modify the HTML, CSS, and JavaScript in templates/index.html to change the appearance and behavior of the web page.

Notes
-----
- The application assumes that the webcam is available and accessible.
- The server stores the detection status and captured images in memory. If you want to persist the data, you'll need to modify the code accordingly.
- The face detection algorithm used in this example is based on the Haar Cascade classifier provided by OpenCV. You can use a different algorithm or a pre-trained model for better performance or accuracy.