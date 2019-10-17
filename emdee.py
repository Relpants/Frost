import requests
import hashlib
import re

# Things gathered:
# Underneath is a class called Session, If you need to fine-tune your
# control over how requests are being made or IMPROVE the PERFORMANCE of your requests
# you may need to use a Session instance directly.

# The reason the performance is improved is Sessions are used to persist parameters 
# across requests, each time you make a request with session, once it has been initialized with
# authentication credentials, the credentials will be persisted.
# When your app makes a connection to a server using a Session, it keeps that connection
# around in a connection pool. When you app wants to connect to the same server again, it
# will reuse a connection from the pool rather than establishing a new one

# Also hexdigest was needed instead of digest because the input expects a string
# digest returns a byte object 
# hexdigest returns a string object



url = "http://docker.hackthebox.eu:40439"  #URL


r=requests.session() 		#Create new session
out = r.get(url)			#HTTP GET
out = re.search("<h3 align='center'>.*</h3>",out.text)   #Grab the line that contains string to encode
out = re.search("[^<h3 align='center'>].*[^</h3>]",out[0])	#Grab just the string


m=hashlib.md5(out[0].encode('utf-8')).hexdigest()	# Create a md5 string from input
data = {'hash': m}				# How the data is past on inspection through developer window
r = r.post(url = url, data = data);	# Make the post
print(r.text)					# Grab the flag 





# Correct code above, difference being that using the session object in the post 
# Vs using a new requests object


"""
url = "http://docker.hackthebox.eu:40439"


r=requests.session()
out = r.get(url)
out = re.search("<h3 align='center'>.*</h3>",out.text)
out = re.search("[^<h3 align='center'>].*[^</h3>]",out[0])

m = hashlib.md5()
m.update(out[0].encode('utf-8'))
m = m.digest()
data = {'hash': m}
r = requests.post(url = url, data = data);

print(r.text)

"""