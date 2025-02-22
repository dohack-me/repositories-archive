FROM python:3.13-slim-bookworm
WORKDIR /app
EXPOSE 8000

RUN apt update && apt install -y socat

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY . /app

CMD ["/app/entry.sh"]
