# pydownloader
Video dowloader and audio converter using the Pytube & Pydub. 

### Requirements
1. Ffmpeg  - Video & Audio Converter - [ffmpeg documentation](https://ffmpeg.org/documentation.html)
2. Pytube  -  A lightweight library for downloading YouTube Videos. - [pytube documentation and usage examples](https://python-pytube.readthedocs.io/en/latest/)
3. Pydub   - Manipulation  of audio on a high level interface - [pydub github & API Markdown](https://github.com/jiaaro/pydub/blob/master/API.markdown)

Installing the required depencies by running:

```
# Update dependency list

sudo apt-get update

# Install converter

sudo apt install ffmpeg

# Install required python packages

pip3 install -r requirements.txt
```

### Usage 

```
usage: downloader.py [-h] [-v | -a | -p | -all] [--verbose] [url [url ...]]

List & Download available YouTube streams

positional arguments:
  url             Video or playlist URL

optional arguments:
  -h, --help      show this help message and exit
  -v, --video     Choose to get video streams
  -a, --audio     Choose to get audio streams
  -p, --playlist  Choose to get audio streams
  -all, --all     Choose to all get streams
  --verbose       Choose verbose mode
```


