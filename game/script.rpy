# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("Binta", color="#000000")
define y = Character("Yanis", color="#000000")
define m = Character("Maydan", color="#000000")
define s = Character("M.Serani", color="#000000")
define inconnu = Character("???", color="#000000")
define Ali = Character("Ali", color="#000000")


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
image Maydan_angry = "Mayden_angry.png"
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

#Mr.Serani
image Serani_default = "serani_default.png"
image Serani_angry = "serani_angry.png"

#ali
image ali_default = "ali_default.png"


#backgrounds

#classroom
image bg_front_gate = "front-gate.jpg"
image bg_school_corridor = "school_corridor_background.jpg"
image bg_classroom_day = "Classroom_01_day.jpg"
image bg_classroom_evening = "Classroom_01_evening.jpg"
image bg_director_office = "Anime_Office_Background.png"


#road to school
image bg_street_evening = "someplace_usa_afternoon.jpg"
image bg_bedroom_evening = "room_dusk_light_on.jpg"

#ending
image bg_black_screen = "black.jpg"


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

    m "Mon nom c'est Maydan, l'oublie jamais parce qu'on va se retrouver."

    hide Mayden_annoyed

    "Maydan partit en courant, probablement pour distancer Binta."


    "Etait-ce une menace ? Devait-elle s'inquiéter ? Binta n'était pas sûre de ce qu'elle devait tirer de cette situation, Après tout ce n'était qu'une petite dispute à la rentrée."
    
    
    "Dans tous les cas, il est temps de commencer les cours, l'adolescente dût se rendre dans la hall d'entrée afin de pouvoir voir quelle classe rejoindre."

    "Quelle fut sa surprise, quand elle se rendit compte qu'elle a déjà fait la rencontre d'un de ses nouveaux camarades de classe ce matin..."

    "Mais bon, il est temps de commencer cette terrible journée se dit Binta, et ainsi commença la rentrée."
    play music "music/Evening.mp3" fadeout 1.0
    scene bg_classroom_evening with fade:
        xalign 0.5
        yalign 0.2
    

    "La journée se termina pour les étudiants du collège Hector Vugo, et Binta prépara ses affaires pour rentrer."
    "Le soleil commençait doucement à rejoindre l'ouest et Binta préférait ne pas trop tarder, ses parents commenceraient à s'inquiéter sinon."
    "Elle avait l'habitude de sortir en douce le soir pour prendre l'air, jusqu'à que ses parents l'attrapèrent la main dans le sac."

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
    
    
    
    play music "music/Study and Relax.mp3"
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
    "\"On verra plus tard\" se dit-elle, ferme les yeux, laissant son esprit divaguer. En quelques instants seulement, elle rejoigna les bras de Morphée."
    
    scene bg_front_gate with fade:
        xalign 0.5  # Centre horizontalement
        yalign 0.2  # Place plus haut verticalement
        zoom 0.8
    
    play music "music/Morning.mp3" loop
    
    "L'esprit encore partiellement engourdi, Binta se rendit au collège pour commencer une nouvelle journée."
    "Les rayons du soleil chauffèrent doucement ses joues et la ramèna petit à petit à ses sens."
    "D'autres étudiants semblèrent la regarder. On ne peut plus souffler un petit peu avant de rentrer ?"
    "Cela faisait déjà quelques jours depuis la rentrée, et Binta semblait s'être bien intégré dans sa classe. Elle discutait avec quelques élèves, entre les cours."
    "Binta se rendit en classe."

    scene bg_classroom_day with dissolve:
        xalign 0.5
        yalign 0.2
    
    

    "\"Quel brouhaha\" se dit Binta. Toute la classe était arrivée avant elle, et cette dernière ne voulait pas faire de vagues. "
    "Binta s'installa rapidement à la place que son professeur principal lui avait attitré."
    "Malgré sa furtive exécution de l'entrée à son bureau, elle pouvait sentir les regards se posaient sur elle."
    "Des chuchotements entrecoupés de rires faisaient écho dans la classe."
    "Chaque chuchotement et rire semblaient renforcer les regards sur Binta. Maydan quant à lui, semblait l'ignorer."
    inconnu "Sortez vos cahiers et taisez-vous, le cours commence !"
    "Sans que la plupart des élèves ne s'en aperçoivent, leur professeur était arrivé et s'était installé."
    "Le sentiment de malaise que ressentait Binta s'estompa peu à peu, les regards concentrés sur ce que le professeur disait."
    "Qu'a-t-il bien pu se passer ? Binta n'arrivait pas à se concentrer et son esprit fit tous les scénario possibles."

    scene bg_school_corridor with dissolve:
        xalign 0.5  # Centre horizontalement
        yalign 0.2  # Place plus haut verticalement
        zoom 0.6
    
    
    "La cloche retentit dans les classes et les couloirs de l'école, transformant les couloirs en un melting pot de bruits et d'élèves."
    "Binta resta en retrait, prenant le temps de ranger ses affaires avec une lenteur calculée, espérant éviter la foule qui s’agglutine dans le couloir."
    "En sortant de la classe, elle put apercevoir un groupe de filles de sa classe la regarder."
    "Elle pouvait voir qu'elles se retenaient de rire, ou du moins essayer. C’est une cascade de rires, étouffés, retenus, comme si tout le monde essayait de ne pas éclater trop fort."
    
    show Binta_anxious at center
    b "Je vois que tout le monde me regarde, qu'est-ce qu'il se passe ?"
    "Les rires ne pouvaient plus se contenir : l'une des filles commença à se tordre de rire, incapable de se retenir davantage."

    play music "music/Echoes_of_Time.mp3" fadeout 1.0 loop
    inconnu "Mais enfin tu comptes tout de même pas faire l'innocente ? On t'a TOUS vu le faire !"
    inconnu "Ouais c'est vrai ça, j'arrive pas à croire que quelqu'un ferait ça dans notre classe franchement !"
    "De quoi parlait-il ? Binta ne semblait pas se rappeler d'avoir fait quoique ce soit qui pourrait attirer les moqueries, que se passe-t-il bon sang !?"
    inconnu "Puisqu'il faut en arriver là... Cette vidéo ne te dit rien ?"
    "La jeune sorta son téléphone pour ensuite lancer une vidéo sur Kokot."
    "Sur cette dernière, elle voit une version d’elle-même taguer la porte d'une maison avec un énorme graffiti rouge sang : "
    "\"GROS NUL !\""
    "L’image est claire, trop claire. Elle regarde avec horreur \"elle-même\" rire et faire un clin d'œil à la caméra avant de s'enfuir en courant."
    "Comment était-ce possible ? Jamais Binta n'aurait fait quoique ce soit de la sorte."
    "Ce n’est pas elle. Elle le sait. Mais… c’est son visage, sa voix. Elle entend même son propre rire. Les commentaires sous la vidéo fusent :"
    "\"{i}Jamais cru qu’elle ferait un truc pareil.\"{/i}"
    "\"{i}OMG, elle est finie.\"{/i}"
    "\"{i}Vous savez c'est qui ?\"{/i}"
    "Binta décide de regarder le nombre de vues : plus de 12000 vues."
    "La vidéo est en train de gagner rapidement en popularité : ses parents, son frère, ses voisins, tous auraient pu voir la vidéo."
    
    show Binta_afraid at center
    hide Binta_anxious
    b "Je peux vous assurer que ce n'est pas moi ! Jamais je ne me permettrai de faire ça, encore moins sur la porte de quelqu'un !"
    inconnu "Ca ne sert à rien de te justifier ma grande, on te voit clairement le faire, c'est bien toi !"
    "Avant que Binta puisse rétorquer, une voix grave l'appela."
    s "Binta, je veux te voir dans mon bureau MAINTENANT."
    "Il s'agissait de nul autre que le directeur de Hector Vugo, M.Serani."
    "Les murmures éclatèrent aussitôt dans les couloirs : \"{i}C’est à cause de la vidéo, c’est sûr.\"{/i}"
    "Elle pouvait aussi entendre : \"{i}Moi, je savais qu’elle était bizarre.\"{/i}"
    "La personne qui a prononcé cette phrase ne la connaissait même pas..."
    
    scene bg_director_office with fade:
        xalign 0.5  # Centre horizontalement
        yalign 0.8  # Place plus haut verticalement
        zoom 2.5

    play music "music/Covert_Affair.mp3" fadeout 1.0 loop
    
    "Le bureau du directeur était plutôt étroit et opressant, on aurait dit que l'agencement de la pièce était conçu pour la confrontation."
    "Monsieur Serani, un homme aux cheveux grisonnants et à l’air sérieux, est assis derrière son bureau."
    show serani_default at right
    s "Assieds-toi, Binta."
    "Elle s’exécuta, ses mains moites posées sur ses genoux."
    s "Tu sais pourquoi tu es ici ?"

    show Binta_anxious at left
    b "J’imagine que c’est à cause de cette vidéo…"
    s "Exactement."
    "Il tourna l’écran sur son bureau vers elle. Le visage de Binta fut figé en train de taguer un mur."
    s "Peux-tu m’expliquer ce qu’on voit là ? Cette vidéo tourne en boucle dans l’école depuis hier soir. Les professeurs sont outrés, et certains élèves disent t’avoir reconnue."
    "Binta sent les larmes monter, mais elle refuse de pleurer."
    show Binta_afraid at left
    hide Binta_anxious
    b "Ce n’est pas moi ! Je n’ai jamais fait ça, je vous jure ! Quelqu’un a truqué cette vidéo."
    s "Truqué, dis-tu ? Ce que je vois ici est très réaliste. Et puis, pourquoi quelqu’un te viserait spécifiquement ?"
    "Elle ouvrit la bouche, mais aucun son n’en sort. Qui aurait fait ça, et pourquoi ? Elle-même n’a pas la réponse."
    b "Mais… ce n’est pas moi ! Vous devez me croire, monsieur Serani, je n’ai rien fait !"
    s "Ecoute Binta... Je ne dis pas que tu es la personne présente dans cette situation, mais si c'est bien le cas il y aura de lourdes conséquences."
    s "Qui plus est, j'ai un témoin qui t'a vu taguer cette porte."
    "Un témoin ? Comment était-ce possible puisque Binta n'a rien fait ?"
    "Avant de pouvoir trouver une réponse concluante, une personne entra dans le bureau du directeur."
    show Binta_afraid at left
    show serani_default at center
    show Mayden_default at right
    m "Pardon pour l'attente M.Serani."
    "C'était Maydan qui rentra dans la pièce."
    "Comment était-ce possible ? Que savait-il ? Ou bien était-il impliqué dans ce montage ?"
    s "Bien Maydan merci d'être venu, peux-tu m'expliquer à nouveau ce que tu sais ?"
    show Mayden_explaining at right
    hide serani_default
    hide Binta_afraid
    hide Mayden_default
    m "Bien monsieur... Tout a commencé à la rentrée, où j'ai bousculé par mégarde Binta. Elle a tout de suite été très énervé, et m'a menacé de me frapper."
    m "Au début je pensais à une simple dispute, mais c'est quand j'ai entendu des bruits étranges et des rires à l'entrée de ma maison que j'ai compris que c'était Binta."
    s "Es-tu sûr que c'était elle ?"
    m "Oui monsieur, j'ai pu apercevoir par la fenêtre Binta courir pour ne pas se faire attraper."
    "Binta était sous le choc : non seulement tout était faux, elle comprit assez vite que la personne derrière tout ça était bien Maydan."

    show Binta_angry at left
    b "Mensonges... TOUT est FAUX ! Ca ne s'est absolument pas passé comme ça !"
    b "Tu m'as bousculé avec ta trotinnette et après ça tu m'as menacé !"
    hide Mayden_explaining
    show Mayden_annoyed at right
    m "Tu devrais avoir honte de mentir à un adulte. Et puis pourquoi je ferais ça à ma propre porte d'entrée ?"
    hide Binta_angry
    hide Mayden_annoyed
    show serani_angry at center
    s "Cela suffit ! Que je ne vous entende plus parler."
    "Binta et Maydan fûrent tous les deux surpris par la voix grave et puissante du directeur. Son aura dans le moment exultait d'autorité."
    s "Sachez que l'affaire sera bien enquêté, les sanctions seront graves pour l'un comme pour l'autre quand j'aurais le fin mot de l'histoire. Maintenant filez en classe."
    "Binta et Maydan se rendirent donc vers la sortie du bureau, Maydan en premier, qui referma avec violence la porte derrière Binta."


    scene bg_school_corridor with dissolve:
        xalign 0.5  # Centre horizontalement
        yalign 0.2  # Place plus haut verticalement
        zoom 0.6

    "Pourquoi agir de façon aussi néfarieuse ? Binta ne méritait clairement pas ce qu'il lui arrivait."
    "Maydan...Ce rat ! Comment avait-il pu faire ça !? La colère sourde que ressentait Binta la rendit aveugle aux nombreux regards et moqueries silencieuses qu'elle subissait."
    "Dans tous les cas cette affaire sera réglée et on connaîtra le fin mot de l'histoire. Binta décida de rentrer chez elle."
    
    scene bg_street_evening with dissolve:
        xalign 0.5
        yalign 0.2
    play music "music/Evening.mp3"

    "Binta n'avait qu'une hâte : de rentrer et s'enfermer dans sa chambre."
    "La révélation du montage l'avait épuisé mentalement, et elle n'avait pas la force de faire quoi que ce soit."
    "Comment avait-il pu faire un montage aussi bien réalisé ? Il est vrai que si Binta ne connaissait pas la personne sur la vidéo, elle-même aurait pu croire qu'il n'y avait aucun trucage."
    "Peut-être l'a-t-on prise en photo ou en vidéo quand elle ne le savait pas ? Elle se rappela qu'elle ressentit des yeux l'observer il y a quelques jours de cela."
    "Ou bien était-ce grâce aux photos qu'elle posta sur Internet ? C'est vrai qu'elles sont facilement accessibles..."
    "Elle irait se renseigner en rentrant, se disait-elle. Il fallait aussi en parler à ses parents, qui risquaient de tomber sur la vidéo eux-aussi."



    
    scene bg_bedroom_evening with dissolve: 
        xalign 0.5
        yalign 0.2
    play music "music/Study and Relax.mp3"

    "Arrivée chez elle, Binta expliqua aussitôt la situation à ses parents. Les deux ne s'y connaissaient pas assez en technologie, mais avait foi en leur fille."
    "Cela rassura un peu l'adolescente de savoir qu'elle n'était pas seule dans cette situation. Bien que pour l'instant, elle était toujours très inquiète."
    "Comme à son habitude, elle prit une pomme du panier et enjamba les marches des escaliers pour atteindre sa chambre."
    "Allongée sur son lit, elle décida de prendre son téléphone pour regarder Kokot et voir si la vidéo était toujours en ligne."
    
    play music "music/Echoes_of_Time.mp3" fadeout 1.0 loop
    "Toujours en ligne avec des vues impressionnants... Mais le pire, c'est qu'il y avait de nouvelles vidéos."
    "Elles proviennent de plusieurs comptes et ne sont plus limités qu'à un seul."
    "On y voit de tout : Binta qui tague des bâtiments et des véhicules, qui renverse des poubelles, qui insulte des gens de sa classe..."
    "Une vidéo retourna particulièrement l'estomac de l'adolescente."
    "On pouvait y voir Binta, un chaton à la main."
    "Elle regarda la caméra, puis sourit: la vidéo se coupant pour laisser la place à des cris et des bruits écœurants."
    "La vidéo fut suffisamment horrible pour qu'une boule d'angoisse monte dans sa gorge, son cœur tambourine à un rythme effréné."
    "Elle jeta son téléphone d’un coup sec, mais il est déjà trop tard : le choc est là, le son gravée dans son esprit comme une brûlure."
    "Les ombres de sa chambre, qui d’ordinaire lui paraissaient familières, lui semblent soudain hostiles."
    "Binta sent des larmes monter, mais elle se retient, envahie par une sensation de honte mêlée de peur."
    "Comment pouvait-on faire quelque chose d'aussi horrible ? Et surtout comment Kokot pouvait-il laisser n'importe qui poster ce genre de choses ?"
    "Elle sentit monter en elle un profond malaise, la sorte qui s'agrippe à vos tripes tel un parasite."
    "Par une curiosité auto-destructrice, elle décida d'aller regarder les commentaires."
    "Elle hésite une seconde, son doigt suspendu au-dessus de l’écran. Elle sait qu’elle ne devrait pas regarder, mais la curiosité et une sombre impulsion l’emportèrent."
    "Binta sentit sa gorge se nouer et son souffle devenir erratique. La vague de haine qu'elle reçut était beaucoup trop important pour la jeune adolescente."
    "\"{i}Trop facile de faire l’innocente maintenant, mais on te connaît et tu vas le payer.\"{/i}"
    "\"{i}Sa pauvre famille, elle doit les décevoir grave.\"{/i}"
    "\"{i}Si c’était ma sœur, je serais mort de honte. Elle devrait disparaître, sérieux.\"{/i}"
    "Elle laisse échapper un sanglot étouffé, étouffant presque un cri."
    "Ces nombreuses vidéos l'exposaient à des milliers de personnes qui ne la connaissait même pas mais qui lui souhaiter du malheur."
    "Ce n'était pourtant pas les noms qu'elle ne reconnaissait pas qui l'a choqué."
    "Elle reconnut certains noms parmi les comptes qui l'attaqua. Des personnes de son collège, voire même de sa classe."
    "Sans qu'elle s'en rende compte à travers ses larmes, elle avait reçu une multitude de messages sur Kokot, tout aussi horrible que les commentaires."
    "L'un  des messages l'ayant particulièrement marqué venait de son amie, qui lui envoya un message quelques jours plus tôt."
    "\"{i}Mieux vaut que tu ne viennes pas en cours.\"{/i}"
    "Le monde en dehors de sa chambre semble lointain, inaccessible."
    "Tout ce qui existe pour elle à cet instant, c’est la douleur de ces commentaires, la peur qu’ils soient ce que les gens pensent vraiment d’elle."
    "et l’impression qu’elle ne pourra jamais effacer cette vidéo, ni ce qu’elle a provoqué..."





    "son frère, qui entendit le grabuge dans la chambre de sa soeur, décida de rentrer."
    show ali_default at center
    Ali "Eh oh qu'est-ce qu'il se passe ici ? Pourquoi tu fais tout un vacarme ?"
    "Binta n'a pas su contenir ses larmes lorsque son frère débarqua soudainement dans sa chambre. Toutes ces émotions devaient bien redescendre un moment ou un autre, de toute manière."
    "Elle expliqua tout en détail à son frère, de la bousculade avec Maydan, aux montages d'elle faisant des actions horribles."


    scene bg_bedroom_evening with fade: 
        xalign 0.5
        yalign 0.2
    play music "music/Study and Relax.mp3"
    
    show ali_default at center
    Ali "D'accord, j'ai compris la situation..."
    "Son frère était plus âgé qu'elle de seulement deux ans, mais il s'y connaissait déjà un rayon en technologie. Il passait le plus clair de son temps dans sa chambre à créer des programmes."
    Ali "Binta… écoute-moi. Ce que t’as vu là, c’est ce qu’on appelle un deep fake. T’en as déjà entendu parler ?"
    "Elle secoua la tête sans le regarder, toujours accablée."
    Ali "C’est une technologie qui utilise l’intelligence artificielle pour coller le visage de quelqu’un sur une vidéo ou des images d’une autre personne."
    Ali "Ça peut paraître hyper réaliste, mais c’est complètement faux. Ce n’est pas toi, d’accord ? C’est une manipulation."
    "Elle relève la tête, ses yeux encore embués de larmes."
    b "Mais… mais les gens y croient ! Ils partagent ça partout ! Et maintenant, tout le monde pense que c’est moi dans cette… cette vidéo horrible…"
    Ali "Je sais que c’est super dur, Binta, mais écoute-moi bien : ce n’est pas ta faute. Les gens qui font ce genre de choses sont des monstres."
    Ali "Il faut qu’on réagisse vite, OK ? On peut signaler cette vidéo, contacter TikTok, et même porter plainte. Mais ce qui est sûr, c’est que personne qui te connaît vraiment ne croira à ces bêtises."
    "Il lui tend son téléphone et la prend dans ses bras, la serrant contre lui avec une douceur fraternelle. Binta laisse enfin échapper un soupir."




    scene bg_classroom_day with fade:
        xalign 0.5
        yalign 0.2
    play music "music/Morning.mp3" fadeout 1.0 loop
    
    "Une journée comme une autre."
    "C'est ce que Yanis se serait dit si Binta n'était pas victime de cyberharcèlement."
    "Les vidéos qui ont circulé n'ont pas forcément détruit la réputation de Binta, puisque les collégiens ont fini par comprendre qu'il s'agissait de deep fake."
    "Cependant tout le monde ne cherche pas à connaître la vérité : un petit groupe continua à créer des deep fake et inventer des mensonges sur Binta : on appelle ça des fake news."
    "Parfois on ne cherche pas forcément LA vérité; seulement celle qui nous convient. Et c'est pour ça que certains croient plus facilement en des mensonges."
    "D'autres préférent fermer leur coeur à la vérité: tout le monde n'est pas un harceleur, mais le silence est tout aussi dangereux."
    "Pendant la pause, Yanis observe le petit comité qui s'était formé."
    "On pouvait les entendre parler d'elle: des idées de deep fake, de fausses rumeurs à répandre... A leur tête se trouvait Maydan."
    
    show Mayden_default_happy at center
    m "Vraiment Sarah ta vidéo est excellente ! On dirait vraiment qu'elle' était chauve !"
    
    hide Mayden_default_happy
    "Le groupe se mit à rire aux éclats, tandis que chaque autre élève de la classe choisit de les ignorer."
    m "Les amis je vais mettre une vidéo sur le groupe de classe je veux que vous repartagiez tous !"
    "Le fameux groupe de classe... Maydan et son groupe l'ont créé sans y inclure Binta. La pauvre ne sait même pas que certains l'utilisent pour se moquer d'elle."
    "Binta s'était mise à une place dans la classe qui permettrait de s'isoler de tous, un moyen pour elle de se couper de l'harcèlement qu'elle subissait."
    "Yanis la regardait, puis son regard se porta sur le groupe de Maydan, toujours en pleine moquerie de Binta."


    menu: 
            "Yanis allait-il laisser les choses se passer ainsi ?"

            "Intervenir":

                jump goodEnding
            
            "Ne rien faire":

                jump badEnding
    



