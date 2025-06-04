# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define r = Character(_("Ruby"), color="#CB3535")
define b = Character(_("Blake"), color="#4C5C64")

# Declare transformations

transform left:
    xalign 0.2
    yalign 1.0
transform right:
    xalign 0.8
    yalign 1.0
transform center:
    xalign 0.5
    yalign 1.0

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    show ruby happy

    r "hey is this thing on"

    r "oh shit"

    show blake happy right

    b "this is crazy"

    # This ends the game.

    jump prologue

    return

label prologue:
    
    scene bg room

    pause

    return

label vampRave:

    scene bg room

    pause

    return

label bugFrat:

    scene bg room

    pause

    return

label oozeBeach:

    scene bg room

    pause

    return

label zombieLocker:

    scene bg room

    pause

    return

label scpWoods:

    scene bg room

    pause

    return

label swirlyEnding:

    scene bg room

    pause

    return

label coolyEnding:

    scene bg room

    pause

    return

label trueEnding:

    scene bg room

    pause

    return

