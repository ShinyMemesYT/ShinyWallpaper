"""This file is to trow functions that improve user experience"""
import os
import random
from constants import *

def file_len(fileName):
    """Counts how many lines a file have"""
    with open(fileName) as m:
        for i, l in enumerate(m):
            pass
    return i + 1



def typeNone(object):
    if str(type(object)) == "<class 'NoneType'>":
        #Preventig imagePath from being a None type
        return True


def downloadCount():
    """Asks to the user how many wallpapers to download"""
    lineNum = file_len("photos-urls.txt")

    dwQuantity = int(input("\tYou have {0} wallpapers to download.\n\tHow many(num) :".format(lineNum)))

    while dwQuantity > int(lineNum) >= 0:
        dwQuantity = int(input("\tIt needs to be less than {} and more than 0 :".format(lineNum)))

    return dwQuantity

def linkUniq():
    """I have some kind of bug, links come duplicated"""
    with open("dw-links.txt", "r") as f:
        os.system("cat dw-links.txt | uniq > downloadeduniq.txt; rm dw-links.txt ; mv downloadeduniq.txt dw-links.txt")

def nameGenerator():
    fileName = []
    fileName.append("wallpaper-")
    for x in range(nameLength):
        unicodeNum = random.randrange(65,122) #A-z in unicode
        fileName.append(chr(unicodeNum))
    fileName.append(".jpeg")
    return fileName