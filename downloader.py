__author__ = "Pedro Gritter"
__email__ = "pedro12345g@gmail.com"
__maintainer__ = "Pedro Gritter"
__version__ = "1.0"

from pytube import YouTube
from pytube import Playlist
import argparse, time

#### Functions ###

def choose_download(youtube):
    streamFormat = int(input("Insert the itag number: "))
    stream = youtube.streams.get_by_itag(streamFormat)

    if args.verbose:
        print('Download started... ')
        print(" ")
        print("Download details:")
        print("Name:"+ str(stream.default_filename))
        print("Size:" + str(stream.filesize) + " bytes")
        print(" ")
        print("Wait...")

    dl_start = time.time()
    stream.download()
    dl_end = time.time()
    dl_totaltime = dl_end - dl_start

    print("Download Finished!")

    if args.verbose:
        print("In: " + str(dl_totaltime) + "s")


parser = argparse.ArgumentParser(description='List & Download available YouTube streams')
#Main arguments (mutual exclusive)
group = parser.add_mutually_exclusive_group()
group.add_argument('-v', '--video', action="store_true", help="Choose to get video streams")
group.add_argument('-a', '--audio', action="store_true", help="Choose to get audio streams")
group.add_argument('-p', '--playlist', action="store_true", help="Choose to get audio streams")
group.add_argument('-all', '--all', action="store_true", help="Choose to all get streams")

#Other Arguments
parser.add_argument('--verbose', action="store_true", help="Choose verbose mode")
parser.add_argument('videos', nargs="*", help="Video or playlist URL")
args = parser.parse_args()


url = str(args.videos)
youtube = YouTube(url)

print('Avaliable Media Streams:')
if args.all:
    for stream in youtube.streams.all():
        print(stream)
    choose_download(youtube)

if args.video:
    for stream in youtube.streams.filter(only_video=True).all():
        print(stream)
    choose_download(youtube)

if args.audio:
    for stream in youtube.streams.filter(only_audio=True).all():
        print(stream)
    choose_download(youtube)
