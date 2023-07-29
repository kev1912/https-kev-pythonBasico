# Importa la biblioteca `requests`.
import requests
# Define la función `get_chuck_norris_jokes()`.

def get_chuck_norris_jokes():
  """Obtiene una lista de chistes de Chuck Norris."""
  # Haz una solicitud GET a la API de Chuck Norris.
  response = requests.get("https://api.chucknorris.io/jokes/random")
  # Obtén la lista de chistes de la respuesta.
  jokes = response.json()["jokes"]
  # Devuelve la lista de chistes.
  return jokes

# Define la función `get_chuck_norris_categories()`.


def get_chuck_norris_categories():
  """Obtiene una lista de categorías de chistes de Chuck Norris."""
  # Haz una solicitud GET a la API de Chuck Norris.
  response = requests.get("https://api.chucknorris.io/categories")
  # Obtén la lista de categorías de la respuesta.
  categories = response.json()["categories"]
  # Devuelve la lista de categorías.
  return categories
# Define la función `menu()`.

def menu():
  """Muestra un menú en la consola y permite al usuario elegir una opción."""
  # Muestra el menú.
  print("Menú")
  print("1. Obtener una lista de chistes de Chuck Norris")
  print("2. Obtener una lista de categorías de chistes de Chuck Norris")
  print("3. Salir")
  # Elige una opción.
  opción = int(input("Elige una opción: "))
  # Ejecuta la opción elegida.
  
  if opción == 1:
    get_chuck_norris_jokes()
  
  elif opción == 2:
    get_chuck_norris_categories()
 
  elif opción == 3:
    exit()
  # Vuelve a mostrar el menú.
  menu()
# Muestra el menú.
menu()