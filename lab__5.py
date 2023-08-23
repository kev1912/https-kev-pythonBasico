import requests
import json
import re
import matplotlib.pyplot as plt
# 1. Obtenga los datos de la API
url = "https://gateway.marvel.com:443/v1/public/characters?"
response = requests.get(url)
data = json.loads(response.content)
# 2. Filtrar las películas por año de lanzamiento
movies = []
for movie in data["results"]:
    if movie["release_date"] > "2000":
        movies.append(movie)
# 3. Filtrar las películas por título
action_movies = []
for movie in movies:
    if re.search("Action", movie["title"]):
        action_movies.append(movie)
# 4. Crear un gráfico de la distribución de calificaciones
ratings = [movie["vote_average"] for movie in action_movies]
plt.hist(ratings, bins=10)
plt.xlabel("Calificación")
plt.ylabel("Número de películas")
plt.title("Distribución de calificaciones de películas de acción")
plt.show()