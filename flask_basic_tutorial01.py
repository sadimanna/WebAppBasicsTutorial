import flask
from flask import Flask, request, jsonify, render_template
import requests
import json

from get_weather import get_weather

W_API_KEY = "ae72f9378f3d4c37b98113340252509"
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    # print("Weather API Key:", W_API_KEY)
    if request.method=="POST":
        city = request.form.get("city")
        # print(city)
        weather_info = get_weather(city, W_API_KEY)
        return render_template("weather.html", weather_data=weather_info, city=city)
    else:
        return render_template("weather.html")

if __name__ == "__main__":
    app.run(debug=True)

    #######################################
    # IF ACCESS DENIED ERROR: #
    ########################################
    # GO TO chrome://net-internals/#socket #
    ########################################
    # FLUSH SOCKET POOLS #
    ########################################