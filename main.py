#Esercizio 0
import random
from flask import Flask,render_template
app = Flask(__name__)

#Esercizio 5
counter = 0

#Esercizio 1
@app.route('/', methods=['GET'])
def homepage():    
    return render_template('numeri.html')

#Esercizio 3/4/5
@app.route('/result/<choice>', methods=['GET'])
def result(choice):
    global counter
    counter += 1
    randval = random.randint(1, 9)
    return render_template('risultato.html', result=(True if randval==int(choice) else False), games_counter=counter)

#Esercizio 0
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)