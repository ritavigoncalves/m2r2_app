import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
from fuzzywuzzy import process
import pickle
import requests
import json

# Datasets
ratings = pd.read_csv('app/static/csv/ratings.csv', sep=',', header=0)
movies = pd.read_csv('app/static/csv/movies.csv', sep=',', header=0)


def find_movie(movie_name):
    #user_ratings = ratings.groupby(ratings['movieId'])['rating'].mean().round(2)
    #movie_ratings = pd.merge(movies, user_ratings, how='left', on='movieId')
    movie_users = ratings.pivot(index='movieId', columns=('userId'), values='rating').fillna(0)

    mat_movie_users = csr_matrix(movie_users)

    # KNN Model
    model_knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=20).fit(mat_movie_users)

    # Extracting a movie_name with the user input
    idx = process.extractOne(movie_name, movies['title'])[2]
    print('Movie selected: ', movies['title'][idx], '| Index: ', idx)

    # Returning indices of and distances to the neighbors of each point 
    distances, indices = model_knn.kneighbors(mat_movie_users[idx], n_neighbors=5)
    
    # Saving the model to disk
    pickle.dump(distances, indices, open('model.pkl','wb'))
    
    # Printing the results
    print('\nHere are your best matches: \n', distances, indices)
    for i in indices:
        print(movies['title'][i].where(i != idx))

find_movie(input)