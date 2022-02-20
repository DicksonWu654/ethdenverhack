from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/post_contract', methods=['POST'])
def post():
    contract = request.form['data']
    print(contract)
    return "recived: {}".format(request.form)

if __name__ == "__main__":
    app.run(debug=True)