import bs4 as bs
import urllib.request
import re
import os
import folderBot
from constants import *
from ordinaryFunctions import *

folderBot.init()

def userPreferences():
    """Use user input for retrieving desired background"""
    backgroundTheme = input("Inser favorite background theme: ")
    url = 'https://www.pexels.com/search/' + str(backgroundTheme)
    #todo: maybe write preferences in a file
    return url

url = userPreferences()

def webRequest(url):
    """Creates a request based in the url"""
    req = urllib.request.Request(url, headers=headers) #Creating a request
    raw_sauce = urllib.request.urlopen(req) #Opening url with created request
    sauce = raw_sauce.read() #Source code
    soup = bs.BeautifulSoup(sauce, features="lxml") #Creating BS4 object

    return soup

soup = webRequest(url)

#Finding all images in url affected by userPreferences
def imageScraping():
    for url in soup.find_all("a"):
        imageWebPath = url.get("href")

        if typeNone(imageWebPath): pass

        else:
            if re.match(pattern, imageWebPath):
            #Fieltering undesired links, and writting desired ones(wallpapers) in a file
                with open("photos-urls.txt", "a") as f:
                    f.write(wallpaperSite + imageWebPath + "\n")


def finalURL(downloadCount):
    with open("photos-urls.txt","r") as k:
        for x in range(downloadCount):

            downloadUrls = k.readline()
            soup = webRequest(downloadUrls)

            for actualURL in soup.find_all("a"):
                imageWebPath = actualURL.get("href")

                if typeNone(imageWebPath):
                    pass

                else:
                    if re.match(pattern2, imageWebPath):
                        # Fieltering undesired links, and writting desired ones(wallpapers) in a file
                        with open("dw-links.txt", "a") as f:
                            f.write(imageWebPath + "\n")


def imageDownloader(downloadCount):
    """"""
    with open("dw-links.txt","r") as m:
        for x in range(downloadCount):
            downloadUrls = m.readline()

            file_name = nameGenerator()
            file_name = "".join(file_name)
            print(file_name)
            os.system("wget -O {} {}".format(file_name, downloadUrls))
            os.system("mv wallpaper* myWallpapers/")


if __name__ == "__main__":
    imageScraping()
    dwQuantity = int(downloadCount())
    finalURL(dwQuantity)
    linkUniq()
    imageDownloader(dwQuantity)
    folderBot.quit()

"""Testing background changing functionality"""
    #imagepath = os.path.abspath("wallpaper-FJcVE.jpeg")
    #bkgr = input("Change background? (y/n)")
    #if bkgr == "y":
    #   os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri {0}".format(imagepath))


#command = "gconftool-2 --set /desktop/gnome/background/picture_filename --type string '/path/to/file.jpg'"
#status, output = commands.getstatusoutput(command)  # status=0 if success
#Setting wallpapers in windows
#import ctypes
#SPI_SETDESKWALLPAPER = 20
#ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, "image.jpg" , 0)"""


"""End of Testing background changing functionality"""


