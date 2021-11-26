FROM python:3.9.6

WORKDIR /usr/src/fast_app

# copy over content, use .dockerignore to exclude files from build
COPY . .

# installs
RUN pip install --no-cache-dir -r requirements.txt