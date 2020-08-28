# Whitehorse
## Completed 8/21/20
###### Flag: xxxxxxxxxxxxxxxx30127f00b0123245583a
- convert to hex
- 16 garbage characters
- #0x3012 - "push"
- #0x7f00 - Value supplied to interrupt that unlocks door
- #0xb012 - call
- #0x3245 - #0x4532 <INT>
- #0x3a58 - area in memory to return @, to call the injected code

# Functions
    coditional_unlock_door - 0x4446
    login - 0x44f4

# Solution
This challenge once again looks at the 8-16 password. However, this challenge requires use of both an overflow and injection of code. Stepping through this program a couple times it becomes pretty apparent that once again overflowing the input password by two characters gives us free reign to any memory location in the program.



    3a60:   3c44 0000 0000 0000   <D......

Specifically, this location is what needs to be replaced, because it will return us to 443c which kills the program. However, even doing this one begins to notice from code execution and the name of the function that the unlock_door function will not unconditionally unlock the doors for us. This part led me to believe that perhaps code injection was require. Thinking about it for a bit I remebered that passing the value #0x7f in the <INT> function will always unlock the door. Looking at the program I narrowed in on a chunk of memory that just through a minor edit I could possibly achieve what I wanted.



## Dissasembly

    445c:  3012 7e00      push	#0x7e

    4460:  b012 3245      call	#0x4532 <INT>

Simply changing #0x7e00 -> #0x7f00 should produce the flag. With this in mind the only place ofcourse I could inject the code was from user input. I would also have to return to that area in the code to begin the execution. As a result my complete injection code and overflow was the following.





## Memory Dump

    3a50:   1111 1111 1111 1111   ........

    3a58:   3012 7f00 b012 3245   0....2E

    3a60:   583a 0000 0000 0000   X:......
 

With this complete the code would attempt to kill the program at the last return statement but instead return to memory location #0x3a58 which is where my custom asm code resided calling the unlock door function with the value that would indeed unconditionally unlock the challenege. 


