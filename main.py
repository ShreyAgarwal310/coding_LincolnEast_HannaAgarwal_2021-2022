from tkinter import *
from tkinter import ttk

window = Tk()
window.configure(background='white')
window.title('Thing')
window.geometry("750x500")

def get_choices():
    state = state_dropdown.get()
    state_boolean = not (state == "Select a State")
    city = cities_dropdown.get()
    city_boolean = not (city == "Select a State First" or city == "")
    min_p = min_price_slider.get()
    max_p = max_price_slider.get()
    type = type_dropdown.get()
    type_boolean = not (type == "Select a Type")
    rating = rating_slider.get()
    inside = 1 == inside_choice.get()

    print(city, state, min_p, max_p, type, rating, inside, state_boolean, city_boolean, type_boolean)

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
fl_cities = ["", "Miami", "Orlando"]
type_options = ["Education", "Sightseeing", "Nature", "Pleasure"]

attractions = [["Golden State Bridge", "San Francisco", "California", 0, "Sightseeing", False, 4.8],
                ["Yosemite National Park", "San Franciso", "California", 15, "Nature", False, 4.8],
                ["Disneyland", "Anaheim", "California", 250, "Pleasure", False, 4.8],
                ["Death Valley National Park", "Los Angeles", "California", 30, "Nature", False, 4.7],
                ["Big Sur", "San Jose", "California", 10, "Nature", False, 4.5],
                ["Lake Tahoe", "San Francisco", "California", 10, "Nature", False, 4.8],
                ["Sequoia National Park", "Los Angeles", "California", 35, "Nature", False, 4.8],
                ["Redwood National Park", "San Francisco", "California", 0, "Nature", False, 4.8],
                ["Joshua Tree National Park", "Los Angeles", "California", 30, "Nature", False, 4.8],
                ["Universal Studios Hollywood", "Los Angeles", "California", 110, "Pleasure", False, 4.6],
                ["Hearst Castle", "San Francisco", "California", 35, "Educational", True, 4.6],
                ["Santa Catalina Island", "Los Angeles", "California", 0, "Sightseeing", False, 4.6],
                ["Channel Islands National Park", "Los Angeles", "California", 0, "Sightseeing", False, 4.7],
                ["The Getty Center", "Los Angeles", "California", 0, "Educational", True, 4.8],
                ["Statue of Liberty", "New York City", "New York", 0, "Sightseeing", False, 4.7],
                ["Central Park", "New York City", "New York", 0, "Nature", False, 4.8],
                ["Rockefeller Center", "New York City", "New York", 40, "Sightseeing", True, 4.7],
                ["Metropolitan Museum of Art", "New York City", "New York", 25, "Educational", True, 4.8],
                ["Broadway", "New York City", "New York", 100, "Sightseeing", False, 4.5],
                ["Empire State Building", "New York City", "New York", 36, "Sightseeing", True, 4.7],
                ["9/11 Memorial", "New York City", "New York", 30, "Educational", False, 4.9],
                ["High Line", "New York City", "New York", 0, "Sightseeing", False, 4.7],
                ["Times Square", "New York City", "New York", 0, "Sightseeing", False, 4.7],
                ["Brooklyn Bridge", "New York City", "New York", 0, "Sightseeing", False, 4.8],
                ["Fifth Avenue", "New York City", "New York", 0, "Sightseeing", False, 4.8],
                ["Grand Central Terminal", "New York City", "New York", 0, "Sightseeing", False, 4.7],
                ["One World Observatory", "New York City", "New York", 43, "Pleasure", True, 4.7],
                ["The Frick Collection", "New York City", "New York", 20, "Educational", True, 4.6],
                ["New York Public Library", "New York City", "New York", 0, "Educational", True, 4.7],
                ["Wall Street", "New York City", "New York", 0, "Sightseeing", True, 4.6],
                ["Radio City Music Hall", "New York City", "New York", 31, "Pleasure", True, 4.7],
                ["St. Patrick's Cathedral", "New York City", "New York", 10, "Sightseeing", True, 4.8],
                ["Carnegie Hall", "New York City", "New York", 300, "Sightseeing", True, 4.7],
                ["Bryant Park", "New York City", "New York", 0, "Sightseeing", False, 4.7]]


state_choice= StringVar(window)
city_choice = StringVar(window)
min_price = DoubleVar(window)
max_price = DoubleVar(window)
type_choice = StringVar(window)
rating_choice = DoubleVar(window)
inside_choice = IntVar()


state_choice.set("Select a State")
city_choice.set("Select a City")


state_dropdown = ttk.Combobox(window, width = 16, textvariable = state_choice)
state_dropdown['values'] = states_options
state_dropdown.place(x = 10, y = 70)  
state_dropdown.bind("<<ComboboxSelected>>", pick_cities)

cities_dropdown = ttk.Combobox(window, width = 16, values = ["Select a State First"])
cities_dropdown.current(0)
cities_dropdown.place(x = 10, y = 110)

type_dropdown = ttk.Combobox(window, width = 16, value = type_options)
type_dropdown.set("Select a Type")
type_dropdown.place(x = 10, y = 150)

inside_check = Checkbutton(window, text = "Inside", variable = inside_choice)
inside_check.place(x = 10, y = 190)

min_price_slider = Scale(window, variable = min_price, from_ = 0, to = 50, orient = HORIZONTAL, resolution = 5)
min_price_slider.place(x = 10, y = 240)
min_price_slider.configure(background = 'white')

max_price_slider = Scale(window, variable = max_price, from_ = 50, to = 300, orient = HORIZONTAL, resolution = 5)
max_price_slider.place(x = 10, y = 290)
max_price_slider.set(300)
max_price_slider.configure(background = 'white')

rating_slider = Scale(window, variable = rating_choice, from_ = 0, to = 5, orient = HORIZONTAL, resolution = 0.1)
rating_slider.place(x = 10, y = 340)
rating_slider.configure(background = 'white')

search_button = Button(window, text='Search', command=get_choices)
search_button.place(x = 50, y = 400)


separator = ttk.Separator(window, orient='vertical')
separator.place(relx=0.2, rely=0, relwidth=.001, relheight=1)

window.mainloop()
