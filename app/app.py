from flask import Flask, render_template
import psutil
import datetime
import os

app = Flask(__name__)

@app.route("/")
def index():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    uptime = datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())
    uptime_str = str(uptime).split('.')[0]

    quote = "Efficiency is doing things right; effectiveness is doing the right things."

    return render_template(
        "index.html",
        cpu=cpu,
        memory=memory,
        disk=disk,
        uptime=uptime_str,
        quote=quote
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
