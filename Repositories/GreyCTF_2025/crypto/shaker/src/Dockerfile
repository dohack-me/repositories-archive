FROM dohackme.azurecr.io/base_images/pwn:python

COPY flag.txt /app/flag.txt
RUN chmod 444 /app/flag.txt

COPY shaker.py /app/run.py
RUN chmod 555 /app/run.py