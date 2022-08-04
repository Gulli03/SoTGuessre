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
    ("0104", "The Devil's Thirst"),         #21
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
    ("0404", "The Crooked Masts"),          #57
    ("0405", "The Sunken Grove"),           #58
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
    ("1300", "Golden Sands Outpost"),       #72
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

def back():
    global state, seen_islands, max_islands, misses
    global forbidden_types, forbidden_regions, forbidden_sizes
    ImageLabel.place_forget()
    BackButton.place_forget()
    GuessFrame.place_forget()
    ResultLabel.place_forget()
    StartButton.configure(text = "Start")
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
    StartButton.place(x = 300, y = 750)
    state = 0
    misses = 0
    seen_islands = []
    max_islands = len(Island_LookUp)
    forbidden_types = []
    forbidden_regions = []
    forbidden_sizes = []

def guess(ID):
    global misses
    answer = int(ImageLabel.cget("text"))
    guessbuttons[ID].configure(state = "disabled")
    if ID == answer:
        guessbuttons[ID].configure(bg = "green")
        for button in guessbuttons:
            button.configure(state = "disabled")
        t = Timer(1, randomize_island)
        t.start()
    else:
        guessbuttons[ID].configure(bg = "red")
        misses += 1

def results(start, end, max_islands):
    global misses
    time = start - end
    av_time = round(time / max_islands, 2)
    time = round(time, 2)
    ImageLabel.place_forget()
    GuessFrame.place_forget()
    ResultLabel.configure(text = f"You guessed {misses} times wrong!\nYou took {time} seconds!\nYou took an average of {av_time} seconds per Island!")
    ResultLabel.place(relx = 0.5, rely = 0.5, anchor = "center")
            
    

