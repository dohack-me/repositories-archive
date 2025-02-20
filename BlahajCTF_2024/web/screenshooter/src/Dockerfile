FROM python:3.13-alpine
WORKDIR /app
EXPOSE 8000

# User is added to be more similar to original challenge, and because the user who runs the flask app matters for this challenge
RUN adduser --uid 1001 --disabled-password nonroot

RUN apk update
RUN apk add firefox
RUN apk add font-terminus

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /app/screenshots
RUN chmod 777 /app/screenshots

COPY . /app

USER 1001
ENTRYPOINT ["python"]
CMD ["app.py"]
