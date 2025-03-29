FROM python:3.10
WORKDIR /app
EXPOSE 5000

RUN pip install flask waitress lxml==4.9.3

COPY . /app

CMD ["python3", "app.py"]