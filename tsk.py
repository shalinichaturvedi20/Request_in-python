import requests
from bs4 import BeautifulSoup
  
URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL)
print(r)

# soup = BeautifulSoup(r.content,"html.parser")
# print(soup)


