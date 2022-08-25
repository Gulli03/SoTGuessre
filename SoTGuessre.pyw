from threading import Timer
import tkinter as tk
import random
import time
import os

Island_LookUp = [
    ("0000", "Crook's Hollow"),             #00
    ("0001", "Devil's Ridge"),              #01
    ("0002", "Discovery Ridge"),            #02
    ("0003", "Plunder Valley"),             #03
    ("0004", "Shark Bait Cove"),            #04
    ("0005", "Snake Island"),               #05
    ("0006", "Thieves' Haven"),             #06
    ("0010", "Barnacle Cay"),               #07
    ("0011", "Booty Isle"),                 #08
    ("0012", "Castaway Isle"),              #09
    ("0013", "Chicken Isle"),               #10
    ("0014", "Cutlass Cay"),                #11
    ("0015", "Fools Lagoon"),               #12
    ("0016", "Lookout Point"),              #13
    ("0017", "Mutineer Rock"),              #14
    ("0018", "Old Salts Atoll"),            #15
    ("0019", "Paradise Spring"),            #16
    ("0100", "Ashen Reaches"),              #17
    ("0101", "Fetcher's Rest"),             #18
    ("0102", "Flintlock Peninsula"),        #19
    ("0103", "Ruby's Fall"),                #20
    ("0104", "Devil's Thirst"),             #21
    ("0110", "Brimstone Rock"),             #22
    ("0111", "Cinder Islet"),               #23
    ("0112", "Cursewater Shores"),          #24
    ("0113", "Flame's End"),                #25
    ("0114", "Forsaken Brink"),             #26
    ("0115", "Glowstone Cay"),              #27
    ("0116", "Magma's Tide"),               #28
    ("0117", "Roaring Sands"),              #29
    ("0118", "Scorched Pass"),              #30
    ("0200", "Sea Dog's Tavern"),           #31
    ("0201", "Reaper's Hideout"),           #32
    ("0202", "Tribute Peak"),               #33
    ("0210", "K-9"),                        #34
    ("0211", "N-13"),                       #35
    ("0300", "Cannon Cove"),                #36
    ("0301", "Crescent Isle"),              #37
    ("0302", "Lone Cove"),                  #38
    ("0303", "Mermaid's Hideaway"),         #39
    ("0304", "Sailor's Bounty"),            #40
    ("0305", "Smuggler's Bay"),             #41
    ("0306", "Wanderers Refuge"),           #42
    ("0310", "Boulder Cay"),                #43
    ("0311", "Lagoon of Whispers"),         #44
    ("0312", "Lonely Isle"),                #45
    ("0313", "Picaroon Palms"),             #46
    ("0314", "Rapier Cay"),                 #47
    ("0315", "Rum Runner Isle"),            #48
    ("0316", "Salty Sands"),                #49
    ("0317", "Sandy Shallows"),             #50
    ("0318", "Sea Dog's Rest"),             #51
    ("0319", "Twin Groves"),                #52
    ("0400", "Kraken's Fall"),              #53
    ("0401", "Marauder's Arch"),            #54
    ("0402", "Old Faithful Isle"),          #55
    ("0403", "Shipwreck Bay"),              #56
    ("0404", "Crooked Masts"),              #57
    ("0405", "Sunken Grove"),               #58
    ("0410", "Black Sand Atoll"),           #59
    ("0411", "Black Water Enclave"),        #60
    ("0412", "Blind Man's Lagoon"),         #61
    ("0413", "Isle of Last Words"),         #62
    ("0414", "Liar's Backbone"),            #63
    ("0415", "Plunderer's Plight"),         #64
    ("0416", "Scurvy Island"),              #65
    ("0417", "Shark Tooth Key"),            #66
    ("0418", "Shiver Retreat"),             #67
    ("0419", "Tri-Rock Isle"),              #68
    ("1000", "Ancient Spire Outpost"),      #69
    ("1001", "Plunder Outpost"),            #70
    ("1100", "Morrow's Peak Outpost"),      #71
    ("1300", "New Golden Sands Outpost"),   #72
    ("1301", "Sanctuary Outpost"),          #73
    ("1400", "Dagger Tooth Outpost"),       #74
    ("1401", "Galleon's Grave"),            #75
    ("2010", "Fort of the Damned"),         #76
    ("2011", "Lost Gold Fort"),             #77
    ("2012", "Crow's Nest Fortress"),       #78
    ("2110", "Molten Sands Fortress"),      #79
    ("2310", "Hidden Spring Keep"),         #80
    ("2311", "Keel Haul Fort"),             #81
    ("2312", "Sailor's Knot Stronghold"),   #82
    ("2410", "Kraken Watchtower"),          #83
    ("2411", "Shark Fin Camp"),             #84
    ("2412", "Skull Keep"),                 #85
    ("3010", "Shrine of Ancient Tears"),    #86
    ("3011", "Shrine of Tribute"),          #87
    ("3310", "Shrine of Ocean's Fortune"),  #88
    ("3311", "Shrine of the Coral Tomb"),   #89
    ("3410", "Shrine of Flooded Embrace"),  #90
    ("3411", "Shrine of Hungering")]        #91

