FROM python:3.11-alpine

WORKDIR /opt/payment

COPY payment.py ./
COPY requirements.txt ./

RUN pip install -r requirements.txt

EXPOSE 4242

CMD [ "python3", "payment.py"]
