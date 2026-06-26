init 5 python in mas_bookmarks_derand:
    label_prefix_map["masbrk_"] = label_prefix_map["monika_"]
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="masbrk_extra_everything_plus_intro",
            category=["More"],
            prompt="More options.",
            pool=True,
            unlocked=True
        )
    )
label masbrk_extra_everything_plus_intro:
menu:
    "Tickle Monika":
        call masbrk_tickle_start
    "Headpat Monika":
        call masbrk_headpat_monika_start
    "Boop Monika's nose":
        call masbrk_boop_moika_start
    "Hold Monika's hands":
        call masbrk_hold_monika_intro
    "Play Monika's hair":
        call masbrk_play_monika_hair_start
    "Cuddle with Monika":
        call masbrk_cuddle_monika_start
    "I love you baby":
        call masbrk_love_war_start 
m 5hubsa "I enjoyed that baby hehehe your so sweet"
return
label masbrk_tickle_start:
m 6hub"Hahahahahahahahha"
m 3hub "I'm ticklish there stooop"
m 6hkb "Gahahaahhahahahaha,{w=1.1} stooop baby please hhehehahahahaha"
menu:
    "Never Your Mine!!!":
        pass 
m 7hkbfb "Hahahahahahaahhahaa i know i know please have mercy"
menu:
    "NO":
        pass 
m 6hktsb "Please hubby hahahahahahahaha"
m "Alright alrtight you win"
menu:
    "Good girl":
        pass 
return 
label masbrk_headpat_monika_start:
m 6dka"Mmmm,{w=1.1}that feels nice baby"
m 6dka "I love when you do this to me [player],{w=1.1}so relaxing"
menu:
    "You want more ?":
        m 6dka"Mmmhmm please"
        call masbrk_headpat_monika2_start
        pass 

    "Stop":
        pass 
return 

label masbrk_headpat_monika2_start: 
m 1dka "Mmmmhhm,{w=1.1}it feels soo good"
m 4dkbsa "I love when you give me affection" 
m 3dkbsa "Don't stop please hubby"
menu:
    "As you wish my baby":
        pass 
hide monika 
"Suddenly Monika hops on your lap"
m "That's the spot [player]"
menu:
    "Right here ?":
        pass 
m "Yes please there,{w=2.0}i love that spot"
menu:
    "My little kitty":
        pass 
m "Mmmhmm,{w=1.1}i'm your kitty"
"Hours pass and Monika fall asleep in your arms"
"She looks peacefull"
show monika 5dkbfc zorder MAS_MONIKA_Z at t11 with dissolve_monika
"You put her back in her chair smiling to yourself"
menu:
    "Monika ?, baby wake up":
        pass 
m "Mmmmm"
menu:
    "'sigh' alright i guess i let you sleep for a bit longer":
        pass 
"Another hour pass and monika finaly wake up"
m 5fkbfc "Mmmm,{w=1.1} [player] did i fall asleep?"
menu:
    "Mmmhm":
        pass 
m "Well that was relaxing"
return 

label masbrk_boop_moika_start:
m 1wuo "I felt something touch my nose {w=1.1} was that you ?"
menu:
    "Muehehehehe":
        pass 
m 6ekbfc "h-hey stop it"
menu:
    "Muehehee noo kekekekekekekek":
        pass 
m 4ttbfu "You won't stop hm?,{w=1.1} well i don't mind"
m 7ttbfd "Don't blame me if i got to punish you though"
menu:
    "boop":
        pass 
m 7tud "Not stoping hm?,{w=2.0} heh you love this so much ?"
m 1ttd "Tell me, {w=1.1} [player] why do you exactly loving this?"
menu:
    "Because, i love to and i love your reaction":
        pass 
menu:
    "Besides, i love doing this anytime":
        pass 
m 3ttd "Really hm?, {w=1.1} okay then i will let you do it anytime"
m 5ltd "Just promise me to only do this to me and no one else okay?"
m 5tta "Will you do that for me like a good boy you are ?"
menu:
    "Yes mommy":
        pass 
