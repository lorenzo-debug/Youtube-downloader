import tkinter
from tkinter import Listbox, Menu, OptionMenu, PhotoImage, Toplevel
from tkinter.constants import CENTER, E, NW, S, SE, SW
import pytube
from tkinter import filedialog
import os

# Creates the window
root = tkinter.Tk()
root.title("Youtube Downloader")
root.geometry("700x500+300+120")
Current = os.getcwd()
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file=f'{Current}/icons/yt-icon.png'))

# Creates the frames
frame = tkinter.Frame(root)
Qframe = tkinter.Frame(root)
Dframe = tkinter.Frame(root)
VPFrame = tkinter.Frame(root)
ResFrame = tkinter.Frame(root)
FFrame = tkinter.Frame(root)
ImgFrame = tkinter.Frame(root)
HFrame = tkinter.Frame(root)

# Creates things in the window
url = tkinter.Entry(frame, width=40, font=(25))

def clearf():
    [url.delete(0, tkinter.END) for url in frame.winfo_children() if isinstance(url, tkinter.Entry)]

label = tkinter.Label(frame, text="Enter the url", font=25)
clear = tkinter.Button(frame, text="Clear", command=clearf)
quitButton = tkinter.Button(Qframe, text="Quit", command=root.destroy)

# Creates a option menu with playlist mode and video mode
options = tkinter.StringVar(VPFrame)
modes = ["Video mode", "Playlist mode", "Audio mode", "Audio playlist"]
l2 = tkinter.Label(VPFrame, text="Select one mode:")
options.set("Video mode")
VideoOrPlaylist = OptionMenu(VPFrame, options, *modes)

# Creates a option menu for video resolutions
resolutionOpt = tkinter.StringVar(ResFrame)
resModes = ["Highest resolution", "1080", "720", "480", "360", "240", "144", "Lowest resolution"]
l3 = tkinter.Label(ResFrame, text="Select a resolution:")
resolutionOpt.set(resModes[0])
Resolution = OptionMenu(ResFrame, resolutionOpt, *resModes)

# Creates the function that catch a directory path
def saveFile():
    global filePath
    filePath = filedialog.askdirectory()
     
    if filePath != "":
        top = Toplevel(root)
        top.geometry("600x100+350+350")
        top.tk.call('wm', 'iconphoto', top._w, PhotoImage(file=f'{Current}/icons/folder.png'))
        frame = tkinter.Frame(top)
        l4 = tkinter.Label(frame, text=filePath)
        l5 = tkinter.Label(frame, text="Path was successfully selected")
        close = tkinter.Button(frame, text="Close", command=lambda: top.destroy())
        l5.grid(row=0)
        l4.grid(row=1)
        close.grid(row=2)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)

def showPath():
    top = Toplevel(root)
    top.geometry("600x100+350+350")
    top.tk.call('wm', 'iconphoto', top._w, PhotoImage(file=f'{Current}/icons/folder.png'))
    frame = tkinter.Frame(top)
    l4 = tkinter.Label(frame, text=filePath)
    l5 = tkinter.Label(frame, text="Path:")
    close = tkinter.Button(frame, text="Close", command=lambda: top.destroy())
    l5.grid(row=0)
    l4.grid(row=1)
    close.grid(row=2)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# Show the video's path
SFrame = tkinter.Frame(root)
spath = tkinter.Button(FFrame, text="Show file path", command=showPath)
spath.grid()

# Creates a button to catch a directory path
saveFileButton = tkinter.Button(FFrame, text="Path to save the file", command=saveFile)

