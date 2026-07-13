from flask import Flask, jsonify
from datetime import datetime
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "Application": "Infrastructure Automation Project",
        "Hostname": socket.gethostname(),
        "Status": "Running",
        "Time": str(datetime.now())
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
