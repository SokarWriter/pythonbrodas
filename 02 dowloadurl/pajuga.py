import pafy
pafy.set_api_key("")

url = "https://www.youtube.com/watch?v=XkvH7z4GxHM"
video = pafy.new(url)

print (video.title)

#print (video.rating)


#print (video.viewcount, video.author, video.length)


#print (video.duration, video.likes, video.dislikes)


#print(video.description)

streams = video.streams
for s in streams:
    print(s.resolution, s.extension, s.get_filesize(), s.url)

best = video.getbest()
print ("------------------------------------------------------------------------------")
filename = best.download(filepath = r"C:\Use-rs\marc\Downloads",quiet=False)

#bestaudio = video.getbestaudio()

#filename = bestaudio.download(filepath = r"C:\Use-rs\marc\Downloads")




