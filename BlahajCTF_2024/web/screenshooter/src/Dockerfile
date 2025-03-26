FROM dohackme.azurecr.io/base_images/web:latest

RUN apk update && apk add firefox && apk add font-terminus

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /app/screenshots
RUN chmod 777 /app/screenshots

RUN adduser --uid 1000 --disabled-password nonroot
USER 1000

COPY . /app