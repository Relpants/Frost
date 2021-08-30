
# Reykjavik

#### Solved 8/30/21

#### Flag: ed8c


## Functions
	-main
	-enc


## General Writeup
Upon opening this challenge main calls what looks like an encryption function. Figuring out what the Enc function did took a sizeable amount of time. However, another call is made in main but it has no label. Based on previous challenges from this site and the function name Enc I took a guess that most likely after enc call some msp430 instructions would be "decrypted in memory". Furthermore setting a breakpoint at the end of the Enc label the password is never prompted until after, in this case being this "hidden" function that is decrypted from memory. To get a moderate feel for what was going on I set a couple break points in Enc and compared the memory dump before and after the function.


## Enc function

The first part of this function essentially counts up from 0-ff ( 100 ) and loads these values from memory locations `0x247d` -> `0x257d`.
Section of code that performs this.

<p align="center">
	<src="files/first.png">
</p>

And memory after this loop is finished

[first_memory](files/first_memory.png)

The next part of the function took me a little bit to understand what was going on and to be honest Im not exactly sure what it is doing other than
taking the memory location from the first step and doing some operations on the string shown below.

[second](files/second.png)

[second_string](files/second_string.png)

What did lead me to think this was just some operations being decrypted from memory is the at the beginning of `0x2470` there is a instruction `b012` 
which happens to be the call instruction in msp430. This seems plausible by the fact that the other function call in main is calling out to a memory location.

[second_memory](files/second_memory.png)

The last part of the encryption function appears to also be doing some xor operations with this same memory region. Specifically from main `0xf8` is loaded into r14 and this loop decrements r14 each iteration.

[third](files/third.png)

The output of this section of the code results in the memory region being the following.

[third_memory](files/third_memory.png)

Again, I notice a couple of what appears to be calls based on the Hex values `b012`.




## Call to 0x2400

Finally we get to the call to 0x2400. Like a previous challenge I solved on this site I stepped through this function a couple times to see 
where I thought it ended at and took that section of memory and threw it in ODA dissassembler. The output of that was the following

[hidden_function](hidden_function1.png)
[hidden_function](hidden_function2.png)

Essentially in closing there is a loop in this area of the code that prints out the string `what's the password?`. Once this is complete
it prompts the user for the password. but the most key component is at `0000048` where we ....

`cmp #0x8ced, 0xffdc`

What this is is actually the flag and its being compared to the password. With this in mind the solution is `ed8c` because of little endianness.

