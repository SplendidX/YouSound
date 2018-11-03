import os
from pytube import YouTube
import subprocess
import re


class GetVideo:
    def __init__(self):
        self.video = input("Please insert video URL: ")
        self.getobject()
        self.getinfo()

    def getobject(self):
        try:
            if self.video == "stop":
                exit()
            else:
                self.video = YouTube(self.video)
        except:
            print("Invalid URL.")
            self.getobject()

    def getinfo(self):
        if "-" in self.video.title:
            self.author = self.video.title.split('-')[0]
            self.author = self.author.strip(" ")
            self.title = self.video.title.split('-')[1]
            self.title = re.sub("[(\[].*?[)\]]", "", self.title)
            self.title = self.title.strip(" ")
        else:
            self.title = self.video.title
            self.title = re.sub("[(\[].*?[\)\]]", "", self.title)
            self.title = self.title.strip(" ")



def catalog():
    directory = os.getcwd()

    if "-" in ytobject.video.title:

        if os.path.exists(str(os.path.join(directory,  ytobject.author))):
            saveDir = str(os.path.join(directory, ytobject.author))

        elif os.path.exists(str(os.path.join(directory, ytobject.author.upper()))):
            saveDir = str(os.path.join(directory, ytobject.author.upper()))

        elif os.path.exists(str(os.path.join(directory, ytobject.author.lower()))):
            saveDir = str(os.path.join(directory, ytobject.author.lower()))

        elif os.path.exists(str(os.path.join(directory,  ytobject.author.capitalize()))):
            saveDir = str(os.path.join(directory, ytobject.author.capitalize()))

        else:
            os.makedirs(os.path.join(directory, ytobject.author))
            saveDir = str(os.path.join(directory, ytobject.author))
    else:
        if os.path.exists(str(os.path.join(directory,  "NONAME"))):
            saveDir = str(os.path.join(directory, "NONAME"))
        else:
            os.makedirs(os.path.join(directory, "NONAME"))
            saveDir = str(os.path.join(directory, "NONAME"))

    print(saveDir)
    return saveDir




def download():

    stream = ytobject.video.streams.first()
    stream.download(saveDir)



def convert():

    commandconv = "ffmpeg -i \"" + os.path.join(saveDir, re.sub("\.", "" , ytobject.video.title)) + "\".mp4 -ab 160k -ac 2 -ar 44100 -vn \"" + os.path.join(saveDir, ytobject.title) + "\".mp3"
    commandrm = "rm \"" + os.path.join(saveDir, re.sub("\.", "" , ytobject.video.title)) + "\".mp4"
    subprocess.call(commandconv, shell=True)
    subprocess.call(commandrm, shell=True)



while True:
    ytobject = GetVideo()
    saveDir = catalog()
    download()
    convert()
