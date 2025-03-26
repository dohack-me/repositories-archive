FROM dohackme.azurecr.io/base_images/web:latest

RUN apk update && apk add chromium

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app