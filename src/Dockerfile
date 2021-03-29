FROM python:3.6

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 3978

CMD [ "python", "app.py"]
