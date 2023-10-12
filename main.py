#for testing you can use below url
#http://localhost:5000/api/get_woz_value?parameter1=%22A00a%20Kop%20Zeedijk%22&parameter2=543.0&parameter3=37.0&parameter4=149.0&parameter5=14.0&parameter6=12.0&parameter7=22.0&parameter8=12.0&parameter9=789.0

from flask import Flask, request, jsonify
from src.get_woz_value import get_woz_value


app = Flask(__name__)

@app.route('/api/get_woz_value', methods=['GET'])
def api_get_woz_value():
    parameter1 = str(request.args.get('parameter1'))
    parameter2 = float(request.args.get('parameter2'))
    parameter3 = float(request.args.get('parameter3'))
    parameter4 = float(request.args.get('parameter4'))
    parameter5 = float(request.args.get('parameter5'))
    parameter6 = float(request.args.get('parameter6'))
    parameter7 = float(request.args.get('parameter7'))
    parameter8 = float(request.args.get('parameter8'))
    parameter9 = float(request.args.get('parameter9'))

    result = get_woz_value(parameter1, parameter2, parameter3, parameter4, parameter5, parameter6, parameter7, parameter8, parameter9)

    return jsonify(result)


if __name__ == '__main__':
    app.run()