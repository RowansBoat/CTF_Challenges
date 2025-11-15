### Name

Meltdown Override

### Description

```
Nuclear reactor core temperature critical! The lead engineer's password has been lost in the chaos. Can you bypass authentication and access the emergency shutdown system before meltdown?
```

### Difficulty

Easy


### Kind

Web

### How to solve

1. The application is vulnerable to SQL injection in the login endpoint
2. The SQL query directly concatenates user input: SELECT * FROM users WHERE username = '${username}' AND password = '${password}'
3. Bypass authentication using a classic SQL injection payload in either field
4. Example: Username: engineer Password: ' OR '1'='1
5. Alternatively: Username: ' OR 1=1 -- Password: (anything)
6. Successfully injecting will return all user records, including the flag in the notes field

### The flag

<details>
CTF{C0R3_0V3RH34T_D3T3CT3D}
  
### Special notes
N/A
