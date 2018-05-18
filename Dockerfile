FROM frolvlad/alpine-python-machinelearning
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
