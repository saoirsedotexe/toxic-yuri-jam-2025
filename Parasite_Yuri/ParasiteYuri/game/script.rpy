# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character(None, what_prefix="{i}", what_suffix="{/i}")

define l = Character("Langston", color="#5dc0d5")

define w = Character("Turner", color="#d95723")

define s = Character("Sutton", color="#c9a3f1")

define k = Character("Knight", color="#98cb83")

define f = Character("Captain", color="#dee46d")

define p = Character("Parasite")

default vitals = False
default scans = False

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "cell.png" or "cell.jpg") to the
    # images directory to show it.

    $ say_style = "Interrogation" #Cutscene or Interrogation

    scene introdream

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "wife.png" to the images
    # directory.

    #show love bullet 1
    
    n "You are home."
    n "You are finally home."
    n "The carpet beneath your feet. {w}The soft of your own bed. {w}The quiet. The quiet."
    n "You are home."
    n "Something drips on your shoulder."
    n "You look up. The ceiling beams have started to melt."
    n "The door oozes. {w}The shelves go concave. {w}The bed splits."
    n "Fire eats at the foundation."
    n "You clutch the infrastructure in place. It comes through your fingers like candle wax. But you stand firm."
    n "What’s left of the house forms a hollow around you. You keep the mantle from toppling in. You force the engravings to hold their shape."
    n "You carry the weight."
    n "Something beeps."
    
    #[TRANSITION TO BEDROOM]
    $ say_style = "Cutscene" #Cutscene or Interrogation
    
    scene act1bedroom
    
    n "And then you wake up. Your pager trills."
    s "Langston."
    s "We need you at the bridge."
    s "Something’s wrong."
    n "You hear your heartbeat in your ears. Static dances over your skin, like a holdover from pins and needles. There’s a weight in your gut."
    n "You take a deep breath, forcing it to pass."
    l "Alright."
    l "I’m on my way."
    n "You get out of bed."
    
    #[TRANSITION TO BRIDGE]
    
    scene act1bridge
    
    n "By the time you arrive at the bridge, the COMMS OFFICER stands hunched over his control deck with his hands pressed to both sides of his headset. The ship’s engineer works hard at something on the ship’s panel, only to turn back to the COMMS OFFICER, and shake his head."
    show CommOfficer
    n "The COMMS OFFICER taps on his microphone."
    s "Captain, do you read me? THE ECOLOGIST. THE NAVIGATOR. Do you read?"
    l "Have we lost signal?"
    n "He glances over his shoulder at you. His brows crease together."
    s "It’s no use. Nothing’s getting through."
    l "What’s the last thing you heard?"
    s "THE ECOLOGIST mentioned wanting to get some further samples from Site C. We confirmed with the schedule, THE NAVIGATOR led them back, then… nothing."
    n "You turn to the ship’s sonar. Each of the payload sites have their own red dot. Another blinking dot represents the party. They’re hovering near the outside of the C dot."
    l "Has Site C ever been a problem before?"
    s "No. Never. We have a transmitter between it and Site D."
    l "How long has it been?"
    s "Fifteen minutes."
    n "You take a deep breath. You stare outside the viewport as if by some miracle, she’ll appear."
    n "She doesn’t."
    l "We need to get out there then. Who else can go?"
    s "They still have time. Protocol is thirty."
    l "Are you joking? Someone needs to go find them — now."
    s "I don’t like it anymore than you do, Langston, but we don’t have a choice. Until it’s a qualifiable emergency, we’d put everyone at risk."
    l "This is ridiculous. This isn’t an emergency to you?"
    n "He gives you a long, hard look."
    s "They’re my friends too, Doctor."
    l "It’s just just friends out there."
    n "Something crackles from his headset. His eyes widen, you jerk upward. He switches the transmitter so you both can hear."
    f "— back — ship —"
    s "Captain? Captain, do you read?"
    f "COMMS OFFICER. Something — down. We need —"
    n "A screech crackles over the transmitter. Followed by something visceral and wet."
    s "Captain? Captain!"
    l "NAVIGATOR? Are you there?"
    n "There’s a rustling on the other end. Like the receiver’s being dragged through dirt. Until suddenly it cuts out. Replaced by heavy breathing."
    w "Mayday, mayday, do you read me?"
    n "You let out a breath you didn’t know you were holding. Your nails bite into your palms. You brush past COMMS OFFICER to lean out the viewport."
    s "NAVIGATOR what’s going on?"
    w "There’s something — It got them. And — coming back."
    n "There’s a jostling of clothing and gear. She’s running."
    s "What do you mean it got them? NAVIGATOR?"
    l "Just come back. Just make it back."
    w "I’m coming."
    n "COMMS OFFICER gives you a look, before diverting his attention back."
    s "NAVIGATOR —"
    w "They’re gone."
    n "COMMS OFFICER’s shoulders collapse. There’s a gentle shake to his hands."
    w "Start the ship!"
    n "The engineer breaks from his trance and moves to the control panel. They wait for the COMMS OFFICER’s orders."
    l "What are you doing?"
    s "I need to think."
    n "THE NAVIGATOR bursts from the treeline outside the viewport."
    l "We don’t have time!"
    s "The Captain —"
    l "— The Captain’s dead. You have to decide."
    n "He hesitates. THE NAVIGATOR comes closer and closer, checking over her shoulder. He squints at her from afar."
    s "Where’s her helmet?"
    l "Start the ship!"
    w "COMMS OFFICER!"
    s "Wait."
    n "From the treeline. Someone else. THE NAVIGATOR turns to look."
    w "ECOLOGIST!"
    n "As ECOLOGIST approaches, they start waving their arms at the ship. Their voice shouts into the NAVIGATOR’S distant receiver."
    k "STOP! STOP!"
    
    scene act1quarantine
    
    n "You stare at the monitors before you. Her various charts fluctuate with every breath, every heartbeat, every muscle twitch. Meanwhile, she sits on the floor, chin on her knees, staring at the ground."
    show wife_base
    n "Your heart clenches."
    n "COMMS OFFICER walks up behind you. His gaze is solemn. It looks like he hasn’t slept since the funeral."
    s "I hope you know what you’re doing."
    l "I do."
    s "You know her best, after all."
    n "He sighs. Then he leaves you with her."
    label checks1:
        menu:
            "> CHECK VITALS":
                n "The feed from her wristband monitor seems normal. No elevated pulse, no abnormal rhythm. It’s as if nothing’s changed at all."
                $ vitals = True
                if vitals == True and scans == True:
                    jump act1
                else:
                    jump checks1
                
            "> CHECK SCANS":
                n "You sort between thermal scans, electrical scans, and internal scans of her body. Nothing out of place."
                $ scans = True
                if vitals == True and scans == True:
                    jump act1
                else:
                    jump checks1

    # These display lines of dialogue.
    
    scene act1
    label act1:
    
    scene act2bedroom
    label act2:
    # [TRANSITION TO BEDROOM]
    
    n "The centrifuge spins and spins and spins. You watch it absentmindedly from your desk chair. This is its third cycle. Your leg bounces beneath your desk."
    n "You rip yourself from the distraction and refocus on your microscope. You adjust the dials, but your vision’s still blurry. Lack of sleep. You push your glasses up to rub your corneas into shape."
    n "The samples beneath the glass still don’t make any sense to you. Nothing’s wrong with them, of course. But there’s just an oddness about them. You think your eyes are tricking you into seeing things that aren’t there, like looking at the walls of a thunderstorm and swearing you can see it spinning into a twister."
    n "You reach across for your desk for the research notes written by your predecessor concerning this planet and its hazards. You flip through the pages looking for… you’re not even sure, at this point. Anything to rule out your worst fears."
    n "Your eye falls onto a subsection written about some sort of creature. Prehensile tendrils, skin secretions, known to be aggressive. You lean in to read more, but there’s a knock at your door."
    #show knight sprite with cast
    k "I hope you don’t mind me stopping by. But it’s not like you’ve been by the infirmary much."
    n "They’re still bandaged up from the attack. Their arm had to be put into a cast. Their lips purse at you."
    l "You should be resting."
    k "Pretty hard to rest when you feel like something might jump out and murder you at any moment."
    n "You turn back to your work. They walk in from behind you anyway."
    k "We should have followed protocol. No one should be exempt from that. Regardless of who they are."
    l "We would have let you in just the same. You can’t pretend that you would have wanted to stay there."
    k "If I had, you would’ve known something was wrong. It’s my job to know what’s out there. It’s yours to take care of us when it’s over. It wasn’t your call to make."
    n "You’re tired of this. You want to get back to your work."
    l "Perhaps the difference between my job and yours is caring for people first."
    k "I’m thinking about the crew. I can't help but think you’ve got something else on your mind."
    n "Before you can snap at her, she levels you with a look."
    k "You weren’t there, Langston. You didn’t see what I saw."
    l "What did you see?"
    k "There’s no way she could have gotten away from that thing in one piece. I saw what it did to the Captain. I saw how it… grabbed her."
    k "I thought she was dead because she should have been."
    k "Maybe her helmet fell off. Maybe not."
    k "But I need to know you’re going to be able to do what needs to be done when you find out."
    k "I need to know your marital problems aren’t going to get me killed."
    l "…"
    l "You don’t—"
    n "The lights cut out, suddenly. An emergency alarm shrieks out from the ship’s speakers. You wince at the sudden strobe lights, shielding your eyes."
    n "Knight’s eyes are filled with horror."
    l "Shit."
    n "You take off running."
    
    scene act2desk
    
    n "The feed of the quarantine hatch is clouded over with decontamination fog. Hands shaking, you remotely turn on a fan to filter it out."
    n "As the haze clears, Turner sits squarely in the center of the room, next to a piece of wall panel. Frayed wires and inner piping now sit exposed in a small rectangle."
    n "You press the monitor’s transmitter to the ship’s bridge."
    n "We’re all good. Everything’s under control."
    s "What happened?"
    n "You take a deep breath."
    l "Nothing. Part of the wall fell off."
    s "Are you sure?"
    l "I’m sure."
    s "Alright. Copy."
    n "You turn off the transmitter and immediately click open the startup prompt."
    
    label act2questioning:
        menu:
            "> WHAT HAPPENED?\n> WHAT DID YOU DO?"
                w "I just… panicked. I feel suffocated. I can’t stay here."