sorted_IslandLookUp = sorted(Island_LookUp, key = lambda x: x[1])

def bind_to_mousewheel(event):
    GuessFrame.bind_all("<MouseWheel>", on_mousewheel)

def unbind_to_mousewheel(event):
    GuessFrame.unbind_all("<MouseWheel>")

def on_mousewheel(event):
    GuessFrame.yview_scroll(int(-1*(event.delta/120)), "units")

def back():
    global state, seen_islands, max_islands, misses
    global forbidden_types, forbidden_regions, forbidden_sizes
    ImageLabel.place_forget()
    BackButton.place_forget()
    GuessFrame.place_forget()
    GuessScrollbar.place_forget()
    ResultLabel.place_forget()
    Searchbar.place_forget()
    SearchLabel.place_forget()
    RegionLabel.place(x = 18, y = 20)
    PlentyReg.place(x = 30, y = 60)
    AncientReg.place(x = 30, y = 100)
    WildsReg.place(x = 30, y = 140)
    DevilsReg.place(x = 30, y = 180)
    NoReg.place(x = 30, y = 220)
    SizeLabel.place(x = 18, y = 280)
    All.place(x = 30, y = 320)
    Big.place(x = 30, y = 360)
    Small.place(x = 30, y = 400)
    ExtrasLabel.place(x = 18, y = 460)
    AddOutposts.place(x = 30, y = 500)
    AddForts.place(x = 30, y = 540)
    AddShrines.place(x = 30, y = 580)
    RemIslands.place(x = 30, y = 620)
    OnlyShowPossible.place(x = 30, y = 660)
    StartButton.place(x = 300, y = 750)
    state = 0
    misses = 0
    seen_islands = []
    max_islands = len(Island_LookUp)
    forbidden_types = []
    forbidden_regions = []
    forbidden_sizes = []
    for button in guessbuttons:
        button.grid_forget()

def guess(ID, index):
    global misses
    answer = ImageLabel.cget("text")
    guessbuttons[index].configure(state = "disabled")
    if ID == answer:
        guessbuttons[index].configure(bg = "green")
        for button in guessbuttons:
            button.configure(state = "disabled")
        t = Timer(1, randomize_island)
        t.start()
    else:
        guessbuttons[index].configure(bg = "red")
        misses += 1
    Searchbar.focus_set()

def results(start, end, max_islands):
    global misses
    time = start - end
    av_time = round(time / max_islands, 2)
    time = round(time, 2)
    ImageLabel.place_forget()
    GuessFrame.place_forget()
    GuessScrollbar.place_forget()
    Searchbar.place_forget()
    SearchLabel.place_forget()
    ResultLabel.configure(text = f"You guessed {misses} times wrong!\nYou took {time} seconds!\nYou took an average of {av_time} seconds per Island!")
    ResultLabel.place(relx = 0.5, rely = 0.5, anchor = "center")

def place_buttons(buttonlist):
    for button in guessbuttons:
        button.grid_forget()
    row = 0
    col = 0
    for button in buttonlist:
        if col == 2:
            row += 1
            col = 0
        if button != 0:
            button.grid(row = row, column = col)
            col += 1