def randomize_island():
    global state, max_islands, start
    for button in guessbuttons:
            button.configure(state = "active", bg = "SystemButtonFace")
    if state == 0:
        start = time.time()
        for widget in OptionsWidgets:
            widget.place_forget()
        state = 1
        ImageLabel.place(x = 190, y = 20)
        StartButton.place_forget()
        BackButton.place(x = 18, y = 20)
        GuessFrame.place(x = 0, y = 350)
        b1.grid(row = 0, column = 0, sticky="ew")
        b2.grid(row = 0, column = 1, sticky="ew")
        b3.grid(row = 0, column = 2, sticky="ew")
        b4.grid(row = 0, column = 3, sticky="ew")
        
        b5.grid(row = 1, column = 0, sticky="ew")
        b6.grid(row = 1, column = 1, sticky="ew")
        b7.grid(row = 1, column = 2, sticky="ew")
        b8.grid(row = 1, column = 3, sticky="ew")

        b9.grid(row = 2, column = 0, sticky="ew")
        b10.grid(row = 2, column = 1, sticky="ew")
        b11.grid(row = 2, column = 2, sticky="ew")
        b12.grid(row = 2, column = 3, sticky="ew")

        b13.grid(row = 3, column = 0, sticky="ew")
        b14.grid(row = 3, column = 1, sticky="ew")
        b15.grid(row = 3, column = 2, sticky="ew")
        b16.grid(row = 3, column = 3, sticky="ew")

        b17.grid(row = 4, column = 0, sticky="ew")
        b18.grid(row = 4, column = 1, sticky="ew")
        b19.grid(row = 4, column = 2, sticky="ew")
        b20.grid(row = 4, column = 3, sticky="ew")

        b21.grid(row = 5, column = 0, sticky="ew")
        b22.grid(row = 5, column = 1, sticky="ew")
        b23.grid(row = 5, column = 2, sticky="ew")
        b24.grid(row = 5, column = 3, sticky="ew")

        b25.grid(row = 6, column = 0, sticky="ew")
        b26.grid(row = 6, column = 1, sticky="ew")
        b27.grid(row = 6, column = 2, sticky="ew")
        b28.grid(row = 6, column = 3, sticky="ew")

        b29.grid(row = 7, column = 0, sticky="ew")
        b30.grid(row = 7, column = 1, sticky="ew")
        b31.grid(row = 7, column = 2, sticky="ew")
        b32.grid(row = 7, column = 3, sticky="ew")

        b33.grid(row = 8, column = 0, sticky="ew")
        b34.grid(row = 8, column = 1, sticky="ew")
        b35.grid(row = 8, column = 2, sticky="ew")
        b36.grid(row = 8, column = 3, sticky="ew")

        b37.grid(row = 9, column = 0, sticky="ew")
        b38.grid(row = 9, column = 1, sticky="ew")
        b39.grid(row = 9, column = 2, sticky="ew")
        b40.grid(row = 9, column = 3, sticky="ew")

        b41.grid(row = 10, column = 0, sticky="ew")
        b42.grid(row = 10, column = 1, sticky="ew")
        b43.grid(row = 10, column = 2, sticky="ew")
        b44.grid(row = 10, column = 3, sticky="ew")

        b45.grid(row = 11, column = 0, sticky="ew")
        b46.grid(row = 11, column = 1, sticky="ew")
        b47.grid(row = 11, column = 2, sticky="ew")
        b48.grid(row = 11, column = 3, sticky="ew")

        b49.grid(row = 12, column = 0, sticky="ew")
        b50.grid(row = 12, column = 1, sticky="ew")
        b51.grid(row = 12, column = 2, sticky="ew")
        b52.grid(row = 12, column = 3, sticky="ew")

        b53.grid(row = 13, column = 0, sticky="ew")
        b54.grid(row = 13, column = 1, sticky="ew")
        b55.grid(row = 13, column = 2, sticky="ew")
        b56.grid(row = 13, column = 3, sticky="ew")

        b57.grid(row = 14, column = 0, sticky="ew")
        b58.grid(row = 14, column = 1, sticky="ew")
        b59.grid(row = 14, column = 2, sticky="ew")
        b60.grid(row = 14, column = 3, sticky="ew")

        b61.grid(row = 15, column = 0, sticky="ew")
        b62.grid(row = 15, column = 1, sticky="ew")
        b63.grid(row = 15, column = 2, sticky="ew")
        b64.grid(row = 15, column = 3, sticky="ew")

        b65.grid(row = 16, column = 0, sticky="ew")
        b66.grid(row = 16, column = 1, sticky="ew")
        b67.grid(row = 16, column = 2, sticky="ew")
        b68.grid(row = 16, column = 3, sticky="ew")

        b69.grid(row = 17, column = 0, sticky="ew")
        b70.grid(row = 17, column = 1, sticky="ew")
        b71.grid(row = 17, column = 2, sticky="ew")
        b72.grid(row = 17, column = 3, sticky="ew")

        b73.grid(row = 18, column = 0, sticky="ew")
        b74.grid(row = 18, column = 1, sticky="ew")
        b75.grid(row = 18, column = 2, sticky="ew")
        b76.grid(row = 18, column = 3, sticky="ew")

        b77.grid(row = 19, column = 0, sticky="ew")
        b78.grid(row = 19, column = 1, sticky="ew")
        b79.grid(row = 19, column = 2, sticky="ew")
        b80.grid(row = 19, column = 3, sticky="ew")

        b81.grid(row = 20, column = 0, sticky="ew")
        b82.grid(row = 20, column = 1, sticky="ew")
        b83.grid(row = 20, column = 2, sticky="ew")
        b84.grid(row = 20, column = 3, sticky="ew")

        b85.grid(row = 21, column = 0, sticky="ew")
        b86.grid(row = 21, column = 1, sticky="ew")
        b87.grid(row = 21, column = 2, sticky="ew")
        b88.grid(row = 21, column = 3, sticky="ew")

        b89.grid(row = 22, column = 0, sticky="ew")
        b90.grid(row = 22, column = 1, sticky="ew")
        b91.grid(row = 22, column = 2, sticky="ew")
        b92.grid(row = 22, column = 3, sticky="ew")

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
        ImageLabel.configure(image = image, text = random_island)
        Name = Island_data[1]
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

