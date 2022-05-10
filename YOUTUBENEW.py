from pytube import YouTube
def downvid():
    global e1
    string1=e1.get()
    yt = YouTube(str(string1))
    videos = yt.streams.all()

    s = 1
    for v in videos:
        print(str(s)+". "+str(v))
        s += 1

    n = int(input("Enter the number of the video: "))
    vid = videos[n-1]

#def dest(vid):
    destination = str(input("Enter the destination: "))
    vid.download(destination)
    print("video successfully downloaded")



from tkinter import *
root=Tk()
title=Label(root,width=5,height=5,text="YOUTUBE DOWNLOADER",fg='red',bg='black')
title.pack(fill='x')
title1=Label(root,width=5,height=4,text="Enter the video link: ")
e1=Entry(root)
title1.pack(fill='x')
e1.pack(fill='x')
button=Button(root,width=5,height=4,text="DOWNLOAD",fg='blue',command=downvid)
button.pack(fill="x")
#title2=Label(root,width=5,height=5,text="ENTER THE DESTINATION",fg='red',bg='black')
#title2.pack(fill='x')
#e2=Entry(root)
#e2.pack(fill='x')
#button1=Button(root,width=5,height=4,text="DOWNLOAD",fg='blue',command=dest(vid))
#button1.pack(fill="x")
root.mainloop()