def search(query):
    searchedButtons = possible_buttons[:]
    if query != "":
        index = 0
        for button in searchedButtons:
            if button != 0:
                if not query.lower() in button.cget("text").lower():
                    searchedButtons[index] = 0
            index += 1

    place_buttons(searchedButtons)
    

def randomize_island():
    global state, max_islands, start, possible_buttons
    for button in guessbuttons:
            button.configure(state = "active", bg = "SystemButtonFace")
    if state == 0:
        possible_buttons = guessbuttons[:]
        start = time.time()
        for widget in OptionsWidgets:
            widget.place_forget()
        state = 1
        ImageLabel.place(x = 190, y = 20)
        StartButton.place_forget()
        BackButton.place(x = 18, y = 20)
        GuessFrame.place(x = 50, y = 400)
        GuessScrollbar.place(height = 525, x = 633, y = 400)
        GuessScrollHelper.place(x = 1, y = 1)
        GuessFrame.create_window((2, 5), window = GuessScrollHelper, anchor = "nw")
        Searchbar.place(x = 51, y = 373, width = 580, height = 25)
        SearchLabel.place(x = 631, y = 373)
        Searchbar.focus_set()

        if Size.get() == 0:
            forbidden_sizes.append(1)
        elif Size.get() == 1:
            forbidden_sizes.append(0)
        
        if not Inc_Outposts.get():
            max_islands -= 7
            forbidden_types.append(1)
        if not Inc_Forts.get():
            max_islands -= 10
            forbidden_types.append(2)
        if not Inc_Shrines.get():
            max_islands -= 6
            forbidden_types.append(3)
        if Exc_Islands.get():
            max_islands -= 69
            forbidden_types.append(0)
        
        if not Inc_Ancient.get():
            forbidden_regions.append(0)
            if not Exc_Islands.get():
                max_islands -= 17
            if Inc_Outposts.get():
                max_islands -= 2
            if Inc_Forts.get():
                max_islands -= 3
            if Inc_Shrines.get():
                max_islands -= 2
        else:
            if not Exc_Islands.get():
                if Size.get() == 0:
                    max_islands -= 10
                elif Size.get() == 1:
                    max_islands -= 7
                
        if not Inc_Devils.get():
            forbidden_regions.append(1)
            if not Exc_Islands.get():
                max_islands -= 14
            if Inc_Outposts.get():
                max_islands -= 1
            if Inc_Forts.get():
                max_islands -= 1
        else:
            if not Exc_Islands.get():
                if Size.get() == 0:
                    max_islands -= 9
                elif Size.get() == 1:
                    max_islands -= 5

        if not Inc_NoReg.get():
            forbidden_regions.append(2)
            if not Exc_Islands.get():
                max_islands -= 5
        else:
            if not Exc_Islands.get():
                if Size.get() == 0:
                    max_islands -= 2
                elif Size.get() == 1:
                    max_islands -= 3
                
        if not Inc_Plenty.get():
            forbidden_regions.append(3)
            if not Exc_Islands.get():
                max_islands -= 17
            if Inc_Outposts.get():
                max_islands -= 2
            if Inc_Forts.get():
                max_islands -= 3
            if Inc_Shrines.get():
                max_islands -= 2
        else:
            if not Exc_Islands.get():
                if Size.get() == 0:
                    max_islands -= 10
                elif Size.get() == 1:
                    max_islands -= 7
                
        if not Inc_Wilds.get():
            forbidden_regions.append(4)
            if not Exc_Islands.get():
                max_islands -= 16
            if Inc_Outposts.get():
                max_islands -= 2
            if Inc_Forts.get():
                max_islands -= 3
            if Inc_Shrines.get():
                max_islands -= 2
        else:
            if not Exc_Islands.get():
                if Size.get() == 0:
                    max_islands -= 10
                elif Size.get() == 1:
                    max_islands -= 6

        if Only_Show_Possible.get():
            index = 0
            for button in possible_buttons:
                ID = sorted_IslandLookUp[index][0]
                exclude = False
                for types in forbidden_types:
                    if int(ID[0]) == types:
                        exclude = True
                for region in forbidden_regions:
                    if int(ID[1]) == region:
                        exclude = True
                for size in forbidden_sizes:
                    if int(ID[2]) == size:
                        exclude = True
                if exclude:
                    possible_buttons[index] = 0
                index += 1

        place_buttons(possible_buttons)

    if query.get() != "":
        query.set("")
        
    if len(seen_islands) < max_islands:
        not_valid = True
        while not_valid:
            not_valid = False
            seen = True
            while seen:
                random_island = random.randrange(len(Island_LookUp))
                seen = False
                for island in seen_islands:
                    if island == random_island:
                        seen = True
            Island_data = Island_LookUp[random_island]
            ID = Island_data[0]
            for types in forbidden_types:
                if types == int(ID[0]):
                    not_valid = True
                    seen = True
            for region in forbidden_regions:
                if region == int(ID[1]):
                    not_valid = True
                    seen = True
            if ID[0] == "0" and not not_valid:
                for size in forbidden_sizes:
                    if size == int(ID[2]):
                        not_valid = True
                        seen = True
        seen_islands.append(random_island)
        image = locations[int(ID[0])][int(ID[1])][int(ID[2])][int(ID[3:])]
        ImageLabel.configure(image = image, text = ID)
    else:
        if max_islands > 0:
            end = time.time()
            results(start, end, max_islands)
        else:
            back()


    
