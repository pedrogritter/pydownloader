__author__ = "Pedro Gritter"
__email__ = "pedro12345g@gmail.com"
__maintainer__ = "Pedro Gritter"
__version__ = "2.0"

from pytube import YouTube
from pytube import Playlist
from pytube.cli import on_progress
from pydub import AudioSegment
import argparse, time

#### Downloader Helper Functions ###

def convert_audio(stream):
    """Given a video stream converts it to mp3."""

    try:
        print("Converting file to mp3...")
        sound = AudioSegment.from_file('./Downloads/' + str(stream.default_filename))
        file_handle= sound.export('./Downloads/' + str(stream.default_filename[:-5])+".mp3", format="mp3")
        print("Conversion Done!\n")
    except e:
        print(e)

def execution_time(start, finish):
    """Given the start and finish time of execution returns the total time in minutes"""

    time = finish - start
    return str(round(time/60, 2))

def download_highresolution(youtube):
    """Given a Youtube video downloads the stream with highest resolution"""

    stream = youtube.streams.get_highest_resolution()

    # Video Information
    video_title= str(stream.default_filename)
    video_size= str(round(stream.filesize/(1024*1024),2))

    if args.verbose:
        print(f'\nDownload started - {video_title} - {video_size}MB\n')

    # Download Video Stream -> Count download time
    start = time.time()
    stream.download('./Downloads')
    end= time.time()

    if args.verbose:
        print(f'\n\nDownload finished - in {execution_time(start, end)} minutes')


def choose_download(youtube):
    """Given a Youtube video it requests the user itag of the wanted stream and downloads it"""

    streamFormat = int(input("Insert the itag number: "))
    stream = youtube.streams.get_by_itag(streamFormat)

    # Video Information
    video_title= str(stream.default_filename)
    video_size= str(round(stream.filesize/(1024*1024),2))

    if args.verbose:
        print(" ")
        print('Download started... \n')
        print("Download details:\n")
        print("Name:"+ video_title +"\n")
        print("Size:" + video_size + 'MB\n')

    # Download Video Stream -> Count download time
    start = time.time()
    stream.download('./Downloads')
    end = time.time()

    print(f'\n\nDownload finished - in {execution_time(start, end)} minutes')

    if args.verbose:
        print("In: " + execution_time(start,end) + "minutes")

    if args.audio:
        print("Do you wish to convert your audio file to mp3 format?")
        conversion = input("Press enter to skip or (y) to convert:")
        if conversion:
            convert_audio(stream)

def no_control_args(args):
    """Returns True if the user did not include any control arguments in the command"""
    return args.highres == False and args.video==False and args.audio==False and args.progressive==False

## Main Downloader Script

parser = argparse.ArgumentParser(description='List & Download available YouTube streams')
#Main arguments (mutual exclusive)
group = parser.add_mutually_exclusive_group()
group.add_argument('-hr', '--highres', action="store_true", help="Choose to get the highest resolution stream")
group.add_argument('-p', '--progressive', action="store_true", help="Choose to get progressive streams")
group.add_argument('-v', '--video', action="store_true", help="Choose to get video streams")
group.add_argument('-a', '--audio', action="store_true", help="Choose to get audio streams")

#Other Arguments
parser.add_argument('--verbose', action="store_true", help="Choose verbose mode")
parser.add_argument('url', nargs="*", help="Youtube Video URL or URLs")
args = parser.parse_args()

# Searches for the video and sets up the callback to run the progress indicator.
for video in args.url:
    try:
        youtube = YouTube(video, on_progress_callback=on_progress)
        try:
            if args.highres:
                download_highresolution(youtube)

            if args.video:
                print('\nAvaliable Video Only Streams:')
                for stream in youtube.streams.filter(only_video=True):
                    print(stream)
                choose_download(youtube)

            if args.audio:
                print('\nAvaliable Audio Only Streams:')
                for stream in youtube.streams.filter(only_audio=True):
                    print(stream)
                choose_download(youtube)

            if args.progressive:
                print('\nAvaliable Video&Audio Streams:')
                for stream in youtube.streams.filter(progressive=True):
                    print(stream)
                choose_download(youtube)

            if no_control_args(args):
                print("Try again by choosing one of these options: -hr -p -a -v")

        except Exception as e:
                print("ErrorDownloadVideo  |  " + str(youtube.title) + "-" + str(url))
                print(e)

    except Exception as e:
        print("ERROR. Check your:\n  -connection\n  -url is a YouTube url\n\nTry again.")
