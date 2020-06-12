from flask import Flask
from flask import request
from flask import jsonify
import datetime

import utils
import hit


startTime = datetime.datetime.now().strftime("%Y-%b-%d %H:%M:%S")

app = Flask(__name__)

@app.route("/")
def show_details() :
    global startTime
    return "hello"

@app.route("/json")
def send_json() :
    global startTime
    return jsonify( {'StartTime' : startTime,
                     'Server Hit': str(hit.getServerHitCount())} )

@app.route("/payload",methods=['GET', 'POST'])
def payload() :
	return str(request.get_data(True,True,False))
if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0')
