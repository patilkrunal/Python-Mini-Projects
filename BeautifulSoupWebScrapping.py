# #! python3
# def function():
# 	print()
#
# if __name__ == '__main__':
# 	function()

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

def function(url):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    cnt = 0
    for tag in tags:
        if cnt == 17:
            url = tag.get('href', None)
            return url

        cnt += 1

if __name__ == '__main__':

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = 'http://py4e-data.dr-chuck.net/known_by_Alyia.html'

    for i in range(7):
        url = function(url)
        print(url)