# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 16:20:19 2022
@author: juanp
"""
import math
from datetime import datetime
class Trig:
    def __init__(self):
        self.pi = math.pi
    def seno(self):
        return math.sin(self.pi)
    def coseno(self):
        return math.cos(self.pi)
    def tangente(self):
        return math.tan(self.pi)
def main():
    # Creamos una instancia de la clase Trig
    trig = Trig()
    # Preguntamos al usuario qué valor desea consultar
    operacion = input("¿Qué valor desea consultar? (seno, coseno o tangente): ")
    # Mostramos el resultado en pantalla
    if operacion == "seno":
        print(trig.seno())
    elif operacion == "coseno":
        print(trig.coseno())
    elif operacion == "tangente":
        print(trig.tangente())
    else:
        print("Operación no válida")
    # Creamos un archivo llamado "log.txt" y en él escribimos:
    # La fecha y la hora en que se realizó la operación
    # La operación realizada (operación y resultado)
    with open("log.txt", "a") as f:
        f.write(f"{datetime.now()}\t{operacion}\t{trig.seno()}\n")
    # Preguntamos al usuario si quiere realizar otra operación
    continuar = input("¿Desea realizar otra operación? (s/n): ")
    # Si el usuario responde "s", volvemos a preguntar qué valor desea consultar
    if continuar == "s":
        main()
if __name__ == "__main__":
    main()



    

    
    




