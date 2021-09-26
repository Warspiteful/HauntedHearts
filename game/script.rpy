# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define pc = Character("[user]")
define c = Character("Chadmir")
define m = Character("Mothman")
define mx = Character("Moth???")
define ge = Character("Ghost")
define e = Character("Echo")
define fe = Character("???")
define f = Character("Franky")

### Backgrounds ###

image party:
   "./images/Backgrounds/101_party.png"
   zoom 0.5
image table:
   "./images/Backgrounds/102_table.png"
   zoom 0.5
image tableRed:
   "./images/Backgrounds/102_table_redder.png"
   zoom 0.5
image outdoors:
   "./images/Backgrounds/103_outdoor.png"
   zoom 0.5

## Echo
image Echo base:
   "./images/ghost neutral.png"
   zoom 0.35
image Echo happy:
   "./images/ghost happy.png"
   zoom 0.35
image Echo flirt:
   "./images/ghost flirty.png"
   zoom 0.35
image Echo blush:
   "./images/ghost blush.png"
   zoom 0.35
image Echo angry:
   "./images/ghost angry.png"
   zoom 0.35
image Echo sad:
   "./images/ghost sad.png"
   zoom 0.35
image Echo surprise:
   "./images/ghost surprised.png"
   zoom 0.35

## Franky
image Franky base:
   "./images/franky neutral.png"
   zoom 0.35
image Franky blush:
   "./images/franky embarrassed.png"
   zoom 0.35
image Franky manic:
   "./images/franky maniacal.png"
   zoom 0.35
image Franky nervous:
   "./images/franky nervous.png"
   zoom 0.35
image Franky bad:
   "./images/franky bad ending.png"
   zoom 0.35
image Franky smile:
   "./images/franky smile.png"
   zoom 0.35

## Chadmir
image Chad upset:
   "./images/Chad upset.png"
   zoom 0.4
image Chad base:
   "./images/Chad neutral.png"
   zoom 0.4
image Chad blush:
   "./images/Chad blush.png"
   zoom 0.4
image Chad angry:
   "./images/Chad angry.png"
   zoom 0.4

## Mothman
image Moth base:
   "./images/moth neutral.png"
   zoom 0.4
image Moth angry:
   "./images/moth angry.png"
   zoom 0.4
image Moth happy:
   "./images/moth happy.png"
   zoom 0.4
image Moth sad:
   "./images/moth sad.png"
   zoom 0.4
image Moth bad:
   "./images/moth bad ending.png"
   zoom 0.4


## Audio ##
define audio.party = "./audio/Party Ambience.wav"
define audio.echo = "./audio/Confessions_from_a_Poltergeist.mp3"
define audio.chad = "./audio/The Vlallad of Chadimir.wav"
define audio.franky = "./audio/Welcome to Franky_s Eldritch Abominations! What Can I Get You_.wav"
define audio.credits = "./audio/Spooky Disco.wav"
define audio.moth = "./audio/jazz noir.wav"


init python:
    config.debug_sound = True
    artist = ('Artist', 'Lucass0717'), ("Artist", "Elena @lennie_ok"),
    voiceActors = ("Voice Actor", "Ian Arlyn"),('Voice Actor','Megan Karow'), ('Voice Actor','Raydee99 - https://www.raydee99.com/'),('Voice Actor', 'Lindsay Jackman') #each parenthesis is a different line of credit#
    composers = ('Composer','Donovan'), ('Composer','Raydee99 - https://www.raydee99.com/')
    writers = ("Writer", "Jonathon Bickelhaupt @AmIAlwrite"), ("Writer", "Jade Edwards @jadegalexandria"), ('Writer', 'Birbstille'), ("Writer", "Scrapsnomancer"), ('Programmer & Writer', 'Warspiteful')
    credits_s = "{size=80}Credits\n\n"
    c1 = ''
    for c in artist:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    for c in voiceActors:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    for c in composers:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    for c in writers:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]


# The game starts here.

label start:
   $ user = renpy.input("What is your name?")
   $ user = user.strip()

   if not user:
         $ user = "Pat Smith"
   play music party
   scene party with fade

   "Well, you hadn’t planned on this."
   
   "You were supposed to be with your friend Theresa for most of the night, but she left you alone almost immediately. Her promises of not bailing early ring empty in your head. What else is new…"
   show Franky base with dissolve

   "But you can take care of that later. It shouldn’t be too hard to find the girl who dresses like a witch every day of the year. For now, all you have to do is focus on finding a way to pass the night."

   "You scan the party for someone, anyone to talk to. Most of the costumes are really impressive, but also a little intimidating. None of them really seem like the kind of company you want to keep on Halloween."

   "There are a few that seem nice enough, even through all the makeup and costuming."

   "Out of everyone that piques your interest, there’s a creepy looking guy in a robe and glasses, a beefy vampire in shorts and a sleeveless shirt, a really impressive Mothman costume with... a detective's outfit on top? And... a classic bedsheet ghost."

   "You want to talk to… "

   menu:
      "The Mothman":
         jump mothman
      "The Vampire":
         jump chadmir
      "The Cultist":
         jump franky
      "The Ghost":
         jump ghost



