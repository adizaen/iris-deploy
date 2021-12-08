import numpy as np
from joblib import load
from flask import Flask, render_template, request

app = Flask(__name__)

# definisi hasil klasifikasi
def HasilKlasifikasi(hasil):
    jenisIris = None
    
    if hasil == 0:
        jenisIris = 'Iris Setosa'
    elif hasil == 1:
       jenisIris = 'Iris Versicolor'
    else:
       jenisIris = 'Iris Virginica'
    
    return jenisIris

# route tampilan awal
@app.route('/', methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
        
        return render_template('index.html', prediction = 'ada post loh')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
