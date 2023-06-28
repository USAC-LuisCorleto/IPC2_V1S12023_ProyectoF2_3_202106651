from flask import Flask, jsonify
from flask import request #pip install flask
import json
app = Flask(__name__)

@app.route('/getUsuarios', methods=['GET'])
def getUsuarios():
    try:
        if request.method == 'GET':
            retorno = {
                "usuarios": [
                    {
                        "rol": "Cliente",
                        "nombre": "Carlos",
                        "apellido": "Castillo",
                        "telefono": "623436789",
                        "correo": "correo@json.com",
                        "contrasena": "calmadito24"
                    },
                    {
                        "rol": "Cliente",
                        "nombre": "Julio",
                        "apellido": "Smith",
                        "telefono": "987554322",
                        "correo": "patras@hotmail.com",
                        "contrasena": "esteadios2"
                    }
                ]
            }
        else:
            retorno = {'mensaje': 'Error en la petición, método incorrecto'}
        return jsonify(retorno)
    except:
        return {"mensaje": "Error interno en el servidor", "status": 500}
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007)