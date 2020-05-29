# This contains Flask APIs that receives movie details and computes the predicted value based on our model
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template, json, Response, send_file
from new_model import pred_movie, find_movie
from scipy.sparse import csr_matrix
from fuzzywuzzy import process


app = Flask(__name__)

# Setting up routes
@app.route('/')
def main():
    return render_template("layout.html")

@app.route('/get_id', methods=['POST'])
def my_mov():
    
    # Finding user_pick
    user_pick = request.form['movie']
    find = find_movie(user_pick)
    pred = pred_movie(user_pick)
    
    return render_template("index.html", my_movie=find, data=pred)

if __name__ == "__main__":
    # For local development, set to True
    app.run(debug=True)

