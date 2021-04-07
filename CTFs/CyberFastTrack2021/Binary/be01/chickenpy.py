import re
import zlib

pdf = open("chicken.pdf", "rb").read()
stream = re.compile(rb'.*?FlateDecode.*?stream(.*?)endstream', re.S)
count = 0
for s in stream.findall(pdf):
	if(count < 550559):
		s = s.strip(b'\r\n')
		try:
			print(zlib.decompress(s))
			print("")
		except:
			pass
	count = count + 1