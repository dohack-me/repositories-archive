FROM dohackme.azurecr.io/base_images/pwn:debian

COPY flag.txt /app/flag.txt
RUN chmod 444 /app/flag.txt

COPY level1 /app/run
RUN chmod +x /app/run