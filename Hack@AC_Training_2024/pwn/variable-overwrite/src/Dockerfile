FROM dohackme.azurecr.io/base_images/pwn:latest

COPY ./chall /srv/app/run
RUN chmod 555 /srv/app/run

COPY ./flag.txt /srv/app/flag.txt
RUN chmod 444 /srv/app/flag.txt