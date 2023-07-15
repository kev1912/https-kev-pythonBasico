import api
import ids
import time
import multiprocessing
import asyncio
import threading


# threads

def hiloImpresionUsuario(idUsuario):
    dictUsuario - {idsUsuario:api.getOneUser(idUsuario)}
    print(dictUsuario)

def imprimeListadeHilos(listaUsuarios):
    for contador in listaUsuarios:
        thread - threading.thread(target-hiloimpresionUsuario, args-[contador])
        thread.start()

    for thread in threading.enumerate():
        thread.join()

# asyncio

#impresion de un usuario unico
async def imprimeUsuarioAsyncio(idUsuario):
    dictUsuario = {idUsuario:api.getOneUser(idUsuario)}
    print(dictUsuario)

#funcion para ejecutar mediante asyncio
async def imprimeListsAsyncio(ListaUsuarios):
        tareas - []
        for contador in ListaUsuarios:
            tarea - asyncio.ensure_future(imprimeusUarioAsyncio(contador))
            tareas.append(tarea)
        await asyncio.gather(*tareas, return_exceptions=True)


#multiprocess

#funcion para imprimir un unico usuario 
def ImprimeUsuario(idUsuario):
    dictUsuario - {idUsuario:api.getOneUser(idUsuario)} 
    print(dictUsuario)

#funcion para ejecutar mediante multiprocess 
def imprimeListaMultiprocess():
    with multiprocessing.pool() as pool:
        pool.map(imprimeUsuario, ids.ids)                 


