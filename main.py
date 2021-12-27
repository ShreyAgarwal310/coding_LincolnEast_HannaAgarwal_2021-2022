from tkinter import *
from tkinter import ttk
import copy

# creates the window of tkinter
window = Tk()
window.configure(background='white')
window.title('Adventour')
window.geometry("750x500")
window.resizable(0, 0)

# this function runs whenever the "search" button is pressed
def search():
    # clears the lists of matches and attractions in the selected city
    global matches
    matches = []
    in_city = []

    # gets all of the data and makes sure it's valid
    state = state_dropdown.get()
    state_boolean = not (state == "Select a State")
    city = cities_dropdown.get()
    city_boolean = not (city == "Select a State First" or city == "Select a City" or city == "Any")
    max_p = max_price_slider.get()
    type = type_dropdown.get()
    type_boolean = not (type == "Select a Type" or type == "Any")
    rating = rating_slider.get()
    inside = 1 == inside_choice.get()

    # checks if data entered is valid and then searches through the data to find acceptable places based on input
    if (inside):
        for i in attractions:
            match_counter = 0
            non_matches = []
            if((i[1] == city or (not city_boolean)) and (i[2] == state or (not state_boolean))):
                if(i[3] <= max_p):
                    match_counter += 1
                else:
                    non_matches.append("Price")

                if(i[4] == type or (not type_boolean)):
                    match_counter += 1
                else:
                    non_matches.append("Type")

                if(i[5]):
                    match_counter += 1
                else:
                    non_matches.append("Inside")

                if(i[6] >= rating):
                    match_counter += 1
                else:
                    non_matches.append("Rating")

                in_city.append([i, match_counter, non_matches])
            
            if((i[1] == city or (not city_boolean)) and (i[2] == state or (not state_boolean)) and (i[3] <= max_p) and (i[4] == type or (not type_boolean)) and (i[5]) and (i[6] >= rating)):
                matches.append(i)
    else:
        for i in attractions:
            match_counter = 1
            non_matches = []
            if((i[1] == city or (not city_boolean)) and (i[2] == state or (not state_boolean))):
                if(i[3] <= max_p):
                    match_counter += 1
                else:
                    non_matches.append("Price")

                if(i[4] == type or (not type_boolean)):
                    match_counter += 1
                else:
                    non_matches.append("Type")

                if(i[6] >= rating):
                    match_counter += 1
                else:
                    non_matches.append("Rating")

                in_city.append([i, match_counter, non_matches])
            
            if((i[1] == city or (not city_boolean)) and (i[2] == state or (not state_boolean)) and (i[3] <= max_p) and (i[4] == type or (not type_boolean)) and (i[6] >= rating)):
                matches.append(i)
    print(matches)
    print(len(matches))
    
    # sets the screen to the first match if there are matches
    if len(matches) > 0:
        update_screen(0)
    # if there aren't matches, it says there aren't any matches
    else:
        print("none")

    if len(matches) > 1:
        next_button.place(x=675, y=20)


# changes the possible selections of the city based on which state the user picked
def change_city_dropdown(e):
    state = state_dropdown.get()
    cities_dropdown['values'] = state_city_dict[state]
    cities_dropdown.configure(state='normal')
    cities_dropdown.set("Select a City")


def update_screen(new_screen):
    if(new_screen + 1 < len(matches)):
        next_button.place(x=675, y=20)
    else:
        next_button.place_forget()

    if(new_screen > 0):
        back_button.place(x=175, y=20)
    else:
        back_button.place_forget()

    title_text.configure(state="normal")
    title_text.delete("1.0", "end")
    title_text.insert('end', matches[new_screen][0])
    title_text.tag_add("center_title", "1.0", "end")
    title_text.configure(state='disabled')
    location_text.configure(state="normal")
    location_text.delete("1.0", "end")
    location_text.insert('end', f"Location: {matches[new_screen][1]}, {matches[new_screen][2]}")
    location_text.configure(state='disabled')
    price_text.configure(state="normal")
    price_text.delete("1.0", "end")
    price_text.insert('end', f"Price: {matches[new_screen][3]}$")
    price_text.configure(state='disabled')
    type_text.configure(state="normal")
    type_text.delete("1.0", "end")
    type_text.insert('end', f"Type: {matches[new_screen][4]}")
    type_text.configure(state='disabled')
    indoor_text.configure(state="normal")
    indoor_text.delete("1.0", "end")
    indoor_text.insert('end', 'This attraction is indoors') if matches[new_screen][5] else indoor_text.insert('end', 'This attraction is not indoors')
    indoor_text.configure(state='disabled')
    rating_text.configure(state="normal")
    rating_text.delete("1.0", "end")
    rating_text.insert('end', f"Rating: {matches[new_screen][6]}")
    rating_text.configure(state='disabled')
    screenNum_text.configure(state="normal")
    screenNum_text.delete("1.0", "end")
    screenNum_text.insert('end', f"{screenNum} / {len(matches)}")
    screenNum_text.configure(state='disabled')


