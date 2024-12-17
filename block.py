import time
from typing import List
from transaction import Transaction

class Block(object):
    def __init__(self, index:int, timestamp:float, proof:int, prev_hash:int):
        self.index = index
        self.timestamp = timestamp
        self.transactions: List[Transaction] = []
        self.proof = proof
        self.prev_hash = prev_hash

    def to_dict(self) -> dict:
        return {
            'index': self.index,
            'timestamp': self.timestamp,
            'transactions': [tx.to_dict() for tx in self.transactions],
            'proof': self.proof,
            'prev_hash': self.prev_hash
        }