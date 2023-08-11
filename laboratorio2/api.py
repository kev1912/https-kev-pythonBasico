import multiprocessing
import api
import ids
def get_user(id):
    # Hacemos la consulta a la API
    user = api.get_user(id)
    # Imprimimos el nombre del usuario
    print(user['name'])
def main():
    # Creamos una lista de procesos
    processes = []
    # Creamos un proceso para cada usuario en la lista
    for id in ids.ids:
        process = multiprocessing.Process(target=get_user, args=(id,))
        processes.append(process)
    # Iniciamos los procesos
    for process in processes:
        process.start()
    # Esperamos a que los procesos terminen
    for process in processes:
        process.join()
if __name__ == "__main__":
    main()