FROM dohackme.azurecr.io/base_images/web:apache

COPY flag.txt /flag.txt

COPY src/* /var/www/html/

RUN adduser --uid 1000 --disabled-password nonroot # challenge runs shell_exec(), better to leave this here