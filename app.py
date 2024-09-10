from flask import Flask, request, render_template, jsonify, send_from_directory
import os

app = Flask(__name__)
detection_status = {}
IMAGE_FOLDER = 'static/images'
if not os.path.exists(IMAGE_FOLDER):
    os.makedirs(IMAGE_FOLDER)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', detection_status=detection_status)

@app.route('/update', methods=['POST'])
def update():
    laptop_id = request.form.get('laptop_id')
    status = request.form.get('status')
    image_filename = request.form.get('image_filename', '')
    detection_status[laptop_id] = {'status': status, 'image_filename': image_filename}
    return 'OK'

@app.route('/status', methods=['GET'])
def status():
    return jsonify(detection_status)

@app.route('/images/<filename>')
def images(filename):
    return send_from_directory(IMAGE_FOLDER, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
