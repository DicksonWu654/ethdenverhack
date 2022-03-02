from flask import Flask, render_template, request

app = Flask(__name__)

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
    app.run(debug=True)