# Hauptprogramm

bgcolor = "#ad813c"

root = tk.Tk()
root.title("SoT-Guessre")
width = 700
height = 950
centerx = int(root.winfo_screenwidth() / 2 - width / 2)
centery = int(root.winfo_screenheight() / 2 - height / 2) - 35
root.geometry(f'{width}x{height}+{centerx}+{centery}')
root.iconbitmap("./data/thieveshaven.ico")
root.resizable(False, False)
root.configure(bg=bgcolor)

BackIm = tk.PhotoImage(file = "./data/back.png")
SearchIm = tk.PhotoImage(file = "./data/search.png")

Inc_Ancient = tk.BooleanVar()
Inc_Ancient.set(True)
Inc_Devils = tk.BooleanVar()
Inc_Devils.set(True)
Inc_NoReg = tk.BooleanVar()
Inc_NoReg.set(True)
Inc_Plenty = tk.BooleanVar()
Inc_Plenty.set(True)
Inc_Wilds = tk.BooleanVar()
Inc_Wilds.set(True)
Size = tk.IntVar()
Size.set(-1)
Inc_Outposts = tk.BooleanVar()
Inc_Forts = tk.BooleanVar()
Inc_Shrines = tk.BooleanVar()
Exc_Islands = tk.BooleanVar()
Only_Show_Possible = tk.BooleanVar()

#Widgets for Main Menu

RegionLabel = tk.Label(root, bg = bgcolor, font = "Papyrus 20 bold", text = "Regions:")

PlentyReg = tk.Checkbutton(root, text = "The Shores of Plenty", font = "Papyrus", variable = Inc_Plenty, bg = bgcolor, activebackground = bgcolor)
AncientReg = tk.Checkbutton(root, text = "The Ancient Isles", font = "Papyrus", variable = Inc_Ancient, bg = bgcolor, activebackground = bgcolor)
WildsReg = tk.Checkbutton(root, text = "The Wilds", font = "Papyrus", variable = Inc_Wilds, bg = bgcolor, activebackground = bgcolor)
DevilsReg = tk.Checkbutton(root, text = "The Devil's Roar", font = "Papyrus", variable = Inc_Devils, bg = bgcolor, activebackground = bgcolor)
NoReg = tk.Checkbutton(root, text = "No Region/Uncharted", font = "Papyrus", variable = Inc_NoReg, bg = bgcolor, activebackground = bgcolor)

SizeLabel = tk.Label(root, bg = bgcolor, font = "Papyrus 20 bold", text = "Island Sizes:")

All = tk.Radiobutton(root, bg = bgcolor, font = "Papyrus", text = "All Sizes", variable = Size, value = -1, activebackground = bgcolor)
Big = tk.Radiobutton(root, bg = bgcolor, font = "Papyrus", text = "Only Big Islands", variable = Size, value = 0, activebackground = bgcolor)
Small = tk.Radiobutton(root, bg = bgcolor, font = "Papyrus", text = "Only Small Islands", variable = Size, value = 1, activebackground = bgcolor)

ExtrasLabel = tk.Label(root, bg = bgcolor, font = "Papyrus 20 bold", text = "Extras:")

