# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define pc = Character("[user]")
define c = Character("Chadimir")
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
   "./images/Backgrounds/103_outdoor_minuswitch.png"
   zoom 0.5
image glass:
   "./images/Backgrounds/103_outdoor_glass.png"
   zoom 0.5
image sky:
   "./images/Backgrounds/104_nightsky.png"
   zoom 0.5

image corner:
   "./images/Backgrounds/105_corner.png"
   zoom 0.5

image credit_bg:
   "./images/Backgrounds/004_background.png"
   

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
image Franky bad:
   "./images/franky mad.PNG"
   zoom 0.35
image Franky love:
   "./images/franky blushing.PNG"
   zoom 0.35
## Chadmir
image Chad sad:
   "./images/Chad upset.png"
   zoom 0.4
image Chad base:
   "./images/Chad neutral.png"
   zoom 0.4
image Chad blush:
   "./images/Chad blush.png"
   zoom 0.4
image Chad mad:
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
define audio.echo = "./audio/Confessions from a Poltergeist.wav"
define audio.chad = "./audio/The Vlallad of Chadimir.wav"
define audio.franky = "./audio/Welcome to Franky_s Eldritch Abominations! What Can I Get You_.wav"
define audio.credits = "./audio/Spooky Disco.wav"
define audio.moth = "./audio/jazz noir.wav"
define audio.title = "./audio/Not-As-Spooky-Disco (title).wav"
define audio.echo_bad = "./audio/Possessed by a Poltergeist.wav"



init python:
   config.debug_sound = True
   artist = ('Character Designer, Artist', '625ApplePie / Cy Greene '), ("Character Design, Character Artist", "APBuffy / Alexa Parker Brown"),("Background Artist, Title UI","Gem")
   producer = ("Producer", "Raydee99"), ("Programmer", "Warspiteful")
   composers = ('Composer','DannyGoldstar'), ('Composer','Raydee99')
   writers = ("Writer", "Emma Hunt"), ("Writer", "Steve Lausier"), ('Writer', 'Megan Karow'), ("Writer", "Jonathon \"Jon Bic\" Bickelhaupt "), ('Additional Writing', 'Raydee99')
   credits_s = "{size=80}Credits\n\n"
   c1 = ''
   for a in producer:
      if not c1==a[0]:
         credits_s += "\n{size=40}" + a[0] + "\n"
      credits_s += "{size=60}" + a[1] + "\n"
      c1=a[0]   
   for a in artist:
      if not c1==a[0]:
         credits_s += "\n{size=40}" + a[0] + "\n"
      credits_s += "{size=60}" + a[1] + "\n"
      c1=a[0]
   for a in composers:
      if not c1==a[0]:
         credits_s += "\n{size=40}" + a[0] + "\n"
      credits_s += "{size=60}" + a[1] + "\n"
      c1=a[0]
   for a in writers:
      if not c1==a[0]:
         credits_s += "\n{size=40}" + a[0] + "\n"
      credits_s += "{size=60}" + a[1] + "\n"
      c1=a[0]

# The game starts here.
label before_main_menu:
   play music title noloop
   queue music title loop
   return
   
label start:
   $ user = renpy.input("What is your name?")
   $ user = user.strip()

   if not user:
         $ user = "Pat Smith"
   play music party
   scene party with fade

   "Well, you hadn’t planned on this."
   
   "You were supposed to be with your friend Theresa for most of the night, but she left you alone almost immediately. Her promises of not bailing early ring empty in your head. What else is new…"

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
   "A person covered in a bedsheet walks past you. They turn to face you, and meet your eyes through two round seeing holes cut through their head."
   "Somehow, you can tell they’re smiling as one corner of the sheet flies up to eagerly wave at you."
   menu:
      "Approach the ghost?":
         pass
   show Echo happy with dissolve
   ge "Oh, hi! I don’t think I’ve ever seen you around before!"
   pc "Yeah, I’m here with a friend. My name’s [user]. You?"
   show Echo base
   ge "Hm… I go by Echo. I think it matches my vibe, don’t you?"
   pc "Definitely!"
   show Echo happy
   e "Great! So nice to meet you~"
   show Echo base
   e "So you came with a friend?"
   pc "Yeah. They’re, uh…"
   "You look through the crowd. Somewhere among the sea of devil horn headbands and horse masks is your friend, but you can’t figure out where they’ve gone."
   pc "I’m sure they’re somewhere."
   e "Aww, no big deal!"
   show Echo flirt
   e "Maybe you can hang out with me, instead~"
   menu:
      "I’d be honored.":
         show Echo surprise
         e "Oh!"
         e "You’re a lot more forward than you look."
         pc "Just trying to have a good time."
         show Echo happy
         e "Yes! You understand!"
         "There’s a pause. It’s a little awkward. You smile at Echo, and they simmer down a bit."
         pc "I’d love to chill with you until my friend comes back."
      "Would you help me find them?":
         show Echo sad
         e "Well, if I’m bothering you…"
         pc " No! You’re not bothering me, I just don’t know anyone else here."
         show Echo base
         e "That’s alright! You know me now, don’t you?"
         pc "Good point."
   show Echo base
   e "So, why’d you come up to me, out of all these crazy creatures? Was it the outfit?"
   "Echo does a little twirl. You get the feeling that if they were wearing a dress, the skirt would flare out."
   "Alas, it’s not a skirt. It’s a bedsheet. It kind of billows out at the bottom, but the top part is painfully stuck to Echo’s body. You wonder how they got it to stay like that."
   menu:
      "Yeah. You look great - super convincing.":
         show Echo surprise
         e "What do you mean, convincing?"
         pc "Well, you look like a ghost. The costume’s really good."
         show Echo base
         e "It… looks like a costume?"
         pc "Is it not supposed to?"
         show Echo sad
         e "It’s fine! As long as you think I look okay!"
      "That, and you called me over. I didn’t want to be rude.":
         show Echo flirt
         e "Well, aren’t you a sweetheart."
         pc "Did it work?"
         e "Hehe… You aren’t rude at all."
   show Echo base
   pc "You do look great, though. Seriously."
   show Echo happy
   e "Thank you!"
   show Echo base
   e "So, who are you wearing?"
   pc "Huh?"
   e "Y’know, the fit?"
   show Echo happy
   e "I design and make all my own outfits; I just wanna know where you got yours!"
   e "Kinda going for a Boo-y Vuitton vibe, y’know?"
   "You can’t decide whether you should correct them or smile and nod. Instead of mulling over it while Echo looks at you, you opt to just move on."
   pc "I got this at Spirit Halloween."
   pc "It’s kind of a niche reference; I dunno if you’d know who I’m supposed to be."
   show Echo base
   e "Oh! I’ve never been to Spirit Halloween; I’ll have to check it out!"
   pc "They’re everywhere."
   show Echo flirt
   e "Maybe you could take me sometime… "
   show Echo happy
   e "I’ve been looking for an excuse to spruce up my wardrobe!"
   menu:
      "You seem to care a lot about clothes, Echo.":
         show Echo surprise
         e "Huh?"
         e "Is that… weird?"
         pc "No, not at all!"
         pc "I was just wondering why."
         show Echo base
         e "Hm… I dunno."
         e "I guess it’s kind of about the customization for me."
         show Echo happy
         e "You can make yourself look as pretty as you want!"
         pc "Echo… "
         pc "I bet you look pretty no matter what you wear."
         show Echo surprise
         e "..."
         show Echo sad
         e "..."
         pc "(Ah, shoot, I messed up.)"
         "You turn to leave; your friend can probably fix this situation for you. As you start to walk away, a cloth-covered hand grabs your wrist."
         "It’s… cold. Freezing, actually; like a block of ice."
         "You turn back around."
         show Echo blush
         e "I haven’t heard that in a really long time."
         e "People don’t usually call me pretty… or handsome, or hot, or anything…"
         e "I don’t let people see what I look like."
         e "But… you called me pretty, even though you’ve never seen my face."
         pc "Oh."
         show Echo happy
         e "Thank you, [user] Really."
         e "I wanna take off my costume and show you what I look like… Can I?"
         pc "Yeah, go for it."
         "Echo’s sheet begins to lift over their head. You grab their shoulders to stop them and look around, making sure that nobody saw."
         pc "Not here!"
         e "Oh, don’t worry! I’ve got something on under this~"
         pc "..."
         pc "Alright, I guess it’s okay."
         e "Echo slowly pulls off their bedsheet."
         # LITERALLY NOTHING LMAO
         hide Echo with dissolve
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
         scene black with fade
         "...Yeah. You think you do."
         # GOOD ENDIN
         jump credits

      "Why waste money? I think you look alright.":
         e "Thank you!"
         show Echo flirt
         pc "Haha, it’s true. Boo-y would be proud."
         pc "Seriously. Like, red carpet stuff."
         pc "Supermodel status."
         show Echo surprise
         e "You’re… laying it on really thick…"
         show Echo base
         e "Wait, did you say it’s a waste of money?"
         pc "I mean, I won’t judge. Whatever makes you happy, I guess."
         "Echo’s head tilts up and down. They seem to be appraising you."
         e "Hm… Oh! I think I see your friend! Behind you."
         hide Echo with dissolve
         "You turn around to see what they’re talking about, only to find the same sea of creatures that greeted you before. When you try to face Echo again, the space in front of you is empty."
         scene black with fade
         "Did you ever tell Echo what your friend looks like?"
         # BAD ENDING
         jump credits
      
      "If you like clothes so much, maybe you should just take mine off me…":
         show Echo angry
         e "..."
         pc "..."
         e "..."
         show Echo happy
         e "Darn. We were getting along so well."
         pc "What?"
         e "You’re kinda gross, [user]."
         pc "Did I say too much?"
         show Echo angry
         e "Yes. You did."
         show Echo happy
         e "But it’s okay!"
         e "You’re right; I do like clothes. And I like your clothes."
         show Echo base
         e "I’ll just borrow them."
         hide Echo with dissolve
         play music echo_bad
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
         scene black with fade
         "\"Might as well take you for a spin!\""
         # WORST END
         jump credits

