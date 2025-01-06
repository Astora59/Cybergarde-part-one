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
    scene front-gate

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    b "Septembre... Si seulement les vacances duraient éternellement"

    "Binta arriva devant le portail de son école. Comme tous les jeunes, elle aurait souhaité passer les vacances aux côtés de ses amis, à jouer et dormir. Mais le temps ne s'arrête pour personne et la rentrée est inévitable"
    "\"{i}Yo les gars vous avez joué à la dernière MAJ Fornite??\"{/i}"
    "\"{i}j'arrive pas à croire que tu regardes Miraculous ! t'es pas trop vieux pour ça ?\"{/i}"
    "Autant dire que le brouhaha était suffisamment difficile à encaisser pour Binta. La vie citadine est bien plus bruyante que celle que l'on peut retrouver en campagne."
    "Les vacances lui manquaient terriblement, mais pas le choix : quand faut y aller, faut y aller !"
    "Binta avance nonchalamment vers le portail de son collège"
    scene hell 
    show Binta angry
    show Maydan happy

    b "selem"
    m "selem"

    # This ends the game.

    return
