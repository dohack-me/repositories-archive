FROM python:3.13-slim-bookworm
WORKDIR /app
EXPOSE 8000

RUN apt-get update && apt-get install -y gcc

COPY . /app

ENTRYPOINT ["python"]
CMD ["app.py"]
