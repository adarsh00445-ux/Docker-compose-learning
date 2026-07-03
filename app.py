from flask import Flask
import socket
import datetime
import platform

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <h1>🚀 DevOps Project</h1>
    <p>Hostname: {socket.gethostname()}</p>
    <p>Time: {datetime.datetime.now()}</p>
    <p>Operating System: {platform.system()}</p>
    <p>Python Version: {platform.python_version()}</p>
    """

app.run(host="0.0.0.0", port=5000)