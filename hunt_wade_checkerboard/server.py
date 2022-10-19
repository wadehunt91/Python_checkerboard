from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html' , numTwo=8, numOne = 8 , colorOne= 'black' , colorTwo='red')

@app.route('/<int:numOne>/')
def one(numOne,):
    return render_template('index.html', numTwo=8, numOne = numOne , colorOne='black' , colorTwo='red')

@app.route('/<int:numOne>/<int:numTwo>')
def two(numOne, numTwo):
    return render_template('index.html', numTwo=numTwo, numOne = numOne , colorOne='black' , colorTwo='red')

@app.route('/<int:numOne>/<int:numTwo>/<string:colorOne>/<string:colorTwo>')
def four(numOne, numTwo, colorOne , colorTwo):
    return render_template('index.html', numTwo=numTwo, numOne = numOne , colorOne= colorOne , colorTwo=colorTwo)

if __name__=="__main__":
    app.run(debug=True)