LANGSTON: Don’t you understand the position I’m in? People already don’t trust us. This is only going to make things worse.

TURNER: You don’t understand what it’s like. You don’t know how alone I feel. What else am I supposed to do?

LANGSTON: You think I don’t know what loneliness feels like?

TURNER: It isn’t the same. 
TURNER: You chose the life you had. You stayed because you wanted to.
TURNER: None of this was my choice.

LANGSTON: But coming here was. Leaving home, for who knows how long, putting yourself in harm’s way.
LANGSTON: If it wasn’t for me, you’d be stuck planetside. At least you have assured safety here.
LANGSTON: Just so long as the others don’t think something’s wrong.

TURNER: …
TURNER: Do you think something’s wrong?

LANGSTON: Let’s begin the questioning.

> DESCRIBE WHAT HAPPENED AT SITE C.
> WHAT HAPPENED TO YOUR HELMET?

TURNER: You already asked me this.

LANGSTON: Tell me again.

TURNER: … Okay.
TURNER: We were attacked. The Captain was killed and dropped our equipment. KNIGHT managed to grab some of it and get away. It grabbed me, but I fought it and wriggled away. My helmet went off with it.
TURNER: I was trying to come home to you.

LANGSTON: After everything that had happened that morning, you were really thinking of me?

TURNER: We’ve fought before. 

