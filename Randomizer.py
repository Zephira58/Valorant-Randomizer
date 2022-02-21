import random
import keyboard
from colorama import Fore, Back, Style
import os
import time

def t5():
    time.sleep(.5)
def t():
    time.sleep(5)
def cls():
    os.system('cls||clear')
def enter():
    print("")
def tc():
    time.sleep(5)
    os.system('cls||clear')


def intro():
    cls()
    print("Hold 'A' to randomly generate Agents")
    enter()
    print("Hold 'W' To randomly Generate Weapons")
    enter()
    print("Hold 'S' To generate sheilds")
    enter()
    print("Hold 'Q' to exit")
    enter()
    print("Hold 'C' for credits")
    enter()
    print("Hold 'Z' to choose a colour")
    enter()

def gen():
    cls()
    print('Generating')
    t5()
    cls()
    print('Generating.')
    t5()
    cls()
    print('Generating..')
    t5()
    cls()
    print('Generating...')
    cls()

intro()

while True:
    if keyboard.read_key() == "a":
        agents = ['Breach ', 'Killjoy ', 'Neon ', 'Astra ', 'Brimstone ', 'Chamber ', 'Cypher ', 'Jett ', 'Kayo ', 'Omen ', 'Phoenix ', 'Raze ', 'Reyna ', 'Sage ', 'Skye ', 'Sova ', 'Viper ', 'Yoru ']
        a1 = random.choice(agents)
        a2 = random.choice(agents)
        a3 = random.choice(agents)
        a4 = random.choice(agents)
        a5 = random.choice(agents)
        cls()
        print("Press 1 to generate a singular Agent.")
        enter()
        print("Press 2 to generate team Agents")
        time.sleep(1)
        if keyboard.read_key() == '1':
            gen()
            print(random.choice(agents))
            tc()
            intro()
        elif keyboard.read_key() == '2':
            a1 = random.choice(agents)
            a2 = random.choice(agents)
            a3 = random.choice(agents)
            a4 = random.choice(agents)
            a5 = random.choice(agents)
            gen()
            print(a1 + a2 + a3 + a4 + a5)
            enter()
            input("Press Enter to return: ")
            intro()    
    elif keyboard.read_key() == "w":
        weapons = ['Classic ', 'Shorty ', 'Frenzy ', 'Ghost ', 'Sheriff ', 'Stinger ', 'Spectre ', 'Bucky ', 'Judge ', 'Bulldog ', 'Guardian ', 'Phantom ', 'Vandal ', 'Marshal ', 'Operator ', 'Ares ', 'Odin ', 'Knife ']
        cls()
        print("Press 1 to generate a singular weapon.")
        enter()
        print("Press 2 to generate team weapons")
        time.sleep(1)
        if keyboard.read_key() == '1':
            gen()
            print(random.choice(weapons))
            tc()
            intro()
        elif keyboard.read_key() == '2':
            w1 = random.choice(weapons)
            w2 = random.choice(weapons)
            w3 = random.choice(weapons)
            w4 = random.choice(weapons)
            w5 = random.choice(weapons)
            gen()
            print(w1 + w2 + w3 + w4 + w5)
            enter()
            input("Press Enter to return: ")
            intro()
    elif keyboard.read_key() == 's':
        shields = ['Light ', 'Heavy ', 'None ']
        cls()
        print("Press 1 to generate a singular sheild.")
        enter()
        print("Press 2 to generate team sheilds")
        time.sleep(1)
        time.sleep(1)
        if keyboard.read_key() == '1':
            gen()
            print(random.choice(shields))
            tc()
            intro()
        elif keyboard.read_key() == '2':
            gen()
            s1 = random.choice(shields)
            s2 = random.choice(shields)
            s3 = random.choice(shields)
            s4 = random.choice(shields)
            s5 = random.choice(shields)
            gen()
            print(s1 + s2 + s3 + s4 + s5)
            enter()
            input("Press Enter to return: ")
            intro()
    elif keyboard.read_key() == "z":
        cls()
        print(Fore.RED +"Hold R for the colour Red")
        print(Fore.BLUE + "Hold B for the colour Blue")
        print(Fore.GREEN + "Hold G for the colour Green")
        print(Fore.YELLOW + "Hold Y for the colour Yellow")
        print(Fore.WHITE)
        time.sleep(1)
    #If the user presses one of the colour buttons on the main menu; or colour menu. It will change the text to be that colour!
    elif keyboard.read_key() == "r":
        cls()
        print(Fore.RED + "You have chosen the colour red!")
        time.sleep(5)
        cls()
        intro()
    elif keyboard.read_key() == "y":
        cls()
        print(Fore.YELLOW + "You have chosen the colour Yellow!")
        time.sleep(5)
        cls()
        intro()
    elif keyboard.read_key() == "b":
        cls()
        print(Fore.BLUE + "You have chosen the colour blue!")
        time.sleep(5)
        cls()
        intro()
    elif keyboard.read_key() == "g":
        cls()
        print(Fore.GREEN + "You have chosen the colour Green!")
        time.sleep(5)
        cls()
        intro()
    #When "Q" is pressed it will shut down the application.
    elif keyboard.read_key() == "q":
        cls()
        print("I hope you have a wonderful day!")
        time.sleep(5)
        break
    #When "C" is pressed it will show the my credits
    elif keyboard.read_key() == "c":
        cls()
        print("Made by Xanthus In my spare time")
        enter()
        print("Check out my other works at https://github.com/Xanthus58")
        enter()
        print("Email me on 'Xanthus58@protonmail.com'")
        enter()
        print("Feel free to fork; submit issues; or otherwise interact with the project here!")
        print("https://github.com/Xanthus58/Valorant-Randomizer")
        enter()
        input("Press Enter to return to the main menu.")
        cls()
        intro()
    else:
        intro()