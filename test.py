from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'From Green Team Testing TESTING WEBOOK3 FROM PR'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

