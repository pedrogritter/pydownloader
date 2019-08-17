__author__ = "Pedro Gritter"
__email__ = "pedro12345g@gmail.com"
__maintainer__ = "Pedro Gritter"
__version__ = "1.0"

from pytube import YouTube
from pytube import Playlist
from pydub import AudioSegment
import argparse, time
#from general import append_to_file


#### Functions ###

def choose_download(youtube):
    streamFormat = int(input("Insert the itag number: "))
    stream = youtube.streams.get_by_itag(streamFormat)
    filesize = stream.filesize


    if args.verbose:
        print(" ")
        print('Download started... \n')
        print(" ")
        print("Download details:\n")
        print("Name:"+ str(stream.default_filename)+"\n")
        print("Size:" + str(round(stream.filesize/(1024*1024),2)) + 'MB\n')
        print(" ")
        print("Wait...")
        print(" ")


    dl_start = time.time()
    stream.download()
    dl_end = time.time()
    dl_totaltime = dl_end - dl_start

    print("Download Finished!")

    if args.verbose:
        print("In: " + str(round(dl_totaltime/60, 2)) + "minutes")

    if args.audio:
        print("Do you wish to convert your webm audio file?")
        conversion = input("Press enter to skip or (y) to convert:")
        if conversion:
            try:
                sound = AudioSegment.from_file(str(stream.default_filename))
                file_handle= sound.export(str(stream.default_filename[:-5])+".mp3", format="mp3")
                print("Conversion Done!\n")
            except e:
                print(e)

parser = argparse.ArgumentParser(description='List & Download available YouTube streams')
#Main arguments (mutual exclusive)
group = parser.add_mutually_exclusive_group()
group.add_argument('-v', '--video', action="store_true", help="Choose to get video streams")
group.add_argument('-a', '--audio', action="store_true", help="Choose to get audio streams")
group.add_argument('-p', '--playlist', action="store_true", help="Choose to get audio streams")
group.add_argument('-all', '--all', action="store_true", help="Choose to all get streams")

#Other Arguments
parser.add_argument('--verbose', action="store_true", help="Choose verbose mode")
parser.add_argument('url', nargs="*", help="Video or playlist URL")
args = parser.parse_args()



url = str(args.url)

# Searches for the video and sets up the callback to run the progress indicator.
try:
    youtube = YouTube(url)
except Exception as e:
    print("ERROR. Check your:\n  -connection\n  -url is a YouTube url\n\nTry again.")
    print(e)


try:
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

except Exception as e:
        print("ErrorDownloadVideo  |  " + str(youtube.title) + "-" + str(url))
        print(e)
