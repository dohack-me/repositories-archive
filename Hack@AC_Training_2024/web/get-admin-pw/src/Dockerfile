FROM dohackme.azurecr.io/base_images/web:latest

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY ./main.py /app/app.py