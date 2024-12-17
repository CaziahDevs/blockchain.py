from flask.json import jsonify
from flask import request, Flask

from block import Block
from blockchain import Blockchain

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


    new_block: Block = blockchain.new_block(proof,blockchain.hash(last_block))

    response = {
        'message': 'New block forged',
        'index': new_block.index,
        'transactions': new_block.transactions,
        'proof': new_block.proof,
    }

    return jsonify(response), 200


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    data = request.get_json(force=True)

    required_fields = ['sender', 'recipient', 'amount']
    
    if not data or not all(field in data for field in required_fields):
        return 'Missing data', 400

    index = blockchain.new_transaction(data['sender'], data['recipient'], data['amount'])
    response = {'message': f'New transaction added to block {index}'}

    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def get_chain():
    chain = blockchain.get_chain
    print(chain)
    response = {
        'chain': chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3333)