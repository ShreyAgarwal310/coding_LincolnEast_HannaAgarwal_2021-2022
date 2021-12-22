import requests
import json
import urllib.request
import shutil
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

window = Tk()
window.configure(background='white')
window.title('Thing')
window.geometry("750x500")

def get_choices():
    state = state_dropdown.get()
    city = cities_dropdown.get()
    min_p = min_price_slider.get()
    print(city, state, min_p)

def pick_cities(e):
    state = state_dropdown.get()
    if(state == "Nebraska"):
        cities_dropdown['values'] = ne_cities
        cities_dropdown.current(0)
    elif(state == "California"):
        cities_dropdown['values'] = ca_cities
        cities_dropdown.current(0)
    elif(state == "New York"):
        cities_dropdown['values'] = ny_cities
        cities_dropdown.current(0)
    elif(state == "Texas"):
        cities_dropdown['values'] = tx_cities
        cities_dropdown.current(0)
    elif(state == "Florida"):
        cities_dropdown['values'] = fl_cities
        cities_dropdown.current(0)
    




states_options = ["Nebraska", "California", "New York", "Texas", "Florida"]
ne_cities = ["", "Lincoln", "Omaha"]
ca_cities = ["", "San Francisco", "Los Angeles", "San Jose", "Anaheim", "Sacramento"]
ny_cities = ["", "New York City", "Broadway", "Brooklyn"]
tx_cities = ["", "Houston", "Dallas", "Austin"]
fl_cities = ["", "Miama", "Orlando"]


state_choice= StringVar(window)
city_choice = StringVar(window)
min_price = DoubleVar(window)


state_choice.set("Select a State")
city_choice.set("Select a City")


state_dropdown = ttk.Combobox(window, width = 16, textvariable = state_choice)
state_dropdown['values'] = states_options
state_dropdown.place(x = 10, y = 50)  
state_dropdown.bind("<<ComboboxSelected>>", pick_cities)

cities_dropdown = ttk.Combobox(window, width = 16, values = ["Select a State First"])
cities_dropdown.current(0)
cities_dropdown.place(x = 10, y = 90)

min_price_slider = Scale(window, variable = min_price, from_ = 0, to = 50, orient = HORIZONTAL)
min_price_slider.place(x = 10, y = 120)
min_price_slider.configure(background='white')







search_button = Button(window, text='Search', command=get_choices)
search_button.place(x = 50, y = 400)


separator = ttk.Separator(window, orient='vertical')
separator.place(relx=0.2, rely=0, relwidth=.001, relheight=1)





window.mainloop()




# location, price, type, inside outside, rating
