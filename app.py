import numpy as np
from joblib import load
from flask import Flask, render_template, request

app = Flask(__name__)

# load eksternal model
filename = 'model.sav'
model = load(filename)

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

# route untuk menampilkan halaman awal (index.html)
@app.route('/')
def home():
    return render_template('index.html')

# route tampilan awal
@app.route('/getResult', methods=['POST'])
def getResult():

    if (request.method == 'POST'):
        # mendefinisikan list untuk menampung data yang akan diinput user
        singleData = []

        # mendefinisikan list untuk menampung data
        dataTest = []

        # input data
        for x in range(4):
            data = request.json[x]
            singleData.append(float(data))

        # menggabungkan tiap single data ke dalam data test
        dataTest.append(singleData)

        # convert dari list ke numpy array
        dataTest = np.array(dataTest)

        # load file scaler
        scaler = load('scaler.bin')
        dataTest = scaler.transform(dataTest)

        # melakukan prediksi data baru
        prediksi = int(model.predict(dataTest))
        
        return render_template('index.html', prediction = HasilKlasifikasi(prediksi))

if __name__ == '__main__':
    app.run(debug=True)