label ghost:
   play music echo
   "A person covered in a bedsheet walks past you. They turn to face you, and meet your eyes through two round seeing holes cut through their head. Somehow, you can tell they’re smiling as one corner of the sheet flies up to eagerly wave at you."
   menu:
      "Approach the ghost?":
         pass
   ge "Oh, hi! I don’t think I’ve ever seen you around before!"
   pc "Yeah, I’m here with a friend. My name’s [user]. You?"
   ge "Hm… I go by Echo. I think it matches my vibe, don’t you?"
   pc "Definitely!"
   e "Great! So nice to meet you~"
   e "So you came with a friend?"
   pc "Yeah. They’re, uh…"
   "You look through the crowd. Somewhere among the sea of devil horn headbands and horse masks is your friend, but you can’t figure out where they’ve gone."
   pc "I’m sure they’re somewhere."
   e "Aww, no big deal!"
   e "Maybe you can hang out with me, instead~"
   menu:
      "I’d be honored.":
         e "Oh!"
         e "You’re a lot more forward than you look."
         pc "Just trying to have a good time."
         e "Yes! You understand!"
         "There’s a pause. It’s a little awkward. You smile at Echo, and they simmer down a bit."
         pc "I’d love to chill with you until my friend comes back."
      "Would you help me find them?":
         e "Well, if I’m bothering you…"
         pc " No! You’re not bothering me, I just don’t know anyone else here."
         e "That’s alright! You know me now, don’t you?"
         pc "Good point."
   e "So, why’d you come up to me, out of all these crazy creatures? Was it the outfit?"
   "Echo does a little twirl. You get the feeling that if they were wearing a dress, the skirt would flare out."
   "Alas, it’s not a skirt. It’s a bedsheet. It kind of billows out at the bottom, but the top part is painfully stuck to Echo’s body. You wonder how they got it to stay like that."
   menu:
      "Yeah. You look great - super convincing.":
         e "What do you mean, convincing?"
         pc "Well, you look like a ghost. The costume’s really good."
         e "It… looks like a costume?"
         pc "Is it not supposed to?"
         e "It’s fine! As long as you think I look okay!"
      "That, and you called me over. I didn’t want to be rude.":
         e "Well, aren’t you a sweetheart."
         pc "Did it work?"
         e "Hehe… You aren’t rude at all."
   pc "You do look great, though. Seriously."
   e "Thank you!"
   e "So, who are you wearing?"
   pc "Huh?"
   e "Y’know, the fit?"
   e "I design and make all my own outfits; I just wanna know where you got yours!"
   e "Kinda going for a Boo-y Vuitton vibe, y’know?"
   "You can’t decide whether you should correct them or smile and nod. Instead of mulling over it while Echo looks at you, you opt to just move on."
   pc "I got this at Spirit Halloween."
   pc "It’s kind of a niche reference; I dunno if you’d know who I’m supposed to be."
   e "Oh! I’ve never been to Spirit Halloween; I’ll have to check it out!"
   pc "They’re everywhere."
   e "Maybe you could take me sometime… "
   e "I’ve been looking for an excuse to spruce up my wardrobe!"
   menu:
      "You seem to care a lot about clothes, Echo.":
         e "Huh?"
         e "Is that… weird?"
         pc "No, not at all!"
         pc "I was just wondering why."
         e "Hm… I dunno."
         e "I guess it’s kind of about the customization for me."
         e "You can make yourself look as pretty as you want!"
         pc "Echo… "
         pc "I bet you look pretty no matter what you wear."
         e "..."
         e "..."
         pc "(Ah, shoot, I messed up.)"
         "You turn to leave; your friend can probably fix this situation for you. As you start to walk away, a cloth-covered hand grabs your wrist."
         "It’s… cold. Freezing, actually; like a block of ice."
         "You turn back around."
         e "I haven’t heard that in a really long time."
         e "People don’t usually call me pretty… or handsome, or hot, or anything…"
         e "I don’t let people see what I look like."
         e "But… you called me pretty, even though you’ve never seen my face."
         pc "Oh."
         e "Thank you, [user.] Really."
         e "I wanna take off my costume and show you what I look like… Can I?"
         pc "Yeah, go for it."
         "Echo’s sheet begins to lift over their head. You grab their shoulders to stop them and look around, making sure that nobody saw."
         pc "Not here!"
         e "Oh, don’t worry! I’ve got something on under this~"
         pc "..."
         pc "Alright, I guess it’s okay."
         e "Echo slowly pulls off their bedsheet."
         # LITERALLY NOTHING LMAO
         pc "..."
         e "..."
         pc "..."
         e " ...Well, don\’t just stare at me…"
         "You’re not sure what you’re staring at."
         "...Honestly, it’s kind of cute that Echo got so worked up over nothing."
         pc "You look great."
         "You think Echo is probably smiling."
         e "Hehe… Thank you. So do you!"
         "You feel Echo’s cold hand in your pocket. Next thing you know, your phone is floating in the air. After a moment, it drops neatly back into your hand."
         e "I just put in my number. We should really check out that Spirit Halloween place sometime."
         pc "I’d love to."
         e "Let me introduce you to some of my friends!"
         "You feel their hand slip into yours. Your cheeks heat up; maybe your body is trying to compensate for the sudden chill."
         pc "Do you wanna put the co-"
         pc "The outfit back on?"
         e "Hm..."
         e "Nah!"
         e "I think you like me better this way~"
         "...Yeah. You think you do."
         # GOOD ENDING

      "Why waste money? I think you look alright.":
         e "Thank you!"
         pc "Haha, it’s true. Boo-y would be proud."
         pc "Seriously. Like, red carpet stuff."
         pc "Supermodel status."
         e "You’re… laying it on really thick…"
         e "Wait, did you say it’s a waste of money?"
         pc "I mean, I won’t judge. Whatever makes you happy, I guess."
         "Echo’s head tilts up and down. They seem to be appraising you."
         e "Hm… Oh! I think I see your friend! Behind you."
         "You turn around to see what they’re talking about, only to find the same sea of creatures that greeted you before. When you try to face Echo again, the space in front of you is empty."
         "Did you ever tell Echo what your friend looks like?"
         # BAD ENDING
      
      "If you like clothes so much, maybe you should just take mine off me…":
         e "..."
         pc "..."
         e "..."
         e "Darn. We were getting along so well."
         pc "What?"
         e "You’re kinda gross, [user]."
         pc "Did I say too much?"
         e "Yes. You did."
         e "But it’s okay!"
         e "You’re right; I do like clothes. And I like your clothes."
         e "I’ll just borrow them."
         "You blink, and Echo is gone. The party continues to buzz around you."
         "Your ears pop, and your head goes fuzzy. Black spots dance in front of your eyes."
         "Your hands lift in front of your face. You aren’t moving them."
         "\"Hehe...\""
         "Your body moves; shifting from foot to foot, rolling your shoulders, cracking your knuckles. Echo is getting used to you."
         "\"[user]....\""
         "\"Your body’s mediocre at best. I’d give it a solid 5/10… maybe a 6, if I’m feeling generous. Still better than your personality, though.\""
         "You take a step. Then two, then three. Briefly, you wonder how you’re doing that without willingly moving your legs."
         "Then it hits you."
         "Echo is in control."
         "\"Might as well take you for a spin!\""
         # WORST END

