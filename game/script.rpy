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

#classroom
image bg_front_gate = "front-gate.jpg"
image bg_school_corridor = "school_corridor_background.jpg"
image bg_classroom_day = "Classroom_01_day.jpg"
image bg_classroom_evening = "Classroom_01_evening.jpg"


#road to school
image bg_street_evening = "someplace_usa_afternoon.jpg"
image bg_bedroom_evening = "room_dusk_light_on.jpg"


#MUSIC


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
    
    play music "music/Morning.mp3" loop

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    b "Septembre... Si seulement les vacances duraient éternellement..."

    "Binta arriva devant le portail de son école. Comme tous les jeunes, elle aurait souhaité passer les vacances aux côtés de ses amis, à jouer et dormir. Mais le temps ne s'arrête pour personne et la rentrée est inévitable."
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
    
    play sound "music/hit_sound_effect.mp3"
    stop music fadeout 1.0
    show bg_front_gate at shake_bg
    with Pause(1.0)  # Pause pour observer l'effet
    
    
    inconnu "\"{i}FAIS ATTENTION OU TU MARCHES IDIOTE !\"{/i}"
    
    
    "Binta avait percuté avec violence un autre jeune homme, très probablement proche de son âge. Comment avait-il pu la percuter avec autant de force ?"

    "C'est en regardant en sa direction, qu'elle se rendit compte de sa trottinette électrique."
    
    play music "music/Junkyard_Tribe.mp3"
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
    play music "music/Morning.mp3"
    scene bg_school_corridor with dissolve:
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
    play music "music/Evening.mp3" fadeout 1.0
    scene bg_classroom_evening with fade:
        xalign 0.5
        yalign 0.2
    

    "La journée se termina pour les étudiants du collège Victor Hugo, et Binta prépara ses affaires pour rentrer."
    "Le soleil commençait doucement à rejoindre l'ouest et Binta préférait ne pas trop tarder, ses parents commenceraient à s'inquiéter sinon."

    scene bg_street_evening with dissolve:
        xalign 0.5
        yalign 0.2

    "Binta marchait seule, son sac à dos battant légèrement contre ses jambes à chaque pas. La journée avait été longue et elle n’avait qu’une hâte : retrouver la chaleur de sa maison."
    
    "Autour d’elle, la rue était déserte. Les seules signes de vie étaient la lumière des maisons de la rue. Cependant elle pouvait sentir une présence l'observer."
    play music "music/Symmetry.mp3" fadeout 1.0
    "C'était une situation assez rare pour cette rue. Il est vrai que peu de personnes l'empruntent, mais au point qu'il n'ait personne ? C'est très singulier."
    
    "Binta empressa le pas : que le pressentiment soit vrai ou faux elle n'avait pas vraiment envie de le savoir."
    
    "Elle se tourna brièvement vers l’arrière, les yeux scrutant l’ombre qui s’étendait derrière elle. Rien. Juste la rue déserte et le lointain bourdonnement des néons."

    "Enfin arrivée devant chez elle, Binta s'empresse de rentrer et de fermer la porte derrière elle."
    
    
    
    play music "music/Space Jazz.mp3"
    scene bg_bedroom_evening with dissolve: 
        xalign 0.5
        yalign 0.2

    "\"Pfiou... Enfin rentrée,\" murmure-t-elle pour elle-même."
    
    "Elle retira ses baskets rapidement, les laissant dépareillées près du tapis de l’entrée, puis attrapa une pomme du panier de fruits sur le comptoir de la cuisine."
    "L'inquiétude qu'elle ressentit avant d'arriver chez elle s'était rapidement dissipée. Sa maison était un lieu sûr pour elle, que personne ne pouvait pénétrer."
    "Elle monta dans sa chambre, ses pas résonnant légèrement sur le bois, créant une petite mélodie familière."
    "Elle vivait avec ses parents et son grand frère. Son père se trouvait dans le salon et regarder probablement un programme sur les aliens. Sa mère quant à elle aimait s'occuper de la cuisine en écoutant de la musique."
    "Elle se laissa tomber sur son lit avec un soupir de soulagement, le poids du monde semblant s’échapper de ses épaules. L’odeur rassurante de sa lessive emplit l’air. "
    "Son téléphone, posé à côté d'elle, éclaire légèrement sa chambre qui commence à inviter la pénombre. Elle décida de le prendre et d'aller sur Kokot."
    "Son pouce glisse rapidement sur l’écran, faisant défiler un flux ininterrompu de vidéos courtes. Tantôt un chat maladroit, tantôt une danse virale qu’elle se promet d’essayer plus tard."
    "Une notification apparaît en haut de l’écran : un message d’une amie. Sans attendre, elle clique dessus."
    "\"{i}T’as vu la vidéo que j’ai envoyée ? Trop drôle, non ?\"{/i}, écrivit son amie."
    "Binta répondit immédiatement, ses doigts tapant vite sur l’écran."
    "\"{i}Omg oui, je rigole encore !! T’es trop bête !\"{/i}"
    "A vrai dire la vidéo n'était pas si drôle que ça, mais ce genre de petits mensonges ne font jamais de mal non ?"
    "D'ailleurs, la vidéo l'a sorti de son cocon. Ca lui a fait penser qu'aucun de ses camarades n'a pris l'initiative de créer un groupe de classe."
    "C'est assez courant d'en créer un, cela permet de coordonner la classe pour les devoirs, la prise de note en cours et ça favorise la cohésion de groupe."
    "\"On verra plus tard\" se disa-elle, ferme les yeux, laissant son esprit divaguer. En quelques instants seulement, elle rejoigna les bras de Morphée."
    
    scene bg_front_gate with fade:
        xalign 0.5  # Centre horizontalement
        yalign 0.2  # Place plus haut verticalement
        zoom 0.8
    
    play music "music/Morning.mp3" loop
    
    "L'esprit encore partiellement endormi, Binta se rendit au collège pour commencer une nouvelle journée."
    "Les rayons du soleil chauffèrent doucement ses joues et la ramèna petit à petit à ses sens."
    "D'autres étudiants semblèrent la regarder. On ne peut plus souffler un petit peu avant de rentrer ?"
    "Binta se rendit en classe."

    scene bg_classroom_day with dissolve:
        xalign 0.5
        yalign 0.2
    
    

    "\"Quel brouhaha\" se dit Binta. Toute la classe était arrivée avant elle, et cette dernière ne voulait pas faire de vagues. "
    "Binta s'installa rapidement à la place que son professeur principal lui avait attitré."
    "Malgré sa furtive exécution de l'entrée à son bureau, elle pouvait sentir les regards se posaient sur elle."
    "Des chuchotements entrecoupés de rires faisaient écho dans la classe."
    "Chaque chuchotement et rire semblaient renforcer les regards sur Binta. Mayden quant à lui, semblait l'ignorer."
    inconnu "Sortez vos cahiers et taisez-vous, le cours commence !"
    "Sans que la plupart des élèves ne s'en aperçoivent, leur professeur était arrivé et s'était installé."
    "Le sentiment de malaise que ressentait Binta s'estompa peu à peu, les regards concentrés sur ce que le professeur disait."
    "Qu'a-t-il bien pu se passer ? Binta n'arrivait pas à se concentrer et son esprit fit tous les scénario possibles."

    scene bg_school_corridor with dissolve:
        xalign 0.5  # Centre horizontalement
        yalign 0.2  # Place plus haut verticalement
        zoom 0.6
    
    
    "La cloche retentit dans les classes et les couloirs de l'école, transformant les couloirs en un melting pot de bruits et de gens."
    "Binta resta en retrait, prenant le temps de ranger ses affaires avec une lenteur calculée, espérant éviter la foule qui s’agglutine dans le couloir."
    "En sortant de la classe, elle put apercevoir un groupe de filles de sa classe la regarder."
    "Elle pouvait voir qu'elles se retenaient de rire, ou du moins essayer. C’est une cascade de rires, étouffés, retenus, comme si tout le monde essayait de ne pas éclater trop fort."
    
    show Binta_anxious at center
    b "Je vois que tout le monde me rigole, qu'est-ce qu'il se passe ?"
    "Les rires ne pouvaient plus se contenir : l'une des filles commença à se tordre de rire, incapable de se retenir davantage."

    play music "music/Echoes_of_Time.mp3" loop
    inconnu "Mais enfin tu comptes tout de même pas faire l'innocente ? On t'a TOUS vu le faire !"
    inconnu "Ouais c'est vrai ça, j'arrive pas à croire que quelqu'un ferait ça dans notre classe franchement !"
    "De quoi parlait-il ? Binta ne semblait pas se rappeler d'avoir fait quoique ce soit qui pourrait attirer les moqueries, que se passe-t-il bon sang !?"
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # This ends the game.

    return