label badEnding:

    play music "music/Evening.mp3" fadeout 1.0
    scene bg_classroom_evening with fade:
        xalign 0.5
        yalign 0.2
    
    "Il avait décidé de ne rien faire."
    "Yanis n'était pas du genre à rester silencieux face à ce genre d'injustice, et pourtant, il laissa les événements se dérouler comme ils se sont déroulés durant déjà plusieurs jours."
    "Pourquoi ne l'avait-il pas défendue ? Il se trouvait mille excuses : \"Ce n’est pas mon problème\", \"Je ne veux pas devenir leur prochaine cible\", \"C’est juste une blague, non ?\""
    "Pourtant, au fond de lui, il savait. Il savait que les moqueries allaient trop loin."
    "Chaque recoin de la salle de la classe lui faisait penser à Binta."
    "Son sourire timide illuminait parfois les journées grises, mais elle était désormais absente. Définitivement absente."
    "Binta n'est pas venue depuis bientôt 3 semaines, une absence aussi prolongée s'avère risquée pour sa place dans l'établissement."
    "En même temps comment revenir ? Ce n'était plus que les deep fake le problème : les collégiens étaient submergés par des fake news sur Binta."
    "Binta aurait tué des animaux, Binta aurait volé plusieurs camarades de classe, Binta aurait des poux..."
    "On a tout entendu concernant Binta, comme s'il s'agissait de la personne la plus horrible au monde."
    "Et tout était faux."
    "La tête pleine de pensées, Yanis rentra chez lui."
    
    scene bg_street_evening with dissolve:
        xalign 0.5
        yalign 0.2  
    
    "Sur le trajet, Yanis jouait la scène en boucle. Si seulement il avait intervenu."
    "Autant pour Binta que pour Maydan : ce comportement finirait par détruire l'humanité qu'il avait."
    "Maydan et lui se connaissaient bien. Ils avaient l'habitude plus jeunes de se retrouver chaque été pour jouer avec les autres jeunes de leur quartier."
    "S'il avait pu mettre fin à la folie de Maydan plus tôt, le jeune homme ne serait pas allé aussi loin."
    "Maintenant tout ceci est trop tard..."
    "Yanis se retourna une dernière fois sur la rue avant de rentrer chez lui. On voyait les familles remplir la rue de discussions et de rires."
    "Demain sera une autre journée pour lui, mais Binta restera bloquée dans le passé."

    scene bg_black_screen with fade:
        xalign 0.5
        yalign 0.2
        zoom 2.0

    centered "{size=+75}{cps=8}{color=#ffffff}BAD ENDING{/color}{/cps}{/size}{p=5.0}{nw}"
    centered "{size=+75}{cps=8}{color=#ffffff}Écrit par:\n\nLes jeunes de Louise Michel{/color}{/cps}{/size}{p=5.0}{nw}"
    centered "{size=+75}{cps=8}{color=#ffffff}Codé par:\n\nVegacy{/color}{/cps}{/size}{p=5.0}{nw}"

    
    
    return 
