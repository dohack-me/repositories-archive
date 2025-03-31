FROM dohackme.azurecr.io/base_images/pwn:python

COPY fake.txt /app/fake.txt
RUN chmod 444 /app/fake.txt

COPY flag.txt /app/flag.txt
RUN chmod 444 /app/flag.txt

COPY main.py /app/run.py
RUN chmod 555 /app/run.py