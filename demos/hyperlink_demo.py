# Import the required libraries
from tkinter import *
import webbrowser

# Create an instance of tkinter frame
win = Tk()


def callback(url):
    webbrowser.open_new_tab(url)


link = Label(win, text="website.com", font=(
    'Helveticabold', 15), fg="blue", cursor="hand2")
link.pack()
link.bind("<Button-1>", lambda e:
          callback("https://www.youtube.com/watch?v=dQw4w9WgXcQ"))

win.mainloop()
