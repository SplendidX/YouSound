import os
from pytube import YouTube
import subprocess
import re

#GetVideo class creates YouTube object from given URL, then performs simple actions to determine the author and title.
class GetVideo:
    def __init__(self):
        self.video = input("Please insert video URL: ")
        self.getobject()
        self.getinfo()

#If user types 'stop', the script quits. If the URL can't be used for creation of YouTube object, it prompts user to enter correct URL.
    def getobject(self):
        try:
            if self.video == "stop":
                exit()
            else:
                self.video = YouTube(self.video)
        except:
            print("Invalid URL.")
            self.getobject()

    """
    If there is '-' symbol in the video title, then it's split to get author and title of the song.
    If there is no '-' symbol, whole video title is used for the song (script output) title.
    getinfo method also cleans the title from unwanted symbols and strings like text in brackets
    """
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


#Checks if there already is a directory for specified artist, if not, creates it and makes it download directory for the song
#If there is no author, check if there is NONAME directory, if not, crates it and makes it download directory for the song
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



#Takes the first stream possible and downloads it as a multimedia (video) file
def download():

    stream = ytobject.video.streams.first()
    stream.download(saveDir)


""" Uses shell commands to extact the audio from multimedia file downloaded by function download() based on the
    directory taken from function catalog(), and video object title (not title modified in getinfo method, as it is NOT
    used as the downloaded clip name).
    
    Uses rm shell command to remove the clip. After extracting the audio it is no longer needed.
"""
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

