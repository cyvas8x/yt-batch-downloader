import youtube_dl

links = open("links.txt", "r")
urls = links.readlines()


def download_mp3():
    with youtube_dl.YoutubeDL(mp3) as ydl:
        ydl.download(urls)


mp3 = {
    "format": "bestaudio/best",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
}

mp4 = {
    "format": "bestvideo+bestaudio/best",
    "postprocessors": [
        {
            "key": "FFmpegVideoConvertor",
            "preferedformat": "mp4",
        }
    ]
}


def download_mp4(resolution):
    resolutions = {"1": 360, "2": 420, "3": 720}
    if resolution not in resolutions:
        print("Invalid resolution option. Please choose one of the following: 1, 2, 3.")
        return
    format_option = f"mp4[height={resolutions[resolution]}]"
    ydl_opts = {"format": format_option}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(urls)


def download_mp4_best():
    format_option = "bestvideo+bestaudio/best"
    ydl_opts = {"format": format_option}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(urls)


print("Pilih opsi dibawah\n")
print("1) Download MP3")
print("2) Download MP4")

# TODO: ADD english Language
# TODO: ADD Download support for MP4
# TODO: Cleaning Code
# FIXME: Add support for MP4


while True:
    choice = input("> ")
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            print(
                input("Pastekan Link nya di file 'links.txt'\n Jika sudah klik Enter ")
            )
            download_mp3()
        elif choice == 2:
            print("Masih dalam pengembangan")
            exit()
            # print(
            #     input("Pastekan Link nya di file 'links.txt'\nJika sudah klik Enter ")
            # )
            # print(
            #     "\nSekedar info, Contoh Jika Resolusi 720 tidak ada maka akan otomatis memilih resolusi terbaik"
            # )
            # print("Choose a resolution option:")
            # print("1) 360")
            # print("2) 420")
            # print("3) 720")
            # resolution = input()
            # download_mp4(resolution)
        else:
            print("Pilih 1 atau 2. Jangan pilih yang lain :3")
    else:
        print("Masukkan Nomer bro")
