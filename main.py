import os
from pytube import YouTube
import subprocess
import re

def getVideo():
    try:
        video = YouTube(input("Please insert video URL: "))
        return video
    except:
        print("Invalid URL.")
        getVideo()

def getInfo():
    author = video.title.split('-')[0]
    author = author.strip(" ")
    title = video.title.split('-')[1]
    title = re.sub("[\(\[].*?[\)\]]", "", title)
    title = title.strip(" ")
    print("Downloading " + title + " by " + author)
    return author, title

def catalog():
    directory = os.getcwd()

    if os.path.exists(str(os.path.join(directory,  author))):
        saveDir = str(os.path.join(directory, author))
    elif os.path.exists(str(os.path.join(directory, author.upper()))):
        saveDir = str(os.path.join(directory, author.upper()))
    elif os.path.exists(str(os.path.join(directory, author.lower()))):
        saveDir = str(os.path.join(directory, author.lower()))
    elif os.path.exists(str(os.path.join(directory,  author.capitalize()))):
        saveDir = str(os.path.join(directory, author.capitalize()))
    else:
        os.makedirs(os.path.join(directory, author))
        saveDir = str(os.path.join(directory, author))

    print(saveDir)
    return saveDir

def download():

    stream = video.streams.first()
    stream.download(saveDir)


def convert():
    commandconv = "ffmpeg -i \"" + os.path.join(saveDir, re.sub("\.", "" , video.title)) + "\".* -ab 160k -ac 2 -ar 44100 -vn \"" + os.path.join(saveDir, title) + "\".mp3"
    commandrm = "rm \"" + os.path.join(saveDir, re.sub("\.", "" , video.title)) + "\".*"
    subprocess.call(commandconv, shell=True)
    subprocess.call(commandrm, shell=True)

video = getVideo()
author, title = getInfo()
saveDir = catalog()
download()
convert()
