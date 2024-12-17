from flask.json import jsonify
from requests import request

from block import Block
from blockchain import Blockchain
from flask import Flask
from uuid import uuid4

#Create node
app = Flask(__name__)
#Create global unique address
node_identifier = str(uuid4()).replace('-', '')
#Create blockchain instance
blockchain:Blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    last_block = blockchain.last_block
    proof:int = blockchain.proof_of_work(last_block.proof)

    blockchain.new_transaction("0",node_identifier, 1)

    new_block: Block = blockchain.new_block(proof, last_block.prev_hash)

    response = {
        'message': 'New block forged',
        'index': new_block.index,
        'transactions': new_block.transactions,
        'proof': new_block.proof,
    }

    return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()

    required_fields = ['sender', 'recipient', 'amount']
    
    if not all(field in values for field in required_fields):
        return 'Missing values', 400

    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])
    response = {'message': f'New transaction added to block {index}'}

    return jsonify(response), 201
    

@app.route('/chain', methods=['GET'])
def get_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3333)