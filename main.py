import youtube_dl
from youtube_dl.utils import ytdl_is_updateable
import yt_dlp

links = open('links.txt', 'r')
urls = links.readlines()

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
print("Pilih opsi dibawah\n")
print("1) Download MP3")
print("2) Download MP4")

# TODO: ADD english Language
# TODO: ADD Download support for MP4
# TODO: Cleaning Code

while True:
    choice = input("> ")
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            print(input("Pastekan Link nya di file 'links.txt'\n Jika sudah klik Enter "))
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download(urls)
        elif choice == 2:
            print("Coming Soon :)")
            break
        else:
            print("Pilih 1 atau 2. Jangan pilih yang lain :3")
    else:
        print("Masukkan Nomer bro")
