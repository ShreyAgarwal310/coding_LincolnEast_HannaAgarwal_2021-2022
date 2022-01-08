from tkinter import ttk, messagebox
from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO
import webbrowser
import requests
import copy
import csv

# creates the window of tkinter
window = Tk()
window.configure(background='white')
window.title('Adventour')
window.geometry("750x500")
window.resizable(0, 0)
window.iconbitmap(r'adventour_logo_icon.ico')

# this function runs whenever the "search" button is pressed


def search():
    # clears the lists of matches and attractions in the selected city and resets the screen number
    global matches, screen_num, in_city
    screen_num = 1
    matches = []
    in_city = []

    # gets all of the data and makes sure it's valid
    state = state_dropdown.get()
    city = cities_dropdown.get()
    city_boolean = not (city == "Select a City" or city == "Any")
    max_p = max_price_slider.get()
    type = type_dropdown.get()
    type_boolean = not (type == "Select a Type" or type == "Any")
    rating = rating_slider.get()
    inside = 1 == inside_choice.get()

    if not (state in states_options):
        messagebox.showerror("State Input Error", "Please Input a Valid State")
    elif not (city in state_city_dict[state] or city == "Select a City" or city == "Any"):
        messagebox.showerror(
            "City Input Error", "Please Input a Valid City \nCheck if the City is in the Selected State")
    elif not (type in type_options or type == "Select a Type" or type == "Any"):
        messagebox.showerror("Type Input Error", "Please Input a Valid Type")
    else:
        # searches through the data to find acceptable places based on input
        if (inside):
            for i in attractions:
                match_counter = 0
                non_matches = []
                if((i[1] == city or (not city_boolean)) and (i[2] == state)):
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

                if((i[1] == city or (not city_boolean)) and (i[2] == state) and (i[3] <= max_p) and (i[4] == type or (not type_boolean)) and (i[5]) and (i[6] >= rating)):
                    matches.append(i)
        else:
            for i in attractions:
                match_counter = 1
                non_matches = []
                if((i[1] == city or (not city_boolean)) and (i[2] == state)):
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

                if((i[1] == city or (not city_boolean)) and (i[2] == state) and (i[3] <= max_p) and (i[4] == type or (not type_boolean)) and (i[6] >= rating)):
                    matches.append(i)

        if(screen_num < len(matches)):
            next_button.tkraise()
            back_button.tkraise()

        if(about_showing):
            about_text.place_forget()
            about_button["text"] = "About"
            about_button.place(x=63, y=460)

        about_text.place_forget()
        about_button["text"] = "About"
        about_button.place(x=63, y=460)

        # sets the screen to the first match if there are matches
        if len(matches) > 0:
            update_screen(0)
        # if there aren't matches, it says there aren't any matches
        else:
            response = messagebox.askokcancel(
                "No Matches Found", "Unfortunately, we weren't able to find any attractions that fit your selected criteria. \n\nWould you like to see other attractions in your selected location? \n\nIf not just click cancel and edit your criteria.")
            if (response):
                update_screen_no_matches(0)
            else:
                clear_screen()

        try:
            if len(matches) > 1 and (not next_button.winfo_viewable()):
                next_button.place(x=675, y=20)
        except TclError:
            pass


# changes the possible selections of the city based on which state the user picked
def change_city_dropdown(e):
    state = state_dropdown.get()
    cities_dropdown['values'] = state_city_dict[state]
    cities_dropdown.configure(state='normal')
    cities_dropdown.set("Select a City")


def pull_up_link(url):
    webbrowser.open_new_tab(url)


