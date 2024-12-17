# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("Binta")
define y = Character("Yanis")
define m = Character("Maydan")

# The game starts here.

label start:

    "Cette oeuvre est un travail de fiction. Toute ressemblance à des personnes ou des événements est totalement fortuite."
    "Si vous êtes témoin de toute forme d'harcèlement ou de cyberharcèlement, ne laissez pas faire ces actions et contactez les autorités compétentes."
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Binta happy

    # These display lines of dialogue.

    b "You've created a new Ren'Py game."

    b "Once you add a story, pictures, and music, you can release it to the world!"


    scene hell 
    show Binta angry
    show Maydan happy

    b "selem"
    m "selem"

    # This ends the game.

    return
