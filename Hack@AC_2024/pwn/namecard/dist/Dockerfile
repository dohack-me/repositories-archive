FROM pwn.red/jail

COPY --from=ubuntu@sha256:e9569c25505f33ff72e88b2990887c9dcf230f23259da296eb814fc2b41af999 / /srv

COPY ./flag.txt /srv/app/flag.txt
ADD "https://www.random.org/cgi-bin/randbyte?nbytes=10&format=h" skipcache
COPY ./namecard /srv/app/run

RUN chmod 444 /srv/app/flag.txt
RUN chmod +x /srv/app/run