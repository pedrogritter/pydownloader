from pytube import YouTube
from pytube import Playlist
import argparse

#url = str(input('Insert the full video URL: '))

#url = "www.youtube.com/watch?v=l3tu7FEcYRg"
url = input("Video url: ")

print(url)

yt = YouTube(url)

print('Avaliable Media Formats')


for stream in yt.streams.all():
    print(stream)

streamFormat = int(input("Insert the itag number: "))

stream = yt.streams.get_by_itag(streamFormat)

print('Download started. Wait... ')

stream.download()