label franky:
   play music franky
   "As you scan the curious faces around the room, someone clumsily bumps into you from behind, nearly knocking you to the floor."
   "Recovering your balance, you turn to find a cloaked figure with curly black hair, spectacles askew from the collision, and glittering brown eyes nervously meeting your gaze."
   "They nearly drop the oddly bound book they're holding when they see you."
   menu:
      "Are you alright?":
         show Franky blush with dissolve
         "Oh dear! Yes, I\'m... I\'m so sorry, are you okay? Oh my, I'm such a klutz... can I get you a band-aid? I think I know where they...?"
         menu:
            "It's okay! No harm, no foul.":
               pass
            "Don't worry about it, it's fine.":
               pass
      "Hey, watch it!":
         show Franky blush with dissolve
         "Oh dear! Oh shoot I did it again, I'm such a klutz... can I get you a band-aid? I think I know where they...?"
         menu:
            "Klutz is one way to put it.":
               pass
            "Don't worry about it, it's fine.":
               pass
   show Franky nervous
   fe "Sorry... guess I'm just feeling a little out of place."
   "You take a moment to look around. There's a bedsheet ghost, a moth version of James Dean, and a vampire himbo just hanging out..."
   pc "Actually... you seem like you fit right in."
   show Franky smile
   fe "Oh. Heh. Yeah, I guess you're right."
   menu:
      "So... what's your name?":
         pass
   f "Oh, sorry... Franky. My name's Franky. With a \"y.\""
   "There is an uncomfortable silence as Franky's eyes dart nervously hither and thither, before finally widening with realization."
   show Franky blush
   f "Oh! I didn't -- shoot! Sorry! What's your name? God, I'm rude."
   menu:
      "It's okay! My name's [user].":
         show Franky smile
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
         show Franky mad
         f "Well... I wouldn't recommend a career in stand-up."
         "Another awkward silence. But this one is yours."
         pc "So, uh... what's with the book?"
         show Franky nervous
         f "It's... my textbook. For school. Yeah. I'm a student. I study... uhm, practical theology, I guess."
         pc "Theology, like religion?"
         jump frankyBad
      "Hey, at least I didn't come dressed as Friar Tuck with no color coordination.":
         jump frankyWorst


label frankyWorst:
   "Suddenly, for reasons you cannot fathom, all of Franky's nervous energy evaporates in an instant."
   show Franky manic
   "They casually flip the strange book open to its bookmarked page, curling an eyebrow as they finger a specific passage."
   "You catch a glimpse of a scratchy text unlike anything you've ever seen. It's as red as blood."
   f "You know, I was only here because I just couldn't figure out what I had to do to get Lord Dagon out of my bathtub."
   f "But you just reminded me! There is one sure-fire way to cast out any of the Old Ones. And better yet, I think you can help me with it."
   f "The surest way to banish an Old One... is with a blood sacrifice."
   show Franky bad
   pc "You have a what in your bathtub?"
   "But it's too late. Franky holds their palm over the page, and a sickly green light illuminates their face, casting a deep shadow over their once-shimmering brown eyes."
   "The last thing you hear, before a sickening crush of tentacular, saltwater flesh climbs out of the book to devour you, is Franky's voice chanting wildly..."
   scene black with fade
   f "Ph'nglui mglw'nafh Cthulhu R'lyeh wgah'nagl fhtagn...    Ph'nglui mglw'nafh Dagon R'lyeh wgah'nagl htogrn...   Dagon! Dagon! Dagon!"
   # ENDING
   jump credits

label frankyNorm:
   show Franky smile
   f "Oh, no one really, I'm just the neighbor."
   pc "Ah, I get it: if there's gonna be noise, might as well join the party, eh?"
   show Franky nervous
   f "Oh, no! No, not at all! I hope they don't think I'm... no! No, I just had some, eh, plumbing issues I need to have looked at."
   pc "Plumbing issues?"
   show Franky blush
   f "Yeah... it's really embarrassing. I'd rather not talk about it."
   jump frankyLead

label frankyLead:
   "You notice them fumbling the oddly bound book in their hands."
   pc "That's some chonky beach reader you've got there."
   show Franky nervous
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
   show Franky blush
   f "Well... plumbing, for one."
   pc "You use theology on your plumbing?"
   f "Oh, Old Ones... you think I'm weird now, don't you?"
   pc "Are you kidding me? I'm riveted!"
   show Franky love
   f "Really? You're... really? Oh my, I'm blushing. Look at my cheeks! They're blushing!"
   "Franky lifts a hand to one of their still-reddening cheeks. It's trembling. You've made an impression."
   f "Oh, I'm sorry, I made you nervous. If it helps... I think you blush real cute. Or... you're cute when you blush. Yeah."
   "Franky clutches the book to their chest, an audible \"eep!\" escaping them as they jolt upright, eyes wide again."
   "After a moment, they seem to notice your own nervousness. Suddenly, their shoulders slacken, relaxed."
   show Franky smile
   f "I think you're cute too."
   pc "So... want to show me your place?"
   f "Yes, please! Although... I might need some help getting Lord Dagon out of my bathtub first..."
   # ENDING
   scene black with fade
   "You have no idea who \"Lord Dagon\" is. Or why he would be in Franky's bathtub."
   "But as Franky tucks the book under one arm and leads you away with the other, you feel a fresh warmth in your cheeks and a weakness in your legs, and as they give you that knowing look with their beaming brown eyes, you come to the realization that you don't much care."
   "Whoever this Dagon chap is, he better finish washing up right quick."
   jump credits