# runs when the next button is pressed to show the next attraction
def next():
    # increments screenNum to go to the next screen
    global screenNum
    screenNum += 1
    print("next")
    # subtract 1 to convert screenNum starting at 1 to an index starting at 0
    update_screen(screenNum - 1)


# runs when the back button is pressed to show the previous attraction
def back():
    # increments screenNum down one to go to the previous screen
    global screenNum
    screenNum -= 1
    print("back")
    # subtract 1 to convert screenNum starting at 1 to an index starting at 0
    update_screen(screenNum - 1)

def about():
    print("about")
    
# initializes all options for state and type
states_options = ["Nebraska", "California", "New York", "Texas", "Florida"]
type_options = ["Any", "Educational", "Sightseeing", "Nature", "Pleasure"]

# dictionary to retrieve cities in each state
state_city_dict = {
    "Nebraska": ["Any", "Lincoln", "Omaha", "Scottsbluff", "North Platte"],
    "California": ["Any", "San Francisco", "Los Angeles", "San Jose", "Anaheim"],
    "New York": ["Any", "New York City"],
    "Texas": ["Any", "Houston", "Dallas", "Austin", "San Antonio", "Fort Worth"],
    "Florida": ["Any", "Miami", "Orlando", "Tampa", "Key West"]
}

# stores the data for the possible places to go
attractions = [["Golden Gate Bridge", "San Francisco", "California", 0, "Sightseeing", False, 4.8],
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
                ["Bryant Park", "New York City", "New York", 0, "Sightseeing", False, 4.7],
                ["Walt Disney World", "Orlando", "Florida", 110, "Pleasure", False, 4.7],
                ["Kennedy Space Center", "Orlando", "Florida", 50, "Educational", False, 4],
                ["Universal Studios", "Orlando", "Florida", 110, "Pleasure", False, 4.7],
                ["Miami Beach", "Miami", "Florida", 0, "Pleasure", False, 4.4],
                ["Everglades National Park", "Miami", "Florida", 0, "Nature", False, 4.6],
                ["Daytona 500 International Speedway", "Orlando", "Florida", 20, "Sightseeing", False, 4.7],
                ["SeaWorld Orlando", "Orlando", "Florida", 80, "Educational", False, 4.5],
                ["Busch Gardens Tampa", "Tampa", "Florida", 15, "Pleasure", False, 4.5],
                ["Duval Street", "Key West", "Florida", 0, "Sightseeing", False, 4.6],
                ["St. Augustine's Historic District", "Key West", "Florida", 0, "Sightseeing", False, 1],
                ["Edison and Ford Winter Estates", "Miami", "Florida", 20, "Sightseeing", True, 4.7],
                ["Salvador Dali Museum", "Tampa", "Florida", 20, "Educational", True, 4.7],
                ["Big Bend National Park", "San Antonio", "Texas", 15, "Nature", False, 4.8],
                ["The Alamo", "San Antonio", "Texas", 0, "Educational", False, 4.6],
                ["San Antonio's River Walk", "San Antonio", "Texas", 0, "Sightseeing", False, 4.7],
                ["Space Center Houston", "Houston", "Texas", 30, "Educational", False, 4.6],
                ["Padre Island National Seashore", "San Antonio", "Texas", 20, "Nature", False, 4.4],
                ["Texas State Capitol", "Austin", "Texas", 0, "Sightseeing", True, 4.7],
                ["Sixth Floor Museum", "Dallas", "Texas", 15, "Educational", True, 4.6],
                ["Fort Worth Stockyards", "Fort Worth", "Texas", 0, "Sightseeing", True, 4.7],
                ["Galveston Beach", "Houston", "Texas", 10, "Sightseeing", False, 4.5],
                ["USS Lexington", "San Antonio", "Texas", 20, "Educational", True, 4.8],
                ["Cadillac Ranch", "Dallas", "Texas", 0, "Sightseeing", False, 4.4],
                ["Natural Bridge Caverns", "San Antonio", "Texas", 30, "Nature", False, 4.7],
                ["Houston's Museum District", "Houston", "Texas", 20, "Educational", True, 4.5],
                ["Gruene Historic District", "San Antonio", "Texas", 10, "Sightseeing", False, 4.3],
                ["Dallas Arboretum", "Dallas", "Texas", 10, "Sightseeing", False, 4.3],
                ["Henry Doorly Zoo", "Omaha", "Nebraska", 20, "Educational", False, 4.8],
                ["Old Market in Omaha", "Omaha", "Nebraska", 0, "Sightseeing", False, 4.4],
                ["Strategic Air and Space Museum", "Omaha", "Nebraska", 15, "Educational", True, 4.7],
                ["Chimney Rock Historic Site", "Scottsbluff", "Nebraska", 0, "Sightseeing", False, 4.2],
                ["Haymarket District in Lincoln", "Lincoln", "Nebraska", 0, "Sightseeing", False, 4.7],
                ["Nebraska State Capitol", "Lincoln", "Nebraska", 0, "Sightseeing", True, 4.5],
                ["Lied Center", "Lincoln", "Nebraska", 50, "Pleasure", True, 4.3],
                ["Sheldon Museum of Art", "Lincoln", "Nebraska", 0, "Educational", True, 4.5],
                ["National Museum of Roller Skating", "Lincoln", "Nebraska", 0, "Educational", True, 3.9],
                ["Scottsbluff National Monument", "Scottsbluff", "Nebraska", 0, "Sightseeing", False, 4.8],
                ["Golden Spike Tower", "North Platte", "Nebraska", 10, "Sightseeing", False, 4.7],
                ["Carhenge", "Scottsbluff", "Nebraska", 0, "Sightseeing", False, 4.6]]

