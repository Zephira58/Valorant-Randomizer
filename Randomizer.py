#Importing all of the required modules for the application
import random
import keyboard
from colorama import Fore, Back, Style
import os
import time
#------------
#Essential Definitions this is going to carry across all of my projects
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
def white():
    print(Fore.WHITE)
#---------------------------
#Application spesific definitions their tied to directly called up aspects of the main application, Such as menus.
def intro():
    white()
    cls()
    print("Hold 'A' to randomly generate Agents")
    enter()
    print("Hold 'W' To randomly Generate Weapons")
    enter()
    print("Hold 'S' To generate shields")
    enter()
    print("Hold 'Q' to exit")
    enter()
    print("Hold 'C' for credits")
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
#---------------------------
intro()
#Makes an infinite reapeating loop
while True:
    if keyboard.read_key() == "a": #Registers keyboard inputs in this case its the letter "A"
        #Lists all of the current agents in the game, in colour
        agents = [Fore.YELLOW +  'Breach, ',Fore.YELLOW +  'Killjoy, ',Fore.BLUE +  'Neon, ',Fore.MAGENTA +  'Astra, ',Fore.YELLOW +  'Brimstone, ',Fore.YELLOW +  'Chamber, ','Cypher, ',Fore.BLUE +  'Jett, ',Fore.BLUE +  'Kayo, ',Fore.MAGENTA + 'Omen, ',Fore.YELLOW +  'Phoenix, ',Fore.YELLOW +  'Raze, ',Fore.MAGENTA +  'Reyna, ',Fore.GREEN +  'Sage, ',Fore.GREEN +  'Skye, ',Fore.BLUE +  'Sova, ',Fore.GREEN +  'Viper, ',Fore.BLUE +  'Yoru, ']
        #Displays a message on singular or team selection
        cls()
        print("Press 1 to generate a singular Agent.")
        enter()
        print("Press 2 to generate team Agents")
        time.sleep(1)
        if keyboard.read_key() == '1': # Detects if the user presses 1 or 2 on their keyboard and reacts acordingly
            gen() #Displays the generating animation
            print(random.choice(agents)) #Displays the singular agent
            tc()#Clears the terminal after 5 secconds
            intro()#Displays the intro once again
        elif keyboard.read_key() == '2':
            #Randomly chooses an agent for each member of the team
            a1 = random.choice(agents)
            a2 = random.choice(agents)
            a3 = random.choice(agents)
            a4 = random.choice(agents)
            a5 = random.choice(agents)
            #Seccond infinate loop makes it impossible to get 2 of the same agents in 1 team as it'll choose again if it detects a similarity
            while True:
                if a1 == a2 or a1 == a3 or a1 == a4 or a1 == a5:
                    a1 = random.choice(agents)
                elif a2 == a1 or a2 == a3 or a2 == a4 or a2 == a5:
                    a2 = random.choice(agents)
                elif a3 == a1 or a3 == a2 or a3 == a4 or a3 == a5:
                    a3 = random.choice(agents)
                elif a4 == a1 or a4 == a3 or a4 == a2 or a4 == a5:
                    a4 = random.choice(agents)
                elif a5 == a1 or a5 == a3 or a5 == a4 or a5 == a2:
                    a5 = random.choice(agents)
                else:
                    break
            gen()#Displays the generating animation
            print(a1 + a2 + a3 + a4 + a5)#Displays all 5 agents that where randomly chosen
            enter()#Effectivly mimicing a return in the terminal; creating a new line
            white()#Sets the terminal colour back to white; from rendering colourd agents
            input("Press Enter to return: ")#Awaits user input before returning to the intro
            intro()
            #Same Code as above; just edited
    elif keyboard.read_key() == "w":
        weapons = ['Classic, ', 'Shorty, ', 'Frenzy, ', 'Ghost, ', 'Sheriff, ', 'Stinger, ', 'Spectre, ', 'Bucky, ', 'Judge, ', 'Bulldog, ', 'Guardian, ', 'Phantom, ', 'Vandal, ', 'Marshal, ', 'Operator, ', 'Ares, ', 'Odin, ', 'Knife ']
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
            white()
            input("Press Enter to return: ")
            intro()
            #Same Code as above; just edited
    elif keyboard.read_key() == 's':
        shields = ['Light, ', 'Heavy, ', 'None ']
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
            white()
            input("Press Enter to return: ")
            intro()
    elif keyboard.read_key() == "q":#Detects if the user presses a button on their keyboard in this case its 'q'
        exit() #Closes the aqqqpplication
    #When "C" is pressed it will show the my credits
    elif keyboard.read_key() == "c":#Detects if the user presses a button on their keyboard in this case its 'c'
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
        input("Press Enter to return to the main menu: ")
        cls()
        intro()