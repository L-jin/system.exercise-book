#cf) wikipedia 

#!/usr/bin/env python3
# Anchor extraction from HTML document
from bs4 import BeautifulSoup
from urllib.request import urlopen
with urlopen('웹주소') as response:
    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.find_all('조건'):
        print(anchor.get('', ''))
