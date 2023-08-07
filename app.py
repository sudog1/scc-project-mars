from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

client = MongoClient('mongodb+srv://sparta:test@cluster0.plgtff3.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/mars", methods=["POST"])
def mars_post():
    name = request.form['name']
    address = request.form['address']
    size = request.form['size']
    doc = {
        'name': name,
        'address': address,
        'size': size
    }
    db.mars.insert_one(doc)
    return jsonify({'msg':'저장 완료'})

@app.route("/mars", methods=["GET"])
def mars_get():
    data = list(db.mars.find({}, {'_id': False}))
    return jsonify({'result': data})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)