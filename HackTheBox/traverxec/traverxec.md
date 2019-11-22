


Got shell with python code

copied linenum.sh onto box
	ran linenum and read type -f readable,executable,writeable

	enumerated

	noticed .htpasswd from readable

	contained hash for david

	used hash and passwd file with John 

		-obtained password

viewed the nostromo folder
	viewed nhttpd.conf

	lists david as directory

	public_www as sub directory

go to website

hit /~david/public_www/

	- use login credentials

using ls -la burrow down into a subfolder

	contains authorized_keys

	using the private key convert to john format

	obtain passphrase

ssh into box with private key and suplly passphrase

nest back into david folder and obtain user flag


#Root

enumerate

once again use read -type f -readable,writeable,executable

look at the bashscripts

nest down and view the log folder

execute server log

notice its run as root

	cat out the shell code

	cat out the shell codewithout "cat"

	view journalctnl

	bring up another shell and view with the script running and not

	see "pager" 

	execute pager

pager is an alias for less

use GTFOBin from less

obtain root shell

