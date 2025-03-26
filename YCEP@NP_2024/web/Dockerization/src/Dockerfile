FROM dohackme.azurecr.io/base_images/web:latest

ENV LD_LIBRARY_PATH="/app"

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app