def verf():
    # Download video
    if options.get() == "Video mode":
        def DownloadVideo():
            try:
                try:
                    VideoUrl = url.get()
                    yt = pytube.YouTube(VideoUrl)
                    if resolutionOpt.get() == "Highest resolution":
                        yt.streams.get_highest_resolution().download(filePath)
                    elif resolutionOpt.get() == "1080":
                        yt.streams.filter(res="1080p").first().download(filePath)
                    elif resolutionOpt.get() == "720":
                        yt.streams.filter(res="720p").first().download(filePath)
                    elif resolutionOpt.get() == "480":
                        yt.streams.filter(res="480p").first().download(filePath)
                    elif resolutionOpt.get() == "360":
                        yt.streams.filter(res="360p").first().download(filePath)
                    elif resolutionOpt.get() == "240":
                        yt.streams.filter(res="240p").first().download(filePath)
                    elif resolutionOpt.get() == "144":
                        yt.streams.filter(res="144p").first().download(filePath)
                    elif resolutionOpt.get() == "Lowest resolution":
                        yt.streams.get_lowest_resolution().download(filePath)
                    top = Toplevel()
                    frame = tkinter.Frame(top)
                    top.title("Video downloaded")
                    top.geometry("800x50+250+350")
                    top.tk.call('wm', 'iconphoto', top._w, PhotoImage(file=f'{Current}/icons/green-check.png'))
                    warning = tkinter.Label(frame, text=f"The video \"{yt.title}\" was downloaded on \"{filePath}\"")
                    close = tkinter.Button(frame, text="Close", command=lambda: top.destroy())
                    warning.grid(row=0, column=1)
                    close.grid(row=1, column=1)
                    frame.place(relx=0.5, rely=0.5, anchor=CENTER)
                except AttributeError:
                    top = Toplevel()
                    frame = tkinter.Frame(top)
                    top.title("Resolution error")
                    top.geometry("300x50+500+350")
                    top.tk.call('wm', 'iconphoto', top._w, PhotoImage(file=f'{Current}/icons/error.png'))
                    warning = tkinter.Label(frame, text="Error, please try another resolution")
                    close = tkinter.Button(frame, text="Close", command=lambda: top.destroy())
                    warning.grid(row=0, column=1)
                    close.grid(row=1, column=1)
                    frame.place(relx=0.5, rely=0.5, anchor=CENTER)
            except NameError:
                top = Toplevel()
                frame = tkinter.Frame(top)
                top.geometry("220x50+550+350")
                top.title("Error")
                top.tk.call('wm', 'iconphoto', top._w, PhotoImage(file=f'{Current}/icons/error.png'))
                warning = tkinter.Label(frame, text="Please enter the path of a folder")
                close = tkinter.Button(frame, text="Close", command=lambda: top.destroy())
                warning.grid(row=0, column=1)
                close.grid(row=1, column=1)
                frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        DownloadVideo()

    # Download playlist
    elif options.get() == "Playlist mode":
        try:
            def DownloadPlaylist():
                try:
                    try:
                        VideoUrl = url.get()
                        p = pytube.Playlist(VideoUrl)
                        if resolutionOpt.get() == "Highest resolution":
                            for video in p.videos:
                                video.streams.get_highest_resolution().download(filePath)
                        elif resolutionOpt.get() == "1080":
                            for video in p.videos:
                                video.streams.filter(res="1080p").first().download(filePath)
                        elif resolutionOpt.get() == "720":
                            for video in p.videos:
                                video.streams.filter(res="720p").first().download(filePath)
                        elif resolutionOpt.get() == "480":
                            for video in p.videos:
                                video.streams.filter(res="480p").first().download(filePath)
                        elif resolutionOpt.get() == "360":
                            for video in p.videos:
                                video.streams.filter(res="360p").first().download(filePath)
                        elif resolutionOpt.get() == "240":
                            for video in p.videos:
                                video.streams.filter(res="240p").first().download(filePath)
                        elif resolutionOpt.get() == "144":
                            for video in p.videos:
                                video.streams.filter(res="144p").first().download(filePath)
                        elif resolutionOpt.get() == "Lowest resolution":
                            for video in p.videos:
                                video.streams.get_lowest_resolution().download(filePath)
                        top = Toplevel()
                        frame = tkinter.Frame(top)
                        top.title("Playlist downloaded")
                        top.geometry("800x50+250+350")
                        top.tk.call('wm', 'iconphoto', top._w, PhotoImage(file=f'{Current}/icons/green-check.png'))
                        warning = tkinter.Label(frame, text=f"The playlist was downloaded on \"{filePath}\"")
                        close = tkinter.Button(frame, text="Close", command=lambda: top.destroy())
                        warning.grid(row=0, column=1)
                        close.grid(row=1, column=1)
                        frame.place(relx=0.5, rely=0.5, anchor=CENTER)
                    except AttributeError:
                        top = Toplevel()
                        frame = tkinter.Frame(top)
                        top.title("Resolution error")
                        top.geometry("300x50+500+350")
                        top.tk.call('wm', 'iconphoto', top._w, PhotoImage(file=f'{Current}/icons/error.png'))
                        warning = tkinter.Label(frame, text="Error, please try another resolution")
                        close = tkinter.Button(frame, text="Close", command=top.destroy())
                        warning.grid(row=0, column=1)
                        close.grid(row=1, column=1)
                        frame.place(relx=0.5, rely=0.5, anchor=CENTER)
                except NameError:
                    top = Toplevel()
                    frame = tkinter.Frame(top)
                    top.geometry("220x50+550+350")
                    top.title("Error")
                    top.tk.call('wm', 'iconphoto', top._w, PhotoImage(file=f'{Current}/icons/error.png'))
                    warning = tkinter.Label(frame, text="Please enter the path of a folder")
                    close = tkinter.Button(frame, text="Close", command=lambda: top.destroy())
                    warning.grid(row=0, column=1)
                    close.grid(row=1, column=1)
                    frame.place(relx=0.5, rely=0.5, anchor=CENTER)
            DownloadPlaylist()
        except KeyError:
            top = Toplevel()
            frame = tkinter.Frame(top)
            top.geometry("220x50+550+350")
            top.title("Mode error")
            top.tk.call('wm', 'iconphoto', top._w, PhotoImage(file=f'{Current}/icons/error.png'))
            warning = tkinter.Label(frame, text="Wrong mode")
            close = tkinter.Button(frame, text="Close", command=lambda: top.destroy())
            warning.grid(row=0, column=1)
            close.grid(row=1, column=1)
            frame.place(relx=0.5, rely=0.5, anchor=CENTER) 

    # Download the audio of the video
    elif options.get() == "Audio mode":
        def DownloadAudio():
            try:
                VideoUrl = url.get()
                yt = pytube.YouTube(VideoUrl)
                a = yt.streams.filter(only_audio=True).all()
                da = a[0].download(filePath)
                base, ext = os.path.splitext(da)
                new_file = base + '.mp3'
                os.rename(da, new_file)
                top = Toplevel()
                frame = tkinter.Frame(top)
                top.title("Audio downloaded")
                top.geometry("800x50+250+350")
                top.tk.call('wm', 'iconphoto', top._w, PhotoImage(file=f'{Current}/icons/green-check.png'))
                warning = tkinter.Label(frame, text=f"The audio of the video \"{yt.title}\" was downloaded on \"{filePath}\"")
                close = tkinter.Button(frame, text="Close", command=lambda: top.destroy())
                warning.grid(row=0, column=1)
                close.grid(row=1, column=1)
                frame.place(relx=0.5, rely=0.5, anchor=CENTER)
            except NameError:
                top = Toplevel()
                frame = tkinter.Frame(top)
                top.geometry("220x50+550+350")
                top.title("Error")
                top.tk.call('wm', 'iconphoto', top._w, PhotoImage(file=f'{Current}/icons/error.png'))
                warning = tkinter.Label(frame, text="Please enter the path of a folder")
                close = tkinter.Button(frame, text="Close", command=lambda: top.destroy())
                warning.grid(row=0, column=1)
                close.grid(row=1, column=1)
                frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        DownloadAudio()

    # Download the audio of the videos from a playlist
    elif options.get() == "Audio playlist":
        try:
            def PlaylistAudio():
                try:
                    VideoUrl = url.get()
                    p = pytube.Playlist(VideoUrl)
                    i = 0
                    for video in p.videos:
                        a = video.streams.filter(only_audio=True).all()
                        da = a[i].download(filePath)
                        base, ext = os.path.splitext(da)
                        new_file = base + '.mp3'
                        os.rename(da, new_file)
                        i += 1
                    top = Toplevel()
                    frame = tkinter.Frame(top)
                    top.title("Audio of the playlist")
                    top.geometry("800x50+250+350")
                    top.tk.call('wm', 'iconphoto', top._w, PhotoImage(file=f'{Current}/icons/green-check.png'))
                    warning = tkinter.Label(frame, text=f"The audio of the playlist was downloaded on \"{filePath}\"")
                    close = tkinter.Button(frame, text="Close", command=lambda: top.destroy())
                    warning.grid(row=0, column=1)
                    close.grid(row=1, column=1)
                    frame.place(relx=0.5, rely=0.5, anchor=CENTER)
                except NameError:
                    top = Toplevel()
                    frame = tkinter.Frame(top)
                    top.geometry("220x50+550+350")
                    top.title("Error")
                    top.tk.call('wm', 'iconphoto', top._w, PhotoImage(file=f'{Current}/icons/error.png'))
                    warning = tkinter.Label(frame, text="Please enter the path of a folder")
                    close = tkinter.Button(frame, text="Close", command=lambda: top.destroy())
                    warning.grid(row=0, column=1)
                    close.grid(row=1, column=1)
                    frame.place(relx=0.5, rely=0.5, anchor=CENTER)
            PlaylistAudio()
        except KeyError:
            top = Toplevel()
            frame = tkinter.Frame(top)
            top.geometry("220x50+550+350")
            top.title("Mode error")
            top.tk.call('wm', 'iconphoto', top._w, PhotoImage(file=f'{Current}/icons/error.png'))
            warning = tkinter.Label(frame, text="Wrong mode")
            close = tkinter.Button(frame, text="Close", command=lambda: top.destroy())
            warning.grid(row=0, column=1)
            close.grid(row=1, column=1)
            frame.place(relx=0.5, rely=0.5, anchor=CENTER) 


