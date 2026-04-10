FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN ls -R /app   

# 🔥 DEBUG LINE

RUN apt-get update && apt-get install -y \
    ffmpeg libsm6 libxext6 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt

CMD ["python3", "app.py"]

