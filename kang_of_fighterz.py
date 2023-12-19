import argparse

#Create Character And Stage Select Mode For A Fighting Game

#Fighters Dictionary to Select Fighter by Number
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

#Game Title -- "Kang Of Fighterz"

# fighter input by number
def select_fighter(fighter_number):
    return fighters.get(fighter_number, "Invalid Fighter Number")
        
# stage input by code
def select_stage(stage_code):
    return mode.get(stage_code, "Invalid Stage Code")
        
# boss input by code
def select_boss(boss_code):
    return bosses.get(boss_code, "Invalid Boss Code")

# error message after making an invalid input (fighter/stage/boss)
def error_code():
    print("Invalid selection made. Please check your inputs.")

# Loading game after selecting figher, stage, and boss
def load_match():
    print(f"\n\nLoading Kang Of Fighterz [...]\n\nRound 1: Stage: {selected_stage}\n----------------------------------\nFighter: {selected_fighter} | Opponent: {selected_boss}\n\nGET READY!!!")

# Dictionary definitions (fighters, bosses, mode) remain the same

# Parsing command-line arguments
# example arguments : '--fighter [1-13] --stage [A-G] --boss [B1-B7]'
parser = argparse.ArgumentParser(description='Kang Of Fighterz Game Setup')
parser.add_argument('--fighter', type=int, required=True, help='Number of the fighter')
parser.add_argument('--stage', type=str, required=True, help='Code of the stage')
parser.add_argument('--boss', type=str, required=True, help='Code of the boss')

args = parser.parse_args()

# Selecting fighter, stage, and boss
selected_fighter = select_fighter(args.fighter)
selected_stage = select_stage(args.stage)
selected_boss = select_boss(args.boss)

# Checking for valid selections
if selected_fighter == "Invalid Fighter Number" or selected_stage == "Invalid Stage Code" or selected_boss == "Invalid Boss Code":
    error_code()
else:
    load_match()