# Verify the function to download
downloadButton = tkinter.Button(Dframe, text="Download", command=verf)

# Help window and button
def helpf():
    Htop = Toplevel()
    Htop.tk.call('wm', 'iconphoto', Htop._w, PhotoImage(file=f'{Current}/icons/help-icon.png'))
    Htop.geometry("575x370+360+180")
    Htop.title("Help/Ajuda")
    my_Menu = Menu(Htop)
    Htop.config(menu=my_Menu)
    def english():
        frame = tkinter.Frame(Htop)
        frame.place(anchor=NW)
        lb1 = Listbox(frame, width=500, height=400)
        lb1.insert(0, "Buttons:")
        lb1.insert(1, "Download = Download the video or playlist or audio")
        lb1.insert(2, "Path to save the file = Select the folder to store the video or playlist")
        lb1.insert(3, "Quit = Close the program")
        lb1.insert(4, "Help/Ajuda = Open the help window")
        lb1.insert(5, "Clear = Clear video link inbox")
        lb1.insert(6, "Show file path = show the path to the folder you selected")
        lb1.insert(7, "----------------------------------------------------------------------------------------------------------------------------------------")
        lb1.insert(8, "Entries:")
        lb1.insert(9, "Enter the url = Link the video or playlist you want to download")
        lb1.insert(10, "----------------------------------------------------------------------------------------------------------------------------------------")
        lb1.insert(11, "Option menu:")
        lb1.insert(12, "Select one mode = Select which mode you want to download the video or the playlist")
        lb1.insert(13, "Select a resolution = Select the resolution you want to download the video")
        lb1.insert(14, "---------------------------------------------------------------------------------------------------------------------------------------")
        lb1.pack()
    english()
    def portuguese():
        frame = tkinter.Frame(Htop)
        frame.place(anchor=NW)
        lb1 = Listbox(frame, width=500, height=400)
        lb1.insert(0, "Botoes:")
        lb1.insert(1, "Download = Faz o download do video ou da playlist ou do audio")
        lb1.insert(2, "Path to save the file = Seleciona a pasta que vai guardar o video ou playlist")
        lb1.insert(3, "Quit = Fecha o programa")
        lb1.insert(4, "Help/Ajuda = Abre a janela de ajuda")
        lb1.insert(5, "Clear = Limpa a caixa de entrada do link do video")
        lb1.insert(6, "Show file path = mostra o caminho da pasta que voce selecionou")
        lb1.insert(7, "----------------------------------------------------------------------------------------------------------------------------------------")
        lb1.insert(8, "Entradas:")
        lb1.insert(9, "Enter the url = Colocar o link do video ou da playlist que quer fazer o download")
        lb1.insert(10, "----------------------------------------------------------------------------------------------------------------------------------------")
        lb1.insert(11, "Menu de opcoes:")
        lb1.insert(12, "Select one mode = Seleciona qual modo voce quer fazer o download do video ou da playlist")
        lb1.insert(13, "Select a resolution = Seleciona a resolucao que voce quer fazer o download do video")
        lb1.insert(14, "---------------------------------------------------------------------------------------------------------------------------------------")
        lb1.pack()
        
    file_menu = Menu(my_Menu)
    my_Menu.add_cascade(label="Languages/Idiomas", menu=file_menu)
    file_menu.add_command(label="Portugues", command=portuguese)
    file_menu.add_command(label="English", command=english)

