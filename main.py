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
    
    if(about_showing):
        about_text.place_forget()
        about_button["text"] = "About"
        about_button.place(x=51, y=430)

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
    price_text.insert('end', f"Price: ${matches[new_screen][3]}")
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
    # subtract 1 to convert screenNum starting at 1 to an index starting at 0
    update_screen(screenNum - 1)


# runs when the back button is pressed to show the previous attraction
def back():
    # increments screenNum down one to go to the previous screen
    global screenNum
    screenNum -= 1
    # subtract 1 to convert screenNum starting at 1 to an index starting at 0
    update_screen(screenNum - 1)

def about():
    global about_showing
    if not about_showing:
        about_text.place(x=152, y=0)
        about_button["text"] = "Close About"
        about_button.place(x=35, y=430)
    else:
        about_text.place_forget()
        about_button["text"] = "About"
        about_button.place(x=51, y=430)

    about_showing = not about_showing
    

def search_hover(e):
    search_button.config(background='white')


def search_leave(e):
    search_button.config(background= 'SystemButtonFace')
    

def about_hover(e):
    about_button.config(background='white')
    

def about_leave(e):
    about_button.config(background= 'SystemButtonFace')
    

def back_hover(e):
    back_button.config(background='white')
    

def back_leave(e):
    back_button.config(background= 'SystemButtonFace')
    

def next_hover(e):
    next_button.config(background='white')
    

