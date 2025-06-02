FROM dohackme.azurecr.io/base_images/pwn:python

RUN pip install pycryptodome

COPY uwusignatures.py /app/run.py
RUN chmod 555 /app/run.py