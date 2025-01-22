# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("Binta", color="#BD93BD")
define y = Character("Yanis")
define m = Character("Maydan", color="#E94F37")
define inconnu = Character("???")


# declare characters sprites
# Binta
image Binta_afraid = "Binta_afraid.png"
image Binta_angry = "Binta_angry.png"
image Binta_annoyed = "Binta_annoyed.png"
image Binta_anxious = "Binta_anxious.png"
image Binta_default_happy = "Binta_default_happy.png"
image Binta_explaining = "Binta_explaining.png"
image Binta_grossed_out = "Binta_grossed_out.png"
image Binta_sad = "Binta_sad.png"
image Binta_sad_notspeaking = "Binta_sad_notspeaking.png"
image Binta_thinking = "Binta_thinking.png"
image Binta_very_happy = "Binta_very_happy.png"

# Mayden
image Mayden_afraid = "Mayden_afraid.png"
image Mayden_angry = "Mayden_angry.png"
image Mayden_annoyed = "Mayden_annoyed.png"
image Mayden_anxious = "Mayden_anxious.png"
image Mayden_default = "Mayden_default.png"
image Mayden_default_happy = "Mayden_default_happy.png"
image Mayden_explaining = "Mayden_explaining.png"
image Mayden_sad = "Mayden_sad.png"
image Mayden_very_happy = "Mayden_very_happy.png"

# Yanis
image Yanis_afraid = "Yanis_afraid.png"
image Yanis_angry = "Yanis_angry.png"
image Yanis_annoyed = "Yanis_annoyed.png"
image Yanis_concerned = "Yanis_concerned.png"
image Yanis_default = "Yanis_default.png"
image Yanis_default_happy = "Yanis_default_happy.png"
image Yanis_explaining = "Yanis_explaining.png"
image Yanis_sad = "Yanis_sad.png"
image Yanis_thinking = "Yanis_thinking.png"
image Yanis_very_happy = "Yanis_very_happy.png"
image Yanis_very_happy_afterThinking = "Yanis_very_happy_afterThinking.png"



#backgrounds
image bg_front_gate = "front-gate.jpg"
image bg_school_corridor = "school_corridor_background.jpg"
image bg_classroom_evening = "Classroom_01_evening.jpg"
image bg_street_evening = "home_evening.png"

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


#character positions 
transform left: 
    xalign 0.0
    yalign 0.3
    zoom (0.5)

transform right: 
    xalign 1.0
    yalign 0.3
    zoom (0.5)

transform center: 
    zoom (0.5)
    yalign 0.3
    xalign 0.5

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

    
    inconnu "\"{i}FAIS ATTENTION OU TU MARCHES IDIOTE !\"{/i}"
    
    
    "Binta avait percuté avec violence un autre jeune homme, très probablement proche de son âge. Comment avait-il pu la percuter avec autant de force ?"

    "C'est en regardant en sa direction, qu'elle se rendit compte de sa trottinette électrique."
    
    show Binta_annoyed at left

    
    b "Mais ça va pas d'accélérer aussi vite aussi proche de l'entrée ? Et qui tu traites d'idiote ? Certainement pas moi j'espère ?"

    show Mayden_annoyed at right
    
    inconnu "Oh si si précisément toi. Pourquoi tu te mets sur ma route ?"

    b "C'est la rentrée ? Peut-être que tu ne l'avais pas remarqué ?"
    
    "Au milieu de la tumulte de la rentrée se trouvait Binta et le jeune homme, leurs voix montant d'un cran à chaque rétorque et insulte."

    "Les quelques élèves qui traînaient encore à pénétrer l'enceinte du collège s’étaient arrêtés pour observer la scène. Le murmure habituel des conversations avait laissé place à un silence tendu, seulement brisé par les échanges des deux adolescents."

    inconnu "QUE CELA CESSE TOUT DE SUITE !"

    "Enfin un surveillant était intervenu pour les séparer, terminant cette dispute aussi brusquement qu'elle avait commencé."

    inconnu "Allez tout de suite rejoindre vos camarades, et je ne veux PLUS vous entendre." 

    "La dispute se termina aussi vite qu'elle ait commencé. Binta pouvait sentir le regard noir du garçon se posait sur elle."   

    scene bg_school_corridor:
        xalign 0.5  # Centre horizontalement
        yalign 0.2  # Place plus haut verticalement
        zoom 0.6
    
    "Les deux ados se dirigèrent vers l'enceinte du collège, séparé par quelques mètres. D'un seul coup, le jeune prit d'abord de l'avance, puis la parole."
    
    show Mayden_annoyed at center

    m "Mon nom c'est Mayden, l'oublie jamais parce qu'on va se retrouver."

    hide Mayden_annoyed

    "Mayden partit en courant, probablement pour distancer Binta."


    "Etait-ce une menace ? Devait-elle s'inquiéter ? Binta n'était pas sûre de ce qu'elle devait tirer de cette situation, Après tout ce n'était qu'une petite dispute à la rentrée."
    
    
    "Dans tous les cas, il est temps de commencer les cours, l'adolescente dût se rendre dans la hall d'entrée afin de pouvoir voir quelle classe rejoindre."

    "Quelle fut sa surprise, quand elle se rendit compte qu'elle a déjà fait la rencontre d'un de ses nouveaux camarades de classe ce matin..."

    "Mais bon, il est temps de commencer cette terrible journée se dit Binta, et ainsi commença la rentrée."

    scene bg_classroom_evening with fade:
        xalign 0.5
        yalign 0.2


    "La journée se termina pour les étudiants du collège Victor Hugo, et Binta prépara ses affaires pour rentrer."
    "Le soleil commençait doucement à rejoindre l'ouest et Binta préférait ne pas trop tarder, ses parents commenceraient à s'inquiéter sinon."

    scene bg_street_evening with dissolve:
        xalign 0.5
        yalign 0.2
        zoom 1.5

    "Binta marchait seule, son sac à dos battant légèrement contre ses jambes à chaque pas. La journée avait été longue et elle n’avait qu’une hâte : retrouver la chaleur de sa maison."
    
    "Autour d’elle, la rue était déserte. Les seules signes de vie étaient la lumière des maisons de la rue. Cependant elle pouvait sentir une présence l'observer."

    "C'était une situation assez rare pour cette rue. Il est vrai que peu de personnes l'empruntent, mais au point qu'il n'ait personne ? C'est très singulier."
    
    "Binta empressa le pas : que le pressentiment soit vrai ou faux elle n'avait pas vraiment envie de le savoir."
    
    "Elle se tourna brièvement vers l’arrière, les yeux scrutant l’ombre qui s’étendait derrière elle. Rien. Juste la rue déserte et le lointain bourdonnement des néons."

    "Enfin arrivée devant chez elle"
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # This ends the game.

    return
