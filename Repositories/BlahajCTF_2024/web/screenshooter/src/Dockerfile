FROM dohackme.azurecr.io/base_images/web:flask

RUN apk update && apk add firefox && apk add font-terminus

RUN mkdir /app/screenshots
RUN chmod 777 /app/screenshots

RUN adduser --uid 1000 --disabled-password nonroot
USER 1000

COPY . /app