def update_screen_no_matches(new_screen):
    global in_city, image_label, screen_num
    if(new_screen + 1 < len(in_city)):
        next_button.place(x=675, y=20)
    else:
        next_button.place_forget()

    if(new_screen > 0):
        back_button.place(x=200, y=20)
    else:
        back_button.place_forget()

    title_text.configure(state="normal")
    title_text.delete("1.0", "end")
    title_text.insert('end', in_city[new_screen][0][0])
    title_text.tag_add("center_title", "1.0", "end")
    title_text.configure(state='disabled')
    location_text.configure(state="normal")
    location_text.delete("1.0", "end")
    location_text.insert(
        'end', f"Location: {in_city[new_screen][0][1]}, {in_city[new_screen][0][2]}")
    location_text.configure(state='disabled')
    price_text.configure(state="normal")
    price_text.delete("1.0", "end")
    price_text.insert('end', f"Price: ${in_city[new_screen][0][3]}")
    price_text.configure(state='disabled')
    type_text.configure(state="normal")
    type_text.delete("1.0", "end")
    type_text.insert('end', f"Type: {in_city[new_screen][0][4]}")
    type_text.configure(state='disabled')
    indoor_text.configure(state="normal")
    indoor_text.delete("1.0", "end")
    indoor_text.insert('end', 'This attraction is indoors') if in_city[new_screen][0][5] else indoor_text.insert(
        'end', 'This attraction is not indoors')
    indoor_text.configure(state='disabled')
    rating_text.configure(state="normal")
    rating_text.delete("1.0", "end")
    rating_text.insert('end', f"Rating: {in_city[new_screen][0][6]}")
    rating_text.configure(state='disabled')
    screen_num_text.configure(state="normal")
    screen_num_text.delete("1.0", "end")
    screen_num_text.insert('end', f"{screen_num} / {len(in_city)}")
    screen_num_text.configure(state='disabled')

    url = in_city[new_screen][0][7]
    r = requests.get(url)
    pil_image = Image.open(BytesIO(r.content))
    pil_image = pil_image.resize((250, 250), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(pil_image)
    image_label['image'] = image
    image_label.place(x=480, y=75)
    window.mainloop()

    # link_url = in_city[new_screen][0[8]
    # link_label = Label(window, text='website', font=('Avenir Next', 14), fg='sky blue')
    # link_label.place(x=500, y=350)
    # link_label.bind("<Button-1", lambda e: pull_up_link(link_url))


def clear_screen():
    global image_label
    title_text.configure(state="normal")
    title_text.delete("1.0", "end")
    title_text.configure(state='disabled')
    location_text.configure(state="normal")
    location_text.delete("1.0", "end")
    location_text.configure(state='disabled')
    price_text.configure(state="normal")
    price_text.delete("1.0", "end")
    price_text.configure(state='disabled')
    type_text.configure(state="normal")
    type_text.delete("1.0", "end")
    type_text.configure(state='disabled')
    indoor_text.configure(state="normal")
    indoor_text.delete("1.0", "end")
    indoor_text.configure(state='disabled')
    rating_text.configure(state="normal")
    rating_text.delete("1.0", "end")
    rating_text.configure(state='disabled')
    screen_num_text.configure(state="normal")
    screen_num_text.delete("1.0", "end")
    screen_num_text.configure(state='disabled')
    image_label.place_forget()
    next_button.place_forget()
    back_button.place_forget()


def update_screen(new_screen):
    global image_label, screen_num, link_label
    if(new_screen + 1 < len(matches)):
        next_button.place(x=675, y=20)
    else:
        next_button.place_forget()

    if(new_screen > 0):
        back_button.place(x=200, y=20)
    else:
        back_button.place_forget()

    title_text.configure(state="normal")
    title_text.delete("1.0", "end")
    title_text.insert('end', matches[new_screen][0])
    title_text.tag_add("center_title", "1.0", "end")
    title_text.configure(state='disabled')
    location_text.configure(state="normal")
    location_text.delete("1.0", "end")
    location_text.insert(
        'end', f"Location: {matches[new_screen][1]}, {matches[new_screen][2]}")
    location_text.configure(state='disabled')
    price_text.configure(state="normal")
    price_text.delete("1.0", "end")
    price_text.insert('end', f"Price: ${matches[new_screen][3]}")
    price_text.configure(state='disabled')
    type_text.configure(state="normal")
    type_text.delete("1.0", "end")
    type_text.insert('end', f"Type: {matches[new_screen][4]}")
    type_text.configure(state='disabled')
    indoor_text.configure(state="normal")
    indoor_text.delete("1.0", "end")
    indoor_text.insert('end', 'This attraction is indoors') if matches[new_screen][5] else indoor_text.insert(
        'end', 'This attraction is not indoors')
    indoor_text.configure(state='disabled')
    rating_text.configure(state="normal")
    rating_text.delete("1.0", "end")
    rating_text.insert('end', f"Rating: {matches[new_screen][6]}")
    rating_text.configure(state='disabled')
    screen_num_text.configure(state="normal")
    screen_num_text.delete("1.0", "end")
    screen_num_text.insert('end', f"{screen_num} / {len(matches)}")
    screen_num_text.configure(state='disabled')

    url = matches[new_screen][7]
    r = requests.get(url)
    pil_image = Image.open(BytesIO(r.content))
    pil_image = pil_image.resize((250, 250), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(pil_image)
    image_label['image'] = image
    image_label.place(x=480, y=75)

    link_url = matches[new_screen][8]
    link_label['text'] = "website"
    link_label.place(x=590, y=330)
    link_label.bind("<Button-1>", lambda e: pull_up_link(link_url))

    window.mainloop()


# runs when the next button is pressed to show the next attraction
def next():
    # increments screen_num to go to the next screen
    global screen_num
    screen_num += 1
    # subtract 1 to convert screen_num starting at 1 to an index starting at 0
    if(len(matches) == 0):
        update_screen_no_matches(screen_num - 1)
    else:
        update_screen(screen_num - 1)


# runs when the back button is pressed to show the previous attraction
def back():
    # increments screen_num down one to go to the previous screen
    global screen_num
    screen_num -= 1
    # subtract 1 to convert screen_num starting at 1 to an index starting at 0
    if(len(matches) == 0):
        update_screen_no_matches(screen_num - 1)
    else:
        update_screen(screen_num - 1)


def about():
    global image_label, about_showing, link_label, screen_num
    if about_showing == False:
        try:
            image_label.place_forget()
        except NameError:
            pass
        try:
            link_label.place_forget()
        except NameError:
            pass
        about_text.place(x=190, y=0)
        about_button["text"] = "Close About"
        about_button.place(x=45, y=460)
        about_text.tkraise()
        about_showing = not about_showing
    else:
        about_text.place_forget()
        about_showing = not about_showing
        next_button.tkraise()
        back_button.tkraise()
        about_button["text"] = "About"
        about_button.place(x=63, y=460)
        update_screen(screen_num - 1)


def search_hover(e):
    search_button.config(background='white')


def search_leave(e):
    search_button.config(background='SystemButtonFace')


def about_hover(e):
    about_button.config(background='white')


def about_leave(e):
    about_button.config(background='SystemButtonFace')


def back_hover(e):
    back_button.config(background='white')


def back_leave(e):
    back_button.config(background='SystemButtonFace')


def next_hover(e):
    next_button.config(background='white')


def next_leave(e):
    next_button.config(background='SystemButtonFace')


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
# name, city, state, price, type, inside, rating, photo link
attractions = list(csv.reader(open("attractions.csv")))
for i in attractions:
    i[3] = int(i[3])
    i[5] = i[5] == "True"
    i[6] = float(i[6])

screen_num = 1
about_showing = False
inside_choice = IntVar()

# creates backup of the attractions list
attractions_backup = copy.deepcopy(attractions)

# creates the dropdown where users select their state
state_dropdown = ttk.Combobox(window, width=16)

state_dropdown['values'] = states_options
state_dropdown.set("Select a State")
state_dropdown.place(x=10, y=140)
state_dropdown.bind("<<ComboboxSelected>>", change_city_dropdown)

# creates the dropdown where users select their city
cities_dropdown = ttk.Combobox(window, width=16, values=[
    "Select a State First"])
cities_dropdown.current(0)
cities_dropdown.place(x=10, y=180)
cities_dropdown.configure(state='disabled')

# creates the dropdown where users select their type of attraction
type_dropdown = ttk.Combobox(window, width=16, value=type_options)
type_dropdown.set("Select a Type")
type_dropdown.place(x=10, y=220)

# creates the dropdown where users select whether or not they want to be outside
inside_check = Checkbutton(window, text="Inside Only",
                           variable=inside_choice, background='white')
inside_check.place(x=10, y=250)

# creates the slider where users decide the maximum price of their attraction
max_price_slider = Scale(window, from_=0, to=300,
                         orient=HORIZONTAL, resolution=5)

max_price_slider.place(x=35, y=300)
max_price_slider.set(300)
max_price_slider.configure(background='white')

max_text = Text(window, background='white', borderwidth=0,
                height=1, width=9, font=("Avenir Next", 10))
max_text.place(x=60, y=280)
max_text.insert('end', 'Max Price')
max_text.configure(state='disabled')

# creates the slider where users decide the rating they want their attraction to be
rating_slider = Scale(window, from_=0, to=5, orient=HORIZONTAL, resolution=0.1)

rating_slider.place(x=35, y=370)
rating_slider.configure(background='white')

ratings_text = Text(window, background='white', borderwidth=0,
                    height=1, width=14, font=("Avenir Next", 10))
ratings_text.place(x=40, y=350)
ratings_text.insert('end', 'Minimum Rating')
ratings_text.configure(state='disabled')

# creates the button users click to search once they have finished their entering
search_button = Button(window, text='Search', command=search)
search_button.place(x=60, y=430)
search_button.bind('<Enter>', search_hover)
search_button.bind('<Leave>', search_leave)

about_button = Button(window, text="About", command=about)
about_button.place(x=63, y=460)
about_button.bind('<Enter>', about_hover)
about_button.bind('<Leave>', about_leave)

# separates the sidebar from the main display
separator = ttk.Separator(window, orient='vertical')
separator.place(relx=0.25, rely=0, relwidth=.001, relheight=1)

# next and back button to go through matching attractions
next_button = Button(window, text="Next >", command=next)
back_button = Button(window, text="< Back", command=back)
next_button.bind('<Enter>', next_hover)
next_button.bind('<Leave>', next_leave)
back_button.bind('<Enter>', back_hover)
back_button.bind('<Leave>', back_leave)

title_text = Text(window, background='white',
                  borderwidth=0, height=1,
                  width=32, font=("Avenir Next", 19))
title_text.place(x=275, y=15)
title_text.tag_configure("center_title", justify='center')
title_text.configure(state='disabled')

location_text = Text(window, background='white', borderwidth=0,
                     height=1, width=37, font=("Avenir Next", 16))
location_text.place(x=200, y=80)
location_text.configure(state='disabled')

price_text = Text(window, background='white', borderwidth=0,
                  height=1, width=37, font=("Avenir Next", 16))
price_text.place(x=200, y=110)
price_text.configure(state='disabled')

type_text = Text(window, background='white', borderwidth=0,
                 height=1, width=37, font=("Avenir Next", 16))
type_text.place(x=200, y=140)
type_text.configure(state='disabled')

indoor_text = Text(window, background='white', borderwidth=0,
                   height=1, width=37, font=("Avenir Next", 16))
indoor_text.place(x=200, y=170)
indoor_text.configure(state='disabled')

rating_text = Text(window, background='white', borderwidth=0,
                   height=1, width=37, font=("Avenir Next", 16))
rating_text.place(x=200, y=200)
rating_text.configure(state='disabled')

screen_num_text = Text(window, background='white',
                       borderwidth=0, height=1, width=7, font=("Avenir Next", 14))
screen_num_text.place(x=425, y=450)
screen_num_text.configure(state='disabled')

image_label = ttk.Label()

link_label = Label(window, font=(
    'Avenir Next', 12), fg='sky blue', bg = 'white')

about_text = Text(window, background='white', borderwidth=0,
                  height=26, width=61, font=("Avenir Next", 14))
about_text.insert("1.0", "The Adventour App is designed to create recommendations for users\n" +
                  "based on entered criteria. \n \n" +
                  "To use to the app, \n \n" +
                  "1. Enter your desired criteria. The top dropdown decides the state, \n" +
                  "the second dropdown decides the city, and the third dropdown \n" +
                  "decides the top of attraction. The check mark indicates whether the \n" +
                  "attraction is indoor (checked) or outdoors (unchecked). The next \n" +
                  "slider is the maximum price and the bottommost slider is the \n" +
                  "minimum rating. Once finished entered, click the search button.\n \n" +
                  "2. Use the back and next button to toggle through the attractions. At \n" +
                  "the bottom of the screen, you can see how many attractions match \n" +
                  "your criteria. \n \n" +
                  "3. Enjoy the attraction you choose! \n \n" +
                  "Credits: Nixon Hanna, Shrey Agarwal")
about_text.configure(state='disabled')

# Read the Image
logo = Image.open("adventour_logo.jpg")

# Resize the image using resize() method
resize_logo = logo.resize((120, 120))
img_logo = ImageTk.PhotoImage(resize_logo)

# create label and add resize image
logo_label = Label(image=img_logo, borderwidth=0)
logo_label.image = img_logo
logo_label.place(x=33.5, y=5)

# function to shutdown window to avoid '_tkinter.TclError' after program exits
def shutdown_ttk_repeat():
    window.eval('::ttk::CancelRepeat')
    window.destroy()

window.protocol("WM_DELETE_WINDOW", shutdown_ttk_repeat)

window.mainloop()