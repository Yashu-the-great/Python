from pytube import YouTube
from moviepy.editor import *
import os

song_path = "/Downloads/"
def download(url:str):
    # song_path = "./music/"
    count = 0
    YouTube(url).streams.first().download(song_path)
    
def convert_to_mp3():
    for e in os.listdir(song_path):
        count = count + 1
        f =e.split(".")
        f = f[len(f)-1]
        if f =="mp4":
            print(e)
            video = VideoFileClip(song_path+e)
            f = e.split(".")
            f.remove("mp4")
            f.append(".mp3")
            s = ""
            f =s.join(f)
            video.audio.write_audiofile(song_path+f)
            os.remove(song_path+e)
        if count == len(os.listdir(song_path)):
            print("No mp4 file.")
    
if __name__ == "__main__":
    while True:
        url = input("Enter the youtube URL")
        download(url)
        # uncomment the line below if you want to download a mp3 file
        # convert_to_mp3()

