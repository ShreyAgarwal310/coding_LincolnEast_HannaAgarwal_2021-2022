import tkinter
from PIL import Image, ImageTk
from io import BytesIO
import requests

window = tkinter.Tk()

url = "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/10/b9/03/73/entrance.jpg?w=1200&h=1200&s=1"
r = requests.get(url)

pilImage = Image.open(BytesIO(r.content))
pilImage = pilImage.resize((200, 200), Image.ANTIALIAS)

image = ImageTk.PhotoImage(pilImage)

label = tkinter.Label(image=image)
label.place(x=0, y=0)

window.mainloop()