StartButton = tk.Button(root, bg = "#33735e", font = "Papyrus 20 bold", text = "Start", command = lambda: randomize_island(), activebackground = "#33735e", height = 1, width = 5)

OptionsWidgets = [RegionLabel, PlentyReg, AncientReg, WildsReg, DevilsReg, NoReg,
                  SizeLabel, All, Big, Small,
                  ExtrasLabel, AddOutposts, AddForts, AddShrines, RemIslands]

ImageLabel = tk.Label(root, bg = bgcolor, image = tk.PhotoImage(file = "./data/default.png"), height = 320, width = 320)
#ImageLabel.place(x = 190, y = 20)

BackButton = tk.Button(root, bg = bgcolor, image = BackIm, command = lambda: back(), activebackground = bgcolor, bd = 0)

GuessFrame = tk.Frame(root, width = 700, height = 445, bg = bgcolor)
GuessFrame.grid_columnconfigure(0, minsize = 175)
GuessFrame.grid_columnconfigure(1, minsize = 175)
GuessFrame.grid_columnconfigure(2, minsize = 175)
GuessFrame.grid_columnconfigure(3, minsize = 175)

b1 = tk.Button(GuessFrame, text = "Ancient Spire Outpost", command= lambda: guess(69))
b2 = tk.Button(GuessFrame, text = "Ashen Reaches", command= lambda: guess(17))
b3 = tk.Button(GuessFrame, text = "Barnacle Cay", command= lambda: guess(7))
b4 = tk.Button(GuessFrame, text = "Black Sand Atoll", command= lambda: guess(59))

b5 = tk.Button(GuessFrame, text = "Black Water Enclave", command= lambda: guess(60))
b6 = tk.Button(GuessFrame, text = "Blind Man's Lagoon", command= lambda: guess(61))
b7 = tk.Button(GuessFrame, text = "Booty Isle", command= lambda: guess(8))
b8 = tk.Button(GuessFrame, text = "Boulder Cay", command= lambda: guess(43))

b9 = tk.Button(GuessFrame, text = "Brimstone Rock", command= lambda: guess(22))
b10 = tk.Button(GuessFrame, text = "Cannon Cove", command= lambda: guess(36))
b11 = tk.Button(GuessFrame, text = "Castaway Isle", command= lambda: guess(9))
b12 = tk.Button(GuessFrame, text = "Chicken Isle", command= lambda: guess(10))

b13 = tk.Button(GuessFrame, text = "Cinder Islet", command= lambda: guess(23))
b14 = tk.Button(GuessFrame, text = "Crescent Isle", command= lambda: guess(37))
b15 = tk.Button(GuessFrame, text = "Crook's Hollow", command= lambda: guess(0))
b16 = tk.Button(GuessFrame, text = "Crow's Nest Fortress", command= lambda: guess(78))

b17 = tk.Button(GuessFrame, text = "Cursewater Shores", command= lambda: guess(24))
b18 = tk.Button(GuessFrame, text = "Cutlass Cay", command= lambda: guess(11))
b19 = tk.Button(GuessFrame, text = "Dagger Tooth Outpost", command= lambda: guess(74))
b20 = tk.Button(GuessFrame, text = "Devil's Ridge", command= lambda: guess(1))

b21 = tk.Button(GuessFrame, text = "Discovery Ridge", command= lambda: guess(2))
b22 = tk.Button(GuessFrame, text = "Fetcher's Rest", command= lambda: guess(18))
b23 = tk.Button(GuessFrame, text = "Flame's End", command= lambda: guess(25))
b24 = tk.Button(GuessFrame, text = "Flintlock Peninsula", command= lambda: guess(19))

