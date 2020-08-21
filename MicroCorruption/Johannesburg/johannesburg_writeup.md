# Whitehorse
## Completed 8/21/20
###### Flag: 1a1a1a1a1b1b1b1b1c1c1c1c1d1d1d1d8081824644
- convert to hex
- 16 garbage characters


# Functions
    unlock_door - 0x4446
    test_password_valid - 0x4452
    login - 0x452c
    strcpy - 0x4624

# Solution
This challenge introduced the concept of a canary value. Namely a value that is placed in memory and checked to make sure it is not be overwritten. In this case the developers aimed to make sure someone did not attempt to overflow the input password. Unfortunately, you can easily bypass this by making sure the address in memory where the canary resides stays the same. Once this part has been figured out it is a simple matter of jumping to the correct point in memory namely the <unlock_door> function. This jump like previous challenges is done at the end of the program when it attempts to jump to the "kill" function.



## Dissasembly

    <placeholder>





## Memory Dump

    <placeholder>


