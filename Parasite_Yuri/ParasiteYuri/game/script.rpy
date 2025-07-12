default vitals = False
default scans = False
default audiolog = False
default release = False
default questioning = False
default surgery_deny = False
default oxygen_deny = False
default haircut = "long"
default meat = 0
default candy = 0

label start:

#  PUT THE DAMN CREDITS IN

    $ say_style = "Interrogation"
    play music "Investigationloop.ogg"

    scene space with fade:
        size(1920, 1080)
    
    n "You are home."
    n "You are finally home."
    n "The carpet beneath your feet. {w}The soft of your own bed. {w}The quiet. The quiet."
    n "You are home."
    n "Something drips on your shoulder."
    n "You look up. The ceiling beams have started to melt."
    n "The door oozes. {w}The shelves go concave. {w}The bed splits."
    n "Fire eats at the foundation."
    n "You clutch the infrastructure in place. It comes through your fingers like candle wax. But you stand firm."
    n "What’s left of the house forms a hollow around you. You keep the mantle from toppling in. You force the engravings to hold their shape until it’s you, too, holding shape. Entombed in a weight of your own making. A gnat forever encased in amber."
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
    
    label act1:
    scene bridge_grounded with fade:
        size(1920, 1080)
    
    n "Metallic thumps reverberate around you as you approach the bridge. These corridors feel like something’s swallowed you whole, too many nooks and crannies, too many winding parts."
    n "You never thought there would be anything worse than hospitals. But you hate this ship. You hate these halls. You hate the chrome interiors, you hate the lining pipes, you hate the vertigo from the artificial gravity, you hate your uniforms, you hate the viewports of nothingness, you hate the vacuum, you hate the noise."
    n "It has been one year, nine months, and nineteen days that you have been aboard the {plain}Soft Touch{/plain}. You want to go home."
    n "You {plain}should{/plain} be home."
    n "You never understood her enthusiasm when she was assigned here. You certainly didn’t share it. You have a thin respect for the Captain, but the rest have no decorum. No manners. They’re as plain and unyielding as the riveted metal plating of the walls on this wretched ship. As harsh as the fluorescent lights. As droning as the engine humming beneath your feet."
    n "You arrive at the bridge, taking a moment to gather yourself. There’s a glow within you, a small, bitter hope, that whatever this emergency is, that it may lead Ariadne to abort your mission early. Then you can put all this behind you."
    n "When the doors of the bridge slide open, a shouting voice reaches you first. Your comms officer has a hand cupping her exposed ear, leaning into her headset as if it will better help her hear through it."
    show comms_officer with dissolve
    s "Knight! Knight, do you copy? Captain, do you read? Turner—"
    l "Have we lost signal?"
    n "Her eyes dart over to meet yours."
    s "It cut off. After… I heard something. A thump. Signal’s been dead just over fifteen minutes, now."
    n "On the ship’s radar, each data collection site glows as a solid green dot, and among them, the party’s red beach blinks. They’re not far from Site C."
    l "Has Site C ever been a problem before now?"
    s "No. Never."
    n "Turner would normally be the one monitoring the radar, but you suppose you’re the next best thing. Not that it helped; conditions surrounding Site C are hazy at worst, from the looks of it. Nothing they haven’t worked in before."
    l "Send me out."
    s "Absolutely not."
    l "If there’s a problem, we need someone to reach them."
    s "That’s not what protocol says."
    s "The best place for you is here, so you can tend to whoever comes back."
    l "Whoever?"
    n "Her mouth twitches. Before she can say anything more, something crackles from her headset. Her eyes widen, you jerk upward. She switches the transmitter so you both can hear."
    #SPRITE NOTE: I’d love if it were possible for the ECOLOGIST’S sprite to fade in and out during this scene to correlate with the signal going in/out
    #FOR KNIGHT- SPRITE: Ecologist_hurt (or whatever I name the spacesuit vers.)
    show comms_officer at midleft with move
    show ecologist_cast at interrogation with pixellate
    k "Mayday, mayday, do you read me?"
    n "Acid fills your stomach. Your nails bite into your palms. You brush past Sutton to lean out the viewport."
    s "Knight, what’s going on?"
    l "Where’s Turner?"
    n "There’s a jostling of clothing and gear. She’s running."
    show ecologist_cast at interrogation
    k "There’s something — It got them. And — coming back."
    n "It’s like you’ve been vacuum-sealed from the inside. A tightness, an unrelenting squeeze threatens your collapse."
    s "What do you mean it got them? Knight?"
    show ecologist_cast at interrogation
    k "—I can’t—"
    s "Knight—"
    k "They’re gone."
    n "There’s a ringing in your ears. Your hands shake. You feel a compulsion to vomit."
    show ecologist_cast at interrogation
    k "Start the ship!"
    n "The engineer breaks from his trance and moves to the control panel. They wait for Sutton’s orders."
    l "We need to find her."
    l "{b}Now.{/b}"
    n "Sutton hesitates. She won’t look at you. Knight comes closer and closer, checking over her shoulder. It becomes more and more obvious she’s injured. Their shoulder swings loose in her suit; she has that same arm clutched to their sternum."
    k "Sutton!"
    n "She squeezes her eyes shut. Then turns for the engineer."
    hide ecologist_cast with dissolve
    show comms_officer at center with move
    s "Open the hatch. Then start us."
    n "The engineer brings the ship’s engines to life. The bridge rumbles with it. You grab her by the shoulder."
    l "What are you doing?"
    s "She’s already gone."
    s "We have to protect the crew. That’s what she would want."
    n "She pulls herself away from you, turning back toward the viewport. Knight is less than twenty meters away and gaining. You stand taut, a hollow reservoir filling with liquid hot ire."
    l "How the hell would you know what she would want?"
    l "She would want to be alive. She would want to be here."
    l "You don’t know anything about her."
    s "Wait."
    n "From the treeline. Someone else. Knight turns to look."
    k "Turner?"
    n "You let out a breath you didn’t know you were holding. Everything releases all at once."
    n "Turner escapes into the clearing, her suit tattered and fluttering behind her. She waves her arms at the ship. Her voice shouts into Knight’s distant receiver."
    # SPRITE NOTE: No sprite for Turner yet as she isn’t on the ship . . and frankly I don’t want to draw a spacesuit vers for her rn. Smiles :-)
    w "STAND BY! STAND BY!"
    n "Your heart beats again. Thank god. Thank god."
    n "Sutton digs her fingers into her eyes, dragging her hands down her face. {w}But then she squints."
    s "Where’s her helmet?"
    n "It’s true. It’s gone. Her hair flows behind her without the confines of the glass."
    n "You turn to go."
    l "I’ll meet them there. I’m getting my kit. Start the ship."
    n "Sutton glances at you. Like she wants to say something. But she doesn’t."
    s "Go ahead. I’ll manage things here."
    n "You leave for your office."
    
    scene quarantine_room_v2 with fade:
        size(1920, 1080)
    n "With your medical kit in hand, you rush down the ship’s infrastructure to the exit ramp. Your fingers lock into place around the handle."
    show ecologist_cast with dissolve
    n "You arrive and Knight stands waiting for you. She’s slumped against a wall, recovering. The door outside is closed. She won’t make eye contact."
    l "Where is she?"
    n "They glance at the glowing communication receiver. You slam your palm into it."
    l "Sutton."
    s "I don’t want this any more than you do, Langston."
    l "What are you talking about?"
    k "She was exposed."
    n "You jerk around to look at them."
    l "What?"
    k "Her helmet. Something must have happened. During the attack. We can’t let her in."
    s "She can stay at the landsite until Second Team comes."
    l "This is bullshit."
    s "This is protocol."
    l "What if the facility isn’t stable enough to hold back whatever attacked you?"
    k "And what if she exposes everyone on board to something she’s carried in? I can’t even test my samples. They got left behind."
    s "I’m sorry. If there were any other way, we would take it. But it just isn’t safe."
    l "What about quarantine? What about quarantine procedures?"
    n "Knight’s brow creases."
    k "No. We can’t be sure decontamination would be enough. We have to leave this to Biohazard."
    l "You said she was dead."
    k "I thought she was. I’m glad she isn’t. I don’t want her to end up killing us all."
    n "You stare at them, clenching your fists. You turn back to the receiver."
    l "Sutton. What does protocol say about quarantine?"
    k "We don’t have sufficient equipment."
    l "I can monitor her. I know her best. If something’s wrong, I'll know with certainty."
    k "You’re not qualified!"
    l "How should we know if we should trust you either?"
    n "They shoot up straight."
    k "Are you crazy? My suit isn’t tampered with!"
    l "How do we know that for sure? What if we’re all already contaminated?"
    s "Enough."
    n "She sighs."
    s "The ship has built in quarantine procedures in the hatch. We let her in, she can stay there, and there’s enough equipment to at least keep her in check."
    s "With what we have, she has to stay inside for at least five days. After that… we’ll have to talk about what to do. In the meantime, Langston will keep watch. Find out if there’s some way to test her for a breach of anything."
    s "Any objections?"
    n "Knight’s face screws up. She takes a deep breath, then winces. She grabs her shoulder."
    k "Fine. But I’ll be looking very carefully at your data."
    n "You just nod. There’s a sort of numbness flowing through your bloodstream. You have to stabilize yourself against the inner hull."
    s "Fine. Open the hatch."
    s "We’ll be taking off in sixty seconds. Both of you go to the infirmary. Prepare for launch, then make sure they’re taken care of."
    k "Knight gives you a parting look. Then leaves you as she navigates down the hall."
    n "The window to the hatch fills with a dense smoke. Decontamination. But you see the light of the outside filter through as the door opens. Through it, you know she’s there. Finally safe."
    n "Your hand lingers on the glass for a moment. Eventually you follow Knight."
    
    scene desk with fade:
        size(1920, 1080)
    n "You stare at the monitors before you. Her various charts fluctuate with every breath, every heartbeat, every muscle twitch. Meanwhile, she sits on the floor, chin on her knees, staring at the ground."
    n "Your heart clenches."
    n "Sutton walks up behind you. Her gaze is solemn. It looks like she hasn’t slept since the funeral."
    show comms_officer at midleft with dissolve
    s "I hope you know what you’re doing."
    l "I do."
    s "You know her best, after all."
    n "She sighs. Then she leaves you with her."
    hide comms_officer with dissolve
    label monitor1:
        menu:
            "> CHECK VITALS":
                if vitals:
                    n "Enough stalling."
                    jump monitor1
                else:
                    n "The feed from her wristband monitor seems normal. No elevated pulse, no arrhythmia. It’s as if nothing’s changed at all."
                    $ vitals = True
                    jump monitor1
            "> CHECK SCANS":
                if scans:
                    n "Enough stalling."
                    jump monitor1
                else:
                    n "You sort between thermal scans, electrical scans, and internal scans of her body. Nothing out of place."
                    $ scans = True
                    jump monitor1
            "> CHECK AUDIO LOG":
                if audiolog:
                    n "Enough stalling."
                    jump monitor1
                else:
                    n "There was an initial conversation she had with Sutton where she filled her in. She seemed to take it well, but you know her enough to recognize the clipped sentences for what they are. No one would want this for themselves."
                    $ audiolog = True
                    jump monitor1
            "> CHECK AIRLOCK RELEASE":
                if release:
                    n "You know, deep down, beneath the denial and the fear and the dread, that there may come a moment where you will have to do what’s necessary. If that moment should come, you know what you need to do."
                    $ questioning = True
                    jump monitor1
                else:
                    n "You don’t want to."
                    $ release = True
                    jump monitor1
            "> BEGIN QUESTIONING" if vitals and scans and audiolog and questioning:
                n "You click on the startup prompt that records your conversation. A pop-up appears with an advisory message: The following questions are best utilized to ascertain the state of being, mental stability, and personhood of quarantine subjects." 
                n "Keep in mind these suggestions are only suggestions. Each subject will differ. Therefore, sometimes it is not what’s said, but how it’s said that will get the most reliable answer."
    n "You take a deep breath."
    scene quarantine_room_v2 with fade:
        size(1920, 1080)
    show screen airlockbutton with dissolve
    $ say_style = "Interrogation"
    play music "InterrOGGationloop.ogg"
    l "This is Doctor Langston, A. initiating quarantine procedure questioning. Are you of sufficient body and mind to proceed?"
    n "She turns to face the speaker. There’s a light in her eyes."
    show wife normal at interrogation with dissolve
    w "Alice."
    l "I need a yes or no answer."
    w "Yes."
    l "Do you consent to quarantine procedures?"
    w "Yes."
    l "Good. Let’s begin."
    label act1question1:
        menu:
            "> WHAT IS YOUR NAME?":
                w "Charlotte Turner. Hyphen Langston, depending on who you ask."
                $ meat += 1
            "> WHAT IS YOUR TITLE?":
                w "Navigator of the Soft Touch. Third in command. Also, your wife."
                $ candy += 1
    label act1question2:
        menu:
            "> WHAT IS THE CURRENT STATE OF OUR MISSION?":
                hide wife normal
                show wifeside towards smile at interrogation
                w "The current… state?"
                w "Things are going well, I think."
                w "This is our last stop on this go around. We were supposed to spend some more time collecting samples, but… well."
                w "Hopefully we have enough."
                $ candy += 1
            "> WHAT IS YOUR ASSIGNMENT?":
                hide wife normal
                show wifeside away smile at interrogation
                w "I help lead the science officers into the field to collect data for Ariadne. And get us to the planets to begin with."
                w "They’re looking for resources, but in order to excavate it’s up to us to find a planet with suitable conditions."
                w "That’s what all the pamphlets say, at least. I’m just the navigator."
                $ meat += 1
    l "You’re doing well so far. Nothing out of the ordinary."
    show wifeside towards frown at interrogation
    w "Is whatever you’re reading off telling you to say that?"
    l "…No. That’s from me."
    w "Well. Thank you. I’d hope so."
    label act1question3:
        menu:
            "> HOW ARE YOU FEELING?":
                hide wifeside
                show wife normal at interrogation
                w "Tired. Anxious, I guess. But that’s not what you’re asking. I feel fine. Fine as I could be, given the circumstances."
                hide wife normal
                $ meat += 1
            "> HAVE YOU EXPERIENCED ANYTHING UNUSUAL?":
                show wifeside away frown darkness at interrogation
                w "Like… what? Other than being attacked and chased and thrown into quarantine, interrogated by my wife? No."
                l "I know this isn’t ideal. But I fought for you. I’d rather you be here than forced to wait there."
                $ candy += 1
    show wifeside towards smile darkness at interrogation
    w "…Thank you, Alice. It’s not like I don’t understand. Safety first."
    w "…Were they really going to leave me there?"
    label act1question4:
        menu:
            "> DESCRIBE THE INCIDENT.":
                show wifeside away
                w "It’s difficult to talk about."
                w "Knight wanted to go back for samples. We got the go ahead and we went. Site C is on the swampy side of the river so when we noticed the transmitter was down, we figured it must have been the humidity and went to make repairs."
                w "But it wasn’t the humidity."
                w "…"
                w "The Captain drew its attention so we could get away. But it caught up to me too."
                w "There was something about its skin that made it… stick. And it was stuck to my helmet."
                show wifeside towards
                w "I did what I had to to survive."
                $ meat += 1
            "> WHAT HAPPENED TO YOUR HELMET?":
                show wifeside away
                w "It’s difficult to talk about."
                w "Knight wanted to go back for samples. We got the go ahead and we went. Site C is on the swampy side of the river so when we noticed the transmitter was down, we figured it must have been the humidity and went to make repairs."
                w "But it wasn’t the humidity."
                w "…"
                w "The Captain drew its attention so we could get away. But it caught up to me too."
                w "There was something about its skin that made it… stick. And it was stuck to my helmet."
                show wifeside towards
                w "I did what I had to to survive."
                $ candy += 1
    label act1question5:
        menu:
            "> I’M SORRY.":
                show wifeside -darkness
                w "I’m sorry too."
                w "I wish there was more I could have done. For the Captain. For Sutton. For you."
                w "I’m just glad I made it home."
                $ meat += 1
            "> KNIGHT THOUGHT YOU WERE GONE.":
                show wifeside frown -darkness
                w "…"
                w "I thought they saw me struggle with it. I thought they might help. I guess I can’t blame them."
                w "I can’t imagine what that must have been like for you. I’m sorry."
                $ candy += 1
    label act1question6:
        menu:
            "> DO YOU WANT TO TALK ABOUT THAT MORNING?":
                show wifeside away frown
                w "…"
                w "It’s behind us now."
                w "In light of everything, I’m sure we both have our regrets."
                w "If there’s anything else to say… we can say it once I’m clear."
                $ meat += 1
            "> WAS ANYTHING ELSE BROUGHT INTO THE SHIP WITH YOU?":
                w "The room probably would’ve taken anything with it when it took my suit."
                w "I didn’t even know it could do that. I guess you have it now? For analysis?"
                w "But anyway. No, I didn’t bring anything else in with me."
                $ candy += 1
    n "This is it. What you’ve been dreading the most. You open the procedural window of your quarantining window, type in your credentials, and a list of etiquette and procedures appears."
    l "I need to take some data to make sure everything’s normal."
    l "Just… bear with me."
    hide wifeside
    show wife normal at interrogation
    w "Whatever it takes."
    n "Each step pertains to the systematic elimination of potential hazards to the ship. Anything decontamination and the rudimentary scans couldn’t catch, this should cover. Some of them are… particularly invasive. You don’t want to overwhelm her and make things worse than they already are."
    n "You read over the instructions on your options."
    label act1torture:
        menu:
            "> EPIDERMAL SCAN":
                n "This involves a censor that would comb over her skin to check for any lesions or entry points. Minimally invasive, medically speaking, but the machine would have to shave her head to leave nothing unchecked."
                n "Do you want to proceed?"
                menu:
                    "> YES":
                        l "I’m going to have the scanner take a closer look at your skin."
                        hide wife normal
                        show wife scared at interrogation
                        l "But… That’s going to mean losing your hair."
                        w "Oh."
                        hide wife scared
                        show wifeside away frown darkness at interrogation
                        w "I see."
                        w "Do I have a choice?"
                        l "…"
                        l "I’m sorry. I know that—"
                        show wifeside towards
                        l "I just want to do what it takes."
                        show wifeside away
                        w "—Yeah, well."
                        w "You’ll do what you have to do. Nothing personal."
                        show wifeside towards smile
                        w "Ha, it  might be even easier this way, anyway."
                        l "What do you mean?"
                        w "It could be like I’m someone else entirely. Maybe it’d help us keep this a little more professional."
                        l "Oh."
                        l "I don’t know."
                        l "I guess so."
                        n "The mechanisms from the wall shift around, preparing for the scan. In spite of everything, she smiles at you."
                        show wifeside away
                        w "You don’t have to stay if you don’t want to."
                        show wifeside tears
                        w "If it would be easier for you, you could go."
                        l "It’s fine." 
                        l "I don’t mind."
                        n "She nods." 
                        w "Like I said. Whatever it takes."
                        n "She lowers her head, her dense curls falling down around her neck. You brace yourself."
                        $ candy += 1
                        $ haircut = "short"
                        show wifeside tears with hpunch
                    "> NO":
                        jump act1torture
            "> BLOOD ANALYSIS":
                n "A mechanical arm would extend from the wall to take her blood. This may sting a little."
                n "Do you want to proceed?"
                menu:
                    "> YES":
                        l "I’m going to have the machine draw your blood so I can analyze it."
                        l "Are you ready?"
                        n "She nods."
                        hide wife normal
                        show wifeside away smile at interrogation
                        w "Seems pretty simple."
                        w "It reminds me of when you had to practice during med school. The fake arm?"
                        show wifeside towards
                        n "She laughs. You missed that sound."
                        w "You were pretty bad at it."
                        l "It’s not easy, you know."
                        l "Especially when you kept wiggling it."
                        w "Real people are twitchy! I was just testing you."
                        show wifeside darkness
                        n "This time, you share a laugh. The mechanisms from the wall shift around, a robotic arm prepares its needle. She stares at it warily."
                        show wifeside away -darkness
                        l "Hey…"
                        l "Are you sure you don’t miss it?"
                        show wifeside towards smile
                        w "Home?"
                        w "Honestly, I think I miss it now more than ever."
                        w "Maybe I was a little hasty. When I said those things."
                        n "Her words linger a while before they actually penetrate. You take a breath."
                        l "Okay."
                        l "We can… talk more about this later."
                        w "Of course."
                        n "The arm takes her blood. She winces, but as always, powers through."
                        $ meat += 1
                    "> NO":
                        jump act1torture

    scene bedroom_light_mode with fade:
        size(1920, 1080)
    label act2:
    
    $ say_style = "Cutscene"
    play music "Investigationloop.ogg"
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
    k "In this hypothetical, I had asked to board, you would've known something was wrong. It's my job to know what's out there. I would be an automatic flight risk."
    k "{i}Your{/i} job is to take care of us when the danger's over. It wasn't your call to make."
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
    
    scene desk with fade:
        size(1920, 1080)
    n "The feed of the quarantine hatch is clouded over with decontamination fog. Hands shaking, you remotely turn on a fan to filter it out."
    n "As the haze clears, Turner sits squarely in the center of the room, next to a piece of wall panel. Frayed wires and inner piping now sit exposed in a small rectangle."
    n "You press the monitor’s transmitter to the ship’s bridge."
    l "We’re all good. Everything’s under control."
    show comms_officer at midleft with dissolve
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
    show wifeside frown at interrogation with dissolve
    
    $ say_style = "Interrogation"
    play music "InterrOGGationloop.ogg"
    label act2question1:
        menu:
            "> WHAT HAPPENED?":
                show wifeside away frown darkness at interrogation
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
                show wifeside towards
                w "Do you think something’s wrong?"
                l "Let’s begin the questioning."
                $ meat += 1
            "> WHAT DID YOU DO?":
                show wifeside away frown darkness at interrogation
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
                show wifeside towards
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
                show wife normal at interrogation
                w "We were attacked. The Captain was killed and dropped our equipment. Knight managed to grab some of it and get away. It grabbed me, but I fought it and wriggled away. My helmet went off with it."
                show wife scared at interrogation
                w "I was trying to come home to you."
                l "After everything that had happened that morning, you were really thinking of me?"
                show wife normal at interrogation
                w "We’ve fought before."
                l "It wasn’t like before."
                w "Why are you doing this? I don’t know what you want, Alice."
                l "I want to make things work."
                n "She stares at the camera, at a loss. She tries to say something, but thinks better of it. Her teeth lock together."
                hide wife normal
                show wifeside away frown at interrogation
                w "We have to get out of this first."
                w "Keep asking your questions."
                $ meat += 1
            "> WHAT HAPPENED TO YOUR HELMET?":
                w "You already asked me this."
                l "Tell me again."
                w "…Okay."
                hide wifeside
                show wife normal at interrogation
                w "We were attacked. The Captain was killed and dropped our equipment. Knight managed to grab some of it and get away. It grabbed me, but I fought it and wriggled away. My helmet went off with it."
                show wife scared at interrogation
                w "I was trying to come home to you."
                l "After everything that had happened that morning, you were really thinking of me?"
                show wife normal at interrogation
                w "We’ve fought before."
                l "It wasn’t like before."
                w "Why are you doing this? I don’t know what you want, Alice."
                l "I want to make things work."
                n "She stares at the camera, at a loss. She tries to say something, but thinks better of it. Her teeth lock together."
                hide wife normal
                show wifeside away frown at interrogation
                w "We have to get out of this first."
                w "Keep asking your questions."
                $ candy += 1
    label act2question3:
        menu:
            "> HAS YOUR CONDITION CHANGED SINCE WE LAST SPOKE?":
                show wifeside towards
                w "No."
                w "I feel the same."
                $ candy += 1
            "> WHAT DO YOU DO WHEN I’M NOT HERE?":
                show wifeside towards smile
                w "What is there to do?"
                w "Stare at the wall. Count the wall tiles. Minus one, now."
                if haircut == "short":
                    show wifeside frown
                    w "I used to braid my hair."
                w "I mostly just think."
                $ meat += 1
    label act2question4:
        menu:
            "> HAVE YOU EXPERIENCED ANY OTHER EMOTIONAL ABNORMALITIES?":
                show wifeside towards frown darkness
                w "What do you think?"
                w "I’m trying to keep it together. I am."
                w "But this is just…"
                w "I don’t even know how long it’s been."
                $ candy += 1
            "> WHAT DO YOU THINK ABOUT?":
                show wifeside towards frown darkness
                w "You."
                show wifeside smile
                w "But also… the crew."
                w "What might happen if something is wrong."
                w "What I could’ve done differently."
                $ meat += 1
    label act2question5:
        menu:
            "> DO YOU FEEL LIKE YOURSELF?":
                show wifeside away smile
                w "Not in the way you mean."
                w "I’m me. I know I’m me."
                w "But at the end of this, I don’t know if I’ll be the same person that I was before."
                $ candy += 1
            "> WHAT COULD YOU HAVE DONE DIFFERENTLY?":
                show wifeside away frown -darkness
                w "I keep running through what happened. It’s on playback. Over and over again."
                w "Maybe if I didn’t hesitate. If I just ran from it."
                show wifeside darkness tears
                w "But when the Captain tried to step in front of us, I froze. I didn’t want to leave them behind."
                w "Is it better to flee for your own sake? Or fight even when hope is lost?"
                w "What do you think?"
                $ meat += 1
    label act2question6:
        menu:
            "> WERE YOU INTENDING TO ESCAPE?":
                show wifeside darkness frown
                w "I guess it’s about time we get to the point."
                w "Could I have gotten very far, realistically?"
                w "I don’t know."
                show wifeside -darkness
                w "I guess the answer to your question is yes. Even if, subconsciously, I knew better."
                w "I just don’t want to be here anymore."
                $ candy += 1
            "> WHAT IF SOMEONE SAW YOU?":
                show wifeside towards darkness frown
                w "Saw what?"
                w "Oh. This."
                w "I didn’t think the alarm would trigger, for one thing."
                w "But even if it did, I knew you’d be the only one to see it."
                show wifeside smile -darkness
                w "I’m in your care, after all."
                $ meat += 1
    hide wifeside
    show wife normal at interrogation
    n "All of a sudden, she stares into the camera for a moment. You get goosebumps."
    w "Can I ask you something?"
    n "You open your mouth to speak, then close it. You glance at the procedures listed on your monitor."
    show wife disdain at interrogation
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
                hide wife disdain
                show wifeside towards frown darkness at interrogation
                w "This has to be mutual, you know."
                w "I want to trust you. I’m forced to trust you."
                w "But if you want me to just be a lab rat you prod at, fine."
                w "I guess you finally have me where you want me."
                $ meat += 13
    hide wifeside
    show wife normal at interrogation
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
                        show wife scared at interrogation
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
                        show wife scared at interrogation
                        w "What are you doing?"
                        l "It’s just an injection."
                        n "She seems to loosen, some. The arm with the needle approaches her, looming over her. She stares at it warily."
                        hide wife scared
                        show wifeside towards frown at interrogation
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
                        show wifeside smile
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
