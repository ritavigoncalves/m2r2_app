import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        # Finding the name of the movie - Lionel
        movie = request.form["movie"]
    return render_template("index.html")

if __name__ == '__main__':
    app.run(port=5000, debug=True)

