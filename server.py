from flask.json import jsonify
from requests import request
from .blockchain import Blockchain
from flask import Flask
from uuid import uuid4

#Create node
app = Flask(__name__)
#Create global unique address
node_identifier = str(uuid4()).replace('-', '')
#Create blockchain instance
blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    return "we'll mine a block"

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()

    required_fields = ['sender', 'recipient', 'amount']
    
    if not all(field in values for field in required_fields):
        return 'Missing values', 400
    
    

@app.route('/chain', methods=['GET'])
def get_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)