label frankyBad:
   show Franky nervous
   f "No! I mean... yes, kind of. Why? Is that... bad?"
   pc "No! I mean... to each their own, right?"
   f "I guess. I'm not a fanatic, though. Oh dear, I hope you don't think I'm a fanatic!"
   pc "Not at all! Sorry if I gave that --"
   f "I mean, just 'cause they call us \"cultists\" doesn't mean we're psycho or anything..."
   pc "I never said you were a --"
   show Franky blush
   f "Although what kind of normal person would accidentally summon Lord Dagon the Fish-God in a bathtub? Stupid, stupid!"
   pc "Lord who?"
   f "Oh, Old Ones, you do think I'm a psycho, don't you? And why not? I sure am behaving like one!"
   pc "I mean, you seem a little stressed, but I don't think --"
   f "I shouldn't even be here! Gods, this is such an imposition!"
   pc "Hey, c'mon --"
   f "I'm sorry, I gotta go. I gotta... I dunno... do some dishes or something... help with the party somehow."
   hide Franky with dissolve
   f "Sorry! It was nice meeting you! Please, go have fun! Sorry! Thanks! Bye!"
   # ENDING
   scene black with fade
   "BAD ENDING: The odd buzz in your head -- surely a side effect of Franky's wheeling centrifuge of nerves -- quiets as they disappear into the next room, plucking up used plates and empty glasses as they go."
   "While you hope they also find some way to enjoy themselves at this strange party, you can't help but feel flustered to be suddenly left right back where you began."
   jump credits

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
   scene corner with fade
   "You move your way through the thick crowd and approach the corner of the room. As you do Mothman notices you and seems a little excited."
   show Moth base with dissolve
   pc "Hey, just wanted to say I like your Mothman outfit."
   m "T̶̾͝h̵̽̈a̵͗͌n̵̊̿k̶͋̿ ̴̇̕y̵͌͘o̶͊͝û̴̈́.̸̏͝"
   pc "Oh wow! Do you have a voice modulator or something in there? Is this for like, cosplay?"
   m "N̵͛̓o̸̓̇.̴́̓"
   m "D̴̨̠̼̈o̵͕̱͋ ̶͙̮̈́̔ͅy̸̨̰̠̏̔̍o̷̱̊͑u̴̲̟̒́ ̵̰̿̾͘u̵̦̝͕̳̇͑̈́͘n̴͓͎͗͜d̶̗̩̼͕͐͝͝e̷̟͍̋̍͝r̸̟͚̊s̵̥̞̪͊ͅt̷̝͚̮͘̚ǎ̸͔̱n̶̢̯̘͂͜ḋ̵̘͕͜ ̸̧̫̱͖̍͠ṁ̵͖̱e̵̢̬͐͘ ̷̬͎̮̫́̀̎w̶̖͂h̴̝̦͈́̔ȅ̶͍̈́n̵̢͕̩̹̅̽̌͐ ̶̡̝̫̳̑͑̈́Ȋ̴̦͕ ̶͓͆s̴̙͎̣͑̌̓͝p̷͚̻̒e̶͕͌̊̌̕͜a̵͖͇͊̑̏̓͜k̸̟̱͇͍̎ ̸̤̀͠ḻ̷͋͝í̷͉̹̳̔͛ͅk̶̤͕̾ę̶̼̭̦͊̿̚ ̶͔̂͒t̶͓͌͊̿͐h̷͚̗̼͐͛̑͝ȋ̵̢̙̝̏s̴̜̹̍͊̄?̸̦̀̕"
   menu:
      "Yeah, I can understand you just fine!":
         "Mothman grunts, acknowledging what you said."
         $ garble = True
      "What?":
         m "That’s fine. I will try my best to speak in your tongue."
         $ garble = False

   pc "So you’re really telling me it’s not cosplay?. You’ve got the Mothman suit on and the detective get-up. I won’t judge you if you do cosplay."
   if garble == True:
      m "I̷͆͆t̴̑̂'̶̎̃s̶͆͛ ̴͐̍p̷͂̄e̵͋͘r̸̀͘f̶̔̎o̵̅̃r̷͋̀m̸̿̕ǎ̸̈́n̶͂͝c̷̉̀e̸͂̓ ̵͐͐ä̸͆r̴̿̃t̴̒̐.̵̂͠"
   else:
      m "It's performance art."
   pc "Hmmm ok. But isn’t it a little warm for performance art? I mean, that dude dressed as a vampire is in board shorts."
   if garble == True:
      m "Ḯ̷̡̨ ̸̨̡à̵̡̧m̷̧͉ ̸̢̲á̶̝͈c̷͈͉ț̶͈̈ǔ̵̧̦a̴̯͖l̶͕͔l̶̡̖y̵̢̡ ̵̹̱q̸̛̩ų̶͕̟i̵̞̘t̵̡̟ẹ̷̡͇ ̴̬̙c̴̣̘ő̷̞͍m̷͚̬f̸̼̬õ̵̧̼r̴̡̡t̴̡̡ä̸̲͈b̵̨̳ļ̷̻̘e̵̩̣.̸̫̈"
   else:
      m "I am actually quite comfortable."
   pc "OK, if you say so. I just… don’t want you to overheat or something."
   "The Mothman holds up a cup full of juice before extending a…proboscis? A straw? They slurp up some juice to your astonishment."
   pc "Wow, your costume is really amazing. You have a built in straw!"
   if garble == True:
      m "Ý̶̖e̸̛̗̝͗̒s̵̗̋̎̉ ̸̰̤́̐ͅë̸̲́͝x̵͚͑̍a̸̦̖̔͐ĉ̵̖t̴͍́l̶̡̝̱͌͝y̶̠̻̦͗,̸̉̕ͅ ̶̥̅ḁ̴͈̮̿ ̷̭̤̓h̶̡̍ủ̷̹̰m̸͓̮͉̂ã̷̦̠̋n̶̹̰͆̒ ̸̻̋͜͝ș̸̤́͘ť̶̢͚̈̕͜r̴̩̗͊̂a̵̛̠̜͌ẅ̷̡́̇̋.̵̼̒̾͗͜"
   else:
      m "Yes exactly, a human straw."
   pc "That’s a weird way to put it but yeah. It’s cool."
   if garble == True:
      m "Ĭ̸̗̇ ̶̛͎̋̽a̴̹͉͘͠m̵͎͑ ̶̺͂̌͠g̷͍̬̭͆͆͠l̵͓̅ḁ̸̼̀͊̚͜d̸̻̬̝̚ ̷̢͉̑̍ỷ̴̱̞̫͊̂ö̵̝́ų̸̟͖́ ̴̼͖̓̀ͅf̸̛̫͔̦̏́ì̵̩̗͊͜͝n̸̺̘̄̍͝d̶͍͈̑͒ ̷̟̮̊͜i̷̢̩͋͋t̷̫͑͝͠ ̸̯̌m̷͙͉͑͜ȩ̴̟̫̉s̶̥̹̥̿̎ṁ̸̢̪̕e̵̺̰̳͑r̴̞͒̇́i̵̳̪͛z̵̺͍̏i̶͉̋́ń̸̖̇ͅg̴̢̙̿.̴̫̽"
   else:
      m "I am glad you find it mesmerizing."
   pc "Your costume design is just really top notch. If I didn’t know any better I would say you’re the real deal!"
   "The Mothman stiffens at the mention of him being a real mothman. He eventually relaxes and nods along when they realise you were joking."
   pc "So, what do you do during the day?"
   if garble == True:
      m "U̶̩̺̓́s̶̢̀̎̀u̴͈̥̒͋̆ͅa̸̭͐̃͋l̵͉͝͝͝l̸̨͕̿̄͝y̷̧̩̥͋ ̵̢̛̒͆s̶͉͍̫̓́l̶̦͔̄͊ę̵͍̤͋̾̕ę̴͔̙͋͊p̷̣̋̈͘.̸̡͖̲̎̃"
   else: 
      m "Usually sleep."
   pc "Oh, you work the night shift?"
   if garble == True:
      m "U̶͚͍̇́ḧ̶̹̗́͝,̸̰̋̆̉ ̴͓̲̖̐͂̃y̶̫͊̉ͅe̶̡̘̋̆͜s̵̨͔͔͘͝,̵̢̣͕͋͋̾ ̵̨̞͔̄t̸̝͑h̶̯͊e̷̢̲͗ ̵̜̓́n̸̚͜i̵̗͚̤͗g̷̞̈́̔̽ḩ̷̋͠͝t̵͍̲̩͆̊͊ ̶̹͒̋ș̷̔̒ḩ̶̈i̵̟̎̾f̸̪̘́t̷̪̣̹́.̶͇͉̾͂"
   else:
      m "Uh, yes, the night shift."
   pc "What’s your job?"
   if garble == True:
      m " Í̷̥͓ ̷̛̝̬͐͋r̶̛̺̳ͅę̵̻̂a̸̯̗͗l̴̩̭̙͂̓l̷̫͗̒͛ÿ̸̨̮͑ ̷̺̉͊l̴͕̤̲̅͐̇i̴̱̝̝͝k̵̬̊͝ẹ̶͉̑́͂ ̴̝͋̏̒ļ̴͚̜̒ȋ̸̞̔̽g̶̡̔h̷̥͎͛̈́͜t̴͈͈͘s̴̞̮̍.̸̛͇̦͚̅͒ ̶͈̦̺̍T̴̗̎h̴̩̫͝ë̸̗̰̙̈͝ỳ̵̤̟͓͛’̸̱̓͘r̸͉̬̳͒e̶͖̚͝ ̷̳̈̒ò̶̞̋͝n̶̓̆ͅe̴̡͎͊͝͠ ̷̼̺͘o̷͕̟̽̈́f̴̫̂ ̶̨̛̓͂m̴̜͝y̴̥̩̦̓̀̀ ̸̻͚̮̃f̸̰̻͚̈á̵̖͓̘͐͠v̵̟̰̦̽o̶̯͛͂͌r̴̢͙̥͑i̵̮̱̔̕t̷̢͙̙́̚é̶̬̬̳ ̴̧͉͇̽̎͗t̶̝͖̄h̴͕̃͐ï̵̞̻͚n̴͙͇̎g̵͙͌̄ŝ̶̨̤.̷͔́͝"
   else:
      m "I really like lights. They’re one of my favorite things."
   pc "So you’re like an electrician who specializes in light fixtures?"
   if garble == True:
      m " Y̶̗͍̍e̶̹̅s̷̞̼͠,̵̠͚̀ ̷͉̻͠ỳ̶̗̳͍̇o̷̡͇̠͘ũ̶̙͕͒ ̴̀́̽ͅẗ̷̝̝̊ó̵̹̝̓͝o̶̬͎̍̏k̸̰̽̀ ̷̲͓͆̄t̶̛̩̯̾̕h̵̗̋e̶͔͈̓́ ̸̼̈́̊̿h̷̬̤̤̕ú̸̧͍̾̆ṁ̷̞͑͛ȧ̷̰͚̜͛n̸̫͊͑ ̴̜̩̈́̌͜w̵̯̒ö̵̝́ͅr̷̭̪͐̌́ḍ̷̩́͆̏͜s̴̩̔͛ ̷̛͚̍͠r̸͓̝̆̉̈́i̸͙̿g̴̻͂ȟ̷̡̲̒̐t̸̢͔͍̃̎́ ̴̞̜̀o̴͉̲͋ͅü̸̦͙̮t̸̩̮̠̍́̄ ̸̦͙͌̔o̷̜͉͐̊͠ḟ̴̧̪̬ ̸̠͍͉̈m̴̠̟̉y̷̫͘͘͜ ̶̦͋̔̀d̸͚̏̎e̷̡̟͛́̓f̶̧̹̾͒̉i̷̖͛̅n̸̢̟̯͛̐͝i̸̪͕̒̈́́t̵͔͘͝ͅé̷͍l̴̥̒̉̇y̵̜̟̔̕ ̴̠̆h̸̭́̍͑u̵̪̠̕ͅm̵͖̬͒̃̃à̴̹͉n̶̤͒́̅ ̸͙̹͆̾m̵̭̫͛o̷͎̫̰͊̏ṳ̵̫̠̅́t̷̞̟͆̒̌h̸̖̝̾.̷͉̊̀͜͜"
   else:
      m "Yes, you took the human words right out of my definitely human mouth."
   pc "That’s really interesting. I would’ve imagined that electricians would work during the day."
   if garble == True:
      m "Y̷͇͖͎̔̀è̸͍̲̞͘s̶̭̻̊̕͝,̵̘̪̔̓ ̷̱̌̓̍t̸̼̣̓̅h̵̢͊̿͌ͅa̷̖̜͠t̶̗̹̝̔͋̈́ ̷͓͑w̷̨̹͛̓̓o̵̤͌u̶̻̅̋l̸͕̎̐́d̴̞͈̈ ̴̟͠͝m̷͈̘̺̋͝a̶̧̤͒̃̚͜k̴͔̱̑̃̚e̴̺̙̥̋̏ ̸͔͇͖̓͠m̴̼̞͖̋͐ơ̵͙͍̻̔ȑ̸̭͍é̵̠͖ ̴̤̯̏͐s̴̥̃̐̍e̶̼͠n̶̳̲̩̒̽̓s̸̠͊e̷͉̦̊ ̴̞̫̥̉̐w̴̺̐o̴̫̥͆ų̸͈̔̒͑l̶̪͉̈́̆͝d̷̹̫̯͂̓̀n̴̨̯̎̌͝’̴͉̺̥̎͗̃t̵̗͆̈ͅ ̴̲͕̉ì̵̝̗t̷̗͚͙̉.̷̛͔͈̥͒"
   else:
      m "Yes, that would make more sense wouldn’t it."
   pc "Anyways… If you’re an electrician and don’t do cosplay, what’s with the trench coat?"
   if garble == True:
      m "Ǫ̶͍̓͗h̴͈̫̚,̷̭͎̔͒̈ ̵̗͊̍t̷̗͕̗̾̈́̽h̵̨̪̪͝ỉ̵̥̲͊͘ṡ̸̙͎̻.̵̨̔"
   else:
      m "Oh this."
   "He pulls at the coat with his… hand? Claw? You also hear the beat of wings but they sound like they’re coming from underneath a blanket."
   if garble == True:
      m "Į̴̹̰̄ ̵̩̖͚̐̑̿a̸͙̞̙͑̚͝t̷̛͎̗̤̍̈e̸͔̗̲͒̈̆ ̷̻̼̤̄͑͠t̸͉̞͒ḥ̶̰̈́è̵̫̓̀ ̸̩̣̽̔p̶͙̼̞͋ṙ̷̟̓͋e̷͎̲̓v̴̞͊̎̚i̶̞̕o̶͓̓̓͝u̵̜̘̔s̷̡̰͈̀ ̵͚̂̈o̵͕͌̈̃w̶̨̛̙͑͘n̸̲͖̝͌̕e̴͚̖͐̐r̷̭̘̠̅.̵̜͗̉͠"
   else:
      m "I ate the previous owner."
   pc "You mean paid?"
   if garble == True:
      m "Y̸̢͉̽̒ë̷͓́s̶̡̏̚.̶͖̫͋̓ ̵̢͇̍͜P̵̻̓̉ã̶̭̦͝ỉ̸̝̈̀d̶̲̫̈́̈.̴̱͍̄̽̑ ̶͎́̊͐Ḯ̶̛͉̤ ̷̼̱̍̔ͅp̴̪̂a̷̦̦̠͗ḯ̵̲̻͑̽d̶̼͖̩͆ ̶̺̀t̵͕̹̍̓̋h̵̡̞̬̏͆͒ẻ̴̫̾ ̴̙͝p̶̖̙̄̔̅r̶̦̠̤̈́è̴̤͙̥v̵̳̟̑͝i̸̦̍o̷̧̠̅͘ǔ̷̬̦̑s̷̱̠̰͑̒̕ ̷̼̆̈ò̵͈̰̖w̵͓̯͋̇͒n̶͓͐̅̆ĕ̶͇̐̉r̷͇̾̓̓.̸͖͚̎̔͊ ̵͙̮̏͋͝N̵̟̉ǒ̴̡̖́t̸͓̓́ ̴̥̻̥̌͑͗a̴̢̜͐ṯ̵̢̝̂ê̶̛̜̽.̷̘͑̓"
   else:
      m "Uh, yes. Paid. I paid the previous owner. Not ate."
   pc "So you’re into thrifting?"
   if garble == True:
      m "Y̴̍̍e̵̎̐s̴̝̐.̸̥̍ ̴̈́̂I̴̍̉ ̵̛̝l̸͉̐o̸̫͝v̴́͊e̷̋̊ ̷͈͂o̶̐͠l̵͂̈́d̸͈͋ ̴͖͠c̵̉͜l̴͐̍ò̶̙t̴̲́h̶͑̈́e̸̅͠s̶̕̕,̷̭̆ ̷͑͐t̵̅̕h̵̋̀e̶͋̈y̷͑̄'̵́̚r̵̐̚e̵͒̐ ̸̺̀v̴̇̆e̴͛͠r̵̅̃y̷̑͛ ̶̀̿t̴̄̐a̶͇̓s̷̈͌t̴͒͠ỳ̷̇.̵̾͊"
   else:
      m "Yes, I love old clothes. They’re very tasty."
   pc "...tasty?"
   "You see Mothman look at his hand. There appears to be several notes scribbled across it."
   if garble == True:
      m "I̷̗͔̺͝ ̶͖̎͂m̵̤͓̙̽e̶͙̠̿̔̾å̴̼̀n̷̟̖̙̽͘t̸̠̯̙͂.̶̼̤̆̃.̶̜͈͋.̶̮̍ ̸̹̎f̸͎̓̕a̸͚̣̕s̶̲͌͌h̵͚̮̽ḯ̸̫̲̥͑o̸̫̜̼̐̄͝n̴̙͚͗͜ä̸̤̹́̈̈́b̴̨͂͝͝ḷ̷̢̿̆e̸̘̾̿.̶̨̺̞̓͂"
   else:
      m "I meant… fashionable."
   pc "Haha, that makes way more sense. Is that like, a saying where you’re from."
   "Mothman pauses to consult his hand."
   show Moth happy
   if garble == True:
      m "Ỵ̸̛̀͠e̵̘̹͑̀́s̴͇̞̽͘,̶̰̝̾̃ͅ ̸̲̈́ĩ̸͙̍t̸̛͓͛̀ ̸̪̊̕͘ĭ̶͚͙͆͜s̵̠̭̉͊͆.̶̻̔̅͛ ̵̧̈́̊S̴̰͆̏͝ó̷̮̳͛m̷̨̆͠e̷̠͓͗t̸̠̔͆͒ì̶̬̫̩m̴̮̆͆ē̴̢̈́ś̵̠͖̝̓͝ ̴͖̞̊́I̵̭͒ ̵͍̮̂͒͝f̶͉͆̕o̸̥͖͗͐́ŗ̴͉̒̈́g̵̩͓̒ͅe̶̫̚t̴̢͔̰̆̚ ̶̛͖̱̒t̵̳͔̹̎h̶̡̭͑a̶̻̼̐̀t̷̢̙́ ̸̻͆I̷̫̓͝͝’̵̛̭m̴͍̘̦̎̈́̿ ̸͙́̃̂n̶̰̄̔͝ő̶͉̺͚t̵̢̛̰͒ ̶͉̭͌̀b̵͎͕͒͘a̸͔͖̜̐͗̚c̵͛͒ͅk̶̤̎ͅ ̶̣̯͖̈h̵̡̄̋o̶͖̺͘m̵͉͝e̴̡̘͈͛̚.̶̞̇̓͘ ̸̜̒̉̈́ͅE̸̮͠͠s̵̟̲͉̄̚p̴̃͜ę̶̩̓c̵̻̩̋ỉ̸̦̫̘͝a̶̩̙̎̽ļ̶̈́́̕l̶̼͆y̷̳̝̿ ̵͓͒̉w̴͇͓̝̓́̌h̶̺̰͉̓͒̂ể̴̢̞͜͝n̶̖̓̑́͜ ̴̘̹̔͜I̸̡̔̇͜’̷̨̼͊͜m̵͍̫̒̊ ̷̯̉͌̓a̶̺͎̎̉r̷̥̈͆͝ỏ̷̫̜̈u̷͍̖͓͒̊̀n̷̛͚̲͐͠d̵̳͉͠ ̶͍̈́̍͋s̶̼̈́̀ù̶̡͙̈́̈c̴͎̟̐̿h̶̜͖̄̚ ̴̢̻̜͆̀̚ḷ̵̡͊̿̔͜o̸̩̳̞͋̑̚v̸͎̩̏͐e̶̛͍͗l̷̦̆̌ͅy̴̦͕͈͗͘ ̷͙̍̒̄͜p̶̯̻̙͋̽͘e̸̡͆ǫ̴͠p̵̢̠̪̽ĺ̴̛̙̹e̵̪͐̈́̍.̸͕̊́͂"
   else:
      m "Yes, it is. Sometimes I forget that I’m not back home. Especially when I’m around such lovely people."
   menu:
      "Be kind.":
         pc "Oh Mr. Mothman, you're too kind."
         if garble == True:
            m "N̷̛̫͗ͅo̸͉͕̖͌̍͝n̴̟̜̣͋̎͠s̸̥̖̦͘e̷͙͆͂ṅ̸̺̕s̵͕̓̐ę̸̘̥͋̋.̵͖̎͗͜ ̴̡̘͔̐Ȳ̴̢o̴̢̢̼͊ù̷̻̋ȑ̶̟̈̚ ̴̣̠̂̈́͝p̴͚͙͚̃̇r̵̨̹̝͝ê̶͕̅š̵̘͌ë̷̺̺́n̴͍̉͋c̷͚͖̝̄ẹ̵͒ ̶̢̫͌́͝ī̶̜̂ś̸͕̫̽ ̸̟̀̌̆ẅ̴͚̣͑ȁ̶̧̰ŗ̶̲̭̀m̸͈͈͌i̸̋̌͑͜n̷̞̜̠͋g̴̗̦̲̐͒̄.̴̻͉̱͋ ̵̢̹̬͊̚L̷̡͙͔͐̈́i̴̬̱͆̅̚k̸̰͗̓ȅ̸͍̐̕͜ ̷̠͈̽ą̶̻̯̅͝ ̶̬͕̘͒͘b̷̝͙̆r̶͙̜̞̊̏̈i̶̠̭̮̎̌̇ḡ̷̼͒h̷̝̹̙̏͐t̵̠̔͑͘ ̴̣͘ĺ̵̫͕̫̀̋i̶̡̎̌g̴̹̈̂͆h̴͓̽͐t̶̰͇͌͛̆ ̷̻̜̥̋̓̂o̷̺͖̭̓̏̓ṅ̷̥̤̆ ̶̫̟̈̚ͅa̵̪̣͕͐͝ ̵̱̞̗̿͋c̴̝̳͔̈̆ọ̷̙͉̌l̵̺͇͆̏͌d̶̡̥̫̐ ̶̡̦̣͑̈n̵̺̘̼̍̅̍i̸̢͓̗͊̾g̸̟̕h̶̡̍̇t̶̤̜̥̀́.̴̡͘"
         else:
            m "Nonsense. Your presence is warming. Like a bright light on a cold night."
         pc "You said that calling clothes tasty was a phrase from home. Where are you from?"
         if garble == True:
            m "Y̷̙̓ȯ̸̹͑̀u̶̘͌ ̸̺͔̈́̒̈́w̸̪͌o̴͉̒̆u̵̟͛́l̵̨̘̲̍̽d̸̠̏́ ̶̧̼̹̑ķ̴̰͎̀ǹ̴͇͎͚ò̶̧̻͈w̷̜̔͑ ̷̜̳̀̈́i̷͖̩͑̀͐t̸̗̫͍͊ ̵̧̫̌ȧ̵̻͉s̴̞̿̍ ̴̻̼̏̀͜W̸̗̊ĕ̴̜̯̍̑ṡ̵͓͕̽͒t̵͖̑̊͆ ̴͎̣͙̄̋̆V̴͇̮̽̈́ĭ̵̦̺͒́ͅr̴̩̬̄͋ǵ̵͖͇̩̏̀ĭ̶̳̜n̴̰̔̀ï̴͔͙͐a̵̤͇̮̎̏́,̵̲̇̂ ̵̬̰̏̽̕b̵̩̘́͊͠û̷̺ṱ̵͍̹̇ ̵͎̗̒͊m̷̳̹̂ͅÿ̸̡̢̩́̏̌ ̶͖̗̕f̷̮̗͇̌̆̏a̶͎͑́̉m̷̻͇͙̀i̸̱͗̈́ḽ̴͎̀͘ŷ̸̫̠͚̆͝ ̴̜͍̆h̴̺̄a̴̦̘̓͒ŝ̸̺̫̽͠ ̸͓̎̄͠a̸̧̱̾l̸̟̠͓̑ẉ̶͒̽a̴̦͗̓͑y̴̞͊͘͝ͅs̴͇̠̭̈ ̸͎̠̺̈̀c̵̈͒͜á̴͖̲l̸͇̄̂l̸̞͖̎e̶͎͊͝ͅd̷͓̄ ̶͙̝̿͋͝ͅi̵͊͜t̴̠̱̀ ̸̦̈́͜ẗ̷͎̱͈́̑h̷̩̅̋ê̷̫̦̂ ̷̤͖̚͝N̴̯̓ĕ̸̹͎͘̕s̶͓͙̟̒̓t̶̰̦͒̆i̴͎̣̰͛̿̈́n̷̩͙͐g̵͕̑͋͝ ̸͇͇͒͑G̵̡͂͒̏r̵̡̥̠̒̔ó̵͈̍u̸̧̕n̸̢̯͎̕d̴̠̼̒̂́s̵͆̌ͅ.̸̤̾͝͠"
         else:
            m "You would know it as West Virginia, but my family has always called it the Nesting Grounds."
         pc " Right, because you're always heading home to those... country roads?"
         if garble == True:
            m "I̸̢̥̱͑͝͝.̵̧̙͕͋.̴̨̩̯̕.̷͕̫̖̈ ̴̡̰͚̒́d̵̯̩͑o̸̦̿̎̕ ̷̹̓̎n̶̩̎ȏ̵̯̞̬̓̚t̶͎̟̙̀̈́ ̸͕̻̊ũ̵͔n̴͉͚̐͋̕d̷̪̥̑̾e̷̥̼͔̓͋͝r̶̮̹͌̚s̶͈̔t̸̥͑͘ạ̶̝̻͂ǹ̴̻͍͓d̶͓̆ ̸̤̠͗͛̚ỳ̸̖̲ͅo̸͕̽́͝ư̶̰͚̗͐̑r̷͙̎͝ ̸̬͔̉š̵̥i̵̭̖͎͝ḻ̶̯̃̀l̸̯̭͖͂̀̌y̶͙͝ ̶̯̘̥́̇̀j̷͙͈̺͆̄ó̵̫̝͎k̸͚͙̕̚e̷͇͈̿͌͘s̶̮̙̓̾̚.̷̧̇"
         else:
            m " I... do not understand your silly jokes."
         pc "Of course not. My life seems so much less interesting and cool than yours. Your unique way of speaking, your work as a nighttime electrician, and your costume, it’s all so much more engaging!"
         if garble == True:
            m "W̶̧̰͗͛͊e̴͔̝͉̎̔ ̸̤̂̓̉m̴͔̠͔̒̿͋a̷͚͙̎͛ý̴̮̳̋́ͅ ̵̩̋ǹ̶͔͘o̷̖̊t̴̬̯͌͐̈́ ̴̊͜h̸̩̫̆́̊ȧ̸̧̘̚v̴͓̮͓͘ȅ̶̼̻ͅ ̶̢̩̼̾̊̎k̸͇̪̳̈́̐ṅ̵̥̮̤o̷̘̤͈̊ẅ̴̛̭̳̯́̓n̸̬͝ ̴̳̇ẻ̵͓̤͇a̵̙̰̥̽c̴̺̤̳̆̇h̸̺͗̓ ̸̾͜o̶̧͒͘̕t̴̲̎ͅh̶̤͓͇̋͘e̷̹͔̩̎̀r̷̺̉͌̕ ̷͎͗̈́͛f̵̘̻̈́͘ò̷̼̮r̷̮̙͑͋ ̸̜͚̮̋̍v̸̪̰͕̄ȅ̸̖̖̀͘ŕ̶̼͉͙̓̾y̷̡͖̬̾ ̵̥́̐ĺ̴̖̦̱̎o̷͔̥͘ń̵͝ͅg̵̢̚,̵̭͋ ̵̼͛b̷͉̪̖͋̉u̵̢̜̳͐̍̋t̷̩̳̓͝ ̵̧̱̎̆I̴̛͈̍͝ ̶̊͜c̴̫̀̿͝a̴͓̰͚͘n̷̥̱̳̊ ̶̻͑t̶̻͔͝ē̸͇͍ͅl̶̡̖̈́l̷̲̫̺͛̉ ̸̭̳͓̒t̸̜̞̤̊ḩ̸̢̾̈́ă̷͈̩̪ṭ̸̭̍̊͠ ̶̝̏y̷̺̓ǫ̷̟͈̈́͒u̶̧̽’̵̢̖͎̍r̷̥̊e̶̯̞̋̏ ̵͕̤̐̊̊å̵̮̀ ̷͉͎͕͑̐v̶̛͍̱̪́̒e̵͙̟͗r̶̼̆̓̎y̸͍̓͜ͅ ̵̭̄́i̶͓̮̽̔̄ņ̴̳̓ͅt̵̻̫̞̕ẹ̸̈̎r̷̛̬͙̟̋e̸̦͚̦͝͠s̶̗̺͆t̷̝̫͝i̵͔͔͐ͅṇ̶̎g̶̭̦̠̃ ̶̙̻̃ḫ̵̪̄͑ú̶͔̖m̸͖̒̓̚ä̶͇́͐͆ǹ̷̹͖́̆ ̵̲͆̍̉p̷̛͚̻̄e̵̫͉͓̍̕r̷̫̒ṣ̷̹̄o̴͕͈͗n̵̨̳̿̋͊.̸̨̫̳̆͊̐ ̴̳͐͝Ą̵̭̺́͒͗ṇ̸̎͘͝d̶̤͉̰̓̉ ̴͚̺͌̽̍y̸̠̘̐̚ọ̶̦̟̇ū̷͓͙̝̽͗’̶̠̂́r̴͔̞͋e̴̋͜ ̶͉̩͑̄́c̸̹̀̑ë̴͇̹́̈́r̴̟̣͔̃t̷̖̀å̶̗̂ḯ̸͚̤́ń̸̗̑͒l̶̬̒̀ỹ̷̦͖̏ ̸̦͒͂ḿ̴͚̙̩̈̂ǒ̸̺̩͎͒ṟ̵̜͘ẹ̷̝́ ̵̧̱͍̒̓̎k̷̭̣͎̇̊̚ị̶̿̿͒n̴̲̯̲̓d̴̪͍́ ̶̦̪̯̒ț̸̰͌̌͒ĥ̶̞̣͖͆̓a̶̬̥̓́n̵̯̰͒́͛ ̶̫̹͛̒͜m̴̠̖̭̄͠ơ̵̘̻̞͗s̴̗̠̍̌̎ṭ̶͔̘͂.̴̧͙͋"
         else:
            m "We may not have known each other for very long, but I can tell that you’re a very interesting human person. And you’re certainly more kind than most."
         pc "What do you mean Mothman?"
         show Moth sad
         if garble == True:
            m "M̸̠͍̙̊̃o̷̟̍̅ş̵͖̄̒͒t̶̫̜͖͋̄ ̶̥̲̓p̷̙͘e̸̙͈̓͝õ̴͈͖͜p̸͖̭̅͗̎ḽ̶̆e̴̛̙͖͒́ ̷̞̅̈̋a̷̲̲̱̎͆r̴͕̤̰̚ẹ̴̯̘̑͂̑ ̴̗̪̊̉͝r̴̖͙̄u̷̪͈̎̆d̵̫̗̼̈͝ȇ̶̢̅͘ ̷͚́ͅẗ̶̖̋o̷̭͎͎̒ ̵̪́m̴̲̰̌ͅĕ̶͎͇͙ ̵̢̎͋̍a̸̦̓̽̽n̵̪͓̕͝d̷̛͉͕͛ͅ ̸̛̱̇͛ͅs̴͍̠̈́̈́̒ḫ̶̀̃̌ü̴̹͖̱̍̾n̶̤̠̾̽̇ ̶̳͍͂̔m̶̛͍̭͐ę̸̝̬͊̊.̶̪̽̈́ ̵͉͚͛Y̴̧̲̐̅o̸̞̬̔͊͑u̷̖͒ ̴̨̏̑ȧ̷̤͔̪͐̕r̸̦̼̍e̶̟̻͌̽ ̷̢͗d̷͉͈̅̈́î̶̻͂̚f̶̅̅̒ͅf̸̙̰̫̅̚e̴̤̮̊̅͂r̸͈̤̋̓̂e̴̻̦̿̈̈n̸̯͓͒t̴̛͈̭̉̉.̵̨̆"
         else:
            m "Most people are rude to me and shun me. You are different."
         
         pc "I still don’t understand. Why would they do that to you?"
         show Moth base
         if garble == True:
            m "Ḫ̶̡͑e̷̮͍̥͌r̸̢̉͆̓e̶̹̞̓,̶̯̾́̎ ̸̻̳̫̎l̶̛͈̻̖̍e̷̩̣̊̍̕t̶͕̞̀͆ ̶͔̥̩͋̋̆m̸̪̦̃̋̋e̸̡̢̚ ̴̫̏s̴̪̖̦͌̇ĥ̴̫̗̝̾o̶̢̜̒̚w̵̡͇̬̽ ̴̨̲͊̽y̴̞̳̜̑̆o̵̲̅͜ṷ̷̭͍͠.̸͉͆"
         else:
            m "Here, let me show you."
         scene outdoors with fade
         "Mothman grabs you by your hand and pulls you away from the party and the noise. He leads you through a crowd of people to the back yard."
         "It’s empty except for you two, and lit only by the fluorescent porch light hanging off the house."
         pc "What is it?"
         show Moth base
         "Mothman seems a little distracted by the porch light but they focus on you. He takes your hand and puts on his furry face."
         if garble == True:
            m "D̴̹̿o̸̫͍̤̒̕͝ ̸̟͕̣̏͂ẏ̶͓͊̇ȏ̸͕̖ǘ̵̯͉̆̀ ̷̯̃̒͜u̷̢̬̓̊n̴̳̝͊d̴̀͜ĕ̸̟̣ȑ̶̺͈͒̀͜s̵̯̫̑͒t̶̫̾ą̴̯͐͂̒ṇ̴̿͝d̷̡̍̂̃ ̶͍̒̌ṁ̶̦̃e̵̩̾ ̷̮̣̓̽ͅn̶͖͘o̸͔̯͆w̴̙͖̰̐̊̚?̵̛̫̹̿͠"
         else:
            m "Do you understand me now?"
         pc "No… but that is a really good costume."
         m "Mothman seems flustered for a moment before returning to his calm demeanor."
         "He takes a step back from you and pulls off his hat and trench coat, revealing his moth-like body."
         if garble == True:
            m "N̸̨̚ö̶̥͈͓́̆̕w̸̨̘͓̚ ̴̞͊d̴͔̬͖͂ȯ̶̌̉ͅ ̶͙̹͋̃͘y̴͈̭͙͛o̶͔̬̝͂̈́̾ṷ̴͎̎̓̈́ ̸͕͖̾ȗ̶͍̯̂ń̵͙̋̕d̴̙̥͋e̷̤̒r̶̝̥̤̄̍͠ś̷̘͂̓t̶̮͔̰͆̓a̵͕̠̪͛͊͘ņ̵͚͎́͌̆d̵͉̈́̃͝ ̷̦́͐w̵̝͘͝h̵̠͋̇ŏ̴͚̩͇ ̷̼̻̀̌̑I̶͎͉͛ ̷͉̑a̴̧̖̟̔̃m̷̧͇̅̈́́?̸͔͍͌͆"
         else:
            m "Now do you understand who I am?"
         pc "Yes… you’re the real Mothman."
         if garble == True:
            m "I̷͚͚͆͗ ̴̦͗ḑ̷́̃̀o̴͓̒́͂ ̸̜̪͎̏ǹ̶̢̹͒̆o̶̡͚̦̒͊t̵̗͉͑͆ ̶̗͂̍a̵̢̗͓͑b̷̩̘̅ḭ̸̜̊d̵̓͊ͅe̸̞̍̌ ̴͉͇͕̒b̷̮͇̱̍̃͒y̸̠̼̗͐ ̵͈̰̿y̸̝̪̍͂͜͝o̷͔̤͉͠u̶͓̿̃ṟ̶̛̘̈́̆ ̷̧̺̍͗͗g̶̠͇̋͐͋e̷͈̭̚ń̷͉̙͕ḏ̴̙̅ͅe̵̲̬̮͋̇̈́r̸̲̲̲̂͛̕ ̴̗̈̽͜ț̴̺̃̇e̷̗͎̾r̴̹̾m̷̤̓̏͝ī̵̳̪͙n̸͙̫̊̔ȏ̵͉̣̀ĺ̸̠͙̘̾̋o̶͖̝̘͐g̶̛̝̥̽̆ý̸̩̬̌̕,̷̙̝͖̎̾͝ ̴̨̘̍b̴͙̟̻͛u̸͎̽͑̚ṱ̵͔̈̿ͅ ̶̬͖̫̿̈́ÿ̵̠́e̶͓̊̍͝s̷̢̺̳̓̚,̴͉̲̌̊̔ ̷̣̰̣̏͝͠t̷̟̋h̸̖͂̚a̵̜͈̿́ẗ̴͙̤́ ̶̤̗̼́į̵̲͍́s̸̨͎̦̀̔͂ ̸̙͙͋ẅ̴̲̪́͛h̷̫̝́̓̕å̸͎̕t̸̪͝ ̶̞͇̂̈t̸̫̞̥̑͌h̷͎̑̑e̸̟͇̅y̵̢̲͔̋̔ ̷̣̒́c̶̬͗́a̵̰̠̅l̸͙̣̯̈́̑l̷̗̿ ̴̭͌̾m̵̺̃̀̓ẹ̵͇̟̓̒.̷̣̺̽͠"
         else:
            mx "I do not abide by your gender terminology, but yes, that is what they call me."
         pc "Oh, I’m sorry. Is there something else you’d prefer to be called?"
         show Moth happy
         if garble == True:
            m "N̶̠̭̝̓o̷̖͖̬͠ ̸̤̰̱̅̏̒n̴͚͇̜͌é̷͉͝ę̶͈̌d̵̳̥̆ ̵͍̜̎̑t̷̜͇͌͜ȍ̶̼̦ ̶̢̕͠a̴̢̨̛̻̿p̴̢͕̹̓͗ō̵̺͇l̸̬̈ö̴̝̓g̸̪͎̉̂͂i̴̹̣̇͆z̷̪̀e̵̙̔͛,̷̼́̿̔ ̷̦̂̔M̷͙͍͉͐̀͐o̴̖̬͈͊̉t̵͚̪̀̃ḧ̸̛̰͘m̷̮̽̑a̵͓͒͗n̸̲͖͍͘ ̸͙̇́ͅi̴̜̍͠s̷͕̪̀͂ ̴̫̂͋f̴̰̿ï̸̡̙̖n̸̙̻̩͂͘ę̸̭̿ ̶̟͉͌͊̉͜f̶̨̏̀̆ö̵̱̪́ŗ̴̣̈́͊͝ ̶̈́̏͜n̵͉͔͓̅ó̶̤̎̈́ẃ̵̧.̸̣̟̫̾͛̚ ̵̺̝̃̅͘I̶̝̼͓͐̋͊ ̶̡͍̉̔ẉ̷͐̚̚i̶̠̔̋̇l̸̪̣̃̏l̸͜͝͝ ̶̮̦͘f̴̺̿̇ì̷̧̝̇͊n̸̻̆̍d̷̡̏͑̉ ̶̳͙͝ȃ̷̦̥̕ ̶̮͌̎̀ǹ̶̖͊a̸̰̺̼͌m̷̬̎̔͊ȩ̴͕̍ ̶̲̥̄̚t̶̲̎͂ͅh̸̙̲̆a̸͉̗͒̎t̷͔͗ ̶͍̏̎̕s̵̥̺͂̾͠ȗ̴̼̠̃̽í̷̘t̷͕͙̎s̶̨͗̎̋ ̶͖̣̪̍m̸̼̜̋͑e̴͚̥̾̽ ̸̮͐̌s̵̫̬̯̈́ô̵̘͊͋o̷͍͂ņ̵͚̬͆͗̅.̷͇̥̫̊̆̇ ̴̫̺̟̍͐͘B̷̬̪͚̅̑u̵͉͝t̶̘̹̪̽̿͂ ̵͕̳̎̒̚t̴̯͂ͅḧ̵̡̹́̓̎͜a̵͚͔͑̍n̶̖̲̦͌̍́ķ̴̬̜̐͒͠ ̸̳͆̓y̵̼̜̼̽o̶̮̽u̵͙͕̎ͅ ̷̗̈f̵̡̯̼̓͠ó̷͇̼r̷̦̂͐ ̸͚͋̐͆͜a̸̝̝̞̎̌s̸͖̲͆́k̷̡͎͙͆̑̄i̴̙͆͒̎n̸̢̒̚͝ͅg̸̥͓͋́́͜ ̶̀̔…̴̳̠̐͌̀"
         else:
            m "No need to apologize, Mothman is fine for now. I will find a name that suits me soon. But thank you for asking …"
         pc "Oh, my name is [user]."
         if garble == True:
            m "W̵͓͑̍e̷̦͎̯̾l̷̞̳̗̈́̏l̵̺͋,̴͎̉͊́ ̷̿̐̌ͅí̷̞̥̺̎͠t̸̓̈͜ ̴̢́̃͜ḯ̷̝̟̀̿ş̵̳͌̈́ ̴̺͚̒n̸̺̝͆̇i̸̲͉̩̓̕c̴̨̒̚ẹ̴̡̡͗̉ ̷̥̎t̴͖̍͊̓o̷̜̣̍ ̸̯̻̯͌̔f̸̫̻͌ù̸͉̂͊l̷͙̰̫̅l̸̗̓y̸̨̰͌͝ ̷̞͑͑m̸̧̍ͅe̸̹͖͐e̸̡̢͈̓̿ţ̵̉̐ ̷̤̝͕̋ỳ̸̼͈̉͠ó̶̧̨̂̽ṵ̴̩̭̒̉̕ [user]."
         else:
            m "Well, it is nice to fully meet you [user]."
         "There’s an awkward pause. You’re both unsure of what to do in a situation like this considering cryptids don’t ever reveal themselves like this."
         pc "Do you… want to go get some food? You can get some fruit juice and fabric and I can get human food."
         if garble == True:
            m "I would… I would really like that."
         else:
            m "I̶͇͊̓ ̷̰̠͙̌̃w̶̧̏͠o̶͇̳̫͒ư̸̺l̸͎͖̤͒̐͘d̵̬̬̚…̶̪̳̼͠ ̶̛̫͍̠̀́I̸̞̕ ̶̢̭͖̒͠w̷͉̿̈́̽o̷͇̐̾͝u̶̳͈̩͆l̵̹̾̋̕ḋ̷̲ ̶̰̌̔̀r̶̟̜͋e̶̞͎͗̽a̷̠̣̤̎̽l̵̻̟̯̋̑l̶̝̥͘ŷ̸̘̿ ̴̮̬̉l̸̘̼̫̃i̷̢̛͍̭̅̎ķ̸͚̠͆ȩ̶͇̏̿ ̵̫̉̊̑t̴̡͖̎̃̈h̴͍͍͌̐a̵̜͆̐̚t̵̹̝̋.̴̱͙̈́̒"
         scene black with fade
         "Mothman pulls on his trench coat and cap before offering a hand to you. You accept it and he pulls you close before taking off into the night sky. You never thought a Halloween party would end with a flight to get fruit, but here you are."
         # GOOD END
         jump credits

      "Be aloof.":
         pc "Oh, um, thanks I guess."
         if garble == True:
            m "Ì̵̱͚̰̚ ̶̘̖̟̈͐͝ã̸̭̻̝p̴͉͘o̵̢̡͕̅́l̷̘̋͠o̴͙̖̅̿g̸̡̠͇͛̍͝i̸̪͘z̷͇̈́ë̷́̿̕ͅ ̶̨̢̾̆ḯ̵̗͍̼f̵͍̖͝ ̷̛͍̦͊t̴͓͌̓̄h̶̞̾͋̚ă̴͔t̷̼̲̓́ ̷̩̳̘̑̓͗w̴̤̓̓̚a̷̖͇̿͐͊s̷̪͆ ̶̦̦̍̇̇ť̵͉͊o̶̤̤͗ő̷̠̒ ̴̙͍͉̾͘f̷̧͈̌̇̈o̶̢͎̅̄̒ŕ̷̥̑̚w̷̞̏à̵̩̮̌͆r̷͇͑̚d̸͕͌̋͆,̴͕̯̩̋́ ̵̪́́I̸̢̘̿̋͠ ̸̟̳̃̃̍a̴̾͜m̷̡͙̒̈́͊ ̷̱̝̉̕ń̵͙̥o̴̬̠͐̿t̶̻̠̘̄̃̂ ̸̣͓͝ù̸̩̂̈́s̵̪͕̝̃̉̈́ȅ̴̼͌d̶̗̬͂ ̷̨̘̮͌t̸̝̏̋o̴̼̲̽̓̒ ̷͙̬̍̓̚ͅṕ̶̡̛e̵̛̖̐̔o̴̻̫̾͂̇p̵͙̙̩͊l̴̟͝é̴̫͓̃ ̴͇͌t̸̥̔r̶̢͌e̸̺͙̐̉̈́ả̶̯͊t̸͖̳̜̆i̶͍̔͆n̶̫̏g̵͈̪̟̀̚ ̶̺̙̠͛m̸̪̈̒e̴̖̎̿ ̶̯̙̂͘s̴̭̬͂o̵͖͈͉̚ ̵͓̝̻̈́w̵̗̮̽ḙ̵͇̙̀l̶͙̾̑̀l̴͖̭̩̈́̔.̴̥̬͋̈́͛"
         else:
            m "I apologize if that was too forward, I am not used to people treating me so well."
         pc "No, no, it’s not your fault. You have been very polite, I’m just… not sure about how interested I am."
         show Moth sad
         if garble == True:
            m "Ḯ̴̳̱̚ ̷̹̄̎̚ŝ̸̨͕̾́͜ȅ̴̡̪̜́ē̴̥̼̜.̶͓̻̆ ̶̞̎͝M̶̗̱̓̓y̸̫̩̏ ̸͇͓̔̈́f̵̥̬̾̔ö̴̱̜̻́̃̂-̶̠̯̟̆ ̸̥̓̒I̸̠͗͊ ̶̙͂͛m̸̬̫̤̀͌e̷͖͎̔̏͗a̵͖̦͒̕n̴̠̆ ̶͕̞͕͘m̶͕̺̈́̎̍ͅy̸̺̪̖͊͝ ̴̭̉̇͐c̸͎̝̫̄o̵̻̎s̶͚̿͛͘ṯ̴̍͜u̶͎̙͌m̶̖͛̊̔ȅ̴̡̺̫ ̷̨͝c̷͙̙̾a̵̹͂͝n̴̛͚̰͛̂ ̵̰̮̉͘c̷̘̝̅͛̅e̶̱̾̂͘r̶̦̉̀ͅͅt̴͈̑̉a̷̜̤̜̔i̶͙̞͂̀̀ń̶̦̯͓l̵͖͌̈́y̷̡̱̔̉́ ̸̱͔̦̒̂̚b̶̩̽̈̅ê̴̛͚̺͗ ̷̢̳͈̀͑̓u̵̟͂n̵̗̬͎̑n̵͙̳͒̃̀e̸͚̟̒r̵̼͜͝v̵̮̆ḯ̷̢̧̜n̴͕̞̳̿g̷̟̦̈́ ̶͍͗̉t̶̡̮̃o̸̢̟̼̽̄͠ ̶̰͓͕͌̈́m̸̢̛̍́o̵̗͒ș̸̢̅̈́̍ẗ̴̨̢̝́ ̷̛͇̞̾͐ͅp̷̧̦͖̾ȅ̴̦o̸̟̅̕p̶͍͎͑̄͘l̷̮̒̏̒ę̸͉̜̾,̷̳̐̋ ̸̲̜͋̏s̷̡͂ȍ̷̬͓͝ ̴̳͆̚I̶̡͌͝ ̷̼̲̊u̴̡͚͇̓ń̷͕̘̂͂d̸̟̖͗é̵̠͗̓r̴͔̲̞͗s̵̞̗͖̈̂ẗ̴̲ȧ̴͎̬̘͠͝ǹ̷̨̛̜d̸̖͎̏͝ͅ.̸̣̖̋̃̕"
         else:
            m "I see. My fo- I mean my costume can certainly be unnerving to most people, so I understand."
         pc "Maybe if we could spend some time together without the costumes… "
         if garble == True:
            m "Ḭ̷́-̶̤̯̇"
         else:
            m "I-"
         if garble == True:
            m "I don’t think I can do that I’m afraid."
         else: 
            m "I̴̮͉̎̈́͘ ̷̗̓d̷̜̹̫̓̓ơ̷̢͊̕ṉ̶̪͒́̑ͅ’̵̡̛̿͝t̷͖̮̺̽ ̸͖̹͒͛t̵̞͕̞̽̔͝h̸̦̫̃ḭ̶̻͋̚͝n̷̨̛̗̼ǩ̶̝͑ ̴̹͇͔̋Ì̶͕̞̟͠ ̶̦̃ç̶̜̱̇̈a̶͕͔̝̋n̴̞͠ ̵͇̜̦̿d̴͈̘́̆ơ̷̫͍̐̓ ̷̳̠͓̍͛̑t̴̡̀͛h̵̳͋a̷̧̟̹͂́̋t̵͓̱͎͘͝ ̷̳̞͊͗Ḯ̴̡̫̥’̷̭̈m̷͕̈́͝ ̴̟̈͛̓ạ̵̖̹̈́̒f̶̟̈́͛r̷̢͕̀̐͘͜à̶͈̾͝į̵̠̪͌̓̈́d̴̞͉̳͊̈.̶̣͋̀"
         pc "It doesn’t have to be tonight, we could go get dinner or something. Or breakfast if that would work better with your schedule!"
         if garble == True:
            m "​​N̴̰̫͎̕o̷̱͑͠,̶̛̘̳͖͗͋ ̸̦̄Ỉ̶̘͔͈̿ ̶̡̜̓̑̇d̴̜̭̝͊o̵̽ͅn̵̩͔̊̌̓’̶̝͚̜̔͊̈t̸̻̄̅̿ ̶̙̹̆̆͠ť̶̙̹͐ḫ̶̝̜̾͌́i̷̮͂n̸̢̄͝k̶̠̖̝̈́̕ ̷̱͐ṯ̵͕̘͋h̵͛́͜a̸̛̹̺͊t̵̜́ ̴̤̎͛w̴̠͐̄i̸̜̪̣͑l̷̳̉l̴̝̃͗ ̵̪̥̑͂̓w̸̺̆̓õ̶̘̤̳͛̕r̶̤̎k̸̨̤̐ ̷̢͕̈͛͛f̵̢̧̍o̷̬͎̒̑̈r̶̺̹͕̄̌͂ ̵̨̢̖̍̆͝ḿ̸̱͆e̷̛͎̊.̸̞̎̋̉"
         else:
            m "No, I don’t think that will work for me."
         pc "Please, I like you, I'm just… unsure."
         if garble == True:
            m "T̵͋͜ḩ̷̥̂ả̷͉̠̔̈ẗ̶̼̣͒ ̴̳̭̲͒͂͌i̷̫̠͛͝͠s̷̛͓̭͔͆ ̷̪͐̏a̵̤̻̠̐̈l̷̩̹̆̄̽ͅr̷̘̳̲͆̃̀ḯ̷̖̘͑g̷̜̠͌͋͝h̸̡́t̶̰͉͂̾̌.̶̰̻̃͌ ̸͖̈́̂Ï̴̮̱̹̃ ̷̡̡̠̾u̷͙͋̋͆n̴͙͝d̸̩͇̿͗e̷̹̰̔̚r̴̨̈ś̷̖t̵͓͠ȁ̵ͅń̶̞͕͆̚ḏ̶͓̑͊̉͜,̸͍͈̉̐̚ ̵̯̐i̸͉̲͚͌̅́ṫ̷͎̈́̈ ̸̥̜́i̵͎̹͇͘͝s̷͉̐͒́ ̴̡̰̯͆̅t̸̬͓͔͛ḩ̵̘́e̷̛̱̦̤̔̀ ̴͍̺̃̔̏n̴̥̝̣̒o̶̡̱̥͛͝r̷̠̔m̸͓̅̈a̸̘̖̩̓̐͠l̵̘͓̮̍͗͒ ̶͍̱̒̕͝r̵̫̟͆̐ͅe̸̠̅̚͝a̶̙̳͌̐c̷̭̘̯̽̎ṭ̴̲̎̾ī̸͙̠ö̸̘̞n̵͎͐̌͝.̶͎̏ ̶̬̥̪̒Ï̵͉̰̎͝ ̶̖̻̱̊à̵ͅm̴̢̩̍̊ ̵̥̘̾̂s̵̹͈̤̈́̒̚ȏ̶̡̳͍̽ȑ̶̫̲r̶̗̺͋y̵̠̯̪̽ ̵̤̎͒w̷̤̆̀̍e̶̘̺̐͛͑ ̸̺̝̅͜m̸͈̬̚̕͜u̴̡͎͂̕s̷̲̎̓̚t̶̨̛̍̚͜ ̶̱̒͠p̴͖̐ä̸̭̰r̴͈͊t̷̰̐̀ ̸̩̭̲̓͑̕w̶̰̪̐͆a̶̩̟̍̑̂y̸̛̛̮͖̙̌s̸͚̠͛̇̄.̴̫̻̈́̈́"
         else:
            m "That is alright. I understand, it is the normal reaction. I am sorry we must part ways."
         hide Moth with dissolve
         pc "But we don’t hav-"
         scene black with fade
         "Before you can finish your sentence Mothman walks away from you. He quickly melts into the crowd at the center of the room, leaving you alone in the corner."
         "Somehow talking to him has left you in a worse position than when you started."
         # BAD END
         jump credits

      "Be rude.":
         pc "What did you call me?"
         show Moth sad
         if garble == True:
            m "L̴̜̰͍̐̎͝o̴͍͑́…̸̘̘̫̓͆̋ ̶̥͈̳̏Ì̶̝̣͎͝͝ ̵̞̿̂͐c̷̥̬̗̉͗̈́a̴͚͒ͅl̵̘̩̃l̴̠͍̓̑é̸̢d̵͙͉̰̉̔͝ ̶̙̂̂͌ỳ̷͖̙̤o̷̥͊͒̍ͅú̷̪͋̿ ̶̹͋̓l̷̺͚̎̆o̶̪̳͠v̷̛̭̌e̸̥̰̒͊͛l̶̬̖̀ẙ̶͕͙͝.̸͈̩̖̃̀̋"
         else:
            m "Lo… I called you lovely."
         "He checks his palm again, this time with a look of worry."
         if garble == True:
            m "D̴̢̔̀i̶͈̼̺̿̊͝d̸̞͊́ ̴̨͈̏͘Î̴̢ ̶̝͈͖͒͝s̷̥̽̎͐a̵͔̦̋̕͘y̶̤̑̇̚ ̷̛͈̭͐͂s̶̬̘̄o̵̰̬̫͠m̴͚̎̒̕ě̸͈͇͖̾͝ṭ̵̾̊͝h̶͎͝͝i̵̠͓͒̑̓n̸̩̊͌g̶̟̈̓͑ ̷̨͓̎͆͝o̵̢̤̱͒f̶̢̬̋̂ḟ̷̥̣̣͘e̸͈̠̎͛n̵̰̹̈s̷̖̓͑i̸͉͐̆v̶̞̦̳́̚e̵̱̳̝̊?̴͍̄́"
         else:
            m "Did I say something offensive?"
         pc "Not really… I just don’t like you that much and that caught me off guard."
         "Mothman’s face contorts into… sadness? Anger? Or, at least a moth’s approximation of some emotion."
         show Moth angry
         if garble == True:
            m "W̵̪̽h̸̬̹̯̏̓̑ä̵͚̬́̽̕t̷̥͆̿ ̸̢͚̖͛̂à̴̝̟̹̌̑ ̴̢̥͂s̷̜͚̈́h̴̦̻̅á̷̲̦͝ṃ̶̠͐e̵̥͐͝…̷̤̍̆͊ ̷̻̭̽̈́͜Ḯ̶̝ ̵̢͖͊͘͝ṱ̶͉̚h̵̰͖͛̏ͅo̸͔͚͌͝ụ̴̻͛́ͅg̷͓̥̟̓̎̏h̷̻̣̫̓͆̑t̵̥̺̀͘ ̵̬͗̎ỳ̸̗͓͖̓͊ō̴͉̺̕u̷̧͍̹̓͐ ̸̯̍̄w̵̨̻͐ͅȯ̴̧̖̣ṷ̸͉̽̓̓ͅl̵͇͗̉̐d̶͋̍̎ͅ ̴̻̠̋̾̾b̴͖̘̯̊ḛ̴̪̅̓̈́ ̸̭̯̮͐̕d̷̻̜̾͆ȋ̵̤͇̽f̴͉̻̤̈͆f̸͉͕̂e̶͖̒͜r̷̼̩͒́e̴͙͊͜n̷͙͖̻̆t̴̢̨̐͑.̴̻͙͉̌̎"
         else:
            m "What a shame… I thought you would be different."
         "Then, suddenly, they launch at you with a speed you never would’ve suspected. As he flies towards you, Mothman rips off the trench coat and hat revealing his bug-like body and large wings."
         scene glass with fade
         "He grabs hold of you before dashing to the window and launching through it. Glass showers the deck as he takes flight with you in tow."
         scene sky with fade
         show Moth angry
         if garble == True:
            m "I̵̳̱͊͜ ̵̳͚̆͜ť̷͙̲̬̏͆h̷͈͇̓o̵̜͉̳̍͑͘ǘ̸̡͆ḡ̸̯͂͝ḩ̴̰̭͂̋t̵̯̼͠ ̶͓̆͂͘ẗ̷͈̱͌̓͜ǫ̷̗̣̂̃͘n̴̬̽̅į̶̐g̶̟̪͂̀h̷̡̦̦̔t̶͔̠̬̾̋ ̶̗͈̰̌ẅ̴̳ͅo̴͎̣̅͘ṳ̷̾̈́̊ĺ̶̙͗d̴̗̃̀ ̶͕͋͋̔e̷̬̳̜̊̈́̆n̷̠̋d̶̹͙͛͊ ̷̦̾d̴̛̦̂͘ị̷̭̋̽͛f̸̛̩̊̾f̶̢͙̜͆̈́̕ȩ̸̙̍͊ř̵̬̠͛͊ẹ̸̍̎͘ͅn̸͉̿̈́ẗ̸͔͉ḻ̵̤͖̎͛y̶̠̾͑ ̷͓̉a̸̠̓͊̏f̷̲̃t̶͇̗̹͠ë̴͔̥̓r̵̺͜͝ͅ ̷̘̭͉́͊̎I̴̻̘̊ ̸̠͐͒̆s̵͉̭̮̀ť̸̫͂a̸̭͂̏̿r̵̼̹̍͘t̴̰́̿̚e̵̘̦̗͑̀d̸̜̜̀͊̇ ̸͍͉̙̊͛t̵̜̏͘a̸̤͛̍̎l̷̪̦̹̈́k̷͔͐i̵͙̬͒̈ṅ̴̰̿g̸̣̟̦͋̕͝ ̸̳͎͗̕ţ̴̤̈͐o̸͔͋̿͝ ̶͙͆͜y̶̰̏̉o̸̗͇͔͛͠u̵̟̱̣̽̓̈́.̷̩͎̙̐ ̶͖͆̈͊B̵͎̠͝u̵̦̓t̷̫͈̹́̀͊ ̸̙͌̓̔y̶̺̑̐͂o̶̳̱̐̇̌ư̴͚̳̠ ̴̻͑a̸͖͐r̵̢̈́e̶̮͆ ̶̭̌̕j̸͔̰̓͋û̷̧̨͒͒͜s̴̮̈̂͜t̶̪͐ ̷̨͇͎̉͆̌l̴͕͗͊i̶̛͕͘͝ḱ̶̘̲̾̾è̷̞̍̑ ̶͍̗̂̀t̷̪̉h̶̤̝͈̍̔e̵͕̹̾̀ ̷̖̈́͒r̸̦̖̞͋̿ē̷̫̠̆̌ͅs̸̬̪̈́t̵̰̋̐.̷̻̬̊͠"
         else:
            m "I thought tonight would end differently after I started talking to you. But you are just like the rest."
         pc "Wh-"
         pc "What is going on? What did I do?"
         show Moth bad
         if garble == True:
            m "Y̷͛͑̚ͅö̶̱́͘ṵ̶̙̊́ ̷̻̿ś̸̹̹͘h̸̼̗̾̄̚ù̷̙̈́n̴̠͊̀̓n̸̞̥̫̎͝e̸̠͔͑͝d̵̗͖̽ ̴̛̼̓́m̸͇̤̕͜e̴̖̿̚͝ ̶̻͈̐̋̌l̸͎̮͛̕͝i̸̧̛̚͝ǩ̶̥̔́ę̷̬͙̀̌͌ ̸̩̔͌t̶͖͐̈́͝h̷͙̖͈̀e̸̢̠̩͆̓ ̷̼̞̈́̋r̷͇̹͑̅͝e̸̙̲̒̅ś̴͓̘̾t̸̙̔̃͛͜ ̸̢̛̜̊͑ȯ̷̜̮̓̈́f̶̔̀ͅ ̵͓̰̣̉̑̕ĥ̵͈͊̈u̵͔̺̞̔́m̵̤̀̉a̸̜̍̂n̷͔͛i̷͚̠̿t̵̺̥̦́y̶͔̿.̷͚̻̖̅̎͝ ̵͚̋̓̈́B̶͖̐͘u̶̜͕̖̓̈́t̴̻͌͛̕ ̵̭̝̏͂͝a̴̢̧̲̓͛͛t̴̖̟̜͆̂͛ ̴̺̌ͅt̶̥̦͌h̴̪͍̎̈́͒͜e̴̦͆ ̷͙͘͠ͅv̶̩̝̄̎̈́e̸̩͔̻̕͠r̷̩͔̃̚͝y̷͉͌̓̊ ̸̣̊l̸̡̛͆ë̵̫̜͍́ȁ̶̝̮̍̀͜ṡ̸̡̺̯ṯ̷͗ ̵̝̇̒͠Ǐ̸̩̓ ̸͙̽̎w̴͖̅o̵̜͗̒̑n̴͎͇̠̂͠͝’̵̭̦͝t̸͙̯͈̓̃͝ ̶͔̓̚g̷̟̻̾̊̓o̴̜͇͉͝ ̶͕̽͂ḥ̴̈̐̂ͅu̴̝̮͎͊͐̉ṇ̵̥̟̿g̵̹̼͐̄̿ṛ̷̖̑̈y̵̧̫̼͊̀͘ ̵̢̞̟̋̀ť̸͉͚̹͒͒õ̶̹̉ņ̵͚̲̌́i̷̡̪̋g̶̘̎́̏h̷̨̲̖͐̅ţ̸̓̆!̸̛̝͓̑"
         else:
            m "You shunned me like the rest of humanity. But at the very least I won’t go hungry tonight!"
         scene black with fade
         "With that Mothman flew you to his lair. He’s not exactly the cleanest eater, so your death was pretty gruesome. But we can skip all the icky, squishy bits."
         # WORST END
         jump credits