label goodEnding:

    "L'harcèlement devait cesser."
    play music "music/Junkyard_Tribe.mp3" loop fadeout 1.0
    show Yanis_angry at left
    y "Assez ! Je sais pas si tu te rends compte de ce que tu fais Maydan, mais ça va beaucoup trop loin !"
    "le cri soudain de Yanis fit sursauter la classe entière. C'était quelqu'un d'assez calme, et personne n'avait entendu sa voix aussi forte."
    y "C'est mal ce que tu fais. Et se taire l'est tout autant. Je ne suis pas le seul dans la classe a pensé que tout ça va trop loin, mais tout le monde a peur de parler. Pas moi."
    "Le groupe de Maydan était bouche bée, le plus choqué étant Maydan. Les deux jeunes hommes se connaissaient du temps où ils vivaient dans le même quartier, et les deux n'ont pas encore pu rattraper le temps perdu."
    
    show Mayden_annoyed at right
    m "Tiens Yanis ça fait longtemps... Et que suis-je en train de faire au juste ?"
    y "Ce que tu fais c'est du cyberharcèlement. C'est mal et c'est puni par la loi !"
    m "Pfff... Même pas vrai !"
    y "Si tu ne me crois pas tu peux aller vérifier sur internet, c'est vrai quoi t'as pourtant l'habitude de l'utiliser quand tu fais des montages de Binta !"
    "En entendant son nom, on pouvait apercevoir Binta restait figée, comme si le moindre mouvement attirerait l'attention vers elle."
    
    show Mayden_anxious at right
    hide Mayden_annoyed
    m "Je... Tout ça c'était pour rire ! On voulait pas faire de mal à Binta, hein Binta tu trouvais ça drôle nan ?"
    "Les mots semblaient vides de sens, même pour Maydan. Il savait pertinemment que ce qu'il faisait était mal."

    show Binta_sad at center
    b "Non... Ce n'était pas drôle. T'as une idée du nombre de personnes qui m'harcèlent en message privée ? Qui pense encore que c'est moi sur ces vidéos ?"


    y "En plus on sait très bien qui a tagué ta porte... Et c'est toi !"
    "Tous savaient au fond d'eux qu'il s'agissait de Maydan derrière chaque vidéo, où il rajouta le visage de Binta, mais aucun ne voulait y croire."
    "Avant que Maydan puisse rétorquer, le professeur d'anglais débarqua dans la classe."
    inconnu "At your desks please... And be quiet !"

    scene bg_classroom_evening with dissolve:
        xalign 0.5
        yalign 0.2
    play music "music/Evening.mp3" fadeout 1.0 loop

    "La cloche signala la fin des cours pour la journée. La dispute survenut auparavant mit un malaise certain dans la classe, mais les choses devaient être dites."
    "Maydan fut le premier à partir de la classe, puis son groupe d'harceleurs, laissant derrière eux les chuchotements de leur classe."
    "Pourquoi personne n'a défendu Binta ? Chacun se trouvait mille excuses : \"Ce n’est pas mon problème\", \"Je ne veux pas devenir leur prochaine cible\", \"C’est juste une blague, non ?\""
    "Pourtant, au fond d'eux, ils savaient. Ils savaient que les moqueries allaient trop loin."
    "Tandis que Yanis rangeait tranquillement ses affaires, il aperçut une silhouette familière s'approcher de lui."

    show Binta_anxious at right
    show Yanis_default_happy at left
    b "Merci encore d'avoir pris ma défense... Ca m'a fait du bien de savoir que j'avais encore des alliés dans la classe."
    "Les mots de Binta consolida ce que Yanis pensait : c'était la meilleure décision à prendre."
    y "Ecoute il y a aucun souci... Si tu as besoin de quoi que ce soit tu peux m'en parler."
    b "Justement, tu aurais des idées pour stopper cette situation ?"

    show Yanis_explaining at left
    hide Yanis_default_happy


    y "Eh bien justement il y a plusieurs choses à faire ! Il faut..."

    menu: 
            y "Eh bien justement il y a plusieurs choses à faire ! Il faut..."

            "Répondre aux moqueries.":

                jump repondreMoquerie
            
            "Ne pas répondre aux moqueries.":

                jump pasRepondreMoquerie
    
