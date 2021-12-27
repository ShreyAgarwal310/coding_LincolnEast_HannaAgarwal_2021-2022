import tkinter
from PIL import Image, ImageTk
from io import BytesIO
import requests

window = tkinter.Tk()

url = "https://lumiere-a.akamaihd.net/v1/images/cg_parks_wdw_50thcelebration_specialoffers_21943_25454ec0.jpeg?region=0,0,800,800"
r = requests.get(url)

pilImage = Image.open(BytesIO(r.content))
pilImage = pilImage.resize((200, 200), Image.ANTIALIAS)


image = ImageTk.PhotoImage(pilImage)

label = tkinter.Label(image=image)
label.pack()

window.mainloop()