label franky:
   play music franky
   "As you scan the curious faces around the room, someone clumsily bumps into you from behind, nearly knocking you to the floor."
   "Recovering your balance, you turn to find a cloaked figure with curly black hair, spectacles askew from the collision, and glittering brown eyes nervously meeting your gaze."
   "They nearly drop the oddly bound book they're holding when they see you."
   menu:
      "Are you alright?":
         "Oh dear! Yes, I\'m... I\'m so sorry, are you okay? Oh my, I'm such a klutz... can I get you a band-aid? I think I know where they...?"
         menu:
            "It's okay! No harm, no foul.":
               pass
            "Don't worry about it, it' fine.":
               pass
      "Hey, watch it!":
         "Oh dear! Oh shoot I did it again, I'm such a klutz... can I get you a band-aid? I think I know where they...?"
         menu:
            "Klutz is one way to put it.":
               pass
            "Don't worry about it, it' fine.":
               pass
   fe "Sorry... guess I'm just feeling a little out of place."
   "You take a moment to look around. There's a bedsheet ghost, a moth version of James Dean, and a vampire himbo just hanging out..."
   pc "Actually... you seem like you fit right in."
   fe "Oh. Heh. Yeah, I guess you're right."
   menu:
      "So... what's your name?":
         pass
   f "Oh, sorry... Franky. My name's Franky. With a \"y.\""
   "There is an uncomfortable silence as Franky's eyes dart nervously hither and thither, before finally widening with realization."
   f "Oh! I didn't -- shoot! Sorry! What's your name? God, I'm rude."
   menu:
      "It's okay! My name's [user].":
         f "[user]. That's lovely."
         pc "Thanks! So's Franky. With a \"y.\""
         f "Aw... thanks!"
         "Franky blushes. Another awkward silence flutters by."
         menu:
            "So, who are you here with?":
               jump frankyNorm
      "Took you long enough. My name's [user].":
         f "Sorry... I have a lot on my mind."
         "Their gaze flutters about again, clearly distracted by something."
         menu:
            "So, who are you here with?":
               jump frankyNorm
            "Jeez... what is this, a space case convention?":
               f "Uhm... no? And you don't have to be so rude either."
   menu:
      "I'm sorry. You're right... guess I'm feeling a little out of place too.":
         jump frankyLead
      "Oh. Sorry. That was a joke.":
         f "Well... I wouldn't recommend a career in stand-up."
         "Another awkward silence. But this one is yours."
         pc "So, uh... what's with the book?"
         f "It's... my textbook. For school. Yeah. I'm a student. I study... uhm, practical theology, I guess."
         pc "Theology, like religion?"
         jump frankyBad
      "Hey, at least I didn't come dressed as Friar Tuck with no color coordination.":
         jump frankyWorst


