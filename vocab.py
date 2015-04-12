from urllib.request import urlopen
import html2text
from bs4 import BeautifulSoup

def vocab():
    a = input("Please Enter a Word to Search : \n")
    data = a.encode('UTF-8') 
    f = urlopen('http://www.vocabulary.com/dictionary/%s' % a)
    soup = BeautifulSoup(f)
    a = soup.select(".short")
    b = a[0].get_text()
    print(b)
    print("\n")

while(1):
    vocab()


