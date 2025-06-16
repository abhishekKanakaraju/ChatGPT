from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Phone connected to system via WiFi!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
