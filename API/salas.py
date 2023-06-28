from flask import Flask, jsonify
from flask import request #pip install flask
import json
app = Flask(__name__)

@app.route('/getSalas', methods=['GET'])
def getSalas():
    try:
        if request.method == 'GET':
            retorno = {
                "cines": [
                    {
                        "nombre": "Cinepolis",
                        "salas": [
                            {
                                "numero": "#USACIPC2_202207892_1",
                                "asientos": "180"
                            },
                            {
                                "numero": "#USACIPC2_202207892_2",
                                "asientos": "280"
                            },
                            {
                                "numero": "#USACIPC2_202207892_3",
                                "asientos": "220"
                            }
                        ]
                    }
                ]
            }
        else:
            retorno = {'mensaje': 'Error en la petición, método incorrecto'}
        return jsonify(retorno)
    except:
        return {"mensaje": "Error interno en el servidor", "status": 500}
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5008)