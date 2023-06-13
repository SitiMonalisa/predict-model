import os
import pandas as pd
import numpy as np
import mysql.connector
from keras.models import load_model
from flask import Flask, request, jsonify

app = Flask(__name__)

model = load_model('Model_fix.h5')

labels = ["beras", "jagung", "buncis", "kacangmerah", "kacanggude",
       "kacangngengat", "kacanghijau", "gramhitam", "lentil", "delima",
       "pisang", "mangga", "anggur", "semangka", "melon musk", "apel",
       "jeruk", "pepaya", "kelapa", "katun", "rami", "kopi"]


mydb = mysql.connector.connect(
  host="34.28.108.156",
  user="root",
  password="123",
  database="recommendation"
)

@app.route("/predict", methods=["POST"])
def predict():
    # ...

    # Membuka kursor untuk menjalankan query
    cursor = mydb.cursor()

    # Menjalankan query untuk mendapatkan data dari tabel
    query = "SELECT N, P, K, temperature, humidity, ph, rainfall FROM recommendation"
    cursor.execute(query)
    data = cursor.fetchall()

    # Menutup kursor
    cursor.close()

    # ...
    data = [
        request.form.get("N"),
        request.form.get("P"),
        request.form.get("K"),
        request.form.get("temperature"),
        request.form.get("humidity"),
        request.form.get("ph"),
        request.form.get("rainfall")
    ]

    # Jika data tidak ada
    if None in data:
        return jsonify({"message": "Maaf, harap isi semua field yang diperlukan."})
    
    try:
        prediksi = np.array([eval(val) for val in data])
        if not isinstance(prediksi, np.ndarray):
            raise ValueError
    except (ValueError, SyntaxError):
        return jsonify({"message": "Maaf, format data gejala tidak valid."})
    
    # Konversi data menjadi format yang dapat digunakan oleh model
    prediksi_df = pd.DataFrame([prediksi], columns=["N", "P", "K", "temperature", "humidity", "ph", "rainfall"])

    # Prediksi
    predictions = model.predict(prediksi_df)

    # Menentukan label berdasarkan nilai probabilitas
    predicted_class = np.argmax(predictions[0])
    predicted_label = labels[predicted_class]

    return jsonify({"message": "Prediksi: " + predicted_label})

    if __name__ == '__main__':
        # Menentukan port berdasarkan variabel lingkungan PORT atau menggunakan port default 8080
        port = int(os.environ.get('PORT', 8000))
        app.run(host='0.0.0.0', port=port)