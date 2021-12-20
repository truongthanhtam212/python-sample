"""
Defines the donkeygothi's user interface.
"""
def show_state(donkeydata):
    print("The donkey is {} years old and has {} eur.\nSatiation: {}\nHappiness: {}\nEnergy: {}"
    .format(
    donkeydata["AGE"],
    donkeydata["MONEY"],
    donkeydata["SATIATION"],
    donkeydata["HAPPINESS"],
    donkeydata["ENERGY"]))
    if donkeydata["RETIRED"] == True:    
        print("The donkey has retired.")

def prompt_choice(donkeydata):
    if donkeydata["RETIRED"] == False:
        choices = ["q", "f", "t", "w"]
        print("Choices: q, f, w, t")
        while True:
            choice = input("Input next choice: ")
            if choice in choices:
                return choice
            else:
                print("Invalid input!")
    else:
        choices = ["q", "r"]
        print("Choices: q, r")
        while True:
            choice = input("Input next choice: ")
            if choice in choices:
                return choice
            else:
                print("Invalid input!")
                