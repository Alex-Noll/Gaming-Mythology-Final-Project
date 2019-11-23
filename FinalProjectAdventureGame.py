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
            print('The inmate manages to suspend their disbelief, calling you a "fucking liar" and threatens to bash your skull in for lying to them\n\nDo you:\n\n#1-Try to explain yourself,\n\n#2-Challenge them to a fight,\n\n or #3-Just leave it be?' )
            lie_inmate_option = input('>')
            if lie_inmate_option == "1":
                print("You explain yourself to the inmate and pacify the situation, now trusting you the inmate tells you why they're in the can too: \n\nA repeat drug smuggler across the border, caught on a cocaine run this time, they proclaim, my name's Wyatt, holler through if you need anything\n\nFeeling like you've made a prison buddy, you both decide to go to sleep for the night.")
                print('You wake up to the sound of gunshots, BANG, BANG, BANG, followed quickly by short, blood-curdling screams, quickly extinguished by more gunshots.\n\n\n\nFrightened, you try to hide yourself in your cell.\n\nLooking across, you finally see Wyatt, standing directly in front of the cell door.\n\nNoticing you staring at him, he looks over as you mouth for him to hide, moments later, three armed mercenaries come over to his door and shoot the lock, freeing him.\n\nIt was all part of his plan, Wyatt knew he would not be in for long')
            elif lie_inmate_option == "2":
                print("You decide that you're not gonna put up with their shit, you call them on their claim and say you'll kill them before they even get the chance, you two argue through the night until you eventually pass out at the window.")
            elif lie_inmate_option == "3":
                print("You decide the best action is inaction, this further infuriates the inmate, they begin throwing sand through the window along with repeated screams of profanity, causing a guard to come investigate")
        elif cell_voice_option == "2":
            print("You tell them that you quite simply just don't know, you woke up in this prison cell and that's all that you know")
            print('Seemingly unsatisfied with your response, the inmate responds with: \n\n"REALLY, how do you wind up here and not know, what are you, STUPID?"\n\nEventually the fellow inmate comes to realize that you might not want to talk or genuinely do not remember, either way they leave you alone and you drift off to sleep.')
        elif cell_voice_option == "3":
            print("You tell them you robbed a bank, you go into immense detail with how you did it, exactly what happened, and how you were caught.")
            print("The inmate, seemingly immersed in your story begins to ask you question after question, fascinated with all of the ins and outs of your story and how you wound up in prison with them.\n\nThings seem to be going well and the inmate tells you how they got in: Smuggling cocaine across the border\n\nFeeling like you've made a prison pal, you both decide to go to sleep")
        elif cell_voice_option == "4":
            print("You tell them that you murdered someone and were caught doing it.")
            print("Immediately the inmate wants to know all of the details, who, how, and why? \n\nDo you tell them -#1 \n\nor \n\n#2-Say that you'd rather not get into it?")
            murder_inmate_choice = input('>')
            if murder_inmate_choice == "1":
                print("You decide to tell them the full story: You were riding your horse through Redmonton on your way to running an errand when a local drunk came wandering out of the salty spitoon looking for a fight.\n\nDespite the fact that you're just riding your horse through town, they draw their revolver and aim it sloppily at your horse.\n\nWithout hesitation, you pull your piece and shoot them straight through the eye.\n\nBecause of the commotion townspeople run over and see the dead drunkard on the saloon steps.\n\nImmediately you're placed under arrest and thrown in jail, and here you are.")
                print('The inmate responds with: "Wow, that is some fucking bullshit, sorry; I would do the exact same though, I have in fact"\n\nYou talk more together and they tell you what they are in for: Smuggling cocaine across the border\n\nFeeling like you have made a prison buddy, you both decide to go to sleep.')
            elif murder_inmate_choice == "2":
                print("Deciding that you don't want to get into it, you leave the inmate guessing, annoyed but somewhat satisfied, they leave you alone for the night, you walk over to your bedroll and go to sleep.")
        elif cell_voice_option == "5":
            print("You tell them that you did things that can't be spoken of without serious repercussion, the things you did were horrible, unspeakable.")
            print('You can hear the sudden increased breathing rate of your fellow inmate as they mutter "What the hell is wrong with you?", your inmate is already obviously spooked, do you \n\n#1-Try to frighten them? \n\n Or \n\n#2-Calm them down?')
            spooked_inmate = input('>')
            if spooked_inmate == "1":
                print('You continue to frighten the inmate until they scream "Stay the fuck away from me you freak, you hear me!"\n\nSatisfied with yourself for the night, you go to sleep comfortably in your bedroll')
            elif spooked_inmate == "2":
                print("You decide you've had enough fun terrorizing your fellow inmate and strive to calm them down.\n\nYou explain yourself and they immediately seem calmer, you two share a conversation where they tell you how they got in: Smuggling cocaine across the border\n\nFeeling like you've made a prison pal, you both decide to go to sleep for the night.")
        elif cell_voice_option == "6":
            print("Words are hard, despite your best efforts all you can manage is a shrill whimper.")
            print("The inmate laughs at you non-stop, you walk over to your bedroll and cry yourself to sleep")
    elif prison_option == "2":
        print('The fellow inmate is angered by your lack of your response and starts screaming\N\N"THE SILENT TYPE HUH, I AM GONNA KILL THE LIFE OUT OF YOU, I WONDER IF YOULL BE SILENT THEN"')
        print("The inmate begins throwing shaking the bars to the window between your cells, suddenly you realize they're powerless and they can't do anything to you, presenting you with two options\n\nDo you:\n\n#1-Go over to the window and punch their hands?\n\nOr\n\n#2-Sit back in your cell and go to sleep?")
        silence_option_inmate = input('>')
        if silence_option_inmate == "1":
            print('You decide to go over to the window bars and smash the inmates fingers against them, they let out a single shrill scream and call you a "fucking asshole" before retreating across their room\n\nIn a much higher pitched voice than last used, they say "Im gonna get you for this, just wait"\n\nUnimpressed, you decide to walk back to your bedroll and go to sleep for the night.')
        elif silence_option_inmate == "2":
            print('You decide to ignore them and just go to sleep in your bedroll. Upset by your lack of attention, the inmate begins scheming.')
