FROM dohackme.azurecr.io/base_images/pwn:debian

COPY flag /app/flag
RUN chmod 444 /app/flag

COPY README /app/README
RUN chmod 444 /app/README

COPY shell.sh /app/run
RUN chmod +x /app/run