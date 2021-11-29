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
   $ notify_music()
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
