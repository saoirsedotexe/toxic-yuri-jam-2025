default vitals = False
default scans = False
default haircut = "long"
default surgery_deny = False
default oxygen_deny = False
default meat = 0
default candy = 0

label start:

    $ say_style = "Interrogation"

    scene space with fade:
        size(1920, 1080)
    
    l "…"
    l "…"
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
    
    $ say_style = "Cutscene"
    
    scene bedroom_dark with fade:
        size(1920, 1080)
    
    n "And then you wake up. Your pager trills."
    s "Langston."
    s "We need you at the bridge."
    s "Something’s wrong."
    n "You hear your heartbeat in your ears. Static dances over your skin, like a holdover from pins and needles. There’s a weight in your gut."
    n "You take a deep breath, forcing it to pass."
    l "Alright."
    l "I’m on my way."
    n "You get out of bed."
    
    scene bridge_grounded with fade:
        size(1920, 1080)
    
    n "By the time you arrive at the bridge, the COMMS OFFICER stands hunched over his control deck with his hands pressed to both sides of his headset. The ship’s engineer works hard at something on the ship’s panel, only to turn back to the COMMS OFFICER, and shake his head."
    show comms_officer with dissolve
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
    
    scene quarantine_room_v2 with irisin:
        size(1920, 1080)
    
    n "You stare at the monitors before you. Her various charts fluctuate with every breath, every heartbeat, every muscle twitch. Meanwhile, she sits on the floor, chin on her knees, staring at the ground."
    show wife normal at interrogation with dissolve
    # show screen airlockbutton
    n "Your heart clenches."
    n "COMMS OFFICER walks up behind you. His gaze is solemn. It looks like he hasn’t slept since the funeral."
    s "I hope you know what you’re doing."
    l "I do."
    s "You know her best, after all."
    n "He sighs. Then he leaves you with her."
    $ say_style = "Interrogation"
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
    
    # q1 name is meat title is candy
    # q2 state of mission candy what is assignment meat
    # q3 feeling meat experienced unusual candy
    # q4 describe incident meat helmet candy
    # q5 sorry meat gone candy
    # q6 talk about that morning meat other choice is candy
    # q7 epidermal candy blood meat
    
    scene act1
    label act1:
    
    scene bedroom_light_mode with irisin:
        size(1920, 1080)
    label act2:
    
    $ say_style = "Cutscene"
    n "The centrifuge spins and spins and spins. You watch it absentmindedly from your desk chair. This is its third cycle. Your leg bounces beneath your desk."
    n "You rip yourself from the distraction and refocus on your microscope. You adjust the dials, but your vision’s still blurry. Lack of sleep. You push your glasses up to rub your corneas into shape."
    n "The samples beneath the glass still don’t make any sense to you. Nothing’s wrong with them, of course. But there’s just an oddness about them. You think your eyes are tricking you into seeing things that aren’t there, like looking at the walls of a thunderstorm and swearing you can see it spinning into a twister."
    n "You reach across for your desk for the research notes written by your predecessor concerning this planet and its hazards. You flip through the pages looking for… you’re not even sure, at this point. Anything to rule out your worst fears."
    n "Your eye falls onto a subsection written about some sort of creature. Prehensile tendrils, skin secretions, known to be aggressive. You lean in to read more, but there’s a knock at your door."
    show ecologist_cast with dissolve
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
    
    scene desk with irisin:
        size(1920, 1080)
    n "The feed of the quarantine hatch is clouded over with decontamination fog. Hands shaking, you remotely turn on a fan to filter it out."
    n "As the haze clears, Turner sits squarely in the center of the room, next to a piece of wall panel. Frayed wires and inner piping now sit exposed in a small rectangle."
    n "You press the monitor’s transmitter to the ship’s bridge."
    n "We’re all good. Everything’s under control."
    show comms_officer with dissolve:
        xalign 0.2
    s "What happened?"
    n "You take a deep breath."
    l "Nothing. Part of the wall fell off."
    s "Are you sure?"
    l "I’m sure."
    s "Alright. Copy."
    hide comms_officer with dissolve
    n "You turn off the transmitter and immediately click open the startup prompt."
    show quarantine_room_v2 with fade:
        size(1920, 1080)
    show wifeside at interrogation with dissolve
    
    $ say_style = "Interrogation"
    label act2question1:
        menu:
            "> WHAT HAPPENED?":
                w "I just… panicked. I feel suffocated. I can’t stay here."
                w "Don’t you understand the position I’m in? People already don’t trust us. This is only going to make things worse."
                w "You don’t understand what it’s like. You don’t know how alone I feel. What else am I supposed to do?"
                l "You think I don’t know what loneliness feels like?"
                w "It isn’t the same." 
                w "You chose the life you had. You stayed because you wanted to."
                w "None of this was my choice."
                l "But coming here was. Leaving home, for who knows how long, putting yourself in harm’s way."
                l "If it wasn’t for me, you’d be stuck planetside. At least you have assured safety here."
                l "Just so long as the others don’t think something’s wrong."
                w "…"
                w "Do you think something’s wrong?"
                l "Let’s begin the questioning."
                $ meat += 1
            "> WHAT DID YOU DO?":
                w "I just… panicked. I feel suffocated. I can’t stay here."
                w "Don’t you understand the position I’m in? People already don’t trust us. This is only going to make things worse."
                w "You don’t understand what it’s like. You don’t know how alone I feel. What else am I supposed to do?"
                l "You think I don’t know what loneliness feels like?"
                w "It isn’t the same." 
                w "You chose the life you had. You stayed because you wanted to."
                w "None of this was my choice."
                l "But coming here was. Leaving home, for who knows how long, putting yourself in harm’s way."
                l "If it wasn’t for me, you’d be stuck planetside. At least you have assured safety here."
                l "Just so long as the others don’t think something’s wrong."
                w "…"
                w "Do you think something’s wrong?"
                l "Let’s begin the questioning."
                $ candy += 1
    label act2question2:
        menu:
            "> DESCRIBE WHAT HAPPENED AT SITE C.":
                w "You already asked me this."
                l "Tell me again."
                w "…Okay."
                hide wifeside
                show wife normal at interrogation with dissolve
                w "We were attacked. The Captain was killed and dropped our equipment. Knight managed to grab some of it and get away. It grabbed me, but I fought it and wriggled away. My helmet went off with it."
                show wife scared at interrogation with dissolve
                w "I was trying to come home to you."
                l "After everything that had happened that morning, you were really thinking of me?"
                show wife normal at interrogation with dissolve
                w "We’ve fought before."
                l "It wasn’t like before."
                w "Why are you doing this? I don’t know what you want, Alice."
                l "I want to make things work."
                n "She stares at the camera, at a loss. She tries to say something, but thinks better of it. Her teeth lock together."
                w "We have to get out of this first."
                w "Keep asking your questions."
                $ meat += 1
            "> WHAT HAPPENED TO YOUR HELMET?":
                w "You already asked me this."
                l "Tell me again."
                w "…Okay."
                hide wifeside
                show wife normal at interrogation with dissolve
                w "We were attacked. The Captain was killed and dropped our equipment. Knight managed to grab some of it and get away. It grabbed me, but I fought it and wriggled away. My helmet went off with it."
                show wife scared at interrogation with dissolve
                w "I was trying to come home to you."
                l "After everything that had happened that morning, you were really thinking of me?"
                show wife normal at interrogation with dissolve 
                w "We’ve fought before."
                l "It wasn’t like before."
                w "Why are you doing this? I don’t know what you want, Alice."
                l "I want to make things work."
                n "She stares at the camera, at a loss. She tries to say something, but thinks better of it. Her teeth lock together."
                w "We have to get out of this first."
                w "Keep asking your questions."
                $ candy += 1
    label act2question3:
        menu:
            "> HAS YOUR CONDITION CHANGED SINCE WE LAST SPOKE?":
                w "No."
                w "I feel the same."
                $ candy += 1
            "> WHAT DO YOU DO WHEN I’M NOT HERE?":
                w "What is there to do?"
                w "Stare at the wall. Count the wall tiles. Minus one, now."
                if haircut == "short":
                    w "I used to braid my hair."
                w "I mostly just think."
                $ meat += 1
    label act2question4:
        menu:
            "> HAVE YOU EXPERIENCED ANY OTHER EMOTIONAL ABNORMALITIES?":
                w "What do you think?"
                w "I’m trying to keep it together. I am."
                w "But this is just…"
                w "I don’t even know how long it’s been."
                $ candy += 1
            "> WHAT DO YOU THINK ABOUT?":
                w "You."
                w "But also… the crew."
                w "What might happen if something is wrong."
                w "What I could’ve done differently."
                $ meat += 1
    label act2question5:
        menu:
            "> DO YOU FEEL LIKE YOURSELF?":
                w "Not in the way you mean."
                w "I’m me. I know I’m me."
                w "But at the end of this, I don’t know if I’ll be the same person that I was before."
                $ candy += 1
            "> WHAT COULD YOU HAVE DONE DIFFERENTLY?":
                w "I keep running through what happened. It’s on playback. Over and over again."
                w "Maybe if I didn’t hesitate. If I just ran from it."
                w "But when the Captain tried to step in front of us, I froze. I didn’t want to leave them behind."
                w "Is it better to flee for your own sake? Or fight even when hope is lost?"
                w "What do you think?"
                $ meat += 1
    label act2question6:
        menu:
            "> WERE YOU INTENDING TO ESCAPE?":
                w "I guess it’s about time we get to the point."
                w "Could I have gotten very far, realistically?"
                w "I don’t know."
                w "I guess the answer to your question is yes. Even if, subconsciously, I knew better."
                w "I just don’t want to be here anymore."
                $ candy += 1
            "> WHAT IF SOMEONE SAW YOU?":
                w "Saw what?"
                w "Oh. This."
                w "I didn’t think the alarm would trigger, for one thing."
                w "But even if it did, I knew you’d be the only one to see it."
                w "I’m in your care, after all."
                $ meat += 1
    hide wifeside
    show wife normal at interrogation
    n "All of a sudden, she stares into the camera for a moment. You get goosebumps."
    w "Can I ask you something?"
    n "You open your mouth to speak, then close it. You glance at the procedures listed on your monitor."
    show wife disdain at interrogation with dissolve
    n "She tilts her head."
    w "Are you there?"
    label act2question7:
        menu:
            "> YES":
                w "You said before you just want to make things work."
                w "What if it’s too late?"
                l "I don’t follow."
                w "I think you do."
                w "How long has the writing been on the wall? I’m willing to accept that. It’s just you."
                w "And then you do this." 
                w "Maybe you think I don’t understand what’s happening. But it’s all crystal clear to me."
                w "What if it doesn’t work? What if it’s the last straw?"
                l "…"
                l "Don’t say that."
                l "It won’t be."
                l "I can keep it together."
                n "She sits, frozen. But the facade cracks. She gives you a soft smile. She almost even laughs."
                w "I’ll keep waiting for you to see it, then."
                w "That’s all."
                $ candy += 1
            "> NO":
                w "This has to be mutual, you know."
                w "I want to trust you. I’m forced to trust you."
                w "But if you want me to just be a lab rat you prod at, fine."
                w "I guess you finally have me where you want me."
                $ meat += 13
    show wife normal at interrogation with dissolve
    n "You’re getting lightheaded. All of this is becoming too much. You hover your cursor back over the contamination protocols."
    n "You’re presented with new options and accompanying instructions."
    label act2torture:
        menu:
            "> SPINAL TAP":
                n "In this procedure, a needle is inserted in between the two lumbar bones to collect a sample of cerebrospinal fluid. A cerebrospinal fluid analysis can detect infection, inflammation in the nervous system, and various neurological conditions."
                n "Approximately 25%% of subjects experience a post-lumbar puncture headache, which can result in nausea, vomiting, dizziness, and migraine, all of which are often resolved by idleness and laying down."
                n "Do you want to proceed?"
                menu:
                    "> YES":
                        n "The wall struggles with the missing panel, but still manages to kick into motion. She jerks towards it, watching the arms form."
                        w "What are you doing?"
                        l "…"
                        n "She stands, backing towards the wall. Two of the panels behind her shove her forward, closer to the bed. Corralling her."
                        w "Make it stop."
                        l "It would be easier if you just laid down."
                        n "She shuffles forward. Then, in the corner of her eye, the discarded bit of wall she tore off. She grabs it, holding it defensively over her shoulder."
                        n "She swings. The panels react in kind, bucking back. One catches her off guard, however, shoving her backward. She cries out and they move in, cornering and cornering her until she’s forced onto the bed. One of the panels pins her down. The other shifts, until an arm with a needle reveals itself."
                        w "ALICE!"
                        l "Whatever it takes."
                        n "You bite your cheek as you watch it happen. The injection, the jump of her skin, the submission. Your knuckles go white against the surface of your desk. Your eyes burn."
                        n "She relaxes, finally. The arms recede. You taste blood."
                        $ meat += 1
                    "> NO":
                        jump act2torture
            "> INSERT PROBE":
                n "A microscopic camera would be inserted into the subject’s bloodstream via needle to monitor their organs from the inside. The camera will then establish transmitters within the body which will then trigger an alert when disturbed. The transmitter is capable of picking up on infection, inflammation, parasites, and other foreign bodies."
                n "The transmitters and camera can only be removed via surgical procedure."
                n "Do you want to proceed?"
                menu:
                    "> YES":
                        n "The wall struggles with the missing panel, but still manages to kick into motion. She jerks towards it, watching the arms form."
                        w "What are you doing?"
                        l "It’s just an injection."
                        n "She seems to loosen, some. The arm with the needle approaches her, looming over her. She stares at it warily."
                        l "What if I don’t want to see it?"
                        n "She doesn’t take her eye off the needle. But you can see her thinking."
                        n "She shrugs. She lays her arm out for ease of access."
                        w "Then don’t."
                        w "It’s your life, Langston. Do with it what you will."
                        n "The needle comes down. She doesn’t wince. She doesn’t move at all."
                        w "But I think things would be a lot easier for you if you were willing to accept it."
                        w "Things change. People change."
                        w "If you don’t change with them, what’s going to be left of you?"
                        w "I don’t think you’d be very happy that way."
                        n "The arm recedes. Blood bubbles at the injection site. She smears it down her skin."
                        n "She smiles."
                        w "Just think about it."
                        n "You feel a surge of cold."
                        n "You intend to."
                        $ candy += 1
                    "> NO":
                        jump act2torture
    if meat >= candy:
        jump meat_route
    else:
        jump candy_route
    return
    # This ends the game.