LANGSTON: It wasn’t like before.

TURNER: Why are you doing this? I don’t know what you want, Alice. 

LANGSTON: I want to make things work.

She stares at the camera, at a loss. She tries to say something, but thinks better of it. Her teeth lock together.

TURNER: We/I have to get out of this first.
TURNER: Keep asking your questions.

> HAS YOUR CONDITION CHANGED SINCE WE LAST SPOKE?

TURNER: No.
TURNER: I feel the same.

> WHAT DO YOU DO WHEN I’M NOT HERE?

TURNER: What is there to do?
TURNER: Stare at the wall. Count the wall tiles. Minus one, now.
TURNER: ((I used to braid my hair.))
TURNER: I mostly just think. 

> HAVE YOU EXPERIENCED ANY OTHER EMOTIONAL ABNORMALITIES?

TURNER: What do you think?
TURNER: I’m trying to keep it together. I am.
TURNER: But this is just…
TURNER: I don’t even know how long it’s been.

> WHAT DO YOU THINK ABOUT?

TURNER: You.
TURNER: But also… the crew. 
TURNER: What might happen if something is wrong. 
TURNER: What I could’ve done differently. 

> DO YOU FEEL LIKE YOURSELF?

TURNER: Not in the way you mean.
TURNER: I’m me. I know I’m me.
TURNER: But at the end of this, I don’t know if I’ll be the same person that I was before. 

> WHAT COULD YOU HAVE DONE DIFFERENTLY?

TURNER: I keep running through what happened. It’s on playback. Over and over again.
TURNER: Maybe if I didn’t hesitate. If I just ran from it.
TURNER: But when the Captain tried to step in front of us, I froze. I didn’t want to leave them behind.
TURNER: Is it better to flee for your own sake? Or fight even when hope is lost?
TURNER: What do you think?

> 

> 

> WERE YOU INTENDING TO ESCAPE?

TURNER: I guess it’s about time we get to the point.
TURNER: Could I have gotten very far, realistically?
TURNER: I don’t know.
TURNER: I guess the answer to your question is yes. Even if, subconsciously, I knew better.
TURNER: I just don’t want to be here anymore.

> WHAT IF SOMEONE SAW YOU?

TURNER: Saw what?
TURNER: Oh. This.
TURNER: I didn’t think the alarm would trigger, for one thing.
TURNER: But even if it did, I knew you’d be the only one to see it.
TURNER: I’m in your care, after all.

All of a sudden, she stares into the camera for a moment. You get goosebumps.

TURNER: Can I ask you something?

