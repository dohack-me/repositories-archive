FROM python:3.13-alpine
WORKDIR /app
EXPOSE 8000

RUN apk update && apk add socat

CMD ["socat", "TCP-LISTEN:8000,nodelay,reuseaddr,fork", "EXEC:\"timeout -s KILL 10m python -u /app/run.py\""]