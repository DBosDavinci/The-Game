# The Game

name = input("Welcome to The Game Zombie apocalypse, please choose your name!")
print("The objective of this game is to reach the airport, which is close to the forest outside of the city. Once you get there you can escape from the zombie infected city.")

keuze1 = input(name,"wakes up in an empty factory, he hears some growling. He turns around and sees a zombie at the entrance of the factory. What will he do?\n"
"a) Run for it\n"
"b) Look for a weapon to slaughter it")

if keuze1 == "A" or "a":
    keuze2 = input(name,"chose to run for it. They walk outside and see a forest close by and a hospital on the opposite side of the road. Where will",name,"go?\n"
    "a) Go to the nearby forest\n"
    "b) Go to the hospital on the opposite side of road")
    if keuze2 == "A" or "a":
        keuze3 = input(name,"arrives in the forest, you arrive at an abandoned house. Will you go inside or go further into the forest?\n"
        "a) Enter the abandoned house\n"
        "b) Go deeper into the forest?")
        if keuze3 == "a" or "A":
            keuze4 = input()
            if keuze4 == "a" or "A":
                keuze5 = input()
                if keuze5 == "a" or "A":
                    keuze6 = input()
                    if keuze6 == "a" or "A":
                        keuze7 = input()
                        if keuze7 == "a" or "A":
                            print(name,"chooses to go left")
                        if keuze7 == "b" or "B":
                            keuze8 = input()
                            if keuze8 == "a" or "A":
                                keuze9 = input()
                                if keuze9 == "a" or "A":
                                    print()
                                if keuze9 == "b" or "B":
                                    keuze10 = input()
                                    if keuze10 == "a" or "B":
                                        print("You walk to the man on the airport, just before you can open your mouth to speak to him you notice he has a weird look on his face. The man walks straight towards you and you try"
                                        "to run from him, but there is already a swarm of zombies behind you. RIP")
                                    if keuze10 == "b" or "B":
                                        print("You walk to the airplane, you drive onto the flying path. A swarm of zombies is coming after you, but you are out of reach. You fly away and you completed the game! Congratulations",name,"!")
                            if keuze8 == "b" or "B":
                                print()                   
                    if keuze6 == "b" or "B":
                        input()                
                if keuze5 == "b" or "B":
                    keuze6 = input("In the house you encounter a zombie, will you attack it or run from it?\n"
                    "a) Attack the zombie\n"
                    "b) Run from the zombie")
                    if keuze6 == "a" or "A":
                        print("You try to attack the zombie, but you fail to swing at the zombie because you don't have enough energy left.")
                    if keuze6 == "b" or "B":
                        print("You try to run from the zombie, but you don't have enough energy left. RIP")
    if keuze2 == "B" or "b":
        keuze3 = input("You walk up to the hospital, but the front door is open. You also spot a broken window on the side of the building.")
        if keuze3 == "a" or "A":
            print("You enter through the front door, but you immediately get ambushed by 3 zombies. RIP")
        if keuze3 == "b" or "B":
            keuze4 = input("You climb through the broken window, it's totally dark inside but you can see something shiny lying on the ground. You pick it up, to inspect it and you find out it's a needle. You feel pretty tired, but is it a good idea to inject yourself?\n"
            "a) Inject yourself with the needle you found lying on the ground.\n"
            "b) Don't inject yourself with the needle you found lying on the ground.")
            if keuze4 == "a" or "A":
                keuze5 = input("After injecting yourself with the needle, you start to feel pretty sick and dizzy. It probably wasn't a good idea to inject yourself with a needle, but how are you going to fix this?\n"
                "a) Drink some water and wait it out\n"
                "b) Inject yourself with some other needles lying on the ground")
                if keuze5 == "a" or "A":
                    keuze6 = input("After drinking some water, you don't feel any better, but you decide to move on. on the streets you see some zombies, will you go further inside the hospital or will you kill the zombies for food?\n"
                    "a) Go further inside the hospital\n"
                    "b) Kill the zombies on the street")
                    if keuze6 == "a" or "A":
                        keuze7 = input("Going further inside the hospital, you hear a zombie behind you, what will you do\n"
                        "a) Try to kill the zombie\n"
                        "b) Try to run away")
                    if keuze6 == "b" or "B":
                        print("You try to kill the zombies, but fail. They outnumbered you. RIP")
                if keuze5 == "b" or "B":
                    print("You die from an overdose. RIP")
            if keuze4 == "b" or "B":
                keuze5 = input("You walk further into the hospital, ")
if keuze1 == "b" or "B":
    keuze2 = input("You find a broken glass bottle on the floor, you can use to try to kill the zombie. Will you try it?\n"
    "a) Attack the zombie\n"
    "b) Look for more weapons outside")
    if keuze2 == "a" or "A":
        print(name,"tries to kill the zombie, you succeed, but while you were killing it 5 other zombies entered the building. RIP")
    if keuze2 == "b" or "B":
        keuze3 = input()
        if keuze3 == "a" or "A":
            keuze4 = input()
            if keuze4 == "a" or "A":
                keuze5 = input()
                if keuze5 == "a" or "A":
                    print()
                if keuze5 == "b" or "B":
                    keuze6 = input()
                    if keuze6 == "a" or "A":
                        keuze7 = input()
                        if keuze7 == "a" or "A":
                            keuze8 = input()
                            if keuze8 == "a" or "A":
                                print()
                            if keuze8 == "b" or "B":
                                keuze9 = input()
                                if keuze9 == "a" or "A":
                                    print()
                                if keuze9 == "b" or "B":
                                    print()
                        if keuze7 == "b" or "B":
                            print()
                    if keuze6 == "b" or "B":
                        print()
            if keuze4 == "b" or "B":
                print()
        if keuze3 == "b" or "B":
            print()