You open your mouth to speak, then close it. You glance at the procedures listed on your monitor.

She tilts her head.

TURNER: Are you there?

> YES

TURNER: You said before you just want to make things work.
TURNER: What if it’s too late?

LANGSTON: I don’t follow.

TURNER: I think you do.
TURNER: How long has the writing been on the wall? I’m willing to accept that. It’s just you.
TURNER: And then you do this. 
TURNER: Maybe you think I don’t understand what’s happening. But it’s all crystal clear to me.
TURNER: What if it doesn’t work? What if it’s the last straw?

LANGSTON: …
LANGSTON: Don’t say that.
LANGSTON: It won’t be.
LANGSTON: I can keep it together.

She sits, frozen. But the facade cracks. She gives you a soft smile. She almost even laughs.

TURNER: I’ll keep waiting for you to see it, then.
TURNER: That’s all.

> NO

TURNER: This has to be mutual, you know.
TURNER: I want to trust you. I’m forced to trust you. 
TURNER: But if you want me to just be a lab rat you prod at, fine.
TURNER: I guess you finally have me where you want me.


You’re getting lightheaded. All of this is becoming too much. You hover your cursor back over the contamination protocols.

You’re presented with new options and accompanying instructions.

> SPINAL TAP

In this procedure, a needle is inserted in between the two lumbar bones to collect a sample of cerebrospinal fluid. A cerebrospinal fluid analysis can detect infection, inflammation in the nervous system, and various neurological conditions. 

Approximately 25% of subjects experience a post-lumbar puncture headache, which can result in nausea, vomiting, dizziness, and migraine, all of which are often resolved by idleness and laying down.

> SPINAL TAP

Do you want to proceed?

> YES
> NO

The wall struggles with the missing panel, but still manages to kick into motion. She jerks towards it, watching the arms form.

TURNER: What are you doing?

LANGSTON: …

She stands, backing towards the wall. Two of the panels behind her shove her forward, closer to the bed. Corralling her.

TURNER: Make it stop.

LANGSTON: It would be easier if you just laid down.

She shuffles forward. Then, in the corner of her eye, the discarded bit of wall she tore off. She grabs it, holding it defensively over her shoulder. 

She swings. The panels react in kind, bucking back. One catches her off guard, however, shoving her backward. She cries out and they move in, cornering and cornering her until she’s forced onto the bed. One of the panels pins her down. The other shifts, until an arm with a needle reveals itself.

TURNER: ALICE!

LANGSTON: Whatever it takes.

You bite your cheek as you watch it happen. The injection, the jump of her skin, the submission. Your knuckles go white against the surface of your desk. Your eyes burn.

She relaxes, finally. The arms recede. You taste blood.

> INSERT PROBE

A microscopic camera would be inserted into the subject’s bloodstream via needle to monitor their organs from the inside. The camera will then establish transmitters within the body which will then trigger an alert when disturbed. The transmitter is capable of picking up on infection, inflammation, parasites, and other foreign bodies. 

The transmitters and camera can only be removed via surgical procedure.

> INSERT PROBE

Do you want to proceed?

> YES
> NO

The wall struggles with the missing panel, but still manages to kick into motion. She jerks towards it, watching the arms form.

TURNER: What are you doing?

LANGSTON: It’s just an injection.

She seems to loosen, some. The arm with the needle approaches her, looming over her. She stares at it warily. 

LANGSTON: What if I don’t want to see it?

She doesn’t take her eye off the needle. But you can see her thinking.

She shrugs. She lays her arm out for ease of access.

TURNER: Then don’t.
TURNER: It’s your life, Langston. Do with it what you will.

The needle comes down. She doesn’t wince. She doesn’t move at all.

TURNER: But I think things would be a lot easier for you if you were willing to accept it.
TURNER: Things change. People change.
TURNER: If you don’t change with them, what’s going to be left of you?
TURNER: I don’t think you’d be very happy that way.

The arm recedes. Blood bubbles at the injection site. She smears it down her skin.

She smiles.

TURNER: Just think about it.

You feel a surge of cold. 

You intend to.


    # l "I'm doctor misery. She needs medicine drug to live."

    # w "I would like medicine drug."

    # p "If you don't give her medicine drug I'll suck you silly"

    # show stickfigure

    # s "I too am in this episode"

    # show stickfigure sad

    # s "I am sad now"

    call screen buttons()

    return

# Two separate routes: one where you get with the parasite and things are awesome 
# and the other where you don't get with the parasite and the parasite kills everyone

# Test choice: Medicine drug or no medicine drug

# Tutorial template code

screen buttons():
    add "bg.png"
    hbox:
        imagebutton auto "images/medicine_%s.png" action Jump("medicine")

        imagebutton auto "images/no-medicine_%s.png" action Jump("no_medicine") 

            

 

    # This ends the game.
