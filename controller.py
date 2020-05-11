from flask import Flask, request, jsonify
from flask_cors import CORS
import GeneticAlgorithm
from model import Coordinate, Route,RouteController
from time import time
app = Flask(__name__)
CORS(app)

@app.route('/',methods=['GET'])
def getFunction():
    return "hola mundo funciona el deploy jeje"

@app.route('/', methods=['POST'])
def findRoutes():
    start_time = time()
    body = None
    body = request.get_json(force=True)
    lista = list(body)
    if len(lista) < 2:
        return []
    destinations = []
    for i in lista:
        destinations.append(Coordinate(i['lat'],i['lng'],'A'))
    #TODO
    ga = None
    ga = GeneticAlgorithm.GeneticAlgorithm(destinations,0.5,10)
    ga.generations(2000)
    best = ga.getBestIndividuo()
    response = []
    for i in best:
        response.append({'lat':i.lat,'lng':i.long})
    elapsed_time = time() - start_time
    print("Elapsed time: %0.10f seconds." % elapsed_time)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=False,port = 5000)