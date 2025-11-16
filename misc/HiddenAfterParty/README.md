
### Name

Hidden Afterparty

### Description

```
Looks like you weren't invited to the true afterparty. There's a locked photo album but only people who went have access to it. Can you crack it open and figure out which club they went to?
Flag format : CTF{} and Replace any space with "_"
```

### Difficulty
Medium

### Flag
<details>CTF{TANTRA_TOKYO}</details>

### Solution
<details> Use a zip cracker tool to break the password on the zip file (named "AfterPartyPhotos.zip"). The password is “boil”. Extract the image from the zip file. Use a steganography tool (https://stylesuxx.github.io/steganography/) to extract hidden morse code from the image. Translate the morse code you get from the website when decoded to get coordinates. Navigate to the coordinates on google maps which points to a club which is the flag.
</details>