b25 = tk.Button(GuessFrame, text = "Fools Lagoon", command= lambda: guess(12))
b26 = tk.Button(GuessFrame, text = "Forsaken Brink", command= lambda: guess(26))
b27 = tk.Button(GuessFrame, text = "Fort of the Damned", command= lambda: guess(76))
b28 = tk.Button(GuessFrame, text = "Galleon's Grave", command= lambda: guess(75))

b29 = tk.Button(GuessFrame, text = "Glowstone Cay", command= lambda: guess(27))
b30 = tk.Button(GuessFrame, text = "Hidden Spring Keep", command= lambda: guess(80))
b31 = tk.Button(GuessFrame, text = "Isle of Last Words", command= lambda: guess(62))
b32 = tk.Button(GuessFrame, text = "K-9", command= lambda: guess(34))

b33 = tk.Button(GuessFrame, text = "Keel Haul Fort", command= lambda: guess(81))
b34 = tk.Button(GuessFrame, text = "Kraken Watchtower", command= lambda: guess(83))
b35 = tk.Button(GuessFrame, text = "Kraken's Fall", command= lambda: guess(53))
b36 = tk.Button(GuessFrame, text = "Lagoon of Whispers", command= lambda: guess(44))

b37 = tk.Button(GuessFrame, text = "Liar's Backbone", command= lambda: guess(63))
b38 = tk.Button(GuessFrame, text = "Lone Cove", command= lambda: guess(38))
b39 = tk.Button(GuessFrame, text = "Lonely Isle", command= lambda: guess(45))
b40 = tk.Button(GuessFrame, text = "Lookout Point", command= lambda: guess(13))

b41 = tk.Button(GuessFrame, text = "Lost Gold Fort", command= lambda: guess(77))
b42 = tk.Button(GuessFrame, text = "Magma's Tide", command= lambda: guess(28))
b43 = tk.Button(GuessFrame, text = "Marauder's Arch", command= lambda: guess(54))
b44 = tk.Button(GuessFrame, text = "Mermaid's Hideaway", command= lambda: guess(39))

b45 = tk.Button(GuessFrame, text = "Molten Sands Fortress", command= lambda: guess(79))
b46 = tk.Button(GuessFrame, text = "Morrow's Peak Outpost", command= lambda: guess(71))
b47 = tk.Button(GuessFrame, text = "Mutineer Rock", command= lambda: guess(14))
b48 = tk.Button(GuessFrame, text = "New Golden Sands Outpost", command= lambda: guess(72))

b49 = tk.Button(GuessFrame, text = "N-13", command= lambda: guess(35))
b50 = tk.Button(GuessFrame, text = "Old Faithful Isle", command= lambda: guess(55))
b51 = tk.Button(GuessFrame, text = "Old Salts Atoll", command= lambda: guess(15))
b52 = tk.Button(GuessFrame, text = "Paradise Spring", command= lambda: guess(16))

b53 = tk.Button(GuessFrame, text = "Picaroon Palms", command= lambda: guess(46))
b54 = tk.Button(GuessFrame, text = "Plunder Outpost", command= lambda: guess(70))
b55 = tk.Button(GuessFrame, text = "Plunder Valley", command= lambda: guess(3))
b56 = tk.Button(GuessFrame, text = "Plunderer's Plight", command= lambda: guess(64))

b57 = tk.Button(GuessFrame, text = "Rapier Cay", command= lambda: guess(47))
b58 = tk.Button(GuessFrame, text = "Reaper's Hideout", command= lambda: guess(32))
b59 = tk.Button(GuessFrame, text = "Roaring Sands", command= lambda: guess(29))
b60 = tk.Button(GuessFrame, text = "Ruby's Fall", command= lambda: guess(20))

b61 = tk.Button(GuessFrame, text = "Rum Runner Isle", command= lambda: guess(48))
b62 = tk.Button(GuessFrame, text = "Sailor's Bounty", command= lambda: guess(40))
b63 = tk.Button(GuessFrame, text = "Sailor's Knot Stronghold", command= lambda: guess(82))
b64 = tk.Button(GuessFrame, text = "Salty Sands", command= lambda: guess(49))

