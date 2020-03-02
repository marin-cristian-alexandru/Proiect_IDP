from flask import request, jsonify, Flask, Response
from heapq import *

app = Flask(__name__)

@app.route("/tranfer")
def transfer_player():
    pass
    
@app.route("/rumor")
def rumor_player():
    pass
#    return jsonify(response), 200

if __name__ == '__main__':
   app.run(debug=True)
