
# New Orleans

#### Solved 8/12/20

#### Flag: B->Jr(q


## Functions
	-main
	-create_password
	-get_password
	-check_password

## General Writeup
	
Running the program and setting the breakpoints shows, that the program firsts does a call to create password. This function makes a 7 character password through a series of loads. Setting a break point after this function or just pausing the debugger shows the password that will be compared with the one from user input. In this case B->Jr(q, the function check_password will "loop" through each character in the password and will jmp if r14 = 0.


## Things of Note
As this is a primer for cleaning the rust off assembly some things to note.

	- mov #0x4142, r5
Means to move **Exactly** 0x4142 into the register r5
