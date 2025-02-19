# BlahajCTF 2024

https://github.com/blahajctf/blahajctf24-public/tree/master/Challenges

# Omitted challenges

- forensics
  - memory
  - wireshonk
    - Both challenges include super large files (1GB and 2GB respectively), which my backend (supabase free tier lmao) doesn't support at the moment.
    - Otherwise, both challenges have no other issues. I am looking to include both of them when I deal with the storage problem.

# Notes

Strangely, some challenge sources lacked its metadata (challenge.yml). 
This means it is impossible to determine the challenge description or its authors. 
For affected challenges, this was noted down on the website.

# Legal

The original repository, [as of writing this, is licensed](https://github.com/blahajctf/blahajctf24-public/blob/2428d072b7b59902547711d75facbb16994fcfec/LICENSE.md) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en).

Therefore, the sources for this repository alone, are licensed under the [same license](LICENSE.md).

Some changes were made.
As stated in the [root README](../README.md), challenge Dockerfile's received additional steps,
mostly consisting of `EXPOSE` instructions.

No changes were made to the challenge's source code.