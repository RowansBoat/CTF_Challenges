### Name

Operators Lock


### Description

```
You decided to investigate further into what caused this meltdown. In all the destruction you managed to find an android phone used by one of the engineers. The device is locked with a pattern, but you successfully extracted the gesture.key file. All you need to do now is decode it.
Flag Format : Put the decoded gesture.key inside CTF{}
```


### Difficulty

Easy


### Kind

Misc


### Author

Rowan


### Notes

Pyhton script gesturemaker.py creates the required file and was not given to users.


### Flag
<details>`CTF{6304258}`</details>

### Solution
<details>1. User first recognizes that this is a Android Gesture Password
2. User then uses a gesture pattern decoder to get password such as this https://github.com/jzyra/DecodeAndroidGesture/tree/master
3. For that link just download the jar then run the following command
4. java -jar DecodeAndroidGesture.jar gesture.key</details>

### Flag
<details>`CTF{6304258}`</details>