label repondreMoquerie :
    show Yanis_explaining
    y "la meilleure chose à faire est de répondre aux moqueries !"
   
    b "Euh... T'es sûr de toi ? Ca leur montrerait pas tout simplement que ça m'atteint ?"
    y "Ah oui c'est pas faux..."
    "Mieux vaut les ignorer. Le silence est le meilleur des mépris."

label pasRepondreMoquerie:
    show Yanis_explaining
    y "La meilleure chose à faire est de les ignorer. Le silence est le meilleur des mépris !"
    show Binta_very_happy at right
    hide Binta_anxious
    b "Oh d'accord je vois ! C'est vrai je ne devrais pas leur montrer que ça m'atteint !"
    
    b "Ensuite ? Tu as d'autres conseils ?"
    menu: 
            y "Bien sûr ! Il faut..."

            "Ne pas prévenir un adulte.":

                jump nePasPrevenir
            
            "Prévenir un adulte.":

                jump Prevenir

label nePasPrevenir:
    y "Mieux vaut ne pas prévenir un adulte, ils ne comprendraient pas de toute façon..."
    show Binta_anxious at right
    hide Binta_very_happy
    b "Ca ne me paraît pas très responsable de ne pas en parler à un adulte de confiance... Et puis, quand on est jeunes c'est les adultes qui ont l'autorité non ?"
    y "Tu marques un point là..."
    "{i}Je donne de très mauvais conseils là non ??{/i}"

