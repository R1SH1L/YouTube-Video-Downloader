from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

root = Tk()                                                                                                             # Creates window.
root.title('YouTube Video Downloader - By Rishil')                                                                      # Sets window title.
root.geometry('400x400')                                                                                                # Sets dimensions of window to 400 pixels by 400 pixels.
root.columnconfigure(0, weight = 1)                                                                                     # Centers everything.

url_label = Label(root, text='Video URL:', font=('Arial', 14))                                                          # Video URL label.
url_label.grid()                                                                                                        # Adding video url label to the GUI.

url = StringVar()                                                                                                       # Setting video url to string.
url_box = Entry(root, width = 50, textvariable = url)                                                                   # Creating entry box.
url_box.grid()                                                                                                          # Adding entry box to the GUI.

root.mainloop()
