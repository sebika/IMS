FROM python:3.11-alpine

WORKDIR /opt/backend

COPY computer_parts_store_project ./
COPY requirements.txt ./

RUN pip install -r requirements.txt

EXPOSE 8000

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]