def next_leave(e):
    next_button.config(background= 'SystemButtonFace')
    

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
attractions = [["Golden Gate Bridge", "San Francisco", "California", 0, "Sightseeing", False, 4.8, "https://www.history.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:good%2Cw_1200/MTY1Mzg0OTc4NTIyMjUyNzU0/golden-gate-bridge-gettyimages-671734928.jpg"],
                ["Yosemite National Park", "San Franciso", "California", 15, "Nature", False, 4.8, "https://44hwtb1ramg42tavjo3od08v-wpengine.netdna-ssl.com/wp-content/uploads/2020/07/DSC00217-1-1200x1200-cropped.jpg"],
                ["Disneyland", "Anaheim", "California", 250, "Pleasure", False, 4.8, "https://cdn1.parksmedia.wdprapps.disney.com/resize/mwImage/1/1600/1600/90/media/abd/refresh/north-america/hollywood-disneyland-tour/abd-north-america-hollywood-disneyland-slideshow-1-sleeping-beauty-castle-1x1.jpg?cb=4"],
                ["Death Valley National Park", "Los Angeles", "California", 30, "Nature", False, 4.7, "https://media.cntraveler.com/photos/5b63277ef2d41408ff7d9f90/1:1/w_3648,h_3648,c_limit/GettyImages-525017352.jpg"],
                ["Big Sur", "San Jose", "California", 10, "Nature", False, 4.5, "https://www.bigsurlodge.com/wp-content/uploads/sites/8/2016/01/BIG-SUR-WATERFALL-THINGS-TO-DO-450x450.jpg"],
                ["Lake Tahoe", "San Francisco", "California", 10, "Nature", False, 4.8, "https://images.barrons.com/im-442067?width=1280&size=1"],
                ["Sequoia National Park", "Los Angeles", "California", 35, "Nature", False, 4.8, "https://www.nps.gov/common/uploads/grid_builder/seki/crop1_1/916C3669-1DD8-B71B-0BE35408261643BC.jpg?width=640&quality=90&mode=crop"],
                ["Redwood National Park", "San Francisco", "California", 0, "Nature", False, 4.8, "https://www.nps.gov/common/uploads/grid_builder/redw/crop1_1/60D0481D-BDC1-4F54-49342D5FB4C8D60E.jpg?width=640&quality=90&mode=crop"],
                ["Joshua Tree National Park", "Los Angeles", "California", 30, "Nature", False, 4.8, "https://assets.simpleviewinc.com/simpleview/image/upload/c_fill,f_jpg,g_xy_center,h_297,q_65,w_315,x_889,y_402/v1/clients/palmsprings/joshua_tree_ecedb690-b210-454b-8203-f807e2448036.jpg"],
                ["Universal Studios Hollywood", "Los Angeles", "California", 110, "Pleasure", False, 4.6, "https://www.universalstudioshollywood.com/tridiondata/ush/en/us/files/images/ush-universal-arch-red-carpet-welcome-back-m.jpg?imwidth=580"],
                ["Hearst Castle", "San Francisco", "California", 35, "Educational", True, 4.6, "https://cambriainns.com/wp-content/uploads/2015/03/hearst1.jpg"],
                ["Santa Catalina Island", "Los Angeles", "California", 0, "Sightseeing", False, 4.6, "https://www.tripsavvy.com/thmb/QiDO05SKkNsLrQVzCnwWRI7jSCQ=/1000x1000/smart/filters:no_upscale()/20090516__0069-1000x1500-58c39fe83df78c353cf97bfc.jpg"],
                ["Channel Islands National Park", "Los Angeles", "California", 0, "Sightseeing", False, 4.7, "https://www.venturaharborvillage.com/wp-content/uploads/channel-islands-national-park.jpg"],
                ["The Getty Center", "Los Angeles", "California", 0, "Educational", True, 4.8, "https://c8.alamy.com/comp/E2AM05/united-states-california-los-angeles-brentwood-hill-jpaul-getty-museum-E2AM05.jpg"],
                ["Statue of Liberty", "New York City", "New York", 0, "Sightseeing", False, 4.7, "https://media.newyorker.com/photos/60df663b833fa66507c7515e/1:1/w_1679,h_1679,c_limit/Gopnik-Little-Liberty.jpg"],
                ["Central Park", "New York City", "New York", 0, "Nature", False, 4.8, "https://static01.nyt.com/images/2021/03/07/nyregion/07travel-central-park-11/07travel-central-park-11-mobileMasterAt3x-v2.jpg"],
                ["Rockefeller Center", "New York City", "New York", 40, "Sightseeing", True, 4.7, "https://cdn.sanity.io/images/bs9rmafh/main/e58a153f0d183f4dc165199e4e8ba0a3e300bc50-1840x2002.jpg?w=800&h=870&fit=crop"],
                ["Metropolitan Museum of Art", "New York City", "New York", 25, "Educational", True, 4.8, "http://www.metmuseum.org/-/media/images/visit/met-fifth-avenue/fifthave_teaser.jpg?sc_lang=en"],
                ["Broadway", "New York City", "New York", 100, "Sightseeing", False, 4.5, "https://static01.nyt.com/images/2020/04/09/arts/00virus-broadway-1/00virus-broadway-1-mediumSquareAt3X-v2.jpg"],
                ["Empire State Building", "New York City", "New York", 36, "Sightseeing", True, 4.7, "https://marvel-b1-cdn.bc0a.com/f00000000179470/www.esbnyc.com/sites/default/files/styles/small_feature/public/2020-02/Green%20lights.jpg?itok=eesKOaKH"]
                ["9/11 Memorial", "New York City", "New York", 30, "Educational", False, 4.9, "https://d3iso9mq9tb10q.cloudfront.net/catalog/product/cache/191a57bb001f092e9eec8a49199fc081/b/b/bbt_product_attractions_new-york_911-memorial_1.jpg"],
                ["High Line", "New York City", "New York", 0, "Sightseeing", False, 4.7, "https://edc.nyc/sites/default/files/styles/1x1_md/public/2019-06/projects-the-highline-photo-brittany-petronella-nyc-and-company-05.jpg?h=56d0ca2e&itok=l-7KQn_B"],
                ["Times Square", "New York City", "New York", 0, "Sightseeing", False, 4.7, "https://www.tripsavvy.com/thmb/rFlaG5E709ir4EWJ21N8E3cRuUc=/3126x3126/smart/filters:no_upscale()/times-square-at-dusk-534858417-59b71eae798a49c4838c1507ec6bbffb.jpg"],
                ["Brooklyn Bridge", "New York City", "New York", 0, "Sightseeing", False, 4.8, "https://i.guim.co.uk/img/media/5abab6a27c22b15b07e7677d70e1d295290f0e57/0_224_6720_4032/master/6720.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=355ed36529a576370af754aab7debff6"],
                ["Fifth Avenue", "New York City", "New York", 0, "Sightseeing", False, 4.8, "https://saksfifthavenue.brickworksoftware.com/assets?format=webp&source=https://cdn.filepicker.io/api/file/hOfEzIYhTq6epllJ2bHa"],
                ["Grand Central Terminal", "New York City", "New York", 0, "Sightseeing", False, 4.7, "https://www.history.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:good%2Cw_1200/MTY4ODE0MzA5NjU1MTkzMDkz/grand-central-terminal-gettyimages-176608565.jpg"],
                ["One World Observatory", "New York City", "New York", 43, "Pleasure", True, 4.7, "https://pyxis.nymag.com/v1/imgs/140/9ef/d7e9d6eeb718d2a264d74302eef5e96886-29-critics-architecture.rsquare.w700.jpg"],
                ["The Frick Collection", "New York City", "New York", 20, "Educational", True, 4.6, "https://images.wsj.net/im-309576?width=1280&size=1"],
                ["New York Public Library", "New York City", "New York", 0, "Educational", True, 4.7, "https://images.adsttc.com/media/images/536b/94aa/c07a/8072/5e00/00cd/large_jpg/1355953846-1674-fp468258-indesign.jpg?1399559319"],
                ["Wall Street", "New York City", "New York", 0, "Sightseeing", True, 4.6, "https://i.guim.co.uk/img/media/85e9729f528365925d985308b6b31df6b650f0b9/0_200_6000_3600/master/6000.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=ce9a51750e09299a8c4958591f970d74"],
                ["Radio City Music Hall", "New York City", "New York", 31, "Pleasure", True, 4.7, "https://aws-tiqets-cdn.imgix.net/images/content/1488b5cbd87845228820239218b57924.jpg?auto=format&fit=crop&h=800&ixlib=python-3.2.1&q=70&w=800&s=247a69401ec103d041afeb2681c89401"],
                ["St. Patrick's Cathedral", "New York City", "New York", 10, "Sightseeing", True, 4.8, "https://cdn.vox-cdn.com/thumbor/2f-EMIobY_hf_zhb0SjuC8HndQI=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/9075677/stpatricks_cathedral.jpg"],
                ["Carnegie Hall", "New York City", "New York", 300, "Sightseeing", True, 4.7, "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/gettyimages-50606902-1556557421.jpg?crop=0.668xw:1.00xh;0.0689xw,0&resize=640:*"],
                ["Bryant Park", "New York City", "New York", 0, "Sightseeing", False, 4.7, "https://static01.nyt.com/images/2021/04/15/arts/14bryant-live/merlin_177032124_68f3d4cb-62d6-47ec-8cb8-fa67f1570a53-mediumSquareAt3X.jpg"], ## Stop here
                ["Walt Disney World", "Orlando", "Florida", 110, "Pleasure", False, 4.7, "https://lumiere-a.akamaihd.net/v1/images/cg_parks_wdw_50thcelebration_specialoffers_21943_25454ec0.jpeg?region=0,0,800,800"],
                ["Kennedy Space Center", "Orlando", "Florida", 50, "Educational", False, 4, "https://www.kennedyspacecenter.com/-/media/DNC/KSCVC/Attraction-Images/Apollo-Saturn-V-Zone/moon-tree-garden-square.ashx?h=900&w=900&la=en&hash=E579E03ADEC1D0E632712E04A670435F2AA4EA64"],
                ["Universal Studios", "Orlando", "Florida", 110, "Pleasure", False, 4.7, "https://travelmamas.com/wp-content/uploads/2018/08/universal_hollywood_entrance_family2_square.jpg"],
                ["Miami Beach", "Miami", "Florida", 0, "Pleasure", False, 4.4, "https://images.squarespace-cdn.com/content/v1/5830e824c534a5539424a2ce/1619372362752-XAVBUXSZTEQID74SMF1E/577F3A76-EE1E-4680-A2ED-9516FB813818.jpg?format=1000w"],
                ["Everglades National Park", "Miami", "Florida", 0, "Nature", False, 4.6, "https://i.natgeofe.com/n/f3cb2ae5-53e1-44d3-ab69-6b3efa0ccbf7/2026_square.jpg"],
                ["Daytona 500 International Speedway", "Orlando", "Florida", 20, "Sightseeing", False, 4.7, "https://frcs.pro/assets/img/track/daytona-international-speedway.jpg"],
                ["SeaWorld Orlando", "Orlando", "Florida", 80, "Educational", False, 4.5, "https://www.bestoforlando.com/common_resources/resize_library/seaworld-orlando-square-logo-210x210.jpg"],
                ["Busch Gardens Tampa", "Tampa", "Florida", 15, "Pleasure", False, 4.5, "https://www.bestoforlando.com/common_resources/resize_library/busch-gardens-tampa-square-logo-210x210.jpg"],
                ["Duval Street", "Key West", "Florida", 0, "Sightseeing", False, 4.6, "https://fastly.4sqi.net/img/general/600x600/1235885_RMB3oa6XTNOpWrVLGna_kp9AJO5t14XG6oNhRHyYSD4.jpg"],
                ["St. Augustine's Historic District", "Key West", "Flordia", 0, "Sightseeing", False, 1, "https://upload.travelawaits.com/ta/uploads/2021/04/downtown-st-augustine-flori6636a2.jpg"],
                ["Edison and Ford Winter Estates", "Miami", "Florida", 20, "Sightseeing", True, 4.7, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQVIaLPelb7GLbBlmhgtWl5PaTUP_Khe_pTsg&usqp=CAU"],
                ["Salvador Dali Museum", "Tampa", "Florida", 20, "Educational", True, 4.7, "https://www.mustdo.com/wp-content/uploads/2016/12/Dali-Museum-St.-Petersburg-Florida.jpg"],
                ["Big Bend National Park", "San Antonio", "Texas", 15, "Nature", False, 4.8, "https://i.pinimg.com/474x/67/4e/66/674e66639f652f4c119b80c534acf3eb.jpg"],
                ["The Alamo", "San Antonio", "Texas", 0, "Educational", False, 4.6, "https://www.history.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:good%2Cw_1200/MTU3ODc5MDg1NjI1MTI0NTc1/alamo-2.jpg"],
                ["San Antonio's River Walk", "San Antonio", "Texas", 0, "Sightseeing", False, 4.7, "https://upload.travelawaits.com/ta/uploads/2021/04/the-san-antonio-river-walk-inb5a0a4.jpg"],
                ["Space Center Houston", "Houston", "Texas", 30, "Educational", False, 4.6, "https://upload.wikimedia.org/wikipedia/en/thumb/c/ce/Space_Center_Houston_Color_Stacked.svg/1200px-Space_Center_Houston_Color_Stacked.svg.png"],
                ["Padre Island National Seashore", "San Antonio", "Texas", 20, "Nature", False, 4.4, "https://render.fineartamerica.com/images/rendered/small/print/images/artworkimages/square/2/padre-island-national-seashore-yinyang.jpg"],
                ["Texas State Capitol", "Austin", "Texas", 0, "Sightseeing", True, 4.7, "https://txhillcountrytrail.com/public/upload/txhillcountrytrail_com/images/sites/HC-site-StateCapitol-Austin.jpg"],
                ["Sixth Floor Museum", "Dallas", "Texas", 15, "Educational", True, 4.6, "https://img.texasmonthly.com/2019/11/dallas-sixth-floor-museum-exterior.jpg?auto=compress&crop=faces&fit=crop&fm=jpg&h=1400&ixlib=php-1.2.1&q=45&w=1400"],
                ["Fort Worth Stockyards", "Fort Worth", "Texas", 0, "Sightseeing", True, 4.7, "https://upload.travelawaits.com/ta/uploads/2021/04/the-fort-worth-stockyards-ine52376-800x800.jpg"],
                ["Galveston Beach", "Houston", "Texas", 10, "Sightseeing", False, 4.5, "https://res.cloudinary.com/culturemap-com/image/upload/c_limit,w_980/v1498082859/photos/200958_original_square.png"],
                ["USS Lexington", "San Antonio", "Texas", 20, "Educational", True, 4.8, "https://images.discerningassets.com/image/upload/c_fill,h_1000,w_1000/c_fit,fl_relative,h_1.0,l_deco_watermark,o_40,w_1.0/c_fill,w_1000,h_1000/v1490500255/USS_Lexington_om0h3r.jpg"],
                ["Cadillac Ranch", "Dallas", "Texas", 0, "Sightseeing", False, 4.4, "https://render.fineartamerica.com/images/rendered/small/print/images/artworkimages/square/3/1-cadillac-ranch-chris-smith.jpg"],
                ["Natural Bridge Caverns", "San Antonio", "Texas", 30, "Nature", False, 4.7, "https://naturalbridgecaverns.com/wp-content/uploads/2019/09/6-10-Natural-Bridge-005-F_4x4.jpg"],
                ["Houston's Museum District", "Houston", "Texas", 20, "Educational", True, 4.5, "https://img.texasmonthly.com/2015/04/tripguides_interior33.jpg?auto=compress&crop=faces&fit=crop&fm=jpg&h=1400&ixlib=php-1.2.1&q=45&w=1400"],
                ["Gruene Historic District", "San Antonio", "Texas", 10, "Sightseeing", False, 4.3, "https://cdn2.hubspot.net/hub/97965/file-808194920.jpg?width=730&name=file-808194920.jpg"],
                ["Dallas Arboretum", "Dallas", "Texas", 10, "Sightseeing", False, 4.3, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRtGxEJHoI7DR13HgywIcSphw-Tp3_gQvUipQ&usqp=CAU"],
                ["Henry Doorly Zoo", "Omaha", "Nebraska", 20, "Educational", False, 4.8, "https://www.loveourcrazylife.com/wp-content/uploads/2015/07/17484135881_faf4233f74_z.jpg"],
                ["Old Market in Omaha", "Omaha", "Nebraska", 0, "Sightseeing", False, 4.4, "https://static.wixstatic.com/media/17973e_03755a2f0ef346c487831e8a95672b02~mv2.jpg/v1/crop/x_1,y_105,w_1454,h_726/fill/w_552,h_448,al_c,q_80,usm_0.66_1.00_0.01/DSC_0236.webp"],
                ["Strategic Air and Space Museum", "Omaha", "Nebraska", 15, "Educational", True, 4.7, "https://www.roadsideamerica.com/attract/images/ne/NEASHsac_5272ks.jpg"],
                ["Chimney Rock Historic Site", "Scottsbluff", "Nebraska", 0, "Sightseeing", False, 4.2, "https://www.chimneyrockpark.com/wp-content/uploads/2016/05/chimneyrock_state.jpg"],
                ["Haymarket District in Lincoln", "Lincoln", "Nebraska", 0, "Sightseeing", False, 4.7, "https://bloximages.chicago2.vip.townnews.com/journalstar.com/content/tncms/assets/v3/editorial/1/47/147575ea-1ec9-5d45-a3c6-bbaa639d3124/5a84f250e0c5d.image.jpg?crop=999%2C999%2C250%2C0&resize=1200%2C1200&order=crop%2Cresize"],
                ["Nebraska State Capitol", "Lincoln", "Nebraska", 0, "Sightseeing", True, 4.5, "https://upload.wikimedia.org/wikipedia/commons/c/cc/Nebraska_State_Capitol_aerial.jpg"],
                ["Lied Center", "Lincoln", "Nebraska", 50, "Pleasure", True, 4.3, "https://www.liedcenter.org/sites/default/files/styles/event_listing/public/teasers/andrew_and_kamerin_on_lied_stage.jpg?itok=0monEkvb"],
                ["Sheldon Museum of Art", "Lincoln", "Nebraska", 0, "Educational", True, 4.5, "https://lh3.googleusercontent.com/proxy/YFxuCWN2KJZBEr5vB-Fdb6cLXY8zqnxwn0isFPHh1MM8e0rbzuU5qCyyRzdQbdx5OgGTvtbZxkeWSQk5jFVbPmpaEahYocIGMKGYotLWnd55wGAg"],
                ["National Museum of Roller Skating", "Lincoln", "Nebraska", 0, "Educational", True, 3.9, "https://ghosty-production.s3.amazonaws.com/fotospot_spots/National-Museum-of-Rollerskating-Fotospot_dd70d6d30b310a43650607af29155fb5/large.jpg"],
                ["Scottsbluff National Monument", "Scottsbluff", "Nebraska", 0, "Sightseeing", False, 4.8, "https://bloximages.chicago2.vip.townnews.com/theindependent.com/content/tncms/assets/v3/editorial/8/c3/8c3df7d2-2748-11e6-9262-676e98c59aed/574db531f1144.image.jpg?crop=1175%2C1175%2C294%2C0&resize=1200%2C1200&order=crop%2Cresize"],
                ["Golden Spike Tower", "North Platte", "Nebraska", 10, "Sightseeing", False, 4.7, "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/10/b9/03/73/entrance.jpg?w=1200&h=1200&s=1"],
                ["Carhenge", "Scottsbluff", "Nebraska", 0, "Sightseeing", False, 4.6, "https://s3-media0.fl.yelpcdn.com/bphoto/v0XSjKbca-cx0tOXHN3pJw/348s.jpg"]]

screenNum = 1
about_showing = False
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
search_button.place(x=50, y=390)
search_button.bind('<Enter>', search_hover)
search_button.bind('<Leave>', search_leave)

about_button = Button(window, text="About", command=about)
about_button.place(x=51, y=430)
about_button.bind('<Enter>', about_hover)
about_button.bind('<Leave>', about_leave)

# separates the sidebar from the main display
separator = ttk.Separator(window, orient='vertical')
separator.place(relx=0.2, rely=0, relwidth=.001, relheight=1)

# next and back button to go through matching attractions
next_button = Button(window, text="Next >", command=next)
back_button = Button(window, text="< Back", command=back)
next_button.bind('<Enter>', next_hover)
next_button.bind('<Leave>', next_leave)
back_button.bind('<Enter>', back_hover)
back_button.bind('<Leave>', back_leave)

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

about_text = Text(window, background='white', borderwidth=0, height=21, width=53, font=("Arial", 14))
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
                          "your criteria. \n \n " +
                          "3. Enjoy the attraction you choose! \n \n" +
                          "Credits: Nixon Hanna, Shrey Agarwal")
about_text.configure(state='disabled')

window.mainloop()
