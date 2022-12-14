from flask import Flask
from flask import jsonify
import retriveData as rd

app = Flask(__name__)

@app.route('/api/weather', methods=['GET'])
@app.route('/api/weather/<param>', methods=['GET'])
def call_function(param=None):
    print('{0}'.format(param))
    if(param=='stats'):
        return jsonify(rd.fetchDataByStation())
    elif(param==None):
        return jsonify(rd.fetchAllWeatherData())
    else:
        return jsonify('Invalid api')

app.run(host="0.0.0.0")