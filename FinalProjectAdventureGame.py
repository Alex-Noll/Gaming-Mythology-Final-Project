# Final Project for CLA 2434
#Alex Noll - November 2019
#Dependencies
#from playsound import playsound
#playsound('Pokémon RedBlueYellow - PC Turning On - Sound Effect.wav')

print('Hello and welcome to my final project adventure game for Gaming & Mythology \n\n This game is python based and all code is open source at github.com/Alex-Noll')
print("Would you like to read some information about the game - #1, or jump right into the game - #2")
print("Please enter either 1 or 2 to select your choice")
launch_option = input('>')
if launch_option == "1":
    print("Excellent, would you like to know about the setting - #1, \n\nThe character classes - #2, \n\nThe controls - #3, \n\nThe motive behind the project - #4, \n\nOr do you just want to hop into the game - #5?")
    print("Please enter either 1,2,3,4,or 5 into the command line")
    info_option = input('>')
    if info_option == "1":
        print('The game takes place in a the Southwestern United States in the late 1800s, but with a twist, magic and monsters abound!\n\nPlayers start off in the small town of Redmonton, a peaceful town, for the most part\n\nFrom Redmonton players can choose where they want to go in the world.')
        print("Would you like to learn more - #1 or hop into the game - #2?")
        setting_option = input('>')
        if setting_option == "1":
            print("What else would you like to learn about?: \n\nThe character classes - #1, \n\nThe controls - #2, \n\nThe motive behind the project - #3, \n\nOr do you just want to hop into the game - #4")
            pset_option = input('>')
            if pset_option == "1":
                print('There are four main character classes: #1-The Brute, #2-The Druid, #3-The Assassin, & #4-The Gunslinger')
                print('Would you like to know more? Y or N?')
                cclass_option = input('>')
                if cclass_option == "y":
                    print('Which class would you like to learn more about? The Brute -#1, \n\nThe Druid -#2, \n\nThe Assassin - #3, \n\nOr The Gunslinger - #4?')
                elif cclass_option == "n":
                    print("Would you like to learn more about #1 - The controls, \n\n#2 - The motive of the project, \n\nor 3# - Hop into the game now?")
                    pcclass_option = input('>')
                    if pcclass_option == "1":
                        print("This is a text-based adventure game, all decisions will be made by entering the text options provided on-screen by the program, usually a number, and pressing ENTER on the keyboard")
        elif setting_option == "2":
            print('So it begins, you wake up imprisoned in a hot, sand-bottomed prison cell made of cobblestone\n\n\n\nIn the shadows you hear a voice from a nearby cell ask you: "What are you in for?"\n\nYou can #1-Respond\n\nor\n\n#2-Ignore them\n\nWhich do you choose?(Type a number choice and press ENTER)')
    elif info_option == "2":
        print('There are four main character classes: #1-The Brute, #2-The Druid, #3-The Assassin, & #4-The Gunslinger')
        print('Would you like to know more? yes or no?\n\n(Enter y for yes or n for no)')
        cclass_option = input('>')
        if cclass_option == "y":
            print('Which class would you like to learn more about? The Brute -#1, \n\nThe Druid -#2, \n\nThe Assassin - #3, \n\nOr The Gunslinger - #4?')
        elif cclass_option == "n":
            print("Would you like to learn more about #1 - The controls, \n\n#2 - The motive of the project, \n\nor 3# - Hop into the game now?")
            pcclass_option = input('>')
            if pcclass_option == "1":
                print("This is a text-based adventure game, all decisions will be made by entering the text options provided on-screen by the program, usually a number, and pressing ENTER on the keyboard")
            elif pcclass_option == "2":
                print("The reasoning behind this project's creation was that I am enrolled in a Gaming & Mythology class in which our final project was to come up with a game idea\n\nI was told there was extra credit if we actually made a game\n\nI like Extra Credit."")
    elif info_option == "3":
        print("This is a text-based adventure game, all decisions will be made by entering the text options provided on-screen by the program, usually a number, and pressing ENTER on the keyboard")
    elif info_option == "4":
        print("The reasoning behind this project's creation was that I am enrolled in a Gaming & Mythology class in which our final project was to come up with a game idea\n\nI was told there was extra credit if we actually made a game\n\nI like Extra Credit.")
        print("What else would you like to learn about?")
#Actual Video Game part
elif launch_option == "2":
    print('So it begins, you wake up imprisoned in a hot, sand-bottomed prison cell made of cobblestone\n\n\n\nIn the shadows you hear a voice from a nearby cell ask you: "What are you in for?"\n\nYou can #1-Respond\n\nor\n\n#2-Ignore them\n\nWhich do you choose?(Type a number choice and press ENTER)')
    prison_option = input('>')
    if prison_option == "1":
        print("You decide to speak, what do you say? \n\n#1-Make up a story\n\n#2-You don't know\n\n#3-You robbed a bank\n\n#4-You killed someone\n\n#5-Horrible, Unspeakable things\n\n#6-Just make a random noise")
        cell_voice_option = input('>')
        if cell_voice_option == "1":
            print("You make up a complex story of grandeur about saving a top politician from an assassination attempt and then being framed for the assassination attempt yourself")
        elif cell_voice_option == "2":
            print("You tell them that you quite simply just don't know, you woke up in this prison cell and that's all that you know")
        elif cell_voice_option == "3":
            print("You tell them you robbed bank, you go into immense detail with how you did it, exactly what happened, and how you were caught.")
        elif cell_voice_option == "4":
            print("You tell them that you murdered someone and were caught doing it.")
        elif cell_voice_option == "5":
            print("You tell them that you did things that can't be spoken of without serious repercussion, the things you did were horrible, unspeakable.")
        elif cell_voice_option == "6":
            print("Words are hard, despite your best efforts all you can manage is a shrill whimper.")
