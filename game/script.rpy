# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("Binta", color="#BD93BD")
define y = Character("Yanis")
define m = Character("Maydan", color="#E94F37")
define s = Character("M.Serani", color="#6FFFE9")
define inconnu = Character("???")
define Ali = Character("Ali", color="#B4D6D3")


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
    "\"On verra plus tard\" se disa-elle, ferme les yeux, laissant son esprit divaguer. En quelques instants seulement, elle rejoigna les bras de Morphée."
    
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
    "Elle regarda la caméra, puis sourit: la vidéo se coupant pour laisser la place à des cris et des bruits écœurants"
    "La vidéo fut suffisamment horrible pour qu'une boule d'angoisse monte dans sa gorge, son cœur tambourine à un rythme effréné."
    "Elle jeta son téléphone d’un coup sec, mais il est déjà trop tard : le choc est là, l’image gravée dans son esprit comme une brûlure."
    "Les ombres de sa chambre, qui d’ordinaire lui paraissaient familières, lui semblent soudain hostiles."
    "Binta sent des larmes monter, mais elle se retient, envahie par une sensation de honte mêlée de peur."
    "Comment pouvait-on faire quelque chose d'aussi horrible ? Et surtout comment Kokot pouvait-il laisser n'importe qui poster ce genre de choses ?"
    "Elle sentit monter en elle un profond malaise, la sorte qui s'agrippe à vos tripes telle une charogne."
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
    "C'est ce que Yanis se serait dit si Binta n'était pas absente depuis déjà deux semaines."
    "Les vidéos qui ont circulé n'ont pas forcément détruit la réputation de Binta, puisque les collégiens ont fini par comprendre qu'il s'agissait de deep fake."
    "Cependant tout le monde ne cherche pas à connaître la vérité : un petit groupe continua à créer des deep fake et inventer des mensonges sur Binta : on appelle ça des fake news."
    "Parfois on ne cherche pas forcément LA vérité; seulement celle qui nous convient."
    "D'autres préférent fermer leur coeur à la vérité: tout le monde n'est pas un harceleur, mais le silence est tout aussi dangereux."
    "Pendant la pause, Yanis observe le petit comité qui s'était formé pendant l'absence de Binta."
    "On pouvait les entendre parler d'elle: des idées de deep fake, de fausses rumeurs à répandre... A leur tête se trouvait Maydan."
    
    show Mayden_default_happy at center
    m "Vraiment Sarah ta vidéo est excellente ! On dirait vraiment que Binta était chauve !"
    
    hide Mayden_default_happy
    "Le groupe se mit à rire aux éclats, tandis que chaque petits groupes "


    
    
    
    
    
    
    # This ends the game.

    return
