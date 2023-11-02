from pymongo import MongoClient



class MyMongoConexion:
    def __init__(self, url: str = "mongodb://localhost:27017"):
        self.client = MongoClient(url)
        self.db = self.client["db_ofrenda"]
        self.mensajes_colecction = self.db["mensajes"]
        

    def ingreso_mensaje(self, datos: dict) -> bool:       
        try:
            res = self.mensajes_colecction.insert_one(datos)
        except Exception as e :
            print(e)
            return False
        return True

        
    def modificar_mensaje(self,id_mensaje:str,msg:str)->bool:      
        try:
            self.mensajes_colecction.update_one({"_id":id_mensaje},{"$set":{"mensaje":msg}})
        except:
            return False
        return True
    
    def obtener_mensaje(self):
        mensajes_mongo=[]
        mensaje_user = self.mensajes_colecction.find()
        for mensaje in mensaje_user:
            mensaje["_id"]=str(mensaje["_id"])
            mensajes_mongo.append(mensaje)
        return mensajes_mongo

mongo_instances = MyMongoConexion()
