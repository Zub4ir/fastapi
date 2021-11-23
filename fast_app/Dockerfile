FROM python:3.9.6

WORKDIR /usr/src/fast_app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .