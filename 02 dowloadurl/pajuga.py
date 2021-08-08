import pafy
import os
#pafy.set_api_key("")

def create_folder(download):
    try:
        os.mkdir(download)
    except OSError:
        print("La creación del directorio  falló" + download)
    else:
        print("Se ha creado el directorio:" + download)

def download_audio(video,download):
    bestaudio = video.getbestaudio()
    bestaudio.download(filepath = download,quiet=False)
    print("Se ha descargado el archivo")
       
def get_url():
    print("enter url")
    uurl = input()
    return uurl

def download_track(download):
    user_url = get_url()
    video = pafy.new(user_url)
    print (video.title)
    download_audio(video,download)


download = "./download/"
create_folder(download)

while True:
    download_track(download)


