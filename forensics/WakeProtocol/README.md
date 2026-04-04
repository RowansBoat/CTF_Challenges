### Name

Wake protocol


### Description 

```
You decide to uncover the truth behind the rumors. Old syslogs hint at a project codenamed DREAMSYNC.
```


### Difficulty

Warmup

### Flag
<details>`CTF{awak3n1ng}`</details>

### Solution
<details>1. Look through the text and notice line 200 and 208
2. [SYSLOG] wake.up.sequence.1="01000011 01010100 01000110 01111011" and [SYSLOG] wake.up.sequence.2="01100001 01110111 01100001 01101011 00110011 01101110 00110001 01101110 01100111 01111101"
4. Combine the two seuences to get 01000011 01010100 01000110 01111011 01100001 01110111 01100001 01101011 00110011 01101110 00110001 01101110 01100111 01111101
5. Simply convert the binary to text to gget the flag. Can just paste into cyberchef and it auto solves it</details>
