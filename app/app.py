from flask import Flask, render_template
import psutil
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    cpu = psutil.cpu_percent(interval=1)  # More accurate with 1-second interval
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    uptime = datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())
    uptime_str = str(uptime).split('.')[0]  # Format uptime cleanly

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
    app.run(debug=True, host='0.0.0.0')
