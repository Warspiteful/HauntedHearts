label ghost:
   play music echo
   $ notify_music()
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