help = tkinter.Button(HFrame, text="Help/Ajuda", command=helpf)
help.grid()

# Image
img = tkinter.PhotoImage(file=f'{Current}/icons/yt-image-small.png')
picTitle = tkinter.Label(ImgFrame, text="Youtube downloader", font=20)
picLabel = tkinter.Label(ImgFrame, image=img)
picTitle.grid()
picLabel.grid()

# Place the things in the window
label.grid(row=0)
url.grid(row=0, column=1, ipady=2.5)
clear.grid(row=0, column=2)
downloadButton.grid(row=1, column=1)
quitButton.grid(row=2, column=2)
l2.grid(row=0)
VideoOrPlaylist.grid(row=1)
l3.grid(row=0, column=1)
Resolution.grid(row=1, column=1)
saveFileButton.grid(row=2)

# Download button and url entry
frame.place(relx=0.5, rely=0.05, anchor=CENTER)
Dframe.place(relx=0.5, rely=0.17, anchor=CENTER)

# Quit button
Qframe.place(relx=1, rely=1, anchor=SE)

# Option menu video and playlist
VPFrame.place(rely=0.4, anchor=SW)

# Option menu resolution
ResFrame.place(relx=1, rely=0.32, anchor=E)

# Select path button
FFrame.place(relx=0.5, rely=1, anchor=S)

# Image frame
ImgFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

# Help button
HFrame.place(relx=0, rely=1, anchor=SW) 

# Loop until close the window 
root.mainloop()