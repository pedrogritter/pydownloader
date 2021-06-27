import pytube

#Adding progress bar
#from pytube.cli import on_progress

url = 'https://www.youtube.com/watch?v=udwLcimxPNU'
#long_video_url= 'https://www.youtube.com/watch?v=1pqvY9Oh0tQ&t=609s'

# Using user given url
# print("Give URL:")
# url = input()

youtube = pytube.YouTube(url)

# With progress bar
#youtube = pytube.YouTube(long_video_url, on_progress_callback=on_progress)

# Get highest resolution stream
video = youtube.streams.get_highest_resolution()

# Video Information
video_title = video.title
video_size = str(round(video.filesize/(1024*1024),2))

print(f'Downloading - {video.title} - {video_size}MBs')

video.download() # In Same Folder
# or
# video.download('./Downloads') # In Other Folder
