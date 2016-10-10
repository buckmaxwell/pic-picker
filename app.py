from flask import Flask, request, send_file, jsonify
import json

app = Flask(__name__)


# API #################################################################################################################

@app.route('/', methods=['GET'])
def search():
    """ Expecting request like, http://localhost:5000?search=Tina+Belcher 
    returns, matching pictures
    """
    # TODO: Implement this properly
    search = request.args.get('search')
    if not search:
        return "please supply a search term!"
    else:
        print search
        return send_file('./Data/c.jpg', mimetype='image/jpg')


# FLASK INFO############################################################################################################


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)