label franky:
   play music franky
   $ notify_music()
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
