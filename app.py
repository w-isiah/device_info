from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/device")
def get_device_info():
    # Get client IP
    client_ip = request.remote_addr

    # Use an external API to get location info (free option: ip-api.com)
    try:
        response = requests.get(f"http://ip-api.com/json/{client_ip}")
        data = response.json()
        country = data.get("country", "Unknown")
        region = data.get("regionName", "Unknown")
        city = data.get("city", "Unknown")
    except:
        country = region = city = "Unknown"

    device_info = {
        "IP Address": client_ip,
        "Country": country,
        "Region": region,
        "City": city,
        "User Agent": request.headers.get("User-Agent")
    }

    return jsonify(device_info)

if __name__ == "__main__":
    app.run(debug=True)
