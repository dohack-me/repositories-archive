FROM dohackme.azurecr.io/base_images/pwn:debian

COPY ld-linux-x86-64.so.2 /app/ld-linux-x86-64.so.2
RUN chmod 555 /app/ld-linux-x86-64.so.2

COPY libc.so.6 /app/libc.so.6
RUN chmod 555 /app/libc.so.6

COPY flag.txt /app/flag.txt
RUN chmod 444 /app/flag.txt

COPY program /app/run
RUN chmod +x /app/run