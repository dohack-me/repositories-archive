FROM python:3.13-alpine
WORKDIR /app
EXPOSE 8000

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT ["python"]
CMD ["app.py"]