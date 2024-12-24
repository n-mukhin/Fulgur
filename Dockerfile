FROM python:3.11-slim

WORKDIR /app

COPY app/requirements.txt .

RUN apt-get update && \
    apt-get install -y graphviz && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY app/ /app

EXPOSE 5000

CMD ["python", "app.py"]
