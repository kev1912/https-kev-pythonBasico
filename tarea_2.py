import requests
import json
def get_user_info(username):
    """
    Esta función obtiene información del usuario a partir de su nombre de usuario.
    Args:
        username: El nombre de usuario del usuario que se quiere obtener información.
    Returns:
        Un diccionario con la información del usuario.
    """
   
    url = f"https://api.zoom.us/v2/{username}"
    response = requests.get(url)
    return response.json()
def get_user_repos(username):
    """
    Esta función obtiene los repositorios del usuario a partir de su nombre de usuario.
    Args:
        username: El nombre de usuario del usuario que se quiere obtener información.
    Returns:
        Una lista con los repositorios del usuario.
    """
    
    url = f"https://api.zoom.us/v2/{username}/repos"
    response = requests.get(url)
    return response.json()
def main():
    """
    Esta función es el punto de entrada del programa.
    Se encarga de mostrar un menú al usuario y de llamar a las funciones apropiadas en función de la opción seleccionada.
    """
    
    while True:
        print("1. Get user info")
        print("2. Get user repos")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            username = input("Enter the username: ")
            user_info = get_user_info(username)
            print(json.dumps(user_info, indent=4))
       
        elif choice == "2":
            username = input("Enter the username: ")
            user_repos = get_user_repos(username)
            for repo in user_repos:
                print(repo["name"])
        
        elif choice== "3":
            break
        
        else:
            print("Invalid choice")
if __name__ == "__main__":
    main()

import matplotlib.pyplot as plt
import numpy as np

# Create a figure and an axes object
fig, ax = plt.subplots()

# Create a line plot
x = np.linspace(0, 10, 100)
y = np.sin(x)
ax.plot(x, y)

# Add a title and labels
ax.set_title("Sin Curve")
ax.set_xlabel("X")
ax.set_ylabel("Y")

# Show the plot
plt.show()