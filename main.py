from flask import Flask, render_template
# from v2_backend.model import Model

app = Flask(__name__)
# model = Model(256)
# model.load_model('models/v1', 'distilbert-base-uncased')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/demo', methods=['GET'])
def demo():
    return render_template('demo.html')

@app.route('/grant', methods=['GET'])
def grant():
    return render_template('grant.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
