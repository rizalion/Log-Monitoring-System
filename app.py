import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

from modules.log_parser import parse_log_file
from modules.threat_detector import detect_threats
from modules.risk_calculator import calculate_risk

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

latest_data = {
    "alerts": [],
    "total_events": 0,
    "success_logins": 0,
    "failed_logins": 0
}

latest_score = 0
latest_level = "LOW"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template(
        "dashboard.html",
        data=latest_data,
        score=latest_score,
        level=latest_level
    )


@app.route("/alerts")
def alerts():
    return render_template("alerts.html", alerts=latest_data["alerts"])


@app.route("/upload", methods=["POST"])
def upload_file():

    global latest_data, latest_score, latest_level

    file = request.files.get("file")

    # ✅ FIX 1: Explicit None check (removes Pylance error)
    if file is None:
        return redirect(url_for("home"))

    filename = file.filename

    # ✅ FIX 2: Ensure filename is valid string
    if not filename:
        return redirect(url_for("home"))

    filename = secure_filename(filename)

    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)

    file.save(file_path)

    # PROCESS LOG FILE
    events = parse_log_file(file_path)
    data = detect_threats(events)

    score, level = calculate_risk(data["alerts"])

    latest_data = data
    latest_score = score
    latest_level = level

    return redirect(url_for("dashboard"))


if __name__ == "__main__":
    app.run(debug=True)