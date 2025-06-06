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

    show love bullet 1.png

    # These display lines of dialogue.

    e "I'm doctor misery. She needs crazy head to live."

    w "You suck at giving head."

    p "What if you sucked it in frightening and interesting ways?"

    # This ends the game.

    return
