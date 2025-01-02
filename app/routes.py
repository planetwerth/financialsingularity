from flask import render_template, jsonify, request
from app import app
from app.blockchain import create_genesis_block, create_new_block

genesis_block = create_genesis_block()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blockchain', methods=['GET'])
def get_blockchain():
    blockchain = [genesis_block]
    return jsonify([block.__dict__ for block in blockchain])

@app.route('/new_block', methods=['POST'])
def new_block():
    data = request.json.get('data')
    new_block = create_new_block(genesis_block, data)
    return jsonify(new_block.__dict__)
