import random
from flask import Flask,render_template
app = Flask(__name__)

counter = 0

@app.route('/', methods=['GET'])
def homepage():    
    return render_template('numeri.html')

@app.route('/result/<choice>', methods=['GET'])
def result(choice):
    global counter
    counter += 1
    randval = random.randint(1, 9)
    return render_template('risultato.html', result=(True if randval==int(choice) else False), games_counter=counter)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)