label Prevenir:
    y "Il est préférable d'avertir un adulte de confiance. Il saura quoi faire dans ce genre de situations."
    y "Ca peut peut être un enseignant, une assistante d'éducation, un parent, une CPE..."
    y "Tu peux même contacter le 3018 au cas où tu n'aurais personne avec qui parler : un adulte t'écoutera et te viendra en aide !"
    b "J'ai prévenu mes parents, je devrais quand même prévenir les enseignants et dire à M.Serani que je me fais harceler..."
    show Binta_sad at right
    hide Binta_anxious
    hide Binta_very_happy
    b "Il pensait que c'était moi qui avait tagué la porte de Maydan... Je ne sais pas s'il est au courant des autres vidéos qui m'harcèlent par contre."
    

    menu: 
            y "Justement concernant les autres vidéos tu devrais..."

            "Laisser les choses se faire.":

                jump letItBe
            
            "Conserver des preuves.":

                jump Preuve

label letItBe:
    y "Je pense que tu devrais laisser les choses se faire. Elles finiront par disparaître."
    b "Justement, c'est pas mieux que j'enregistre les preuves de mon harcèlement ? Pour plus facilement prouver mon innocence et leur culpabilité."
    y "Ah mais oui bien sûr..."
    "{i}Je suis VRAIMENT à côtés de la plaque...{/i}"

