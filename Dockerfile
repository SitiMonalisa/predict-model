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

ENV PYTHONUNBUFFERED=1

ENV HOST 0.0.0.0

EXPOSE 8080

# Menjalankan aplikasi Flask ketika container dimulai
CMD ["python", "main.py"]

# FROM python:3.10.3-slim-buster

# WORKDIR /app

# COPY requirements.txt requirements.txt

# RUN pip install -r requirements.txt

# COPY . .

# ENV PYTHONUNBUFFERED=1

# ENV HOST 0.0.0.0

# EXPOSE 8080

# CMD ["python", "main.py"]
