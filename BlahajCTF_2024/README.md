# BlahajCTF 2024

https://github.com/blahajctf/blahajctf24-public/tree/master/Challenges

# Omitted challenges

- forensics
  - memory
  - wireshonk
- rev
  - blahajcyptor

These challenges include large files, which my backend (supabase free tier lmao) doesn't support at the moment.
Otherwise, both challenges have no other issues. I am looking to include both of them when I deal with the storage problem.

- misc
  - modelanswer
  - modelanswer 2

Not sure if my VPS can handle Tensorflow stuff and I don't really want to try lmao

Other challenges not listed here might be missing as you read this. I will try to add those when I can!

# Notes

Strangely, some challenge sources lacked its metadata (challenge.yml). 

This means it is impossible to determine the challenge description or its authors. 
For affected challenges, this was noted down on the website.

# Legal

The original repository, [as of writing this, is licensed](https://github.com/blahajctf/blahajctf24-public/blob/2428d072b7b59902547711d75facbb16994fcfec/LICENSE.md) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en).

Therefore, the sources for this repository alone, are licensed under the [same license](LICENSE.md).

Some changes were made.
For this repository, most Dockerfile's were rewritten with a standardized format (mostly because the original ones were so messy)

No changes were made to the challenge's source code, except the following:
- web/babysql/requirements.txt
  - Added `markupsafe==2.0.1` due to https://github.com/pallets/markupsafe/issues/304
- web/calculator/app.py
  - Removed debug route `/supersecretadminpanelasdf123456789/<newpage>`