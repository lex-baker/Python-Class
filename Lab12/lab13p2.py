# Author: Lex Baker
# Date: 11/8/22
# Lab 13, Classes

import webbrowser
from time import sleep

# My implementation of the Song class and the PlaylistManager class

class PlaylistManager():
    def __init__(self):
        self.song_list = []
    
    def addSong(self, title, url, duration):
        self.song_list.append(Song(title, url, duration))

    def printAll(self):
        for song in self.song_list:
            song.printInfo()
    
    def playAll(self):
        for song in self.song_list:
            song.play()

    
class Song:
    def __init__(self, title, url, duration):
        self.title = title
        self.url = url
        self.duration = duration

    def printInfo(self):
        print(self.title, self.duration)
    
    def play(self):
        # open song via self.url
        webbrowser.open(self.url)
        time_split = self.duration.split(":")
        seconds = int(time_split[0]) * 60 + int(time_split[1])
        sleep(seconds)
        # sleep until song has ended
        print("I hope you enjoyed the song!")


def testSongPrintInfo():
    s1 = Song("Help - The Beatles","https://www.youtube.com/watch?v=2Q_ZzBGPdqE", "02:19")
    s1.printInfo()

def testSongPlay():
    s1 = Song("Help - The Beatles","https://www.youtube.com/watch?v=2Q_ZzBGPdqE", "02:19")
    s1.play()

def main():
    # testSongPrintInfo()
    # testSongPlay()


    # Instantiate PlaylistManager
    playlistMgr = PlaylistManager()
    keepGoing = ""
    while(keepGoing != "DONE"):

        # Ask for info about song
        title = input("Song title: ")
        url = input("YouTube video: ")
        duration = input("Video duration (MM:SS): ")

        ## TODO: Add the Song to the PlaylistManager
        playlistMgr.addSong(title, url, duration)

        keepGoing = input("Add another song? YES to continue, DONE to end: ")

    ## TODO: when done adding songs print all the songs
    playlistMgr.printAll()
    ## TODO: after printing all songs, play them all.
    playlistMgr.playAll()


if __name__ == "__main__":
    main()