label frankyWorst:
   "Suddenly, for reasons you cannot fathom, all of Franky's nervous energy evaporates in an instant. They casually flip the strange book open to its bookmarked page, curling an eyebrow as they finger a specific passage. You catch a glimpse of a scratchy text unlike anything you've ever seen. It's as red as blood."
   f "You know, I was only here because I just couldn't figure out what I had to do to get Lord Dagon out of my bathtub. But you just reminded me! There is one sure-fire way to cast out any of the Old Ones. And better yet, I think you can help me with it."
   f "The surest way to banish an Old One... is with a blood sacrifice."
   pc "You have a what in your bathtub?"
   "WORST ENDING: But it's too late. Franky holds their palm over the page, and a sickly green light illuminates their face, casting a deep shadow over their once-shimmering brown eyes. The last thing you hear, before a sickening crush of tentacular, saltwater flesh climbs out of the book to devour you, is Franky's voice chanting wildly..."
   f "Ph'nglui mglw'nafh Cthulhu R'lyeh wgah'nagl fhtagn...    Ph'nglui mglw'nafh Dagon R'lyeh wgah'nagl htogrn...   Dagon! Dagon! Dagon!"
   # ENDING

label frankyNorm:
   f "Oh, no one really, I'm just the neighbor."
   pc "Ah, I get it: if there's gonna be noise, might as well join the party, eh?"
   f "Oh, no! No, not at all! I hope they don't think I'm... no! No, I just had some, eh, plumbing issues I need to have looked at."
   pc "Plumbing issues?"
   f "Yeah... it's really embarrassing. I'd rather not talk about it."
   jump frankyLead

label frankyLead:
   "You notice them fumbling the oddly bound book in their hands."
   pc "That's some chonky beach reader you've got there."
   f "This? Oh, no not really. It's, ah... a textbook. Yeah. For... school."
   pc "Oh cool! What do you study?"
   f "It's, ah... kind of hard to describe. I guess... yeah, I guess you could call it \"practical theology?\""
   menu: 
      "Sounds interesting! What makes it practical?":
         jump frankyGood
      "Theology? Like...religion?":
         jump frankyBad

label frankyGood:
   f "Well, it's, uh... it's supposed to help with tangible issues, if you treat it respectfully."
   pc "What kind of tangible issues?"
   f "Well... plumbing, for one."
   pc "You use theology on your plumbing?"
   f "Oh, Old Ones... you think I'm weird now, don't you?"
   pc "Are you kidding me? I'm riveted!"
   f "Really? You're... really? Oh my, I'm blushing. Look at my cheeks! They're blushing!"
   "Franky lifts a hand to one of their still-reddening cheeks. It's trembling. You've made an impression."
   f "Oh, I'm sorry, I made you nervous. If it helps... I think you blush real cute. Or... you're cute when you blush. Yeah."
   "Franky clutches the book to their chest, an audible \"eep!\" escaping them as they jolt upright, eyes wide again. After a moment, they seem to notice your own nervousness. Suddenly, their shoulders slacken, relaxed."
   f "I think you're cute too."
   pc "So... want to show me your place?"
   f "Yes, please! Although... I might need some help getting Lord Dagon out of my bathtub first..."
   # ENDING
   "GOOD ENDING: You have no idea who \"Lord Dagon\" is. Or why he would be in Franky's bathtub. But as Franky tucks the book under one arm and leads you away with the other, you feel a fresh warmth in your cheeks and a weakness in your legs, and as they give you that knowing look with their beaming brown eyes, you come to the realization that you don't much care. Whoever this Dagon chap is, he better finish washing up right quick."

label frankyBad:
   f "No! I mean... yes, kind of. Why? Is that... bad?"
   pc "No! I mean... to each their own, right?"
   f "I guess. I'm not a fanatic, though. Oh dear, I hope you don't think I'm a fanatic!"
   pc "Not at all! Sorry if I gave that --"
   f "I mean, just 'cause they call us \"cultists\" doesn't mean we're psycho or anything..."
   pc "I never said you were a --"
   f "Although what kind of normal person would accidentally summon Lord Dagon the Fish-God in a bathtub? Stupid, stupid!"
   pc "Lord who?"
   f "Oh, Old Ones, you do think I'm a psycho, don't you? And why not? I sure am behaving like one!"
   pc "I mean, you seem a little stressed, but I don't think --"
   f "I shouldn't even be here! Gods, this is such an imposition!"
   pc "Hey, c'mon --"
   f "I'm sorry, I gotta go. I gotta... I dunno... do some dishes or something... help with the party somehow. Sorry! It was nice meeting you! Please, go have fun! Sorry! Thanks! Bye!"
   # ENDING
   "BAD ENDING: The odd buzz in your head -- surely a side effect of Franky's wheeling centrifuge of nerves -- quiets as they disappear into the next room, plucking up used plates and empty glasses as they go. While you hope they also find some way to enjoy themselves at this strange party, you can't help but feel flustered to be suddenly left right back where you began."

