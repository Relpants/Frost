# bm03 - Medium


## Walkthrough

Execute program flag gets mentioned that its "cutoff" and that only part of it
is showing. Most likely a patch, or manipulation in the binary just like the previous challenge.
Fire up ghidra once again and immediately see the function that is needed to be manipulated. 
The function does some string manipulation and some other stuff, but honestly we dont care about any of that stuff
because depending on the row value will determine if you get the flag correctly or not. I figure
at this point its a worth while rabbit hole to go down, and this time im in luck as debug symbols are present
which makes editing that value trivial. Sure enough setting the rows value to be what the IF statement is looking 
for prints out the flag.