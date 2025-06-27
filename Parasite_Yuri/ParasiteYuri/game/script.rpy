# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character(None, what_prefix="{i}", what_suffix="{/i}")

define e = Character("Langston", color="#5dc0d5")

define w = Character("Wife", color="#d95723")

define c = Character("Comms Officer", color="#c9a3f1")

define p = Character("Parasite")

define s = Character("Stickfigure")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "cell.png" or "cell.jpg") to the
    # images directory to show it.

    $ say_style = "Interrogation" #Cutscene or Interrogation

    scene cell

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "wife.png" to the images
    # directory.

    #show love bullet 1
    
    n "You are home."
    n "You are finally home."
    n "The carpet beneath your feet. {w}The soft of your own bed. {w}The quiet. The quiet."
    n "You are home."
    n "Something drips on your shoulder."
    n "You look up. The ceiling beams have started to melt."
    n "The door oozes. {w}The shelves go concave. {w}The bed splits."
    n "Fire eats at the foundation."
    n "You clutch the infrastructure in place. It comes through your fingers like candle wax. But you stand firm."
    n "What’s left of the house forms a hollow around you. You keep the mantle from toppling in. You force the engravings to hold their shape."
    n "You carry the weight."
    n "Something beeps."
    
    #[TRANSITION TO BEDROOM]
    $ say_style = "Cutscene" #Cutscene or Interrogation
    
    n "And then you wake up. Your pager trills."
    c "Langston."
    c "We need you at the bridge."
    c "Something’s wrong."
    n "You hear your heartbeat in your ears. Static dances over your skin, like a holdover from pins and needles. There’s a weight in your gut."
    n "You take a deep breath, forcing it to pass."
    e "Alright."
    e "I’m on my way."
    n "You get out of bed."


    # These display lines of dialogue.

    e "I'm doctor misery. She needs medicine drug to live."

    w "I would like medicine drug."

    p "If you don't give her medicine drug I'll suck you silly"

    show stickfigure

    s "I too am in this episode"

    show stickfigure sad

    s "I am sad now"

    call screen buttons()

    return

# Two separate routes: one where you get with the parasite and things are awesome 
# and the other where you don't get with the parasite and the parasite kills everyone

# Test choice: Medicine drug or no medicine drug

# Tutorial template code

screen buttons():
    add "bg.png"
    hbox:
        imagebutton auto "images/medicine_%s.png" action Jump("medicine")

        imagebutton auto "images/no-medicine_%s.png" action Jump("no_medicine") 

            

 

    # This ends the game.
