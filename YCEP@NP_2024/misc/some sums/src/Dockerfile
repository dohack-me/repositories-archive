FROM debian:12-slim
WORKDIR /srv/app
EXPOSE 8000

RUN apt-get update && apt-get install -y socat python3

COPY ./entry.sh /srv/app/entry.sh
RUN chmod 555 /srv/app/entry.sh

COPY ./flag.txt /srv/app/flag.txt
RUN chmod 444 /srv/app/flag.txt

COPY ./main.py /srv/app/main.py
RUN chmod 555 /srv/app/main.py

CMD ["/srv/app/entry.sh"]