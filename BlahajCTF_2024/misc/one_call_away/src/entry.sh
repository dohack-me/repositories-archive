#!/usr/bin/env sh
socat TCP-LISTEN:8000,nodelay,reuseaddr,fork EXEC:"timeout -s KILL 10m python3 /app/jail.py",stderr