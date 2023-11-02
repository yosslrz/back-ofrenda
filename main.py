from fastapi import FastAPI
import ingresos

app = FastAPI()

app.include_router(ingresos.router)

@app.get("/")
async def raiz():
    return {"Hola mundo"}

