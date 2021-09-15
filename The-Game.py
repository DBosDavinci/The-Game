# The Game

name = input("Welcome to The Game Zombie apocalypse, please choose your name!")
print("The objective of this game is to reach the airport, which is close to the forest outside of the city. Once you get there you can escape from the zombie infected city.")

keuze1 = input("You wake up in an empty factory, he hears some growling. You around and sees a zombie at the entrance of the factory. What will he do?\n"
"a) Run for it\n"
"b) Look for a weapon to slaughter it")

if keuze1 == "a" or keuze1 == "A":
    keuze2 = input("You chose to run for it. You walk outside and see a forest close by and a hospital on the opposite side of the road. Where will you go?\n"
    "a) Go to the nearby forest\n"
    "b) Go to the hospital on the opposite side of road")
    if keuze2 == "a" or keuze2 == "A":
        keuze3 = input("You arrive in the forest, you arrive at an abandoned house. Will you go inside or go further into the forest?\n"
        "a) Enter the abandoned house\n"
        "b) Go deeper into the forest?")
        if keuze3 == "a" or keuze3 == "A":
            keuze4 = input()
            if keuze4 == "a" or keuze4 == "A":
                keuze5 = input()
                if keuze5 == "a" or keuze5 == "A":
                    keuze6 = input()
                    if keuze6 == "a" or keuze6 == "A":
                        keuze7 = input()
                        if keuze7 == "a" or keuze7 == "A":
                            print(name,"chooses to go left")
                        elif keuze7 == "b" or keuze7 == "B":
                            keuze8 = input()
                            if keuze8 == "a" or keuze8 == "A":
                                keuze9 = input()
                                if keuze9 == "a" or keuze9 == "A":
                                    print()
                                elif keuze9 == "b" or keuze9 == "B":
                                    keuze10 = input()
                                    if keuze10 == "a" or keuze10 == "A":
                                        print("You walk to the man on the airport, just before you can open your mouth to speak to him you notice he has a weird look on his face. The man walks straight towards you and you try"
                                        "to run from him, but there is already a swarm of zombies behind you. RIP")
                                    elif keuze10 == "b" or keuze10 == "B":
                                        print("You walk to the airplane, you drive onto the flying path. A swarm of zombies is coming after you, but you are out of reach. You fly away and you completed the game! Congratulations",name,"!")
                            elif keuze8 == "b" or keuze8 == "B":
                                print()                   
                    elif keuze6 == "b" or keuze6 == "B":
                        keuze7 = input("You decided not to eat the flesh from the zombie you just killed. When continuing walking back on the road, you can go two ways. Right or Left?\n"
                        "a) Go right\n"
                        "b) Go left")
                        if keuze7 == "a" or keuze7 == "A":
                            input()
                        elif keuze7 == "b" or keuze7 == "B":
                            print("You walk to the left, but you didn't read the sign that said Minefield. RIP")
                elif keuze5 == "b" or keuze5 =="B":
                    keuze6 = input("In the house you encounter a zombie, will you attack it or run from it?\n"
                    "a) Attack the zombie\n"
                    "b) Run from the zombie")
                    if keuze6 == "a" or keuze6 =="A":
                        print("You try to attack the zombie, but you fail to swing at the zombie because you don't have enough energy left.")
                    elif keuze6 == "b" or keuze6 == "B":
                        print("You try to run from the zombie, but you don't have enough energy left. RIP")
    elif keuze2 == "b" or keuze2 == "B":
        keuze3 = input("You walk up to the hospital, but the front door is open. You also spot a broken window on the side of the building.")
        if keuze3 == "a" or keuze3 == "A":
            print("You enter through the front door, but you immediately get ambushed by 3 zombies. RIP")
        elif keuze3 == "b" or keuze3 == "B":
            keuze4 = input("You climb through the broken window and cut yourself, it's totally dark inside but you can see something shiny lying on the ground. You pick it up, to inspect it and you find out it's a needle. You feel pretty tired, but is it a good idea to inject yourself?\n"
            "a) Inject yourself with the needle you found lying on the ground.\n"
            "b) Don't inject yourself with the needle you found lying on the ground.")
            if keuze4 == "a" or keuze4 == "A":
                keuze5 = input("After injecting yourself with the needle, you start to feel pretty sick and dizzy. It probably wasn't a good idea to inject yourself with a needle, but how are you going to fix this?\n"
                "a) Drink some water and wait it out\n"
                "b) Inject yourself with some other needles lying on the ground")
                if keuze5 == "a" or keuze5 == "A":
                    keuze6 = input("After drinking some water, you don't feel any better, but you decide to move on. on the streets you see some zombies, will you go further inside the hospital or will you kill the zombies for food?\n"
                    "a) Go further inside the hospital\n"
                    "b) Kill the zombies on the street")
                    if keuze6 == "a" or keuze6 == "A":
                        keuze7 = input("Going further inside the hospital, you hear a zombie behind you, what will you do\n"
                        "a) Try to kill the zombie\n"
                        "b) Try to run away")
                    elif keuze6 == "b" or keuze6 == "B":
                        print("You try to kill the zombies, but fail. They outnumbered you. RIP")
                elif keuze5 == "b" or keuze5 == "B":
                    print("You die from an overdose. RIP")
            elif keuze4 == "b" or keuze4 == "B":
                keuze5 = input("You walk further into the hospital and you smell something horrible coming from a room a couple of meters away. Will you go check it out?\n"
                "a) Check out the room\n"
                "b) Don't check out the room")
                if keuze5 == "a" or keuze5 == "A":
                    print("You go to check out the room, after entering the room you find out the horrible smell is a dead body, and a zombie is standing on top of it. It immediately jumps to you, and due to the injury you sustained earlier, the zombie kills you. RIP")
                if keuze5 == "b" or keuze5 == "B":
                    keuze6 = input("You don't go to check out the room, but you are feeling really low on energy, because of the injury you sustained earlier. You want to look for some food, but where?\n"
                    "a) Search the bin you saw before entering the hospital\n"
                    "b) Try to kill zombies on the streets")
                    if keuze6 == "a" or keuze6 == "A":
                        keuze7 = input("You went to go and check out the bin outside the hospital, in there you found some food, but it seems rotten. Will you eat it?\n"
                        "a) Eat the food\n"
                        "b) Don't eat the food")
                        if keuze7 == "a" or keuze7 == "a":
                            print("You decided not to eat the food you found, and walk along the steet looking for other food. You encounter a zombie, but due to your lack of energy you can't get away or kill the zombie. RIP")
                        if keuze7 == "b" or keuze7 == "B":
                            print("You eat the food and you immediately taste that it's very bad, but you keep eating because otherwise you will die of starvation. After finishing the food you feel really sick, and after a couple of minutes die. RIP")
                    if keuze6 == "b" or keuze6 == "B":
                        print("You go on the steets to kill some zombies to eat, but due to the injury you sustained earlier, you lack the ability to kill a zombie. RIP")
