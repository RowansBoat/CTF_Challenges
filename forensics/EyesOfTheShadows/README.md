### Name

Eyes Of The Shadows

### Description

```
You stand face to face with what looks like 2 eyes spread very far apart. The eyes inform you that this problem, at its base, has 2 layers.
```

### Difficulty

HARD

### Flag
<details>
`CTF{/esc4p3d_the_r0om/}`
</details>

### How to solve
<details>
1. First paste this image into cyberchef
2. Run To Hex on the image and copy the output
3. Now using from hex and render image paste what you copied into the input
4. You now must edit the height values for this image.
5. Find this in the hex ff c0 00 0b 08 00 22 01 f4
6. Change "00 22" to very large hex values to expand the image. 99 99 works
7. Scan this QR code you now have
8. This gives you a base64 string
9. Now just convert base64 to a png and scan that qr code
10. This will give you the flag
</details>
