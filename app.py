from flask import Flask, request, jsonify
import db.database

app = Flask(__name__)

db.database.init_db()

@app.route('/', methods=['GET'])
def get():
    return jsonify({'msg': 'It works'})


if __name__ == '__main__':
    app.run(debug=True)
