label mothman:
   play music moth
   $ notify_music()
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
