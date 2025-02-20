FROM php:7.2-apache
COPY src/ /var/www/html/
COPY src/flag.txt /flag.txt
#COPY src/000-default.conf /etc/apache2/000-default.conf
COPY src/000-default.conf /etc/apache2/sites-available/000-default.conf
COPY src/ports.conf /etc/apache2/ports.conf
RUN adduser --uid 1001 --disabled-password nonroot
CMD ["apache2-foreground"]