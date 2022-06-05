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
    print("Press 'A' to randomly generate Agents")
    enter()
    print("Press 'W' To randomly Generate Weapons")
    enter()
    print("Press 'E' to generate abilities")
    enter()
    print("Press 'S' To generate shields")
    enter()
    print("Press 'C' for credits")
    enter()
    print("Hold 'Q' to exit")
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
def invalid():
    enter()
    print("Sorry your input is invalid please try again")
    tc()
    intro()
#---------------------------
intro()
#Makes an infinite reapeating loop
while True:
    if keyboard.read_key() == "q":#Detects if the user presses a button on their keyboard in this case its 'q'
        cls()
        print("Made by Xanthus In my spare time")
        enter()
        print("Check out my other works at https://github.com/Xanthus58")
        enter()
        print("Email me on 'Xanthus58@protonmail.com'")
        enter()
        print("Feel free to fork; submit issues; or otherwise interact with the project here!")
        print("https://github.com/Xanthus58/Valorant-Randomizer")
        time.sleep(5)
        break #Closes the application
    #When "C" is pressed it will show my credits
    elif keyboard.read_key() == "a": #Registers keyboard inputs in this case its the letter "A"
        #Lists all of the current agents in the game, in colour
        agents = [Fore.YELLOW +  'Breach, ',Fore.YELLOW +  'Killjoy, ',Fore.BLUE +  'Neon, ',Fore.MAGENTA +  'Astra, ',Fore.YELLOW +  'Brimstone, ',Fore.YELLOW +  'Chamber, ','Cypher, ',Fore.BLUE +  'Jett, ',Fore.BLUE +  'Kayo, ',Fore.MAGENTA + 'Omen, ',Fore.YELLOW +  'Phoenix, ',Fore.YELLOW +  'Raze, ',Fore.MAGENTA +  'Reyna, ',Fore.GREEN +  'Sage, ',Fore.GREEN +  'Skye, ',Fore.BLUE +  'Sova, ',Fore.GREEN +  'Viper, ',Fore.BLUE +  'Yoru, ',Fore.RED +  'Fade, ']
        #Displays a message on singular or team selection
        cls()
        print("Press 1 to generate a singular Agent.")
        enter()
        print("Press 2 to generate team Agents")
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
            input("Press Enter to return \n")#Awaits user input before returning to the intro
            intro()
            #Same Code as above; just edited
        else:
            invalid()
    elif keyboard.read_key() == "e":
        white()
        cls()
        Abilities = ["C,", "Q,", "E,", "None,", "All,", "C+Q,", "C+E,", "Q+E,", "Q+C,"]
        print("Press 1 to generate a singular ability")
        enter()
        print("Press 2 to generate team abilites")
        if keyboard.read_key() == "1":
            gen()
            print(random.choice(Abilities))
            time.sleep(5)
            intro()
        elif keyboard.read_key() == "2":
            e1 = random.choice(Abilities)
            e2 = random.choice(Abilities)
            e3 = random.choice(Abilities)
            e4 = random.choice(Abilities)
            e5 = random.choice(Abilities)
            gen()
            print(e1,e2,e3,e4,e5)
            enter()
            input("Press Enter to return\n")
            intro()
        else:
            invalid()
    elif keyboard.read_key() == "w":
        weapons = [Fore.WHITE + 'Classic, ',Fore.MAGENTA + 'Shorty, ',Fore.YELLOW + 'Frenzy, ',Fore.WHITE +  'Ghost, ',Fore.WHITE +  'Sheriff, ',Fore.YELLOW + 'Stinger, ',Fore.YELLOW + 'Spectre, ',Fore.MAGENTA + 'Bucky, ',Fore.MAGENTA + 'Judge, ',Fore.RED +  'Bulldog, ',Fore.RED +  'Guardian, ',Fore.RED +  'Phantom, ',Fore.RED +  'Vandal, ',Fore.CYAN + 'Marshal, ',Fore.CYAN + 'Operator, ',Fore.RED +  'Ares, ',Fore.RED +  'Odin, ',Fore.WHITE +  'Knife, ']
        white()
        cls()
        print("Press 1 to generate a singular weapon.")
        enter()
        print("Press 2 to generate team weapons")
        if keyboard.read_key() == '1':
            gen()
            print(random.choice(weapons))
            time.sleep(5)
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
            input("Press Enter to return\n")
            intro()
            #Same Code as above; just edited
        else:
            invalid()
    elif keyboard.read_key() == 's':
        shields = [Fore.YELLOW + 'Light, ',Fore.GREEN + 'Heavy, ',Fore.WHITE + 'None, ']
        white()
        cls()
        print("Press 1 to generate a singular sheild.")
        enter()
        print("Press 2 to generate team sheilds")
        if keyboard.read_key() == '1':
            gen()
            print(random.choice(shields))
            time.sleep(5)
            intro()
        elif keyboard.read_key() == '2':
            s1 = random.choice(shields)
            s2 = random.choice(shields)
            s3 = random.choice(shields)
            s4 = random.choice(shields)
            s5 = random.choice(shields)
            gen()
            print(s1 + s2 + s3 + s4 + s5)
            enter()
            white()
            input("Press Enter to return\n")
            intro()
        else:
            invalid()
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
        input("Press Enter to return to the main menu\n")
        cls()
        intro()