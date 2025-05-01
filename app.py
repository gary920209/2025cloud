from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from 2025cloud!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
