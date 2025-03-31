FROM dohackme.azurecr.io/base_images/pwn:debian

COPY flag /app/flag
RUN chmod 444 /app/flag

COPY chall /app/run
RUN chmod +x /app/run