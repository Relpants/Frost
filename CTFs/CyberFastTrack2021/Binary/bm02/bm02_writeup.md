# bm02 - Medium

## Walkthrough

Pulled this sucker up into ghidra. Look at main realize it just prints the message when running.
Obviously, means that we will have most likely a "flag" function that needs to be called, through
patching the binary. Sure enough the printFlag function exists and checks a parameter to see if its equal. 
A couple ways we could do this, either patching the IF statement or just setting that parameter to the value
the IF statement is looking for. In this case because ghidra has been giving me problems with exporting binaries.
I fired up GDB and through some tedious breakpoints was able to set the value of the memory location the parameter 
refers to. This didnt have debug symbols which made it a little bit harder than bm03.
