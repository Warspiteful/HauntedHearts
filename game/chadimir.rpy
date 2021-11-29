# Chadmir
label chadmir:
   play music chad
   $ notify_music()
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
