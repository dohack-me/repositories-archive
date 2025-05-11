# YCEP 2025 @ NP

https://github.com/NullSec-SIG/YCEP2025-Challenge-Repo/tree/main/challenges

# Omitted Challenges

- forensics
  - Stealth Mode Activated
  - Through Out

These challenges include large files, which my backend (supabase free tier lmao) doesn't support at the moment.
Otherwise, these challenges have no other issues.
I am looking to include them when I deal with the storage problem.

- misc
  - Sh3llSh0ck

Distributed files not available.

# Notes

- misc
  - Crazy Cipher

Challenge was moved to `crypto`.

- pwn
  - train_bank

Turned off buffering for `stdout` and `stdin` to fix image. Distributed source code was also changed.

- pwn
  - train_bank
  - train_bofchall

No compiled binaries were provided. They were compiled by myself with `gcc chal.c -no-pie -o chal`