from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Server is working!"  # Simple test route

if __name__ == '__main__':
    app.run(debug=True, port=5000)