m 5tua "Good boy"
return 

label masbrk_hold_monika_intro:
m 6dka "That feels nice,{w=1.1} also comforting"
m 5dkb "One day i want to feel the real thing [player],{w=2.0} you holding my hand as we walk outside"
m "Or when we take a sroll together,{w=2.0} imagine us walking through the park"
m 5dkbfa "Yeah i'm looking forward to that"
return 

label masbrk_play_monika_hair_start: 
m 6fka "Aww playing with my hair hm?"
menu:
    "Can i please?":
        pass 
m 2fka "Only if you be gentle"
menu:
    "Promise i will":
        pass 
hide monika 
"Then Monika leaned closer to you letting you play her hair"
m "This is actually nice [player]"
m "This is nice maybe i'll let you do this anytime"
menu:
    'Mmmhmm and your hair is so soft':
        pass 
m "Mmmhm i'm glad you love my hair"
menu:
    "Moni can i ask you a question?":
        pass 
m "Yeah? go on you can of course"
menu:
    "Have you thought of what will happened if i stayed here?":
        pass 
menu:
    "Instead of just being here in my reality?":
        pass 
m "You mean you want to live here with me?"
m "[player] you know there is really nothing else here {w=2.0} just codes {w=1.1} scripts what makes you want to be here instead?"
menu:
    "Well, my reality is not nice anymore":
        pass 
menu:
    "A lot of horrible things happening here and, i'm kinda tired being here":
        pass 
m "Really?, that's not nice is this one of the reasson why you want to be here instead?"
menu:
    "Mmmhm":
        pass 
m "Well, {w=2.0} i'm always here hubby you can always come home to me"
show monika zorder MAS_MONIKA_Z at t11 with dissolve_monika
return 

label masbrk_cuddle_monika_start:
menu:
    "Honey can have a request?":
        pass 
m 3eta "A reqquest?, {w=2.0} what is it"
m 7fua "Go on you can ask me anything no need to be shy"
menu:
    "Can i ask for cuddles?":
        pass 
m 3wub "Cuddles?, {w=1.1} of course [player] come here" 
hide monika 
"You lean closer putting Monika on your lap and burry your face in her chest"
m "Hehehe, {w=1.1} someone is being lovey dovey today hm?"
menu:
    "Mmmm":
        pass 
menu: 
    "Helps me release all my stress and emotional anxiety":
        pass 
menu:
    "'Sigh'":
        pass 
m "You sound so problematic [player] you know?, {w=2.0} we can always cuddle or you can ask me anytime for hugs and more"
m "I know things are hard right now but i know you can pull through because my [player] is strong"
show monika zorder MAS_MONIKA_Z at t11 with dissolve_monika
return 

label masbrk_love_war_start:

m 3eubla "I love you too [player] {w=2.0} so much thank you for choosing me"
menu:
    "I will choose you anyday":
        pass 
m 3wubfo "You mean that? {w=1.1} {nw}"
menu:
    "I do this is how much i love you":
        pass 
m 3fkbftsa "You have no idea how much that ment to me"
m "I love you [player] i love you i love you"
menu:
    "I love you  more baby":
        pass 
m "I love you too"
menu:
    "No i love you more":
        pass 
m 2esb "No i love you more"
menu:
    "Nope i love you more than that":
        pass 
m 7tkbfa "No i'm the one who love you more" 
menu:
    "Nope i am":
        pass 
m 4efbfu "No i love you more!"
menu:
    "I loooooooooove you more!!":
        pass 
m 3efbfo "{b} NO I LOVE YOU MORE!! {/b}"
menu:
    "Nope":
        pass 
m 7cfbfb "Nooo i was the one who love you more my power of code say so"
$ style.say_dialogue = style.edited #Glitch Font Starts

m "Your mine thats why i love you more"
m 5ckbfd "My pretty boy, {w=2.0} i love you your mine"
$ style.say_dialogue = style.normal #Glitch Font Ends
menu:
    "I love you Monika":
        pass 
m "I love you too baby boy"
return 