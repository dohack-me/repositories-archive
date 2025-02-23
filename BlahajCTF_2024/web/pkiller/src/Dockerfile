FROM php:7.2-apache
EXPOSE 80

COPY 000-default.conf /etc/apache2/sites-available/000-default.conf
COPY ports.conf /etc/apache2/ports.conf

COPY flag.txt /flag.txt

COPY src/* /var/www/html/

RUN adduser --uid 1001 --disabled-password nonroot # challenge runs shell_exec(), better to leave this here
CMD ["apache2-foreground"]