# Cusco
## Completed 8/20/20
###### Flag: 1234567812345678FD 
- F = 46, D = 44 -> 0x4644 -> <unlock_door>

# Functions
    unlock_door - 0x4446
    test_password_valid - 0x4452
    login - 0x4500

# Solution
This challenge involved performing a buffer overflow, to make a return to a custom address. In this challenge no the password is listed to be only 8-16 characters long. No matter what password you put the program will produce an incorrect password and exit. However in the login function the add instruction to the sp by #10 can point the sp to a custom target if you overflow the password by 2 characters. Again, in this case we want to point it at the add 0x4446 which is the "unlock door" function



## Dissasembly
    453a:  3150 1000      add	#0x10, sp
    453e:  3041           ret
    
@ This point sp points to 43ee


## Memory Dump

    43e8:   ee43 3000 1e45 3132   .C0..E12

    43f0:   3334 3536 3738 3132   34567812

    43f8:   3334 3536 3738 4644   345678FD





After instruction at 453a, sp now points to 43fe. The memory dump at this location is 0x4446 and the instruction that is executed is ret so we execute ret #0x4446 which jumps to the unlock door function


