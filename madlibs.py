# A game of madlibs.

import os
width = os.get_terminal_size().columns #Gets the width of the console in characters.

logo = [
"::::    ::::      :::     :::::::::  :::        ::::::::::: :::::::::   ::::::::  ::: ",
"+:+:+: :+:+:+   :+: :+:   :+:    :+: :+:            :+:     :+:    :+: :+:    :+: :+: ",
"+:+ +:+:+ +:+  +:+   +:+  +:+    +:+ +:+            +:+     +:+    +:+ +:+        +:+ ",
"+#+  +:+  +#+ +#++:++#++: +#+    +:+ +#+            +#+     +#++:++#+  +#++:++#++ +#+ ",
"+#+       +#+ +#+     +#+ +#+    +#+ +#+            +#+     +#+    +#+        +#+ +#+ ",
"#+#       #+# #+#     #+# #+#    #+# #+#            #+#     #+#    #+# #+#    #+#     ",
"###       ### ###     ### #########  ########## ########### #########   ########  ### "]

for i in logo: # Prints the logo to the center of the console.
	print(i.center(width))

import random
plays = 0 # counts the number of games the user has played.
madlibs = [
    {"sentence": "What's a cow's favourite meal? It's /1!", "replacements": ["noun"]},
    {"sentence": "Why did the chicken cross the road? To /1 their /2 /3!", "replacements": ["verb", "adjective", "noun"]}
    ] #TODO: Write more madlibs.

def play():
    # Defines variables:
    madlibChoice = random.choice(madlibs) # Chooses a madlib game at random.
    inputs = []
    newSentence = ""
    placeholder = "/1"
    
    # Asks the player for input and creates a funny new sentence:
    for i in range(len(madlibChoice["replacements"])): # Prompts the user for inputs:
        inputs.append(input("I need a " + madlibChoice["replacements"][i] + ": "))
        if i == 0:
            newSentence = madlibChoice["sentence"].replace(placeholder, inputs[i])
        else:
            placeholder = "/" + str(i + 1)
            newSentence = newSentence.replace(placeholder, inputs[i])        
    print(newSentence.center(width))
    
    # Increments the number of rounds the user has played:
    global plays
    plays += 1


while True: # Asks the player to play again or to quit:
    if plays > 0:
        answer = ""
        while answer != "y" or answer != "q":
            answer = input("Press [Y] to play again. Press [Q] to quit." + "\n").lower()
            if answer == "y":
                print("Let's play another round!")
                play()
            elif answer == "q":
                print("Thank you for playing!")
                quit()
    else:
        play()
