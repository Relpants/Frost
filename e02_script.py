import subprocess
import os

#run program
proc = subprocess.Popen(["nc E02-target.allyourbases.co 8137"], stdout = subprocess.PIPE, shell = True)
#grab output
(out, err) = proc.communicate()
print(out)



#input back in