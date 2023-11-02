import base64
import io
import os
from PIL import Image

def almacena_imagen(data_ima: str, nombre: str)->str:
    directorio_logo = os.getcwd() + "\img"
    file_logo = nombre+".txt"
    path = os.path.join(directorio_logo, file_logo)
    with open(path, "w") as file_logo:
        file_logo.write(data_ima)
    return directorio_logo

def recupera_imagen():
    imagenes = []
    carpeta = os.getcwd() + "\img"
    for archivo in os.listdir(carpeta):
        ruta_completa = os.path.join(carpeta, archivo)
        try:
            with open(ruta_completa, "rb") as txt_file:
                data_url = txt_file.read()
            imagenes.append(data_url)
        except Exception as e:
            print(e)
            return False
    return imagenes

       





