from pytube import Playlist
from sys import argv

link = argv[1]
p = Playlist(link)
print(f"Downloading: {p.title}")

for video in p.videos:
    video.streams.first().download("/home/pain/Videos")