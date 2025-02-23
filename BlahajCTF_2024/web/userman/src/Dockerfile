FROM php:8.2-apache
EXPOSE 80

COPY 000-default.conf /etc/apache2/sites-available/000-default.conf
COPY ports.conf /etc/apache2/ports.conf

COPY src/* /var/www/html/

RUN mkdir /var/www/html/databases
RUN chmod 777 /var/www/html/databases

CMD ["apache2-foreground"]