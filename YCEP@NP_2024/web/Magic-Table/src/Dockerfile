FROM php:8.3.7-apache
EXPOSE 80

COPY 000-default.conf /etc/apache2/sites-available/000-default.conf
COPY ports.conf /etc/apache2/ports.conf

COPY src /var/www/html/

CMD ["apache2-foreground"]