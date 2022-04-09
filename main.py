import os
from tkinter import *

win = Tk()

p1 = PhotoImage(file="logo.png")
win.iconphoto(False, p1)

filePath_label = Label(win, text="File Path", font=("calibre", 20))
filePath_label.pack(pady=5, padx=5)
filePath_entry = Entry(win, width=50)
filePath_entry.pack(pady=5, padx=5)

fileName_label = Label(win, text="File Name", font=("calibre", 20))
fileName_label.pack(pady=5, padx=5)
fileName_entry = Entry(win, width=50)
fileName_entry.pack(pady=5, padx=5)

title_label = Label(win, text="Title", font=("calibre", 20))
title_label.pack(pady=5, padx=5)
title_entry = Entry(win, width=50)
title_entry.pack(pady=5, padx=5)

link_label = Label(win, text="Link", font=("calibre", 20))
link_label.pack(pady=5, padx=5)
link_entry = Entry(win, width=50)
link_entry.pack(pady=5, padx=5)


def manipulate(title, link):
    link = str(link) + "&modestbranding=1&rel=0"
    data = f'''<!DOCTYPE html>
<html style="text-align: center;" style="background-color: yellow">
<head>
    <title style="text-align: center;" style="color: green">{title}</title>
</head>
<body style="background-color:black;">
        <iframe width="1900" height="941" src="{link}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</body>
</html>'''
    return data


def writeHTML(fileLoc, title, link):
    file = open(fileLoc, "w")
    data = manipulate(title, link)
    file.write(data)
    file.close()
    finalFileLoc = fileLoc[:-4] + ".html"
    os.rename(fileLoc, finalFileLoc)
    return finalFileLoc


def submit():
    filePath = filePath_entry.get()
    fileName = fileName_entry.get()
    fileLoc = filePath + "\\" + fileName + ".txt"
    title = title_entry.get()
    link = link_entry.get()
    location = writeHTML(fileLoc, title, link)

    def fileOpen():
        os.startfile(location)

    openButton = Button(win, text="Open", font=("calibre", 20), command=fileOpen)
    openButton.pack(pady=5, padx=5)


submitButton = Button(win, text="Enter", font=("calibre", 20), command=submit)
submitButton.pack(pady=5, padx=5)
win.mainloop()
