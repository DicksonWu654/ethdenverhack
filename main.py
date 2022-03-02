from flask import Flask, render_template, request
import numpy as np

from v2_backend.model import Model

app = Flask(__name__)
model = Model(256)
model.load_model('models/v1', 'distilbert-base-uncased')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/post_contract', methods=['POST'])
def post():
    contract = request.form['data']
    try:
        output = model.classify(contract, 256)
        classification = np.argmax(np.array(output))
        return f"{classification}"
    except:
        return "Error"

if __name__ == "__main__":
    app.run(debug=True)
