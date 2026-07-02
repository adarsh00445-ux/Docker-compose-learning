from flask import Flask
import socket
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <h1>🚀 DevOps Project</h1>
    <p>Hostname: {socket.gethostname()}</p>
    <p>Time: {datetime.datetime.now()}</p>
    """

app.run(host="0.0.0.0", port=5000)