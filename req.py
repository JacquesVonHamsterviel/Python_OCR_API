import requests
import base64
import sys
url='http://127.0.0.1:5689'

img_path=sys.argv[1]

with open(img_path,'rb') as f:
    base64_img=base64.b64encode(f.read())
data={'img':base64_img,'lan':'ch'}
r=requests.post(url,data)
print(r.text)