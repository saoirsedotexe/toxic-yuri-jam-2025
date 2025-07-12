label meat_route:
    
    $ say_style = "Cutscene"
    play music "Investigationloop.ogg"
    # ACT 2 MEAT
    # TRANSITION TO BEDROOM
    scene bedroom_dark:
        size(1920, 1080)
    n "You hold your head in your hands at the edge of your bed. You've scarcely been near it at all since Turner's return. It brings you no comfort now."
    n "From across the room, your computer monitor blares red. All your sample’s vials have run dry, toppled over across your desk. You’re surrounded by crumpled pieces of paper, all of them wrong, seemingly triggered by some sort of glitch in the system."
    n "It’s possible those needles haven’t been replaced in ages. Perhaps the vials themselves are contaminated. Something. Some kind of mistake."
    n "The results are wrong.{w} You don't need them." 
    n "Everything you’ve ever needed was right here. In this room. Your hands. Her hands. You let it slip away. You let this happen. It’s up to you to make it right."
    n "Your gaze slides across the room. Your doctor’s kit. You stand, crouching down, until you find a booklet of folded fabric. Your tools."
    n "The rubber tube goes taut as you hold it between both hands. Then you wrap it, slowly, around your bicep. You clench it tighter with your teeth."
    n "The needle glints silver in this light. You release the air inside and hold the point against your inner arm. The vein there thumps with the constriction."
    n "You take a breath. THen plunge. The tube grows warm against your skin."
    n "You shake off the rubber, then get to work. The vial gets placed into the centrifuge. Your blood begins to circulate, then whirl, causing your cells to separate."
    n "You sit, watching. Your hands grip your knees until you can’t take it anymore."
    n "It'll take a few hours. Hours you can't spare waiting."

    # TRANSITION TO MONITOR
    scene desk with fade:
        size(1920, 1080)

    n "She's in bed when you shake the monitor awake. Her back faces away from you."
    n "You start up the session."
    
    $ say_style = "Interrogation"
    play music "InterrOGGationloop.ogg"    
    scene quarantine_room_v2 with dissolve:
        size(1920, 1080)
    label act2meatquestion1:
        menu:
            "> WHAT IS YOUR NAME?":
                n "She raises her head over her shoulder, bleary eyed."
                show wifeside towards frown at interrogation
                w "Alice?"
                w "What are you doing?"
            "> WHAT IS YOUR TITLE?":
                n "She raises her head over her shoulder, bleary eyed."
                show wifeside towards frown at interrogation
                w "Alice?"
                w "What are you doing?"
    label act2meatquestion2: 
        menu: 
            "> WHAT IS YOUR NAME?":
                n "Her brows crease. Her gaze searches the speaker in the wall. She finds nothing."
                w "Charlotte Turner. Navigator of the Soft Touch. Third in command."
            "> WHAT IS YOUR TITLE?":
                n "Her brows crease. Her gaze searches the speaker in the wall. She finds nothing."
                w "Charlotte Turner. Navigator of the Soft Touch. Third in command."
    label act2meatquestion3: 
        menu:
            "> WHAT ARE YOU TO ME?":
                n "She sits up. Her arms fold across her chest."
                hide wifeside
                show wife scared at interrogation
                w "I don't understand."
                w "I'm your wife."
            "> WHAT IS YOUR ROLE?":
                n "She sits up. Her arms fold across her chest."
                hide wifeside
                show wife scared at interrogation
                w "I don't understand."
                w "I'm your wife."
    label act2meatquestion4:
        menu:
            "> SAY IT AGAIN.":
                w "I'm… your wife."
            "> DESCRIBE YOUR CONDITION.":
                n "That doesn't matter."
                jump act2meatquestion4
    label act2meatquestion5:
        menu:
            "> DESCRIBE ANY EMOTIONAL INCONSISTENCIES.":
                n "That doesn't matter."
                jump act2meatquestion5
            "> DO YOU LOVE ME?":
                w "…"
                w "Of course I do."
                w "Do you love me?"
                l "More than anything."
                l "More than you can understand."
                l "I'm so scared of losing you."
                l "I don't know what I'd do."
                w "You don't have to be."
                w "I'm right here."
                l "For now."
                n "She fidgets."
                hide wife scared
                show wifeside towards frown at interrogation
                w "Is something wrong?"
                w "What do you want me to say?"
    label act2meatquestion6:
        menu:
            "> HOW DID WE MEET?":
                hide wife scared
                show wifeside away frown at interrogation
                w "It was university."
                w "We shared a physics class. My friend knew you from other courses. She said you were shy."
                w "She wasn't even sure if… well."
                w "But I wanted to meet you. You always seemed so confident in discussions. You always had all the right answers."
                w "You wanted to be a doctor. I didn't know what I wanted."
                w "But… we ended up hitting it off."
                w "Being around you was the direction I needed."
            "> WHERE WAS OUR FIRST DATE?":
                hide wife scared
                show wifeside towards frown at interrogation
                w "It took us a while to figure that out."
                w "You wanted a study date. I guess you wanted to make it into something productive."
                w "But I thought it might be fun to try and get you a little out of your shell. And eventually you agreed."
                show wifeside smile
                w "So we went roller skating. I thought you might find it charming in an old-timey sort of way."
                w "You didn't. But I think you tried."
                w "I liked knowing that you would at least try."
    label act2meatquestion7:
        menu:
            "> WHAT WERE YOUR WEDDING VOWS?":
                show wifeside towards frown
                w "…"
                w "To support you. To light your path forward."
                w "To go where you go. To stay where you stay."
                w "To love you steadfastly, fervently, eternally."
            "> WHAT WERE MY WEDDING VOWS?":
                show wifeside away frown
                w "…"
                w "To follow me always. To stand by me in darkness."
                w "To hold yourself open to me. To meet me where I am."
                w "To love me recklessly, loyally, eternally."
    label act2meatquestion8:
        menu:
            "> THEN WHY DID YOU LEAVE?":
                show wifeside away
                w "This isn't fair."
                w "It's more complicated than that."
                w "Do you want me to retread a thousand arguments? For what?"
                w "I'm already at your whim whenever you want."
                show wifeside towards
                w "Ask something else."
            "> WHY COULDN'T YOU LOVE ME?":
                show wifeside away
                w "This isn't fair."
                w "It's more complicated than that."
                w "Do you want me to retread a thousand arguments? For what?"
                w "I'm already at your whim whenever you want."
                show wifeside towards
                w "Ask something else."
    l "You said you loved me before."
    l "Did you lie?"
    w "Please. Stop this."
    l "How do I know if you've been lying?"
    l "How would I know?"
    l "Have you been lying this whole time?"
    w "…" 
    w "If you really believed that, you would shoot me out."
    n "Your jaw aches with how hard you've grit your teeth. There's a weight over your back as you bend over the monitor."
    n "You open the contamination protocols."
    label act2meattorture:
        menu:
            "> DIAGNOSTIC SURGERY" if surgery_deny == False:
                n "A surgery undertaken to track down any particularly elusive contaminant. An entry point would be cut down the abdomen so that the major bodily organs could then be scanned. Upon detection, foreign bodies would be removed, disposed of, then separated for analysis."
                n "Do you want to proceed?"
                menu:
                    "> YES.":
                        n "No."
                        $ surgery_deny = True
                        jump act2meattorture
                    "> NO.":
                        $ surgery_deny = True
                        jump act2meattorture
            "> OXYGEN DEPRIVATION" if oxygen_deny == False:
                n "In which the oxygen of containment is lowered to the point that the body is driven into a state of shock, thus rendering them unconscious and prone. Pathogens and viral bodies deteriorate under these extreme conditions and parasites either fall into stasis or wither and die."
                n "Do you want to proceed?"
                menu:
                    "> YES.":
                        n "No."
                        $ oxygen_deny = True
                        jump act2meattorture
                    "> NO.":
                        $ oxygen_deny = True
                        jump act2meattorture
    # ONLY AFTER SELECTING NO ON BOTH PREVIOUS OPTIONS
    n "You enter your credentials, unlocking a list of other possible options. You scroll through. One stands out."
    label act2meatect:
        menu:
            "> ELECTROCONVULSIVE THERAPY":
                n "Small shockwaves applied to the brain and central nervous system. Can be used to probe contaminant activity and stimulate other multicellular organisms."
                n "Do you want to proceed?"
                menu:
                    "> YES.":
                        n "The panels of the wall shift behind her. Before she can move, two arms latch onto her. She tries, fails, to rip herself away."
    label act2meatquestion9:
        menu:
            "> WHO ARE YOU?":
                hide wifeside
                show wife scared at interrogation
                w "I've already told you!"
                n "A dialogue prompt for the application of the ECT nodes appears. You once again enter your credentials. The amount of allowed amps increases."
                n "You raise the mA to 15. Her body jolts."
                w "Alice!"
    label act2meatquestion10:
        menu:
            "> WHO ARE YOU?":
                w "Enough! Enough!!"
                n "You apply 25 mA. She folds into herself. She cries out."
                w "CHARLOTTE TURNER! MY NAME IS CHARLOTTE TURNER!"
    label act2meatquestion11:
        menu:
            "> WHO ARE YOU?": 
                n "You apply 100 mA. She spasms. She falls off the bed. The arms hold her upright. She's shaking."
                w "YOUR WIFE! YOUR WIFE!"
    label act2meatquestion12:
        menu:
            "> WHO ARE YOU?":
                n "You apply 150 mA. She can't scream anymore. She doesn't move. She drools. Burns blacken her arms."
                n "Your mouse whips across the screen to pull open her vitals. Her heart monitor dances across its readings. Still alive."
                n "You're practically heaving your breaths. You can see your pulse at the corner of your vision."
    label act2meatquestion13:
        menu:
            "> Charlotte?":
               n "She doesn't answer."
               l "Charlotte?"
    hide screen airlockbutton
    $ say_style = "Cutscene"
    play music "Investigationloop.ogg"
    
    # END ACT 2
    # TRANSITION TO BRIDGE
    scene bridge with fade:
        size(1920, 1080)
    
    show comms_officer at midleft with dissolve
    show ecologist_cast at interrogation with dissolve
    n "You pass out copies of your findings. Every test, analysis, and scan reaches the same conclusion: no contamination."
    l "She's clear. As I knew she would be."
    l "There was never anything to be concerned about."
    n "The crew reads over your findings. There's a few nods, a few whispers. A room full of relieved faces. Except for one."
    n "Knight scowls at your report. They step forward."
    k "It says the bulk of these results came back within a few hours of each other."
    k "What did you spend the rest of your time doing?"
    l "Questioning. I wanted to make certain that the woman in quarantine is the same woman I married."
    l "There's a summary of our exchanges on page six."
    n "Knight flips through the pages. They squint at the words."
    k "It says there's a recording of your sessions."
    l "Yes. There is."
    k "I'd like to hear them."
    l "You don't have clearance."
    k "I don't have clearance? To check your work?"
    k "Are we really supposed to let you have the final say despite your obvious bias?"
    l "If I suspected her of anything, I would have followed protocal. Simple."
    l "Our conversations were personal."
    k "I assure you I'm not interested in the intricacies of your relationship. Our safety takes precendence over your sexual tension."
    l "There's no need to be snide."
    l "She's safe. That's all that matters as far as you're concerned."
    n "Sutton's brows knit together as she reviews your papers. She takes a deep breath."
    s "No one wants to doubt you. Or her."
    s "But… I don't want to dismiss any concern."
    s "Did she ever explain what happened to her helmet?"
    l "It came off during the attack. She removed it to free herself."
    k "Convenient."
    s "…"
    s "Your report seems sound. I don't see anything that sticks out to me as insecure."
    s "We have no reason to believe Dr. Langston's assessment isn't accurate."
    s "We can hesitate in the way of fear all we like. But at the end of the day, the call we make could end an innocent woman's life."
    s "Is that a call you're willing to make?"
    k "…"
    k "No."
    k "I don't know."
    s "We've left her in there long enough."
    n "You release your breath. You've been smiling to yourself for hours, but now you allow the others to see it."
    n "Knight gives you a parting look before departing with the rest of the crew."
    s "I'll head down there, then."
    s "You coming?"
    n "Your exhaustion hits you all at once. The stress of everything that’s happened. The lack of sleep. All your thoughts, consumed by her. You need to be somewhere dark for a long, long while."
    n "But not yet."
    l "Yes. I'm coming."
    n "She nods. She cracks a small smile."
    s "You did good."
    s "I'm glad to see everything worked out."
    l "As am I."
    n "She pats you on the shoulder, then walks further into the ship."
    n "You follow."

    # [TRANSITION TO AIRLOCK] 
    scene quarantine_room_v2 with fade:
        size(1920, 1080)
    n "She types her security clearance into the keypad by the airlock. Her eyes keep glancing at you. It’s difficult to contain your excitement."
    s "Opening now."
    n "The door slowly rises. In its wake, she's there."
    show wife normal with dissolve
    n "Her expression is vacant. The burns on her arms have been sufficiently covered by her gown — you ignore them."
    n "She approaches you. You hold your breath."
    n "She stops right in front of you."
    n "She throws her arms around you, embracing you. You prop your chin carefully over her shoulder."
    l "It's okay."
    l "It's over."
    n "Sutton smiles at her. Turner doesn't acknowledge her."
    s "Good to see you back, Turner."
    s "…I'll give you some room."
    n "She waves, then takes her leave."
    n "She holds you tighter."
    l "We can still make things work."
    n "She says nothing."

    # [TRANSITION TO BEDROOM]
    scene bedroom_dark with fade:
        size(1920, 1080)
    play music "i use this power for evil.ogg"
    n "You wake to the sound of screaming."
    n "She's gone from her side of the bed."
    n "You stand, half-numb and gummy-eyed, approaching the door. You grab haphazardly for something, anything — you manage a syringe."

    # [TRANSITION TO BRIDGE]
    scene bridge with fade:
        size(1920, 1080)
    n "The door slides open. The scent hits you first. Raw iron. A heavy metallic cloud that clings to your soft palate. Red rust stains the exterior hall to the bedroom."
    n "Your hands begin to shake."
    n "You pass by bits and pieces of your crew. People you've patched up. People who have come to you in need."
    n "The engineer vivisected in the hall.{w} The computer technician in chunks in the recreation room.{w} The geologist run through in the cafeteria."
    n "You make it to the bridge to find Sutton laying in her own viscera. Her mouth gapes open, mid-shout, arm outstreteched. Toward the receiver, you guess. Not that it would have done anyone any good."
    n "It's hard to feel anything at all. There's a hollow void where your feelings should be."
    n "Footfall approaches you from behind. You turn as Knight grabs you by the shoulders, shaking you."
    show ecologist_cast with dissolve
    k "WHAT DID YOU DO?"
    n "You only stare back. They shove you aside, manning the control deck. They hesitate, lost in all the buttons and dials, before grabbing Sutton's headset and receiver."
    k "MAYDAY, MAYDAY, SOFT TOUCH TO ARIADNE, THERE'S SOMETHING ON OUR SHIP, THERE'S SOMETHING—"
    n "A dark blur whips past you, coiling around Knight's throat. The remaining words choke out of them as they sputter, clawing at their bindings."
    scene murder with dissolve:
        size(1920, 1080)
    n "You follow the shape back to the source. She's standing in the threshold of the bridge, blood soaked, arm extended. A vine-like tendril extends from an opening in her wrist. Her expression is vacant. Her eyes move slowly towards you."
    l "I thought —"
    c "You were wrong."
    n "She flings Knight across the bridge. Their body lands, hard, against the rail, toppling over the side, down into the navigator's pit. You can almost hear the crack of bone."
    n "The edge of the control deck presses into your back as you step into it. You hold your hands by your side, syringe hidden against your wrist."
    c "I should've known you wouldn't accept reality."
    l "Charlotte, you can hear me. This isn’t you. You’re still able to stop–"
    c "You'd keep talking forever and never listen. There is no Charlotte. There's only me."
    n "She reaches out for you and you jab, needlepoint out, thumb hovering over the plunger, but she’s faster. The tendril shoots out, flashing past you, digging into your wrist. The bones groan against her grasp until they fold. The syringe clatters against the floor."
    scene pinned with dissolve:
        size(1920, 1080)
    n "She pins your wrist down behind you, against the deck. You struggle as she looms over you. She holds out her other arm. A second tendril slinks closer, curling around your neck, up your jaw, over your mouth."
    l "Charlotte —"
    c "Only me."
    c "I'll show you what real love looks like."
    n "She slips through your open mouth, past your teeth and your tongue and your throat. You cough, gag, choke."
    n "There's no malice in her eyes, when you meet them."
    n "Something snaps inside you. Like a plucked string. The world itself goes concave. Sensation itself has been reduced to clips. A burning in your chest. An all encompassing wet. A sudden emptiness."
    n "Your own breath is hard and dripping blood. A body slides from the deck and onto the floor. Your tendrils wrap around the controls."
    scene go_home with dissolve:
        size(1920, 1080)
    y "Time to go home."

return