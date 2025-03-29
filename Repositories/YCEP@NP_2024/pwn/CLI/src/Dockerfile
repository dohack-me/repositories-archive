FROM debian:12-slim
WORKDIR /srv/app
EXPOSE 8000

RUN apt-get update && apt-get install -y socat

COPY ./entry.sh /srv/app/entry.sh
RUN chmod 555 /srv/app/entry.sh

# Original Dockerfile moved flag to ".flag"
COPY ./flag /srv/app/.flag
RUN chmod 444 /srv/app/.flag

COPY ./README /srv/app/README
RUN chmod 444 /srv/app/README

COPY ./shell.sh /srv/app/run
RUN chmod 555 /srv/app/run

CMD ["/srv/app/entry.sh"]