AddOutposts = tk.Checkbutton(root, text = "Include Outposts", font = "Papyrus", variable = Inc_Outposts, bg = bgcolor, activebackground = bgcolor)
AddForts = tk.Checkbutton(root, text = "Include Forts", font = "Papyrus", variable = Inc_Forts, bg = bgcolor, activebackground = bgcolor)
AddShrines = tk.Checkbutton(root, text = "Include Shrines", font = "Papyrus", variable = Inc_Shrines, bg = bgcolor, activebackground = bgcolor)
RemIslands = tk.Checkbutton(root, text = "Exclude Islands", font = "Papyrus", variable = Exc_Islands, bg = bgcolor, activebackground = bgcolor)
OnlyShowPossible = tk.Checkbutton(root, text = "Only show possible Options", font = "Papyrus", variable = Only_Show_Possible, bg = bgcolor, activebackground = bgcolor)

StartButton = tk.Button(root, bg = "#33735e", font = "Papyrus 20 bold", text = "Start", command = lambda: randomize_island(), activebackground = "#33735e", height = 1, width = 5)

OptionsWidgets = [RegionLabel, PlentyReg, AncientReg, WildsReg, DevilsReg, NoReg,
                  SizeLabel, All, Big, Small,
                  ExtrasLabel, AddOutposts, AddForts, AddShrines, RemIslands, OnlyShowPossible]

#Widgets for Guessing

ImageLabel = tk.Label(root, bg = bgcolor, image = tk.PhotoImage(file = "./data/default.png"), height = 320, width = 320)

BackButton = tk.Button(root, bg = bgcolor, image = BackIm, command = lambda: back(), activebackground = bgcolor, bd = 0)

GuessFrame = tk.Canvas(root, width = 600, height = 525, bg = "#735629", highlightthickness = 0)
GuessFrame.grid_propagate(False)

GuessScrollbar = tk.Scrollbar(root, orient = "vertical", command = GuessFrame.yview)

GuessScrollHelper = tk.Frame(GuessFrame, bg = "#735629")
GuessScrollHelper.bind("<Configure>", lambda e: GuessFrame.configure(scrollregion = GuessFrame.bbox("all")))

GuessFrame.configure(yscrollcommand = GuessScrollbar.set)
GuessFrame.bind("<Enter>", bind_to_mousewheel)
GuessFrame.bind("<Leave>", unbind_to_mousewheel)

guessbuttons = []

index = 0
for island in sorted_IslandLookUp:
    guessbuttons.append(tk.Button(GuessScrollHelper, text = island[1], command = lambda ID = island[0], i = index: guess(ID, i), width = 40))
    index += 1

query = tk.StringVar()
Searchbar = tk.Entry(root, textvariable = query)
SearchLabel = tk.Label(root, image = SearchIm, bg = bgcolor)
query.trace("w", lambda *args: search(query.get()))

ResultLabel = tk.Label(bg = bgcolor, font = "Papyrus 20 bold", text = "You guessed 0 times wrong!")

back()

ancient_big = []
ancient_small = []

for image in os.listdir("./data/Ancient Isles/Big/"):
    ancient_big.append(tk.PhotoImage(file = "./data/Ancient Isles/Big/" + image))
for image in os.listdir("./data/Ancient Isles/Small/"):
    ancient_small.append(tk.PhotoImage(file = "./data/Ancient Isles/Small/" + image))

ancient_isles = [ancient_big, ancient_small]

devils_big = []
devils_small = []

for image in os.listdir("./data/Devils Roar/Big/"):
    devils_big.append(tk.PhotoImage(file = "./data/Devils Roar/Big/" + image))
for image in os.listdir("./data/Devils Roar/Small/"):
    devils_small.append(tk.PhotoImage(file = "./data/Devils Roar/Small/" + image))

devils_roar = [devils_big, devils_small]

no_region_big = []
no_region_small = []

for image in os.listdir("./data/No Region/Big/"):
    no_region_big.append(tk.PhotoImage(file = "./data/No Region/Big/" + image))
for image in os.listdir("./data/No Region/Small/"):
    no_region_small.append(tk.PhotoImage(file = "./data/No Region/Small/" + image))

