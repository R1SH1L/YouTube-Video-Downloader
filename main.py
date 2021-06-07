from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

root = Tk()                                                                                                             # Creates window.
root.title('YouTube Video Downloader - By Rishil')                                                                      # Sets window title.
root.geometry('400x400')                                                                                                # Sets dimensions of window to 400 pixels by 400 pixels.
root.columnconfigure(0, weight = 1)                                                                                     # Centers everything.

# "Video URL" Label
url_label = Label(root, text='Video URL:', fg = 'Blue', font=('Arial', 14))                                             # Video URL label.
url_label.grid()                                                                                                        # Adding video url label to the GUI.

# Video url that gets inputted.
url = StringVar()                                                                                                       # Setting video url to string.
url_box = Entry(root, width = 50, textvariable = url)                                                                   # Creating entry box.
url_box.grid()                                                                                                          # Adding entry box to the GUI.

# Error Message for Video URL
url_error = Label(root, text = 'Error', fg = 'Red', font = ('Arial', 10))
url_error.grid()

# "Save Video" Label
save_label = Label(root, text='Save Location:', fg = 'Blue', font = ('Arial', 14))                                      # Save Video label.
save_label.grid()                                                                                                       # Adding save video label to the GUI.

# Choose Path Button
path_button = Button(root, width = 10, bg = 'Red', fg = 'White', text = 'Choose Path')
path_button.grid()

# Error Message for Path Choosing
path_error = Label(root, text = 'Error of Path', fg = 'Red', font = ('Arial', 10))
path_error.grid()


download_quality = Label(root, text = 'Select Video Quality:', fg = 'Blue', font = ('Arial', 14))
download_quality.grid()



root.mainloop()
