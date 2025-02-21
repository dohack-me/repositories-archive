FROM debian:12-slim
WORKDIR /srv/app
EXPOSE 8000

RUN apt-get update && apt-get install -y socat

COPY ./libc.so.6 /srv/app/libc.so.6
RUN chmod 555 /srv/app/libc.so.6

COPY ./ld-linux-x86-64.so.2 /srv/app/ld-linux-x86-64.so.2
RUN chmod 555 /srv/app/ld-linux-x86-64.so.2

COPY ./entry.sh /srv/app/entry.sh
RUN chmod 555 /srv/app/entry.sh

COPY ./flag.txt /srv/app/flag.txt
RUN chmod 444 /srv/app/flag.txt

COPY ./enotes /srv/app/run
RUN chmod 555 /srv/app/run

CMD ["/srv/app/entry.sh"]
