FROM python:3.13-slim-bookworm
EXPOSE 8000
WORKDIR /app

RUN apt-get update && apt-get install -y socat

COPY . /app

RUN chmod -R 555 /app

CMD ["/app/entry.sh"]
