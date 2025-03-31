FROM dohackme.azurecr.io/base_images/pwn:debian

COPY ld-2.35.so /app/ld-2.35.so
RUN chmod 555 /app/ld-2.35.so

COPY libc.so.6 /app/libc.so.6
RUN chmod 555 /app/libc.so.6

COPY flag.txt /app/flag.txt
RUN chmod 444 /app/flag.txt

COPY anshin-impact /app/run
RUN chmod +x /app/run