label Preuve: 
    y "Garde des preuves de ton cyberharcèlement. Crée un dossier avec les vidéos, les commentaires, les messages que tu reçois..."
    y "Documente ce que tu faisais à certains moments lors de la diffusion des vidéos, enregistre les noms des comptes qui t'harcèlent..."
    y "En bref, avoir le plus de preuves de ton harcèlement va faciliter le travail des autorités compétentes pour incriminer tes harceleurs."
    b "Merci beaucoup pour tous ces conseils vraiment... J'espère que la dispute ne t'attirera aucun ennui."
    y "Je ne me laisserai pas atteindre par tout ça ne t'en fais pas... Je vais bloquer et signaler tout ce que je vois qui serait néfaste pour moi."
    b "Et pour le groupe de classe sur Whatsapp ? Personne ne m'a ajouté..."
    y "Effectivement si personne ne t'a ajouté, c'est vraiment pas bien ! Tout le monde devrait être inclus pour éviter de se sentir à l'écart..."
    b "Tu as des conseils en particulier ?"
    y "Oui ! L'idéal serait d'avoir des modérateurs, qui pourront juger de la bonne conduite de la classe !"
    b "Oh c'est une superbe idée ! On en parlera aux professeurs pour qu'ils nous aident à mettre le groupe en place !"


    "Après cette longue discussion sur le cyberharcèlement, nos deux adolescents prirent leur chemin respectif."
    "Yanis était fier de lui pour avoir intervenu, et fier de Binta pour avoir été si courageuse. Il espérait que les bons conseils qu'il lui a donné serait utile pour Binta."
    

    scene bg_front_gate with fade:
        xalign 0.5  # Centre horizontalement
        yalign 0.2  # Place plus haut verticalement
        zoom 0.8
    play music "music/Morning.mp3"

    "Plusieurs jours ont passé depuis la dernière discussion entre Yanis et Binta. Un long weekend a marqué une pause dans la vie scolaire des étudiants."
    "Il n'avait pas trop pu regarder si le contenu dégradant envers Binta continuer. Si c'était le cas, Yanis devra voir Maydan en personne."

    scene bg_school_corridor:
        xalign 0.5  # Centre horizontalement
        yalign 0.2  # Place plus haut verticalement
        zoom 0.6
    "Arrivé à l'entrée de sa classe, M.Serani interpella Yanis."

    show Serani_default at center
    s "Bonjour Yanis, pourrais-tu me suivre dans mon bureau s'il te plait ?"
    y "Bonjour monsieur, oui bien sûr..."
    "De quoi s'agissait-il ?"


    scene bg_director_office with dissolve:
        xalign 0.5  # Centre horizontalement
        yalign 0.8  # Place plus haut verticalement
        zoom 2.5
    play music "music/Covert_Affair.mp3" loop
    "Une fois arrivé dans le bureau du directeur, Yanis remarqua qu'il n'était pas le seul à avoir été convoqué."
    "Dans la pièce se trouvait Binta, son regard essayant de fuir un maximum la présence de Maydan, qui était assis à côté d'elle."
    s "Tu peux t'asseoir Yanis."
    "M.Serani avait un grand canapé en face de son bureau. Yanis décida de prendre la place du centre, qui sépare Binta de Maydan."
    show Serani_default at center
    s "Bien. Il a été porté à mon attention que Maydan eut la porte de sa maison taguée par Binta, parmi d'autres vidéos que Binta aurait prise d'elle."
    show Maydan_angry at right
    hide Serani_default
    m "Ouais exactement ! J'espère que tu répondras de tes actions Binta !"
    "Chacun pouvait sentir la nervosité dans la voix tremblante de Maydan."
    "Binta, quant à elle, semblait simplement regarder le directeur en souriant."
    s "Justement à ce propos... Maydan nous allons te renvoyer de l'établissement. Je vais convoquer tes parents pour convenir à ton expulsion."

    play music "music/Hot Pursuit.mp3" fadeout 1.0 loop
    show Serani_angry at center
    hide Maydan_angry

    s "Non seulement tu m'as menti, moi le directeur, mais tu as aussi créé de fausses images de Binta, des deep fake."
    s "Binta, montre-lui."
    "Binta, d'un sourire triomphant, sortit son téléphone."
    "Dessus, on pouvait y voir un dans le gestionnaire de fichiers un dossier au nom bien singulier : \"PREUVES.\""
    "Maydan savait que c'était fini pour lui."
    "Dans ce dossier, on pouvait voir les nombreuses images et vidéos truqués de Binta, mais pour chacune de ces images, on y trouvait aussi de légers indices."
    "Binta avait répertorié tous les moments où le deep fake n'était pas convaincant."
    "En effet l'adolescent avait mal utilisé la technologie: on pouvait voir à certains moments des artéfacts; des erreurs dans le montage."
    "Les bordures entre le visage et les cheveux ou le cou peuvent être mal définies."
    "Les ombres sur le visage peuvent être mal placées ou ne pas correspondre à l'éclairage général de l'image."
    "Des zones floues peuvent être visibles près des cheveux, des vêtements, ou autour du visage."
    "Les deepfakes peuvent générer des expressions faciales ou des mouvements étranges qui ne correspondent pas à la posture générale de la personne."
    "Tous ces indices permettent de repérer si une vidéo est authentique ou non."
    "Les preuves sont accablantes : toutes les vidéos sont truqués."
    "Sur certaines vidéos, on pouvait même voir la \"main\" de Binta être blanche, indiquant ainsi que ce n'était pas elle, mais bien Maydan qui est responsable des deep fake."

    show Binta_explaining at left
    hide Serani_angry

    b "Ce n'est pas tout; en utilisant des outils comme Deepware Scanner ou InVID, on peut repérer les moments où il y a usage de deep fake."
    b "Avec mon frère, j'ai pu récolter un maximum de preuves me permettant de me disculper. Fallait y réfléchir à deux fois avant de m'attaquer."
    "Maydan ne tenait plus : on pouvait le voir visiblement nerveux, la tête baissée et jouant avec ses pouces."
    b "Bien entendu, si les deep fake sont faux, on peut conclure logiquement que les choses qui se dites sur moi le sont aussi. Ce sont des fake news."
    s "Quelque chose à dire pour ta défense peut-être ?"
    "Le directeur posa une question à Maydan, mais rien qu'il ne dirait pouvait le sauver."
    
    show Mayden_afraid at right
    m "C'est vrai... C'est vrai ! Quasiment tout est de moi ! Mais pas tout, j'ai pas été le seul à faire ça je vous le jure !"
    "Maydan, dans une pathétique tentative pour éviter l'expulsion, dénonca tous les complices de l'harcèlement."
    
    show Serani_default at center
    s "Bien merci Maydan, sache que tes acolytes seront eux aussi punis sévèrement."
    m "Je...Je..."
    m "C'est vrai tout ça est allé trop loin. Au début j'avais fait ça pour me venger, mais en voyant les stats que je faisais sur Kokot... J'ai pas su m'arrêter."
    m "Plus j'en faisais, mieux je me sentais. Je faisais tout ça pour le buzz."
    hide Serani_default
    show Serani_angry at center
    s "Le buzz... Je déteste ce mot. Regarde où cela t'a mené, tu pensais qu'il n'y avait aucune conséquence à tes actes ?"
    m "..."
    "Maydan préféra ne pas répondre, pour ne pas aggraver sa situation."
    s "Le pire dans cette situation, c'est que personne ne remet en question ce qu'il regarde. On vous vend une information et vous la consommez."
    s "Hélas, c'est aussi pour ça que l'harcèlement de Binta a pris de l'ampleur. Personne n'a cherché à savoir si tout cela était vrai, ni éthique."
    s "Je pense qu'il est temps pour votre génération de prendre du recul sur ce que vous voyez sur Internet. Regardez où cela nous mène."
    "M.Serani regarda avec une grande désapprobation Maydan. Son regard aurait pu suffire à terrifier le jeune homme, s'il n'avait pas le regard aussi fuyant."
    hide Serani_angry
    show Yanis_concerned at center
    y "Euh monsieur, pourquoi m'avez-vous convoqué, si ce n'est pas indiscret ?"
    "Même s'il n'avait rien à se reprocher, l'intensité du regard de M.Serani le mettait mal à l'aise, comme si un poids invisible pesait soudain sur ses épaules."
    hide Yanis_concerned
    show Serani_default at center
    s "Oui... Et bien je t'ai convoqué pour te remercier. Binta m'a fait part de ton intervention en classe. Pour l'avoir défendu et conseillé."
    hide Serani_default
    show Yanis_concerned at center
    y "Oh eh bien écoutez, je n'ai fait que mon devoir citoyen !"
    "Yanis s'était dit que sa petite blague détenderait l'atmosphère. Personne n'a ri."
    hide Yanis_concerned
    show Serani_default at center
    s "Je voulais aussi te remercier Binta. Tu as été exemplaire et courageuse malgré cette situation. Je m'excuse d'avoir douté de toi une seconde."
    b "Ca ne fait rien monsieur le directeur je vous assure. Merci de m'avoir cru."
    s "Maydan, quant à toi, tu n'as rien à dire à Binta ?"
    "Maydan avair l'air effondré : son dos était voûté comme si le poids de ses pensées l'écrasait. Ses mains tremblantes étaient posées sur ses genoux."
    hide Mayden_afraid
    show Mayden_sad at right
    m "Euh... Oui. Binta je suis vraiment désolé pour tout ce que je t'ai fait subir. Tu ne méritais pas ça. Si cela te va, je peux tout supprimer et faire une vidéo d'excuse sur mon compte kokot."
    s "Bien. Sur ce, si vous n'y voyez aucune objection, Binta et Yanis, je vous demanderai de rejoindre votre classe, j'attends les parents de ce jeune homme."
    "Maydan le savait : c'était son dernier jour à Hector Vugo. Rien n'y changerait ça. L'air abattu, il regarda les deux adolescents quitter la pièce."


    scene bg_street_evening with fade:
        xalign 0.5
        yalign 0.2

    play music "music/Evening.mp3"

    "Le dénouement de l'harcèlement se fera petit à petit avec l'intervention du corps enseignant."
    "Les élèves impliqués dans l'affaire, de cyberharcèlement, dont Maydan, ont tous été expulsés du collège."
    "L'affaire a fait un bruit retentissant dans les média. Qui aurait crû que des jeunes soient capables de tout ça ?"
    "Pour Yanis, l'affaire paraîssait déjà loin pourtant. La vie reprit assez vite son cours pour Binta, acclamée en héroïne par les élèves et la presse."
    inconnu "Attends !"
    "Une voix s'exclama derrière Yanis, le sortant de ses pensées."

    show Binta_default_happy at right
    b "Salut Yanis ! Tu rentres chez toi ?"

    show Yanis_default_happy at left
    y "Ouais c'est exact... Toi aussi ?"
    b "Oui j'emprunte ce chemin, on fait la route ensemble ?"
    
    hide Yanis_default_happy
    show Yanis_very_happy at left
    y "Avec plaisir !"
    "A vrai dire Yanis attendait une opportunité comme celle-ci pour se rapprocher de Binta."
    "Et c'est ainsi que cette histoire se termine, mais celle de nos protagonistes ne fait que commencer."


    scene bg_black_screen with fade:
        xalign 0.5
        yalign 0.2
        zoom 2.0

    centered "{size=+75}{cps=8}{color=#ffffff}GOOD ENDING{/color}{/cps}{/size}{p=5.0}{nw}"
    centered "{size=+75}{cps=8}{color=#ffffff}Écrit par:\n\nLes jeunes de Louise Michel{/color}{/cps}{/size}{p=5.0}{nw}"
    centered "{size=+75}{cps=8}{color=#ffffff}Codé par:\n\nVegacy{/color}{/cps}{/size}{p=5.0}{nw}"

    # This ends the game.

    return
