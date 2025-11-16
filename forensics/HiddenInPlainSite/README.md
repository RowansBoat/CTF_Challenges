### Name

Hidden In Plain Site

### Description

```
We extracted the browsing history from a lead engineer's workstation right before the meltdown. Something tells me we can find some useful information if we take a careful look at the websites they visited.
```

### Difficulty

Medium

### Kind

Forensics

### Build instructions

Run browser-history-ctf.py to create the simulated browsing history database

### The Flag
<details>`CTF{Br0ws1ng_H1st0ry_T3lls_All}`</details>

### Solution
<details>
1. Open the database probably through sqlite3 browsing_history.db or through an online viewer https://sqliteviewer.app
2. If done in terminal
    * sqlite3 browsing_history.db
        * sqlite> .tables
        * sqlite> SELECT * FROM urls;
3. Recognize that https://pastebin.com/Q1RGe0JyMHdzMW5nX0gxc3QwcnlfVDNsbHNfQWxsfQ== has a base64 string at the end
4. Paste Q1RGe0JyMHdzMW5nX0gxc3QwcnlfVDNsbHNfQWxsfQ== into any base64 decoder for the flag
</details>
