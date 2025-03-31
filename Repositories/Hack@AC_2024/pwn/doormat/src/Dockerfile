FROM dohackme.azurecr.io/base_images/pwn:debian

COPY ld-2.27.so /app/ld-2.27.so
RUN chmod 555 /app/ld-2.27.so

COPY libc-2.27.so /app/libc-2.27.so
RUN chmod 555 /app/libc-2.27.so

COPY flag.txt /app/flag.txt
RUN chmod 444 /app/flag.txt

COPY doormat /app/run
RUN chmod +x /app/run