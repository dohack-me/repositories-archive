FROM dohackme.azurecr.io/base_images/pwn:debian

RUN dpkg --add-architecture i386
RUN apt-get update && apt-get install -y libc6:i386 libstdc++6:i386

COPY chal /app/run
RUN chmod +x /app/run