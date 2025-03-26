FROM python:3.13-alpine
WORKDIR /app
EXPOSE 5000

RUN pip install flask waitress

ENTRYPOINT ["python"]
CMD ["/app/app.py"]