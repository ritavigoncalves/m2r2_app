# This contains code for the machine learning model to predict the movies
from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix
from fuzzywuzzy import process  
import numpy as np
import pandas as pd
import pickle
import csv

# Datasets
# users
df_users_ratings = pd.read_csv('static/df_users_ratings_file_to_test.csv', sep=',', index_col='movieId', header=0)
# movies
df_movies_ratings = pd.read_csv('static/df_movie_ratings_file_to_test.csv', sep=',', index_col=0, header=0)

## -------- ##

def find_movie(movie_name):

    # Extracting a movie_name with the user input 'Movie selected: ',  | Index: ', idx
    idx = process.extractOne(movie_name, df_movies_ratings['title'])[2]
    return df_movies_ratings['title'][idx]

"""# ------------------- #
# Machine learning model with pickle
movie_users = ratings.pivot(index='movieId', columns=('userId'), values='rating').fillna(0)
mat_movie_users = csr_matrix(movie_users)

model_knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=5)
pickle.dump(model_knn, open('model.pkl','wb'))
# ------------------- # """

def pred_movie(movie_name):
    # Compressed Sparse Row Matrix, because most of the elements are zeros 
    # dataset matrix: df_users_ratings 
    # this: df_movie_ratings_full_reduced | replaces: df_movies_ratings
    mat_movie_users = csr_matrix(df_users_ratings)

    idx = process.extractOne(movie_name, df_movies_ratings['title'])[2]

    # KNN Model
    model_knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=6).fit(mat_movie_users)

    # Returning indices of and distances to the neighbors of each point
    indice = model_knn.kneighbors(mat_movie_users[idx], n_neighbors=6, return_distance=False)

    # Printing the results -- if i != idx:
    for i in indice:
        list_mov = list(df_movies_ratings['title'][i].where(i != idx))
        return list_mov
