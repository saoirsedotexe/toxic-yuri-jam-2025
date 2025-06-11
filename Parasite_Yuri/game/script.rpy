# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define d = Character("Doctor")

define w = Character("Wife")

define p = Character("Parasite")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "cell.png" or "cell.jpg") to the
    # images directory to show it.

    scene cell

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "wife.png" to the images
    # directory.

    show love bullet 1

    # These display lines of dialogue.

    e "I'm doctor misery. She needs medicine drug to live."

    w "I would like medicine drug."

    p "If you don't give her medicine drug I'll suck you silly"

# Two separate routes: one where you get with the parasite and things are awesome 
# and the other where you don't get with the parasite and the parasite kills everyone

# Test choice: Medicine drug or no medicine drug

# Tutorial template code

screen buttons:
    add "bg.png"
    hbox:
        imagebutton:
             auto: "medicine%s.jpeg"
             action Jump("medicine")

        imagebutton: 
             auto: "no_medicine%s"
             action Jump("no_medicine%s.jpeg")

 

    # This ends the game.

    return
