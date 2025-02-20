FROM zenika/alpine-chrome:with-puppeteer
WORKDIR /app
EXPOSE 8000

USER root

RUN apk update
RUN apk add --no-cache python3 py3-pip

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt --break-system-packages

COPY ./package.json /app/package.json
COPY ./package-lock.json /app/package-lock.json
RUN npm ci

COPY . /app

ENTRYPOINT ["python3"]
CMD ["app.py"]