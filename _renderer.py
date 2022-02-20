from concurrent.futures import process
from flask import Flask, render_template, request

from core_integration.reentrymain import process_gpt3

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/post_contract', methods=['POST'])
def post():
    contract = request.form['data']
    try:
        classification = process_gpt3(contract)
        return classification
    except:
        return "Error"


if __name__ == "__main__":
    app.run(debug=True)