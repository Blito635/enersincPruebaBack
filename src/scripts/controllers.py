from .query import Query
from flask import request, json
from psycopg2.errors import Error as PGError


query_helper = Query()



def datosPersona():
    res = {"status": False, "codigo": 0, "msg": "", "obj": {}}
    try:
        args=list(request.args.items())
    except Exception as e :
        res["status"]= False
        res["msg"] = f" error {e}"
        return res

    try:
        query = query_helper.buscar("modelo_persona",args)
        
        
    except Exception as e:
        res["status"]= False
        res["msg"] = f" error {e}"
        return res

    res["msg"] = "Consulta exitosa"
    res["status"] = True
    res["codigo"] = 200
    res["obj"]=json.loads(json.dumps(query))

    return res

def crearPersona():
    res = {"status": False, "codigo": 0, "msg": "", "obj": {}}
    try:
        if not request.json:
            raise Exception("Request con body vacio")
        Data = request.json
    except Exception as e :
        res["status"]= False
        res["msg"] = f" error {e}"
        return res
    
    try:
        query=query_helper.insertar("modelo_persona",Data)
        
    except Exception as e:
        res["status"]= False
        res["msg"] = f" error {e}"
        return res
    
    res["msg"] = "La persona ha sido creado exitosamente"
    res["status"] = True
    res["codigo"] = 200
    res["obj"] = json.loads(json.dumps(query))

    return res

def modificarPersona():
    res = {"status": False, "codigo": 0, "msg": "", "obj": {}}
    try:
        if not request.json:
            raise Exception("Request con body vacio")
        args=list(request.args.items())
        Data = request.json
    except Exception as e :
        res["status"]= False
        res["msg"] = f" error {e}"
        return res
    
    try:
        query_helper.update("modelo_persona",args ,Data)
        
    except Exception as e:
        res["status"]= False
        res["msg"] = f" error {e}"
        return res

    res["msg"] = "La persona ha sido modificado exitosamente"
    res["status"] = True
    res["codigo"] = 200

    return res

def eliminarPersona():
    res = {"status": False, "codigo": 0, "msg": "", "obj": {}}
    try:
        args=list(request.args.items())
    except Exception as e :
        res["status"]= False
        res["msg"] = f" error {e}"
        return res

    try:
        query_helper.delete("modelo_persona",args)

    except PGError as e:
        res["status"]= False
        res["msg"] = f" error {e}"
        return res
    except Exception as e:
        res["status"]= False
        res["msg"] = f" error {e}"
        return res
    
    res["msg"] = "La persona ha sido eliminada exitosamente"
    res["status"] = True
    res["codigo"] = 200

    return res


def cruDoctor():
    if request.method == "POST":
        return crearPersona()
    elif request.method == "GET":
        return datosPersona()
    elif request.method == "PUT":
        return modificarPersona()
    elif request.method == "DELETE":
        return eliminarPersona()
