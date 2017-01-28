import bs4 as bs
import urllib.request
import re
import os

try:
    os.mkdir("myImages")
except Exception:
    pass

"""Fake headers for the website"""
headers = {}
headers["User-Agent"] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

backgroundTheme = input("Inser favorite background theme: ")
url = 'https://www.pexels.com/search/' + str(backgroundTheme)

#Creating a request to the website with fake headers.
req = urllib.request.Request(url, headers=headers)
raw_sauce = urllib.request.urlopen(req) #opens url
sauce = raw_sauce.read() #reads url source
soup = bs.BeautifulSoup(sauce, features="lxml") #creates bs4 object

#Slice for images
pattern = r"/photo/"

for url in soup.find_all("a"):
    imgsUrls = url.get("href")

    if str(type(imgsUrls)) == "<class 'NoneType'>": pass
    else:
        if re.match(pattern, imgsUrls):
            with open("photoUrls.txt", "a") as f:
                f.write(imgsUrls + "\n")


def imageDownload(url,name):
    urllib.request.urlretrieve(url,name)

if __name__ == "__main__":
    pass


#with open("source.txt", "w", encoding="utf-8") as f:
#    f.write(sauce_string)




