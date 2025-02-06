from flask import Flask, jsonify, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_score():
    score = random.randint(0, 100)
    return jsonify({"score": score})

@app.route('/sum_score', methods=['POST'])
def sum_score():
    data = request.get_json()
    total_score = sum(data.get("values", []))
    return jsonify({"score": total_score})


"""
if __name__ == '__main__':
    app.run(debug=True)
"""
def handler(event, context):
    return app(event, context)
