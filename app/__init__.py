import numpy as np
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the pickle
distances, indices = pickle.load(open('model.pkl','rb'))
print(distances, indices)

from app import routes

def predict():
    # Getting data from the POST request
    #data = request.get_json(force=True)
    
    # Making predictions using pickle
    return jsonify(distances, indices)
