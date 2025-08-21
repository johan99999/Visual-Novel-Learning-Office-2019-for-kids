# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Ewing")
define pov = Character("[povname]")



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show ewing normal

    # These display lines of dialogue.

    e "Halo."
    e "Kenalin, aku Ewing."
    python:
        povname = renpy.input("Nama kamu siapa?", length=32)
        povname = povname.strip()

        if not povname:
            povname = "Tanpa Nama"
    e "[povname], senang mengenalmu!"


    # This ends the game.

    return
