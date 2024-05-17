# Base image olarak Python'un resmi imajını kullan
FROM python:3.9-slim

# Çalışma dizinini oluştur ve ayarla
WORKDIR /app

# Gereksinim dosyasını kopyala ve bağımlılıkları yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyalarını kopyala
COPY . .

# Streamlit'in varsayılan portunu belirt
EXPOSE 8501

# Uygulamayı çalıştır
CMD ["streamlit", "run", "app/app.py"]