#Create Character And Stage Select Mode For A Fighting Game

#Fighters Dictionary to Select Fighter By #
fighters = {
        1: "Axel",
        2: "Skate", 
        3: "Mai",
        4: "Ryu",
        5: "King",
        6: "Sagat",
        7: "Dhalsim",
        8: "Terry Bogard",
        9: "M. Bison",
        10: "Hayabusa",
        11: "Felicia",
        12: "Zangief",
        13: "Kitana"
}

#Bosses Dictionary to Select Boss by Special Code
bosses = {
        "B1": "Keisha",
        "B2": "Shin Akuma",
        "B3": "Dr. Robotnik",
        "B4": "Lord Zeed",
        "B5": "Brother Umar da Conquered",
        "B6": "Kage",
        "B7": "Shredder"    
}

#Mode Dictionary to Select Stage by Special Code
mode = {
            "A": "Eiffel Tower",
            "B": "Easter Island",
            "C": "Tokyo Tower",
            "D": "Statue Of Liberty",
            "E": "London Bridge",
            "F": "Taj Mahal",
            "G": "Keisha's House"
        }

#Game Title

game = "Kang Of Fighterz"

#player select menu

player = int(input(f"{game}\n\nPress # To Select Your Fighter \n\n{fighters} \n(Press 0 to Quit): "))

if not player == 0:
   
    while not fighters.get(player):
        print("You Did Not Choose the Correct #!")
        player = int(input(f"Press # To Select Your Fighter \n\n{fighters} \n(Press 0 to Quit): "))
        
    else:
        print(f"You Chose {fighters.get(player)}")

#stage mode select menu
    stage  = input(f"Press Code To Select Stage \n\n{mode} \n(Press Q to Quit): ")
    
    if not stage == "Q":
            while not mode.get(stage):
                print("You Did Not Choose The Correct Stage!")
                stage  = input(f"Press Code To Select Stage \n\n{mode} \n(Press Q to Quit): ")

#boss mode select menu
    enemy = input(f"Press Code To Select Boss \n\n{bosses} \n(Press Q to Quit): ")
    if not enemy == 'Q':
            while not bosses.get(enemy):
                print("Invalid Number!")
                enemy = input(f"Press Code To Boss \n\n{bosses} \n(Press Q to Quit): ")

#Loading match
    
            print(f"\n\nLoading {game} [...]\n\nRound 1: Stage: {mode.get(stage)}\n----------------------------------\nFighter: {fighters.get(player)} | Opponent: {bosses.get(enemy)}\n\nGET READY!!!")
    else:            

#To Shutdown Game After Quitting Stage Mode Menu

        print(f"\n\nShutting Down {game} ...\n\n GOOD BYE!!!")        
else:

#To Shutdown Game After Quitting on Player Select

    print(f"\n\nShutting Down {game} ... \n\nGOOD BYE!!")

