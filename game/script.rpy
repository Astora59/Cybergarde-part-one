# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("Binta")
define y = Character("Yanis")
define m = Character("Maydan")


# declare characters sprites
image Binta_annoyed = "Binta_annoyed.png"



#backgrounds
image bg_front_gate = "front-gate.jpg"


# effects
#screenshake
transform shake_bg:
    linear 0.05 xoffset -10  # Déplace légèrement à gauche
    linear 0.05 xoffset 10   # Déplace légèrement à droite
    linear 0.05 xoffset -5   # Retourne légèrement à gauche
    linear 0.05 xoffset 5    # Retourne légèrement à droite
    linear 0.05 xoffset 0    # Revient à la position initiale




#resize character
transform size_normal:
    ysize 600
    fit "contain"



# The game starts here.

label start:

    "Cette oeuvre est un travail de fiction. Toute ressemblance à des personnes ou des événements est totalement fortuite."
    "Si vous êtes témoin de toute forme d'harcèlement ou de cyberharcèlement, ne laissez pas faire ces actions et contactez les autorités compétentes."
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg_front_gate:
        xalign 0.5  # Centre horizontalement
        yalign 0.2  # Place plus haut verticalement
        zoom 0.8

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
    "Binta avance nonchalamment vers le portail de son collège et lève sa tête, une nouvelle journée commence."
    scene bg_front_gate:
        xalign 0.5  # Centre horizontalement
        yalign 0.5  # Place plus haut verticalement
        zoom 1.5
       
    "D'un pas distrait par ses rêveries, Binta se dirigea vers le portail de l'école."

    scene bg_front_gate:
        xalign 0.5  # Centre horizontalement
        yalign 0.5  # Place plus haut verticalement
        zoom 1.5
    
    
    # mettre screenshake
    show bg_front_gate at shake_bg
    with Pause(1.0)  # Pause pour observer l'effet

    
    "\"{i}FAIS ATTENTION OU TU MARCHES IDIOTE !\"{/i}"
    
    
    "Binta avait percuté avec violence un autre jeune homme, très probablement proche de son âge. Comment avait-il pu la percuter avec autant de force ?"

    "C'est en regardant en sa direction, qu'elle se rendit compte de sa trottinette électrique."
    
    show Binta_annoyed: 
        yalign 0.3
        zoom (0.5)
    b "Mais ça va pas d'accélérer aussi vite aussi proche de l'entrée ? Et qui tu traites d'idiote ? Certainement pas moi j'espère ?"
    m "oh si si précisément toi"
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # This ends the game.

    return