# Chadmir
label chadmir:
   play music chad
   "The guy dressed as a vampire seems pretty chill. Maybe he ran out of time to finish his costume – he’s partially dressed as a vampire, and partially just as… a bro? His cape looks pretty authentic though, and he has some killer fake fangs."
   "He’s standing all by himself, just kind of swaying to the music. Everyone else is giving him a pretty wide berth - there’s at least a 5 foot space around him on any side. He seems harmless, though, and super relaxed."
   "You decide to go talk to him."
   show Chad base with dissolve
   c "S\’up, dude?"
   pc "Hi."
   c "Oh, is it okay if I call you dude?"
   menu:
      "That’s fine!":
         $ dude = True
         c "Okay, dude. Sick."
      "Actually, I’d rather you didn’t.":
         $ dude = False
         c "Oh, sorry!"
   c " I’m Chadimir, but you can just call me Chad. It’s all chilllll."
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
         show Chad blush
         c "Oh heyyy, thanks."
      "Well your costume seems a little… confused?":
         c "Ah, I just couldn’t pull everything together in time. It suuuucks."  
   show Chad base
   c "I just borrowed some of this stuff from my new friend Drake. Hey, do you know Drake? Drake Ula?"
   pc "No, sorry."
   c "Ah, that’s a bummer. He’s a pretty chillll guy."
   pc "You seem like you’re having a good time."
   c "Oh, yeahhh. I’m just really excited to be here. I can’t believe I got invited."
   menu:
      "Well, who wouldn't want a guy like you at their party?":
         show Chad blush
         c "Heh. That’s nice.. I mean… some people might not…"
      "Yeah, you do seem kind of out of place.":
         c "Ohhhh. Well, y’know, I only know a couple people here."
   show Chad sad
   c "It’s just hard for a guy like me to go anywhere without someone asking me, y’know?"
   pc "Oh. Do you have anxiety?"
   show Chad base
   if dude == True:
      c " Nahhhh, I’m chill, bro. I just don’t like going anywhere without being invited."
   else:
      c " Nahhhh, I’m chill, [user]. I just don’t like going anywhere without being invited."
   menu:
      "Oh, well that’s very considerate of you.":
         show Chad blush
         c "Yeah. Well, y’know, I kind of have to be, but uh, thanks."
      "Huh. You’re not very confident, are you? ":
         c "Heyyyy, man. You don’t need to judge."
   show Chad base
   c "Anyways. What brings you to this fiiine abode?"
   menu:
      "I’m definitely looking for a little adventure. Maybe I’ll meet someone tonight…":
         pass
      "I just wanted to check out the party.":
         pass
      "I mostly came to look at the costumes. Everyone just looks so silly.":
         jump cWorst
   c "Heyyyy, that’s the spirit. You never know what might happen."
   show Chad blush
   c "I’m kinda hoping that maybe I’ll meet someone too… "
   menu:
      "Well, you did meet me.":
         c "I guess I did. You’re pretty awesome."
      "The night is young. Maybe you still will.":
         show Chad base
         c "Yeah, maybe. Doesn’t seem like there’s many contenders though."
   show Chad base
   c "You wanna go check out the food?"
   pc "Sure."
   scene table with fade
   "You walk over to the food table together. It’s covered in all kinds of delicious-looking snacks."
   show Chad base with dissolve
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
   show Chad blush
   c "Oh, wooow. I appreciate that. You’re reallyyyy nice, y’know?"
   pc "Thanks. You are too."
   show Chad base
   c "Aw."
   c "Welllll, not everyone agrees with you though."
   pc "Oh no! Why?"
   show Chad sad
   c "I, uh, recently went through a big life change. It’s kinda affected everything… my diet, my sleep schedule, even, like the places I can hang out…"
   c "Some of my friends just haven’t been very supportive while I’m, y’know, figuring stuff out."
   show Chad base
   c "That’s why I was so excited that I got invited to come here."
   pc "Well, sounds like they’re not such good friends then."
   show Chad sad
   c "I guess not."
   pc "Well, I’m glad we got to spend this time together."
   show Chad blush
   c "Me too."
   show Chad base
   c "Hey, [user]. Can I tell you a secret?" 
   pc "..."
   pc "What kind of secret?"
   c "It’s a biiiig deal. I haven’t really told anybody other than Drake. "
   pc "Wow. Well, you can tell me if you want."
   show Chad blush
   c "Okay. Wooow, this is hard."
   "Chad takes a deep breath, preparing himself to tell you the secret. He leans in to whisper in your ear."
   show Chad base
   c "I’m not just dressed up as a vampire. "
   c "..."
   c " I actually… am a vampire."
   pc "..."
   pc "Ha, great Halloween prank. "
   show Chad sad
   c "..."
   pc "C’mon Chad, I’m not that gullible."
   "Chad shakes his head at you. He’s still standing pretty close… close enough that you can see how truly real those fangs look."
   c "It’s not a prank, bro."
   pc "You’re… what?"
   pc "No way. I can’t believe it."
   "But you see the intense look in his bright red eyes, and you think back to all the things he’s told you over the course of the party… could it be true?"
   show Chad base
   c "It’ll help if you say it. Say it out loud."
   pc "..."
   pc "You’re a vampire!"
   "You’re trying really hard not to freak out in the middle of this room full of people. Chad… is a vampire. A blood sucking, undead vampire who sleeps in a coffin. Maybe."
   "It’s a lot to process. But Chad is still just standing there with you, not judging as you try not to panic."
   c "I know it’s a lot to take in."
   pc "Yeah…"
   c "But I promise I’d never hurt you."
   show Chad blush
   c "Actually…"
   pc "What?"
   c "I was going to ask if you wanted to get out of here."
   pc "..."
   pc "Get out of here? Like, together?"
   show Chad base
   c "Yeahhh… I mean, if you’re down?"
   show Chad blush
   c "You’re the nicest person I’ve met all night, and you haven’t freaked out about my, uh, new life changes."
   if dude == True:
      c "I want to get to know you. And I promise not to suck your blood, dude."
   if dude == False:
      c "I want to get to know you. And I promise not to suck your blood, [user]."
   "You gulp. It sounds a little scary… but looking up at the dumb face, with those muscles and how kind he’s been... you can’t deny that Chad would be a good guy to have around."
   pc "Alright. Let’s get out of here."
   scene black with fade
   "He reaches out to take your hand as you walk out of the party together, and you have a feeling that this Halloween is going to be the best one yet. After all, even if he is a vampire, he’s the nicest himbo you’ve ever met."
   "YOU AND CHAD HAD A LOVELY GARLIC-FREE  DINNER TOGETHER"
   "THE END"
   # ENDING
   jump credits





