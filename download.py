from __future__ import unicode_literals
import youtube_dl

urls = []
with open('urls.txt') as f:
    urls = f.read().split()

file_name = '%(title)s.%(ext)s'
ydl_opts = {'outtmpl': './DOWNLOADED/' + file_name}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(urls)