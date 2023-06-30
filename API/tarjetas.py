from flask import Flask, jsonify
from flask import request #pip install flask
import json
app = Flask(__name__)

@app.route('/getTarjetas', methods=['GET'])
def getTarjetas():
    try:
        if request.method == 'GET':
            retorno = {
        "tarjetas": [
            {
                "tipo": "Debito",
                "numero": "7584653789576451",
                "titular": "Freddy Monterroso",
                "fecha_expiracion": "12/2029"
            },
            {
                "tipo": "Debito",
                "numero": "9800764578366174",
                "titular": "Miguel Carrillo",
                "fecha_expiracion": "10/2030"
            }
            ]
            }
        else:
            retorno = {'mensaje': 'Error en la petición, método incorrecto'}
        return jsonify(retorno)
    except:
        return {"mensaje": "Error interno en el servidor", "status": 500}
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010)