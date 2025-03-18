FROM dohackme.azurecr.io/base_images/web:latest

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

RUN apk add --no-cache ca-certificates curl firefox geckodriver

COPY . /app