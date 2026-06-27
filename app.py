from flask import Flask
import socket
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "project": "Poisson Docker Revision",
        "hostname": socket.gethostname(),
        "time": str(datetime.now()),
        "author": "Divyansh"
    }

@app.route("/health")
def health():
    return {
        "status": "healthy"
    }

@app.route("/env")
def env():
    return {
        "environment": os.getenv("ENVIRONMENT", "Not Set")
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)