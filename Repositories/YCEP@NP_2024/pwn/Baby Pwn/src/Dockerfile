FROM debian:12-slim
WORKDIR /srv/app
EXPOSE 8000

RUN apt-get update && apt-get install -y socat

COPY ./entry.sh /srv/app/entry.sh
RUN chmod 555 /srv/app/entry.sh

# Program requires the flag file to be named as "flag"
COPY ./flag /srv/app/flag
RUN chmod 444 /srv/app/flag

COPY ./chall /srv/app/run
RUN chmod 555 /srv/app/run

CMD ["/srv/app/entry.sh"]