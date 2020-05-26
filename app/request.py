import requests

# URL
url = 'http://localhost:5000/api/'

# Change the value of experience that you want to test
movie_name = "toy story"

r = requests.post(url,json=movie_name)
print(r.json())