elif keuze1 == "b" or keuze1 == "B":
    keuze2 = input("You find a broken glass bottle on the floor, you can use to try to kill the zombie. Will you try it?\n"
    "a) Attack the zombie\n"
    "b) Look for more weapons outside")
    if keuze2 == "a" or keuze2 == "A":
        print(name,"tries to kill the zombie, you succeed, but while you were killing it 5 other zombies entered the building. RIP")
    elif keuze2 == "b" or keuze2 == "B":
        keuze3 = input("You decided to go look for more weapons, which way do you go?\n"
        "a) Go right\n"
        "b) Go left")
        if keuze3 == "a" or keuze3 == "A":
            keuze4 = input("You decided to walk to the left. When walking across the streets you spot an abandoned car and a house. Where will you go?\n"
            "a) Try to break into the abandoned car\n"
            "b) Enter the house")
            if keuze4 == "a" or keuze4 == "A":
                keuze5 = input("After entering the house, You can go into the living room or upstairs, where will you go?\n"
                "a) Go upstairs\n"
                "b) Go into the living room")
                if keuze5 == "a" or keuze5 == "A":
                    print(name,"decides to walk up the stairs, when you are about halfway upstairs a zombie comes around the corner. You startle and fall down the stairs and break your neck. RIP")
                elif keuze5 == "b" or keuze5 == "B":
                    keuze6 = input("You go into the living room, there seems to be a curious smell. You want to figure out what it is.\n"
                    "a) Check the table\n"
                    "b) Check the closet")
                    if keuze6 == "a" or keuze6 == "A":
                        keuze7 = input("You check out the table, but you cant there seem te be anything. You go to further check out the house. Where do you go?\n"
                        "a) Go into the basement\n"
                        "b) Go into the kitchen")
                        if keuze7 == "a" or keuze7 == "A":
                            keuze8 = input("After going into the basement, you hear some loud growling. Will you check it out or run back up?\n"
                            "a) Check out the basement further\n"
                            "b) Run back upstairs")
                            if keuze8 == "a" or keuze8 == "A":
                                print("You walk further into the basement, even though you hear a lot of growling. You walk up to the boiler, and a zombie appears from behind it. Because you are low on energy you cant get away and the zombie eats you. RIP")
                            elif keuze8 == "b" or keuze8 == "B":
                                keuze9 = input("You run back upstairs, but you trip on the stairs. The zombies catch up to you. What will you do?\n"
                                "a) Try to run from the zombies\n"
                                "b) Try to kill the zombies")
                                if keuze9 == "a" or keuze9 == "A":
                                    print("You try to run from the zombies, but because you are low on energy you can't get away. RIP")
                                elif keuze9 == "b" or keuze9 == "B":
                                    print("You decide to try to kill the zombies, but because you are low on energy you fail to kill them. RIP")
                        elif keuze7 == "b" or keuze7 == "B":
                            print("You decided to go to the kitchen for some food, because you feel quite low on energy. In the refrigerator you find a bowl of salad. You eat, but after eating it you feel dizzy and fall over. RIP")
                    elif keuze6 == "b" or keuze6 == "B":
                        print("You decided to open the closet, but when you tried to open the closet it falls over and crushes you. RIP")
            elif keuze4 == "b" or keuze4 == "B":
                print(name,"tries to break into an abandoned car. You break the window and open te car from te inside. The keys are still in the car and you try to start the car, but the car instantly explodes. RIP")
        elif keuze3 == "b" or keuze3 == "B":
            print(name,"decides to go left, a zombie is coming after you and you hit a dead end. RIP")