screenNum = 1
inside_choice = IntVar()

# creates backup of the attractions list
attractions_backup = copy.deepcopy(attractions)

# creates the dropdown where users select their state
state_dropdown = ttk.Combobox(window, width=16)

state_dropdown['values'] = states_options
state_dropdown.set("Select a State")
state_dropdown.place(x=10, y=70)  
state_dropdown.bind("<<ComboboxSelected>>", change_city_dropdown)

# creates the dropdown where users select their city
cities_dropdown = ttk.Combobox(window, width=16, values=["Select a State First"])
cities_dropdown.current(0)
cities_dropdown.place(x=10, y=110)
cities_dropdown.configure(state='disabled')

# creates the dropdown where users select their type of attraction
type_dropdown = ttk.Combobox(window, width=16, value=type_options)
type_dropdown.set("Select a Type")
type_dropdown.place(x=10, y=150)

# creates the dropdown where users select whether or not they want to be outside
inside_check = Checkbutton(window, text="Inside Only", variable=inside_choice, background='white')
inside_check.place(x=10, y=190)

# creates the slider where users decide the maximum price of their attraction
max_price_slider = Scale(window, from_=0, to=300, orient=HORIZONTAL, resolution=5)

max_price_slider.place(x=10, y=250)
max_price_slider.set(300)
max_price_slider.configure(background='white')

max_text = Text(window, background='white', borderwidth=0, height=1, width=9, font=("Arial", 10))
max_text.place(x=10, y=230)
max_text.insert('end', 'Max Price')
max_text.configure(state='disabled')

# creates the slider where users decide the rating they want their attraction to be
rating_slider = Scale(window, from_=0, to=5, orient=HORIZONTAL, resolution=0.1)

rating_slider.place(x=10, y=320)
rating_slider.configure(background='white')

ratings_text = Text(window, background='white', borderwidth=0, height=1, width=14, font=("Arial", 10))
ratings_text.place(x=10, y=300)
ratings_text.insert('end', 'Minimum Rating')
ratings_text.configure(state='disabled')

# creates the button users click to search once they have finished their entering
search_button = Button(window, text='Search', command=search)
search_button.place(x=50, y=420)

# separates the sidebar from the main display
separator = ttk.Separator(window, orient='vertical')
separator.place(relx=0.2, rely=0, relwidth=.001, relheight=1)

# next and back button to go through matching attractions
next_button = Button(window, text="Next >", command=next)
back_button = Button(window, text="< Back", command=back)

title_text = Text(window, background='white', 
                  borderwidth=0, height=1, 
                  width=32, font=("Arial", 19))
title_text.place(x=223, y=18)
title_text.tag_configure("center_title", justify='center')
title_text.configure(state='disabled')

location_text = Text(window, background='white', borderwidth=0, height=1, width=37, font=("Arial", 16))
location_text.place(x=225, y=80)
location_text.configure(state='disabled')

price_text = Text(window, background='white', borderwidth=0, height=1, width=37, font=("Arial", 16))
price_text.place(x=225, y=110)
price_text.configure(state='disabled')

type_text = Text(window, background='white', borderwidth=0, height=1, width=37, font=("Arial", 16))
type_text.place(x=225, y=140)
type_text.configure(state='disabled')

indoor_text = Text(window, background='white', borderwidth=0, height=1, width=37, font=("Arial", 16))
indoor_text.place(x=225, y=170)
indoor_text.configure(state='disabled')

rating_text = Text(window, background='white', borderwidth=0, height=1, width=37, font=("Arial", 16))
rating_text.place(x=225, y=200)
rating_text.configure(state='disabled')

screenNum_text = Text(window, background='white', borderwidth=0, height=1, width=7, font=("Arial", 14))
screenNum_text.place(x=425, y=450)
screenNum_text.configure(state='disabled')

about_text = Text(window, background='black', borderwidth=0, height=5, width=37, font=("Arial, 16"))
about_text.place(x=200, y=10)
about_text.insert()
about_text.configure(state='disabled')

window.mainloop()