label mothman:
   play music moth
   "You scan the party for someone, anyone to talk to."
   "Most of the costumes are really impressive, but also a little intimidating."
   "None of them really seem like the kind of company you want to keep on Halloween."
   "Well, except for the guy in the Mothman costume."
   "The really good Mothman costume with the full detective costume on top of it to be exact."
   "The eyes are a little creepy but he’s also furry, so it will make approaching him that much easier."
   #SHOW
   "He’s standing in the corner all by himself, watching over the party. Maybe he’s a wallflower who needs someone to get him to open up?"
   menu:
      "Approach the Mothman.":
         pass
   "You move your way through the thick crowd and approach the corner of the room. As you do Mothman notices you and seems a little excited."
   pc "Hey, just wanted to say I like your Mothman outfit."
   m "T̶̾͝h̵̽̈a̵͗͌n̵̊̿k̶͋̿ ̴̇̕y̵͌͘o̶͊͝û̴̈́.̸̏͝"
   pc "Oh wow! Do you have a voice modulator or something in there? Is this for like, cosplay?"
   m "N̵͛̓o̸̓̇.̴́̓"
   pc "Oh come on, you’re kidding. You’ve got the Mothman suit on and the detective get-up. I won’t judge you if you do cosplay."
   m "I̷͆͆t̴̑̂'̶̎̃s̶͆͛ ̴͐̍p̷͂̄e̵͋͘r̸̀͘f̶̔̎o̵̅̃r̷͋̀m̸̿̕ǎ̸̈́n̶͂͝c̷̉̀e̸͂̓ ̵͐͐ä̸͆r̴̿̃t̴̒̐.̵̂͠"
   pc "Hmmm ok. But isn’t it a little warm for performance art? I mean, that dude dressed as a vampire is in board shorts."
   m "I am actually quite comfortable."
   pc "OK, if you say so. I just… don’t want you to overheat or something."
   "The Mothman holds up a cup full of juice before extending a…proboscis? A straw? They slurp up some juice to your astonishment."
   pc "Wow, your costume is really amazing. You have a built in straw!"
   m "Yes exactly, a human straw."
   pc "That’s a weird way to put it but yeah. It’s cool."
   m "I am glad you find it mesmerizing."
   pc "Your costume design is just really top notch. If I didn’t know any better I would say you’re the real deal!"
   "The Mothman stiffens at the mention of him being a real mothman. He eventually relaxes and nods along when they realise you were joking."
   pc "So, what do you do during the day?"
   m "Usually sleep."
   pc "Oh, you work the night shift?"
   m "Uh, yes, the night shift."
   pc "What’s your job?"
   m "I really like lights. They’re one of my favorite things."
   pc "So you’re like an electrician who specializes in light fixtures?"
   m "Yes, you took the human words right out of my definitely human mouth."
   pc "That’s really interesting. I would’ve imagined that electricians would work during the day."
   m "Yes, that would make more sense wouldn’t it."
   pc "Anyways… If you’re an electrician and don’t do cosplay, what’s with the trench coat?"
   m "Oh this."
   "He pulls at the coat with his… hand? Claw? You also hear the beat of wings but they sound like they’re coming from underneath a blanket."
   m "I ate the previous owner."
   pc "You mean paid?"
   m "Uh, yes. Paid. I paid the previous owner. Not ate."
   pc "So you’re into thrifting?"
   m "Y̴̍̍e̵̎̐s̴̝̐.̸̥̍ ̴̈́̂I̴̍̉ ̵̛̝l̸͉̐o̸̫͝v̴́͊e̷̋̊ ̷͈͂o̶̐͠l̵͂̈́d̸͈͋ ̴͖͠c̵̉͜l̴͐̍ò̶̙t̴̲́h̶͑̈́e̸̅͠s̶̕̕,̷̭̆ ̷͑͐t̵̅̕h̵̋̀e̶͋̈y̷͑̄'̵́̚r̵̐̚e̵͒̐ ̸̺̀v̴̇̆e̴͛͠r̵̅̃y̷̑͛ ̶̀̿t̴̄̐a̶͇̓s̷̈͌t̴͒͠ỳ̷̇.̵̾͊"
   pc "...tasty?"
   "You see Mothman look at his hand. There appears to be several notes scribbled across it."
   m "Ĭ̶̳ ̵̈́̍m̶̄͐é̵̻a̵̓͗n̸͛t… fashionable."
   pc "Haha, that makes way more sense. Is that like, a saying where you’re from."
   "Mothman pauses to consult his hand."
   m "Yes, it is. Sometimes I forget that I’m not back home. Especially when I’m around such lovely people."
   menu:
      "Be kind.":
         pc "Oh Mr. Mothman, you're too kind."
         m "Nonsense. Your presence is warming. Like a bright light on a cold night."
         pc "You said that calling clothes tasty was a phrase from home. Where are you from?"
         m "You would know it as West Virginia, but my family has always called it the Nesting Grounds."
         pc " Right, because you're always heading home to those... country roads?"
         m " I... do not understand your silly jokes."
         pc "Of course not. My life seems so much less interesting and cool than yours. Your unique way of speaking, your work as a nighttime electrician, and your costume, it’s all so much more engaging!"
         m "We may not have known each other for very long, but I can tell that you’re a very interesting human person. And you’re certainly more kind than most."
         pc "What do you mean Mothman?"
         m "Most people are rude to me and shun me. You are different."
         pc "I still don’t understand. Why would they do that to you?"
         m "Here, let me show you."
         "Mothman grabs you by your hand and pulls you away from the party and the noise. He leads you through a crowd of people to the back yard."
         "It’s empty except for you two, and lit only by the fluorescent porch light hanging off the house."
         pc "What is it?"
         "Mothman seems a little distracted by the porch light but they focus on you. He takes your hand and puts on his furry face."
         m "Do you understand me now?"
         pc "No… but that is a really good costume."
         m "Mothman seems flustered for a moment before returning to his calm demeanor."
         "He takes a step back from you and pulls off his hat and trench coat, revealing his moth-like body."
         m "Now do you understand who I am?"
         pc "Yes… you’re the real Mothman."
         mx "I do not abide by your gender terminology, but yes, that is what they call me."
         pc "Oh, I’m sorry. Is there something else you’d prefer to be called?"
         m "No need to apologize, Mothman is fine for now. I will find a name that suits me soon. But thank you for asking …"
         pc "Oh, my name is [user]."
         m "Well, it is nice to fully meet you [user]."
         "There’s an awkward pause. You’re both unsure of what to do in a situation like this considering cryptids don’t ever reveal themselves like this."
         pc "Do you… want to go get some food? You can get some fruit juice and fabric and I can get human food."
         m "I would… I would really like that."
         "Mothman pulls on his trench coat and cap before offering a hand to you. You accept it and he pulls you close before taking off into the night sky. You never thought a Halloween party would end with a flight to get fruit, but here you are."
         # GOOD END
      "Be aloof.":
         pc "Oh, um, thanks I guess."
         m "I apologize if that was too forward, I am not used to people treating me so well."
         pc "No, no, it’s not your fault. You have been very polite, I’m just… not sure about how interested I am."
         m "I see. My fo- I mean my costume can certainly be unnerving to most people, so I understand."
         pc "Maybe if we could spend some time together without the costumes… "
         m "I-"
         m "I don’t think I can do that I’m afraid."
         pc "It doesn’t have to be tonight, we could go get dinner or something. Or breakfast if that would work better with your schedule!"
         m "No, I don’t think that will work for me."
         pc "Please, I like you, I'm just… unsure."
         m "That is alright. I understand, it is the normal reaction. I am sorry we must part ways."
         pc "But we don’t hav-"
         "Before you can finish your sentence Mothman walks away from you. He quickly melts into the crowd at the center of the room, leaving you alone in the corner. Somehow talking to him has left you in a worse position than when you started."
         # BAD END
      "Be rude.":
         pc "What did you call me?"
         m "Lo… I called you lovely."
         "He checks his palm again, this time with a look of worry."
         m "Did I say something offensive?"
         pc "Not really… I just don’t like you that much and that caught me off guard."
         "Mothman’s face contorts into… sadness? Anger? Or, at least a moth’s approximation of some emotion."
         m "What a shame… I thought you would be different."
         "Then, suddenly, they launch at you with a speed you never would’ve suspected. As he flies towards you, Mothman rips off the trench coat and hat revealing his bug-like body and large wings."
         "He grabs hold of you before dashing to the window and launching through it. Glass showers the lawn as he takes flight with you in tow."
         m "I thought tonight would end differently after I started talking to you. But you are just like the rest."
         pc "Wh-"
         pc "What is going on? What did I do?"
         m "You shunned me like the rest of humanity. But at the very least I won’t go hungry tonight!"
         "With that Mothman flew you to his lair. He’s not exactly the cleanest eater, so your death was pretty gruesome. But we can skip all the icky, squishy bits."
         # WORST END