label cBad:
   show Chad sad
   c "Alright."
   show Chad base
   c "Heyyy, I think I’m gonna go see if I can find my guy Drake."
   pc "Oh, you’re leaving? "
   c "Yeahhh. Sorry, [user], maybe I’ll see you around."
   scene black with fade
   "And with that, Chad turns and disappears into the crowd. You’re left with the lingering sense that there was something… different about him, but now you’ll never be able to figure it out."
   # ENDING
   jump credits
   
label cWorst:
   show Chad mad
   if dude == True:
      c "Heyyyy, dude. I think everyone looks great."
   else:
      c "Heyyyy, [user]. I think everyone looks great."
   show Chad base
   c "Do you not like dressing up for Halloween?"
   menu:
      "I guess I’m just not feeling it right now.":
         jump cBad
      "I do. I just feel like all these ones are stupid and tacky.":
         show Chad mad
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
   scene black with fade
   "Chad comes right up to you, so close that you start to go cross-eyed looking into his vivid eyes. You can see how sharp the fangs he has are, smell the waft of something metallic coming off of him."
   "Then he lunges forward and there’s a sharp pinch at your neck, and slowly... the world fades to black."
   # ENDING
   "YOU HAVE DIED FROM PISSING OFF CHAD"
   jump credits



   

label credits:
   play music credits 
   image cred = Text(credits_s, text_align=0.5)
   image theend = Text("{size=80}The End", text_align=0.5)
   image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5)
   scene credit_bg with fade

   $ credits_speed = 25
   show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
   show theend:
      yanchor 0.5 ypos 0.5
      xanchor 0.5 xpos 0.5
   with dissolve
   with Pause(1.5)
   hide theend


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
