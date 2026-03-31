### Name

The Dean Scream

### Description

```
Previous eboard members were gathering some examples of campaign speeches. They an infamous example of what you definitely shouldn't do. Something seems slightly off about this video though? 
Note : Headphones are not required nor needed for this challenge. If you want to view the video you probably need VLC Media Player.
```

### Difficulty

Medium

### Kind

Forensics

### Flag
<details>
`CTF{Wh@T_N0T_to_D0}`
</details>

### How to solve
<details>
1. Realize that one of the frame looks completely different
2. Extract the frames with ffmpeg example below
3. ffmpeg -i TheDeanScream.avi.avi frames/frame%04d.png
4. Find frame0038.png which is the different one
5. Run zsteg on the frame or use another lsb program
6. zsteg frame0038.png
7. This also works -  https://stylesuxx.github.io/steganography/ 
</details>
