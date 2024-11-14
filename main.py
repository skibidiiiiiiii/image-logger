from flask import Flask, send_file, request
import datetime

app = Flask(__name__)

IMAGE_PATH = "image.png"

def log_request():
    with open("log.txt", "a") as log_file:
        log_entry = f"{datetime.datetime.now()} - IP: {request.remote_addr}\n"
        log_file.write(log_entry)

@app.route('/')
def show_image():
    log_request()
    return send_file(IMAGE_PATH, mimetype='image/png')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