# Chadmir
label chadmir:
   play music chad
   "The guy dressed as a vampire seems pretty chill. Maybe he ran out of time to finish his costume – he’s partially dressed as a vampire, and partially just as… a bro? His cape looks pretty authentic though, and he has some killer fake fangs."
   "He’s standing all by himself, just kind of swaying to the music. Everyone else is giving him a pretty wide berth - there’s at least a 5 foot space around him on any side. He seems harmless, though, and super relaxed."
   "You decide to go talk to him."
   c "S’up, dude?"
   pc "Hi."
   c "Oh, is it okay if I call you dude?"
   menu:
      "That’s fine!":
         $ bro = true
         c "Okay, dude. Sick."
      "Actually, I’d rather you didn’t.":
         $ bro = false
         c "Oh, sorry!"
   c " I’m Chadamir, but you can just call me Chad. It’s all chilllll."
   pc "Nice to meet you. I’m [user]."
   c "Enjoying the party?"
   menu:
      "Yeah, this is great. Everyone’s outfits are amazing.":
         pass
      "I just got here. Some of the costumes are so scary.":
         pass
   "It’s true. The Mothman in the corner looks like their costume is made of real… fur? And Chad has some red contacts for his eyes that look pretty intense."
   c "Yeahhh, everyone here is the real deal, for sureee. We take All Hollow’s Eve prettyyy seriously."
   menu:
      "Yeah, I mean, you look really great.":
         c "Oh heyyy, thanks."
      "Well your costume seems a little… confused?":
         c "Ah, I just couldn’t pull everything together in time. It suuuucks."  
   c "I just borrowed some of this stuff from my new friend Drake. Hey, do you know Drake? Drake Ula?"
   pc "No, sorry."
   c "Ah, that’s a bummer. He’s a pretty chillll guy."
   pc "You seem like you’re having a good time."
   c "Oh, yeahhh. I’m just really excited to be here. I can’t believe I got invited."
   menu:
      "Well, who wouldn't want a guy like you at their party?":
         c "Heh. That’s nice.. I mean… some people might not…"
      "Yeah, you do seem kind of out of place.":
         c "Ohhhh. Well, y’know, I only know a couple people here."
   c "It’s just hard for a guy like me to go anywhere without someone asking me, y’know?"
   pc "Oh. Do you have anxiety?"
   c " Nahhhh, I’m chill bro. I just don’t like going anywhere without being invited."
   menu:
      "Oh, well that’s very considerate of you.":
         c "Yeah. Well, y’know, I kind of have to be, but uh, thanks."
      "Huh. You’re not very confident, are you? ":
         c "Heyyyy, man. You don’t need to judge."
   c "Anyways. What brings you to this fiiine abode?"
   menu:
      "I’m definitely looking for a little adventure. Maybe I’ll meet someone tonight…":
         pass
      "I just wanted to check out the party.":
         pass
      "I mostly came to look at the costumes. Everyone just looks so silly.":
         jump cWorst
   c "Heyyyy, that’s the spirit. You never know what might happen. "
   c "I’m kinda hoping that maybe I’ll meet someone too… "
   menu:
      "Well, you did meet me.":
         c "I guess I did. You’re pretty awesome."
      "The night is young. Maybe you still will.":
         c "Yeah, maybe. Doesn’t seem like there’s many contenders though."
   c "You wanna go check out the food?"
   pc "Sure."
   "You walk over to the food table together. It’s covered in all kinds of delicious-looking snacks."
   c "Oh, heyyy. Garlic bread."
   pc "You wanna try some?"
   c "Nahhh, I don’t do garlic. Gotta get those gains, y’know? And there’s not enough protein in there for me."
   c "You could have some though."
   pc "Are you sure?"
   c "Well, I mean… if you want to..."
   menu:
      "Okay, sounds tasty.":
         jump cBad
      "Nah, garlic makes your breath smell bad. Besides, if you’re not having any, I don’t want you to feel left out.":
         pass
   c "Oh, wooow. I appreciate that. You’re reallyyyy nice, y’know?"
   pc "Thanks. You are too."
   c "Aw."
   c "Welllll, not everyone agrees with you though."
   pc "Oh no! Why?"
   c "I, uh, recently went through a big life change. It’s kinda affected everything… my diet, my sleep schedule, even, like the places I can hang out…"
   c "Some of my friends just haven’t been very supportive while I’m, y’know, figuring stuff out."
   c "That’s why I was so excited that I got invited to come here."
   pc "Well, sounds like they’re not such good friends then."
   c "I guess not."
   pc "Well, I’m glad we got to spend this time together."
   c "Me too."
   c "Hey, [user]. Can I tell you a secret?" 
   pc "..."
   pc "What kind of secret?"
   c "It’s a biiiig deal. I haven’t really told anybody other than Drake. "
   pc "Wow. Well, you can tell me if you want."
   c "Okay. Wooow, this is hard."
   "Chad takes a deep breath, preparing himself to tell you the secret. He leans in to whisper in your ear."
   c "I’m not just dressed up as a vampire. "
   c "..."
   c " I actually… am a vampire."
   pc "..."
   pc "Ha, great Halloween prank. "
   c "..."
   pc "C’mon Chad, I’m not that gullible."
   "Chad shakes his head at you. He’s still standing pretty close… close enough that you can see how truly real those fangs look."
   c "It’s not a prank, bro."
   pc "You’re… what?"
   pc "No way. I can’t believe it."
   "But you see the intense look in his bright red eyes, and you think back to all the things he’s told you over the course of the party… could it be true?"
   c "It’ll help if you say it. Say it out loud."
   pc "..."
   pc "You’re a vampire!"
   "You’re trying really hard not to freak out in the middle of this room full of people. Chad… is a vampire. A blood sucking, undead vampire who sleeps in a coffin. Maybe."
   "It’s a lot to process. But Chad is still just standing there with you, not judging as you try not to panic."
   c "I know it’s a lot to take in."
   pc "Yeah…"
   c "But I promise I’d never hurt you."
   c "Actually…"
   pc "What?"
   c "I was going to ask if you wanted to get out of here."
   pc "..."
   pc "Get out of here? Like, together?"
   c "Yeahhh… I mean, if you’re down?"
   c "You’re the nicest person I’ve met all night, and you haven’t freaked out about my, uh, new life changes."
   if bro == true:
      c "I want to get to know you. And I promise not to suck your blood, dude."
   if bro == false:
      c "I want to get to know you. And I promise not to suck your blood, [user]."
   "You gulp. It sounds a little scary… but looking up at the dumb face, with those muscles and how kind he’s been... you can’t deny that Chad would be a good guy to have around."
   pc "Alright. Let’s get out of here."
   "He reaches out to take your hand as you walk out of the party together, and you have a feeling that this Halloween is going to be the best one yet. After all, even if he is a vampire, he’s the nicest himbo you’ve ever met."
   "YOU AND CHAD HAD A LOVELY GARLIC-FREE  DINNER TOGETHER"
   "THE END"
   # ENDING





