##
# Title: Python Flask endpoint within Amazon Virtual Private Cloud (VPC)
# to allow lambda to communicate with ethereum helper functions
# Version: v00_01
# Author: Nzwisisa Chidembo <nzwisisa@gmail.com>
##

from flask import Flask, jsonify, request
# Replace <helper function file> with your helper python file
import <helper function file> as sk

app = Flask(__name__)

@app.route('/', methods=["POST"])
def post():
    if request.is_json:
        data = request.get_json()
        res = sk.lambda_handler(data,[])
        return jsonify(res)
    else:
        return jsonify(state='Request was not JSON')

# Include the internal VPC ip address of your AWS EC2 instant
if __name__ == '__main__':
    app.run(host='xxxxxxxxx',debug=True)
