# Main file with Flask
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import model

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def sign_up():

    if request.method == "POST":
        
        # Finding the name of the movie - Lionel
        movie = request.form["movie"]
        
        # Predict movie with KNN model
        output = model.find_movie
    
    return render_template("index.html", prediction=output)

if __name__ == '__main__':
    app.run()

