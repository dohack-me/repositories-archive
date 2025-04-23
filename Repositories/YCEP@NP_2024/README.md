# YCEP 2024 @ NP

https://github.com/NullSec-SIG/YCEP2024-Challenge-Repo/tree/main/challenges

# Omitted challenges

- forensics
  - Excel, My Beloved
  - Galvanized Square Steel
  - red herrings
- misc
  - pachinko

These challenges include large files, which my backend (supabase free tier lmao) doesn't support at the moment.
Otherwise, these challenges have no other issues.
I am looking to include them when I deal with the storage problem.

- web
  - SQLi

Stack not supported by orchestrator.
I could rewrite the app to use SQLite, but with how generic this challenge is, it's not a priority.

- misc
  - grab this
  - ugly handwriting
  - welcome

Personal judgement, irrelevant

# Notes

- misc
  - some sums

Changed line 40 from `i == 10` to `i == 1000`.
I assume this was a typo, as the source code and challenge description implies you need to solve 1000 sums, not 10.
It would also be too easy to manually do.