FROM dohackme.azurecr.io/base_images/web:flask

RUN pip install selenium python-dotenv

RUN apk add --no-cache ca-certificates curl firefox geckodriver

COPY . /app