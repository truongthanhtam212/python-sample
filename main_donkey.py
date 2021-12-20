import donkeylogic
import donkeydefs
import donkeyinterface

"""
Goal: Make a user interface module for an otherwise functioning donkeygotchi.
"""
def main():
    donkeydata = donkeylogic.init()
    
    while True:
        donkeyinterface.show_state(donkeydata)
        choice = donkeyinterface.prompt_choice(donkeydata)
        if choice == donkeydefs.QUIT:
            break
        elif choice == donkeydefs.FEED:
            donkeylogic.feed(donkeydata)
        elif choice == donkeydefs.TICKLE:
            donkeylogic.tickle(donkeydata)
        elif choice == donkeydefs.WORK:
            donkeylogic.work(donkeydata)
        elif choice == donkeydefs.RESET:
            donkeydata = donkeylogic.init()

if __name__ == "__main__":
    main()