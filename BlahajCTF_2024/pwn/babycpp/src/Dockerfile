FROM debian:12-slim
WORKDIR /srv/app
EXPOSE 8000

RUN dpkg --add-architecture i386
RUN apt-get update && apt-get install -y socat libc6:i386 libstdc++6:i386

COPY ./entry.sh /srv/app/entry.sh
RUN chmod 555 /srv/app/entry.sh

COPY ./chal /srv/app/run
RUN chmod 555 /srv/app/run

CMD ["/srv/app/entry.sh"]