### Name

Brick Smuggler


### Description

```
A warehouse employee was caught uploading symmetric encrypted data to an external FTP server. We need to know what they stole.
```


### Difficulty

Hard


### Kind

Forensics

### Author

Rowan

### The flag
<details>
`CTF{tunnel_made_of_bricks}`
</details>

### How to solve
<details>
1. Open File in Wireshark
2. If you start by looking at TXT records you will find a query which contains a TXT with hint=famous_toy_brand inside
3. Key can be guessed here or can be found by looking at the only HTTP request which contains "TEVHTw=" which is base64 for LEGO
4. Key = LEGO
5. Filter by FTP per the challenge description
6. NO.90 has the info STOR flag.txt
7. Got to where that was stored based on the info provided by wireshark.
8. Search tcp.port == 20
9. Find packet with FTP data - NO.95
10. Right click NO.95 -> Follow -> TCP Stream
11. Copy the data as RAW
12. 0f11013438302921292918222d2122102323182d3e2c24243f38
13. Translate data on cyberchef to binary. From Hex + To Binary
14. Go to Dcode and solve the XOR cipher.
15. Text to XOR'd step 13 with ASCII Key as LEGO then Decrypt
</details
