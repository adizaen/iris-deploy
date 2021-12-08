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
        # mendefinisikan list untuk menampung data yang akan diinput user
        singleData = []

        # mendefinisikan list untuk menampung data
        dataTest = []

        singleData = [x for x in request.form.values()]

        # menggabungkan tiap single data ke dalam data test
        dataTest.append(singleData)

        # convert dari list ke numpy array
        dataTest = np.array(dataTest)

        # load file scaler
        scaler = load('scaler.bin')
        dataTest = scaler.transform(dataTest)

        # load eksternal model
        filename = 'model.sav'
        model = load(filename)

        # melakukan prediksi data baru
        prediksi = int(model.predict(dataTest))
        
        return render_template('index.html', prediction = HasilKlasifikasi(prediksi))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
