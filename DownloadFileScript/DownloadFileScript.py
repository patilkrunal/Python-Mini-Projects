# save-webpage.py

import urllib.request, urllib.error, urllib.parse

url = input("Enter URL: ")
fn = input("Enter output filename: ")

response = urllib.request.urlopen(url)
webContent = response.read()

f = open(fn, 'wb')
f.write(webContent)
f.close