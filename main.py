import subprocess
#
links = open('links.txt', 'r')
# # with open('links.txt', 'r') as file:
#     # print(file.readlines())
#
urls = links.readlines()
#
for url in urls:
    subprocess.call(['youtube-dl', '-x', '--audio-format', 'mp3', '-o', '%(title)s.%(ext)s', url])

# from pytube import YouTube

#list of URLs

# from yt_dlp import *
#
# #list of URLs
#
# urls = links.readlines()
# links = open('links.txt', 'r')
#
# for url in urls:
#     yt_dlp.downloader(url, format='mp3')
