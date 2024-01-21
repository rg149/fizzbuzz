from flask import Flask, request, jsonify
from .fizzbuzz_logic import get_stats, get_result

app = Flask(__name__)


@app.route('/fizzbuzz', methods=['GET'])
def fizzbuzz():
    try:
        int1 = int(request.args.get('int1'))
        int2 = int(request.args.get('int2'))
        limit = int(request.args.get('limit'))
        str1 = request.args.get('str1')
        str2 = request.args.get('str2')

        result = get_result(int1, int2, limit, str1, str2)
        return result

    except ValueError as e:
        return jsonify({"error": "Invalid input. Ensure all parameters are of valid type (int, str)."}), 400


@app.route('/statistics', methods=['GET'])
def statistics():

    stats_result = get_stats()
    return stats_result


@app.route("/", methods=['GET'])
def home():
    return {'message': 'Fizzbuzz Home. Please read API Guide for more details.'}


if __name__ == '__main__':
    app.run(debug=True)
