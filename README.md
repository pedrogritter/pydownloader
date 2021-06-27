# pydownloader
Video downloader and audio converter using the Pytube & Pydub.

### Requirements
1. Ffmpeg  - Video & Audio Converter - [ffmpeg documentation](https://ffmpeg.org/documentation.html)
2. Pytube  -  A lightweight library for downloading YouTube Videos. - [pytube documentation and usage examples](https://python-pytube.readthedocs.io/en/latest/)
3. Pydub   - Manipulation  of audio on a high level interface - [pydub github & API Markdown](https://github.com/jiaaro/pydub/blob/master/API.markdown)

Installing the required dependencies by running:

```
# Update dependency list

sudo apt-get update

# Install converter

sudo apt install ffmpeg

# Activate virtualenv and install required python packages:

source venv/bin/activate

python -m pip install -r requirements.txt

# or

pip3 install -r requirements.txt
```

### Usage

```
usage: downloader.py [-h] [-hr | -p | -v | -a] [--verbose] [url [url ...]]

List & Download available YouTube streams

positional arguments:
  url                Youtube Video URL or URLs

optional arguments:
  -h, --help         show this help message and exit
  -hr, --highres     Choose to get the highest resolution stream
  -p, --progressive  Choose to get progressive streams
  -v, --video        Choose to get video streams
  -a, --audio        Choose to get audio streams
  --verbose          Choose verbose mode
```
