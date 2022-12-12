FROM python:3.9 as app-blockchain
WORKDIR /usr/src
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY app-blockchain app-blockchain
