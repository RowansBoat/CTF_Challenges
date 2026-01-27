### Name
Embedded Logs

### Description

```
One of our logs shows that there is some data that got encrypted during the shift. Maybe we can get to the bottom of this if you get me that data. I also heard something about a 1 and 5?
```

### Difficulty
Medium

### Kind

Forensics

### Author
Rowan

### Flag
<details>
`CTF{embedded_through_layers}`
</details>

### How to solve
<details>
1. This can all be done in cyberchef
2. In the log take out the V1WLj3O6g3OchCOcC2i1EBOtiMAkjB5xhrArkV==
3. First decode with Affine ciphger a = 1 b = 5
4. Then base64 decode
5. then rot13 decode
</details>
