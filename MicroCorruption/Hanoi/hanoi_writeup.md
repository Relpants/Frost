# Hanoi
## Completed 8/14/20
###### Flag: AAAAAAAAAAAAAAAA8c 
- just need 8c @ 0x2410

# Functions
    unlock_door - 0x4448
    test_password_valid - 0x4454
    login - 0x4520

# Solution
This challenge involves both making a viable password that is between 8-16 characters and beating a canary value at memory address 0x455a. Overall this challenge is pretty simple and after running the program a couple times we learn that <test_password_valid> essentially just verifies the password is between 8-16 characters, if not the program will hit the instruction.



    4548:  0f93           tst	r15

    454a:  0324           jz	$+0x8

    454c:  f240 a000 1024 mov.b	#0xa0, &0x2410





## Dissasembly

    455a:  f290 8c00 1024 cmp.b	#0x8c, &0x2410

    4560:  0720           jne	#0x4570 <login+0x50>





## Memory Dump

    2400:   8c8c 8c8c 8c8c 8c8c   ........

    2408:   8c8c 8c8c 8c8c 8c8c   ........

    2410:   8c8c 


Thus sending the password 'XXXXXXXXXXXXXXXX8c' will unlock the door as the memory add #2410 will contain the 8c that the cmp.b at #455a requires to login correctly.


