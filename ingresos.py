from fastapi import APIRouter,HTTPException
from pydantic import BaseModel,validator
from mongodbconexion import mongo_instances
import numpy as np
from funciones import almacena_imagen,recupera_imagen


def no_esta_vacio(valor):
    if not isinstance(valor, bool) and not valor.strip():
        raise ValueError("El campo no debe estar vacío")
    return valor

class mensaje(BaseModel):
    mensaje:str
    autor:str|bool =False

    verifica =validator('mensaje')(no_esta_vacio)

class Imagen(BaseModel):
    nombre:str|bool=False
    imagen:str
    verifica =validator('imagen')(no_esta_vacio)

router=APIRouter()

@router.post("/Ingreso_mensaje")
async def ingreso_mensaje(ms:mensaje):
    if not ms.autor:
        ms.autor = "Anonimo"
    print(ms)
    if not mongo_instances.ingreso_mensaje(dict(ms)):
        raise HTTPException(status_code=404, detail="Error al registrar")
    return {"message": "Mensaje guardado con exito", 'status': 'success'}

@router.get("/Obtener_mensajes")
async def obtener_mensaje():
    msg = mongo_instances.obtener_mensaje()
    if not msg:
        raise HTTPException(status_code=404, detail="Error al obtener mensaje")
    return msg

@router.post("/ingreso_imagen")
async def ingreso_imagen(imagenes:Imagen):
    if not imagenes.nombre:
        imagenes.nombre = "img"+str(np.random.randint(1,100))
    if "data:image" not in imagenes.imagen:
        raise HTTPException(status_code=404, detail="Debe ser un data:image")
    if not almacena_imagen(imagenes.imagen,imagenes.nombre):
        raise HTTPException(status_code=404, detail="No se logro almacenar la imagen")
    return {"message": "Imagen guardada con exito", 'status': 'success'}

@router.get("/obtener_imagenes")
async def obtener_imagenes():
    return recupera_imagen()