no_region = [no_region_big, no_region_small]

plenty_big = []
plenty_small = []

for image in os.listdir("./data/Shores of Plenty/Big/"):
    plenty_big.append(tk.PhotoImage(file = "./data/Shores of Plenty/Big/" + image))
for image in os.listdir("./data/Shores of Plenty/Small/"):
    plenty_small.append(tk.PhotoImage(file = "./data/Shores of Plenty/Small/" + image))

shores_of_plenty = [plenty_big, plenty_small]

wilds_big = []
wilds_small = []

for image in os.listdir("./data/The Wilds/Big/"):
    wilds_big.append(tk.PhotoImage(file = "./data/The Wilds/Big/" + image))
for image in os.listdir("./data/The Wilds/Small/"):
    wilds_small.append(tk.PhotoImage(file = "./data/The Wilds/Small/" + image))

the_wilds = [wilds_big, wilds_small]
islands = [ancient_isles, devils_roar, no_region, shores_of_plenty, the_wilds]

ancient_outposts = [[tk.PhotoImage(file = "./data/Outposts/Ancient Isles/ancientspireoutpost.png"), tk.PhotoImage(file = "./data/Outposts/Ancient Isles/plunderoutpost.png")]]

devils_outposts = [[tk.PhotoImage(file = "./data/Outposts/Devils Roar/morrowspeakoutpost.png")]]

plenty_outposts = [[tk.PhotoImage(file = "./data/Outposts/Shores of Plenty/goldensandsoutpost.png"), tk.PhotoImage(file = "./data/Outposts/Shores of Plenty/sanctuaryoutpost.png")]]

wilds_outposts = [[tk.PhotoImage(file = "./data/Outposts/The Wilds/daggertoothoutpost.png"), tk.PhotoImage(file = "./data/Outposts/The Wilds/galleonsgraveoutpost.png")]]

outposts = [ancient_outposts, devils_outposts, [], plenty_outposts, wilds_outposts]

ancient_forts = [[], [tk.PhotoImage(file = "./data/Forts/Ancient Isles/fortofthedamned.png"), tk.PhotoImage(file = "./data/Forts/Ancient Isles/lostgoldfort.png"), tk.PhotoImage(file = "./data/Forts/Ancient Isles/thecrowsnestfortress.png")]]

devils_forts = [[], [tk.PhotoImage(file = "./data/Forts/Devils Roar/moltensandsfortress.png")]]

plenty_forts = [[], [tk.PhotoImage(file = "./data/Forts/Shores of Plenty/hiddenspringkeep.png"), tk.PhotoImage(file = "./data/Forts/Shores of Plenty/keelhaulfort.png"), tk.PhotoImage(file = "./data/Forts/Shores of Plenty/sailorsknotstronghold.png")]]

wilds_forts = [[], [tk.PhotoImage(file = "./data/Forts/The Wilds/krakenwatchtower.png"), tk.PhotoImage(file = "./data/Forts/The Wilds/sharkfincamp.png"), tk.PhotoImage(file = "./data/Forts/The Wilds/skullkeep.png")]]

forts = [ancient_forts, devils_forts, [], plenty_forts, wilds_forts]

ancient_shrines = [[], [tk.PhotoImage(file = "./data/Shrines/Ancient Isles/shrineofancienttears.png"), tk.PhotoImage(file = "./data/Shrines/Ancient Isles/shrineoftribute.png")]]

plenty_shrines = [[], [tk.PhotoImage(file = "./data/Shrines/Shores of Plenty/shrineofoceansfortune.png"), tk.PhotoImage(file = "./data/Shrines/Shores of Plenty/shrineofthecoraltomb.png")]]

wilds_shrines = [[], [tk.PhotoImage(file = "./data/Shrines/The Wilds/shrineoffloodedembrace.png"), tk.PhotoImage(file = "./data/Shrines/The Wilds/shrineofhungering.png")]]

shrines = [ancient_shrines, [], [], plenty_shrines, wilds_shrines]

locations = [islands, outposts, forts, shrines]

seen_islands = []
max_islands = len(Island_LookUp)
state = 0
start = 0
misses = 0

forbidden_types = []
forbidden_regions = []
forbidden_sizes = []

root.mainloop()
