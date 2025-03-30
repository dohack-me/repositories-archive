FROM debian:12-slim
WORKDIR /app
EXPOSE 8000

RUN apt-get update && apt-get install -y socat

CMD ["socat", "TCP-LISTEN:8000,nodelay,reuseaddr,fork", "EXEC:\"timeout -s KILL 10m /app/run\""]