label cBad:
   c "Alright."
   c "Heyyy, I think I’m gonna go see if I can find my guy Drake."
   pc "Oh, you’re leaving? "
   c "Yeahhh. Sorry, ___playername___, maybe I’ll see you around."
   "And with that, Chad turns and disappears into the crowd. You’re left with the lingering sense that there was something… different about him, but now you’ll never be able to figure it out."
   # ENDING
   
label cWorst:
   if dude == true:
      c "Heyyyy, dude. I think everyone looks great."
   else:
      c "Heyyyy, [user]. I think everyone looks great."
   c "Do you not like dressing up for Halloween?"
   menu:
      "I guess I’m just not feeling it right now.":
         jump cBad
      "I do. I just feel like all these ones are stupid and tacky.":
         c "Okayyyy, now you’re just being rude."
   pc "I mean, there’s someone over there dressed as a ghost with literally just a sheet over their head."
   c "That ghost happens to be my friend."
   pc "Some ghost."
   c "Okayyyy, I’ve had enough now."
   "Suddenly, Chad rises to his full height, bearing his suspiciously-real looking fangs. His red contacts are glowing somehow? "
   c "All these creatures here, we’re prettyyyy much all real. I’m not just some guy dressed as a vampire. I actually am a vampire."
   "Your jaw drops. The costumes all look so fake… and yet the look in Chad’s red eyes, the intensity as he stalks towards you… is it possible he’s actually telling the truth?"
   pc "What?"
   pc "No way"
   c "Ohhhh, you better believe it."
   c "And if you think it’s okay to be mean to my friends…"
   c "Well, you’re about to find out how hard I can bite back."
   "Chad comes right up to you, so close that you start to go cross-eyed looking into his vivid eyes. You can see how sharp the fangs he has are, smell the waft of something metallic coming off of him."
   "Then he lunges forward and there’s a sharp pinch at your neck, and slowly... the world fades to black."
   # ENDING
   "YOU HAVE DIED FROM PISSING OFF CHAD"



   

label credits:
   play music credits 
   image cred = Text(credits_s, text_align=0.5)
   image theend = Text("{size=80}The End", text_align=0.5)
   image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5)
   $ credits_speed = 25
   scene black with fade
   show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
   show theend:
      yanchor 0.5 ypos 0.5
      xanchor 0.5 xpos 0.5
   with dissolve
   with Pause(1.5)
   hide theend


   image mushGood = Text("{size=80}Love it When a Plan Fungs Together", text_align=0.5)

   show mushGood:
      yanchor 0.5 ypos 0.5
      xanchor 0.5 xpos 0.5
   with dissolve
   with Pause(1.5)
   hide roseBad
   with dissolve
   with Pause(credits_speed - 5)
   with dissolve
   with Pause(1)
   show thanks:
      yanchor 0.5 ypos 0.5
      xanchor 0.5 xpos 0.5
   with dissolve
   with Pause(3)
   hide thanks
   with dissolve
return
