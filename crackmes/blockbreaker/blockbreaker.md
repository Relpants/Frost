# Blockbreaker

## Solved: 8/30/21

## Flag: homeisaperson

### Writeup
I began this challenge by going through the code and looking for function opcodes `55 89 E5` signifying a good chance of the beginning of a function.
However, this was not needed because the function that majority of the challenge comprised of was the following. 

<p align="center">
	<img src = "files/blockbreaker_code.png">
</p>
<p align="center">
	<img src = "files/blockbreaker_code2.png">
</p>

This challenge was a great exercise in endianness in ghidra. There is most likely better solutions I could do in defining the variables. I noticed that ultimately 
there is some XOR checking at the end of this block of code. It appears also to have this condition that alternates what "word" you xor the other string with. Based on the 
length its checking for earlier in this segment of code 15 characters or a pad with A. Some of the variables i believe were better represented as a single byte array. 
This cleanup I think also helped me wrap my head on the little endian memory mapping.


<p align="center">
	<img src = "files/blockbreaker_code3.png">
</p>


With this in mind the array your comparing to can really be thought of in this order

`0A 03 02 06 ` `02 11 13 15` `04 19 11 03` `01 22 2a`

with every 5 bytes xor with the world block/break. Specifically, based on how the checks are done the XOR can be thought of as



`0A 03 02 06 02` `11 13 15 04 19` `11 03 01 22 2a` 

^
`62 6c 6f 63 6b` `62 72 65 61 6b` `62 6c 6f 63 6b`


Giving us the final answer of



`homeisaperson`

<p align="center">
	<img src = "files/answer.jpg">
</p>