b65 = tk.Button(GuessFrame, text = "Sanctuary Outpost", command= lambda: guess(73))
b66 = tk.Button(GuessFrame, text = "Sandy Shallows", command= lambda: guess(50))
b67 = tk.Button(GuessFrame, text = "Scorched Pass", command= lambda: guess(30))
b68 = tk.Button(GuessFrame, text = "Scurvy Island", command= lambda: guess(65))

b69 = tk.Button(GuessFrame, text = "Sea Dog's Rest", command= lambda: guess(51))
b70 = tk.Button(GuessFrame, text = "Sea Dog's Tavern", command= lambda: guess(31))
b71 = tk.Button(GuessFrame, text = "Shark Bait Cove", command= lambda: guess(4))
b72 = tk.Button(GuessFrame, text = "Shark Fin Camp", command= lambda: guess(84))

b73 = tk.Button(GuessFrame, text = "Shark Tooth Key", command= lambda: guess(66))
b74 = tk.Button(GuessFrame, text = "Shipwreck Bay", command= lambda: guess(56))
b75 = tk.Button(GuessFrame, text = "Shiver Retreat", command= lambda: guess(67))
b76 = tk.Button(GuessFrame, text = "Shrine of Ancient Tears", command= lambda: guess(86))

b77 = tk.Button(GuessFrame, text = "Shrine of Flooded Embrace", command= lambda: guess(90))
b78 = tk.Button(GuessFrame, text = "Shrine of Hungering", command= lambda: guess(91))
b79 = tk.Button(GuessFrame, text = "Shrine of Ocean's Fortune", command= lambda: guess(88))
b80 = tk.Button(GuessFrame, text = "Shrine of Tribute", command= lambda: guess(87))

b81 = tk.Button(GuessFrame, text = "Shrine of the Coral Tomb", command= lambda: guess(89))
b82 = tk.Button(GuessFrame, text = "Skull Keep", command= lambda: guess(85))
b83 = tk.Button(GuessFrame, text = "Smuggler's Bay", command= lambda: guess(41))
b84 = tk.Button(GuessFrame, text = "Snake Island", command= lambda: guess(5))

b85 = tk.Button(GuessFrame, text = "The Crooked Masts", command= lambda: guess(57))
b86 = tk.Button(GuessFrame, text = "The Devil's Thirst", command= lambda: guess(21))
b87 = tk.Button(GuessFrame, text = "The Sunken Grove", command= lambda: guess(58))
b88 = tk.Button(GuessFrame, text = "Thieves' Haven", command= lambda: guess(6))

b89 = tk.Button(GuessFrame, text = "Tri-Rock Isle", command= lambda: guess(68))
b90 = tk.Button(GuessFrame, text = "Tribute Peak", command= lambda: guess(33))
b91 = tk.Button(GuessFrame, text = "Twin Groves", command= lambda: guess(52))
b92 = tk.Button(GuessFrame, text = "Wanderers Refuge", command= lambda: guess(42))

guessbuttons = [b15, b20, b21, b55, b71, b84, b88, b3, b7, b11, b12, b18, b25, b40, b47, b51, b52, b2, b22, b24,
                b60, b86, b9, b13, b17, b23, b26, b29, b42, b59, b67, b70, b58, b90, b32, b49, b10, b14, b38, b44,
                b62, b83, b92, b8, b36, b39, b53, b57, b61, b64, b66, b69, b91, b35, b43, b50, b74, b85, b87, b4,
                b5, b6, b31, b37, b56, b68, b73, b75, b89, b1, b54, b46, b48, b65, b19, b28, b27, b41, b16, b45,
                b30, b33, b63, b34, b72, b82, b76, b80, b79, b81, b77, b78]

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
