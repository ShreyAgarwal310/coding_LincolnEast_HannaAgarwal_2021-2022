import tkinter
from PIL import Image, ImageTk
from io import BytesIO
import requests

window = tkinter.Tk()

url = "https://s.yimg.com/os/weather/1.0.1/shadow_icon/60x60/partly_cloudy_night@2x.png"
r = requests.get(url)

pilImage = Image.open(BytesIO(r.content))
pilImage.mode = 'RGBA'
pilImage = pilImage.resize((200, 200), Image.ANTIALIAS)

image = ImageTk.PhotoImage(pilImage)

label = tkinter.Label(image=image)
label.place(x = 400, y = 400)
label.image = image

window.mainloop()
