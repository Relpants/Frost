import requests
import hashlib
import re


url = "http://docker.hackthebox.eu:40443/api/action.php?Parameter=_admin"


r=requests.session()

r = r.get(url = url);
print(r.text)