FROM dohackme.azurecr.io/base_images/pwn:debian

COPY flag.txt /app/flag.txt
RUN chmod 444 /app/flag.txt

COPY namecard /app/run
RUN chmod +x /app/run

ADD "https://www.random.org/cgi-bin/randbyte?nbytes=10&format=h" skipcache