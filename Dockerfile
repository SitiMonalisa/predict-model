# Menggunakan image yang mendukung Python
FROM python:3.9-slim

# Mengatur working directory ke /app
WORKDIR /app

# Menyalin file requirements.txt ke dalam container
COPY requirements.txt .

# Menginstal dependensi dari requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Menyalin model H5 dan file main.py ke dalam container
COPY Model_fix.h5 main.py ./

# Menjalankan aplikasi Flask ketika container dimulai
CMD ["python", "main.py"]
