import os
import pygame
from tkinter import *
from tkinter.filedialog import askdirectory
from mutagen.id3 import ID3
from PIL import Image, ImageTk


def stop():
    pygame.mixer.music.pause()
    pygame.mixer.music.unpause()

def nextsong():
    global index
    index += 1
    pygame.mixer.music.load(listsongs[index])
    pygame.mixer.music.play()

def prevsong():
    global index
    index-=1
    pygame.mixer.music.load(listsongs[index])
    pygame.mixer.music.play()


def playmusic():
    pygame.mixer.music.play()

# def chooseDir2():
#     global listbox
#     global realname
#     chooseDir()
#
#     listbox.update()



listsongs=[]
realname=[]

index=0
def chooseDir():
    dir=askdirectory()
    os.chdir(dir)
    for files in os.listdir(dir):
        if files.endswith(".mp3"):

            realdir=os.path.realpath(files)
            audio=ID3(realdir)
            realname.append(audio['TIT2'].text[0])
            listsongs.append(files)

    pygame.mixer.init()
    pygame.mixer.music.load(listsongs[0])

    # pygame.mixer.music.play()
    #


root=Tk()



# path="C:/Users/vicky/PycharmProjects/Music Player"

img=Image.open("12.png")
img2=img.resize((30,20),Image.ANTIALIAS)
img3=ImageTk.PhotoImage(img2)

root.geometry("344x350")
root.title("Music Player")
root.wm_iconbitmap("1.ico")


chooseDir()

label=Label(root, text="MusicPlayer")
label.pack()

listbox=Listbox(root)

realname.reverse()
for item in realname:
    listbox.insert(0,item)
listbox.pack()



playbutton=Button(root,image=img3, text="Play Song",relief=FLAT, command=playmusic).pack()
nextbutton=Button(root, text="Next Song", command=nextsong).pack()
prevbutton=Button(root, text="Prev Song",command=prevsong).pack()

pausebutton=Button(root, text="Pause Song", command=stop).pack()

opendir=Button(root, text="Open Directory").pack()








root.mainloop()