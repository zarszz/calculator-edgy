FROM python:3.8

WORKDIR /src/app

COPY . /src/app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
