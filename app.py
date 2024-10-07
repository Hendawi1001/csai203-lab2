from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', result=None)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']
    major = request.form['major']
    return render_template('result.html', name=name, age=age,major=major)

if __name__ == '__main__':
    app.run(debug=True)
