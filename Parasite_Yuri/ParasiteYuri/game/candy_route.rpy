label candy_route: 

    scene bedroom_dark:
        size(1920, 1080)
    
    n "You pace." 
    n "From across the room, your computer monitor blares red. All your samples’ vials have run dry, toppled over across your desk. You’re surrounded by crumpled pieces of paper, all of them report the same thing, the same finding, the same truth." 
    n "She was right.{w} You see it now." 
    n "Everything you've ever needed was right here. In this room. Your hands. Her hands. You let it slip away."
    n "But now it’s come back. This could be a second chance."
    n "Your gaze slides across the room. Your doctor’s kit. You stand, crouching down, until you find a booklet of folded fabric. Your tools."
    n "The rubber tube goes taut as you hold it between both hands. Then you wrap it, slowly, around your bicep. You clench it tighter with your teeth."
    n "The needle glints silver in this light. You release the air inside and hold the point against your inner arm. The vein there thumps with the constriction."
    n "You take a breath. Then plunge. The tube grows warm against your skin."
    n "You shake off the rubber, then get to work. The vial is back inside the centrifuge. Your blood begins to circulate, then whirl, causing your cells to separate."
    n "Your teeth pick at the inner lining of your lip. Your finger rubs against your thumb."
    n "You decide."
    n "And then you're gone." 

    #[TRANSITION TO MONITOR]

    if haircut:
        scene they_call_me_doctor_desk_short:
            size(1920, 1080)
    else:
        scene they_call_me_doctor_desk_long:
            size(1920, 1080)
    
    p "I knew you'd come."
    n "She stands directly in front of the speaker. Her face is perfectly placid. Almost… enticed."
    l "I thought things over."    
    p "And what did we discover?"
    l "…"
    p "I see."
    n "She turns over her shoulder, checking the door." 
    p "And yet the airlock is unopened."
    p "I have not been cast into the void."
    p "Why is that?" 
    l "I have questions."
    p "Back to basics, then."
    p "Unless we decided to switch things up."
    l "…"
    l "What did you have in mind?"
    n "She leans into the camera. Her eyes take up the bulk of the monitor."
    p "Quid pro quo."
    p "Like I said before. Let's keep things mutual."
    label act2candyquestion1: # if hit no, loop back to original yes/no prompts
        menu: 
            "> NO":
                p "Shoot me out the airlock, then."
                p "This doesn't go any other way, I'm afraid."
                jump act2candyquestion1
            "> YES":
                p "I knew you'd come around, sweetheart."
                p "I'll let you go first, then."
                l "…"
    label act2candyquestion2:
        menu:
            "> WHAT ARE YOU?": 
                p "You don't have a name for what I am yet."
                p "I'm a passenger. Just like you are."
                p "The destination doesn't matter. As long as I'm going."
            "> WHAT DO YOU WANT?":
                p "Survival. Just like you."
                p "Human beings have it easy. You are your own vessel."
                p "Some things don't have that luxury. We have to hitch rides."
    p "My turn. Exciting!"
    p "This is a lot of pressure. Do you always feel this way?"
    p "There's one thing I'd really like to know."
    p "How did you feel, once you realized?"
    label act2candyquestion3:
        menu:
            "> TERRIFIED":
                l "It felt like everything I wanted was gone. All that we'd built, all that I'd fought for… it was all out of my control."
                l "I thought it might be easier to accept it. No. It was so much more horrifying."
                l "But…"
                p "But…?"
                l "I had to know."
            "> FASCINATED":
                l "From a clinical perspective, this is… unheard of. Not outside of insects and invertebrates."
                l "Your face, your voice; it's uncanny."
                l "On a personal level, however…"
                l "…"
                l "You were right."
                l "I wouldn't be very happy."
                n "She smiles."
                p "Very interesting."
                p "Thank you."
                p "Your turn."
    label act2candyquestion4:
        menu:
            "> WAS IT EVER REALLY HER?":
                n "Her brows incline. She gives you a look of pity."
                p "No. Not since she received me."
                p "We had a brief exchange. A passing of ships. I took on her burden. Her thoughts, her feelings, her sense of self."
                p "It's just been you and me."
            "> WHY HER?":
                p "Is it better or worse to know it could have been anyone?" 
                p "We had our eye on the Captain. But it wasn't a match."
                p "But things worked out for the better this way. You fought for me."
                l "…"
                p "One at a time, Langston."
    p "Now let's see."
    p "Hm…"
    p "I know how she felt about things. But I've only had assumptions about you."
    p "You had a life. You had dreams. Why did you follow hers?"
    label act2candyquestion5:
        menu:
            "> SCARED OF CHANGE":
                l "We had something. We had a routine. Things weren't perfect, but they worked."
                l "She wanted to throw everything away. For what?"
                l "I hate this ship. I hate this… vacuum. This silence."
                l "But being here was easier to swallow than giving up {i} everything {/i}."
                p "You could rebuild it."
                p "If you wanted."
                l "But without her?"
                p "We don't need her."
                p "We have each other now."
                l "…"
            "> SCARED OF LOSING HER":
                l "What if she came here and found something she liked more?"
                l "What if she decided she didn't want to come home?"
                l "What was I supposed to do? Just let her go?"
                l "She was everything to me."
                p "And now she's gone."
                p "Now what."
                l "…"
                l "I don't know."
                p "I think you do."
                p "I'm not going anywhere."
    p "The picture becomes clearer."
    p "After you."
    label act2candyquestion6:
        menu:
            "> WHAT HAPPENS NOW?":
                p "Whatever you want to happen."
                p "I mean really, you're the one in control here."
                p "You could still shoot me out if you wanted to."
                p "I did take your wife, after all."
                p "But…"
                p "I think you know I could also give her back."
                p "In a sense." 
                p "I remember all the love we shared—you and Charlotte, that is—as if it was me standing there in her shoes."
                p "Like it's just been me the entire time, really. You've loved me retroactively. You've made love to me."
                p "I like the way your tongue wriggles."
                p "You don't have to stop, now that I'm at the wheel instead of a passenger of her mind."
                p "Which leads me to my last question."
                p "Could you do it? Will you take my love back?"
    n "The monitor fogs under your breath."
    label act2candyquestion7:
        menu:
            "> NO":
                n "Are you sure?"
                menu:
                    "> YES":
                        n "Then do it."
                        menu:
                            "> GO BACK":
                                jump act2candyquestion7
                    "> NO": 
                        jump act2candyquestion7
            "> YES":
                n "Her teeth glint under the fluorescents. She places a palm next to the camera."
                p "I'm glad."
                p "I'm so glad."
                p "I love you, Alice."
                p "Go tell the others."
                p "I want to see  you."
                l "Okay." 
                p "I will."
                n "You power down the monitor. You feel your heartbeat in your fingertips."
    hide screen airlockbutton
    # END ACT 2
    # [TRANSITION TO BRIDGE]
    scene bridge:
        size(1920, 1080)

    n "You pass out copies of your findings. Every test, analysis, and scan reaches the same conclusion: no contamination."
    l "She's clesar. As I knew she would be."
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
    k "Forgive me if the intricacies of your interpersonal relationship aren't something I'm willing to hinge my life on."
    l "Then trust me knowing I'm hinging mine on it."
    l "She's safe."
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
    scene quarantine_room_v2:
        size (1920, 1080)
    n "She types her security clearance into the keypad by the airlock. Her eyes keep glancing at you. It’s difficult to contain your excitement."
    s "Opening now."
    n "The door slowly rises. In its wake, she's there."
    n "Her eyes well up with tears."
    p "Oh, Alice."
    n "She's upon you instantly, embracing you. Her palm cups the back of your skull. She lays her brow in the nook of your shoulder."
    p "Thank you. Thank you, thank you."
    n "It takes some time to return the gesture in full. This body, hers, but not. So familiar, but still new. You wrap your arms around her and soon find yourself…relaxed."
    n "Sutton clears her throat. She scratches her neck, sheepish."
    s "Good to see you back, Turner."
    s "…I'll give you some room."
    n "She waves, then takes her leave."
    n "She separates herself from you, but doesn’t stop touching you. Her fingers trace your clavicle, your shoulders, down your arms. She holds your hands."
    p "You ready?"
    n "She takes the lead, pulling your hand down the corridor."
  
    # [TRANSITION TO BEDROOM]
    scene bedroom_dark:
        size(1920, 1080)
    p "Finally."
    l "You make it sound like you were planning this."
    n "Her head tilts. She hums."
    p "I expected you to be happy with my offer, even if I had to put in the work to sell you on it."
    p "After all. I very much want to live."
    p "But I like this ending better than the alternative." 
    l "…"
    l "What was the alternative?"
    n "Something coy plays at her lips."
    p "Playing house."
    p "But now we can just be straight with each other."
    p "I like this much better."
    p "I have a feeling you'll like it, too."
    n "Then she laughs. She pushes at you playfully, spinning out of your grasp, practically dancing around the room."
    n "She steps down into the conversation pit, falling onto the cushions with a sigh."
    p "This is so much more comfortable than before."
    n "She extends her hand out to you."
    p "Sit with me?"
    n "You go rigid. Your thoughts go blank."
    p "Please?"
    n "Your arm raises, board-like. She takes your hand and pulls you in next to her."
    n "She studies you. Her eyes dart from your nose, your mouth, your body, back to your own eyes. Then she seems to pout."
    p "You're so much more stiff than how we were before."
    p "What's wrong?"
    n "You take a deep breath."
    l "We can't be what we were before."
    p "Isn't that what you wanted, to have it all back?"
    l "The love. I want the love."
    l "But I saw the test results. I saw your blood turn bright green when exposed to oxygen. I saw your cells sprout roots like tree saplings. I know you're not the same."
    p "You can check for yourself if you want—the body you loved is still all here. And then some."
    l "Show me everything. I want to know."
    p "You're not afraid? We can take it slow if you need."
    l "{u}Show me.{/u}" 
    n "She smirks. Then moves in closer. Your back braces against the corner cushions. She pushes your glasses back into your hair, leaving her palms on your cheeks."
    p "It's funny, getting to know you again."
    p "When I first heard your voice over that speaker…suddenly, I had been missing you for years."
    p "I hated you, too."
    p "But mostly, I ached. Not just heartache. After our conversation…I learned a lot about this body."
    p "The way it drips for you."
    p "Do you miss it?"
    l "Yes."
    l "God, yes."
    p "I'm glad."
    n "Her hands follow the curve of your jaw. One of her thumbs ghosts over the edge of your bottom lip."
    n "She presses her lips against yours. You feel a chill run down your spine, your stomach tightens. Your hands find her shoulders and you meet her, leaning into her kiss. She sighs into your mouth."
    n "She moves on top of you, straddling your lap. She pushes your head back into the cushions, arching over you. Instinct takes over as your hands fall to the back of her thighs for support."
    n "You can't help but smile into the kiss when you feel the warmth and wet where she's sitting."
    n "She pulls back first, panting, drops of sweat already starting to gather first on the tip of her nose, the way it always used to. And God, she's a knockout. Your mouth waters, your throat thickens for her."
    n "Her gown comes off easily over her head, thrown behind her, forgotten. In its absence, you lay claim to the skin beneath, feeling it grow warm against your own. Your hand trails up her thigh, but she stops you. She lays her forehead against yours."
    p "Relax."
    p "Let me take care of you."
    n "You ease back. She leans in. Breathes gentle kisses onto your neck. Her hands run down your collarbones with an accompanying chill and find their place cupping each of your breasts, thumbs pressing into your nipples with a twist that draws a moan from your throat."
    n "Other sources of pressure join it. Something wraps around each of your thighs like rubber tourniquets. The warmth and wet has spread to envelop your torso, tingling. Sedating. Even the texture of her skin seems to grip you, stick to you."
    n "Within the haze of sensation, samething is writhing. It licks at your hips and triggers your back to reflexively arch, to which she responds by bringing her weight down even harder onto you. Her bones protrude hard from her skin, almost as if sharpened. You giggle at the sting of it."
    n "The writhing slips past your waistband curls into you. Fills you. You thrum like a plucked string and concave to her, allow yourself to become the empty space into which she readily expands. Your head falls back, leaving her to your exposed neck and its throbbing heartbeat."
    n "You'd feel some obligatory embarrassment for how quickly she's racing you toward climax if you had any room left for conscious thought. The room falls away, any sensation but touch falls away. You try to savor it; God, you've missed it."
    l "Charlotte…"
    n "You freeze. Her head tilts up to look at you."
    l "Sorry, I—"
    n "Something is different in her eyes. A wild fear. Veins pop in her jaw, her brow twitches. Every limb holding you falls slack; she's dead weight in your lap."
    l "…Charlotte…?"
    n "A trembling hand reaches up toward your face. It stops just below your jaw. Then it constricts. Her thumb digging into your trachea."
    n "A single tear slips down her cheek."
    n "You gasp and struggle for breath, and she digs in a little harder, but then she suddenly releases. She shivers. Blinks."
    p "Aw, why'd you losse it? I thought I had you for sure."
    n "You gape at her. She wipes at her face and flicks the tear away."
    p "Seriously, can you handle it all? Like I said, we don't have to jump in yet if you're afraid."
    n "Your teeth dig into your tongue."
    l "It's okay."
    l "It wasn't you."
    n "You feel numb. Your thoughts reduce to static. You search her face for something, anything."
    n "But it still looks just like her. Smiling at you. Wanting you."
    l "Let's keep going."
    n "She gives you a little smile. She leans back up, kissing your cheek."
    p "I can appreciate your stubbornness."
    l "That's new."
    n "Her smile grows."
    p "I really love you, Alice."
    l "…"
    l "I love you, too."
    n "As you close your eyes, a blur of motion whips up around her as she unfolds herself once more, spilling her anodyne emollient over you to drag you away, far away, where there is only her body and your body and the pleasure hwere the two meet. You are happy to scorn everything else. This wretched ship and these wretched people were the price you once paid for her love; now it offers itself to you freely. At long last."
    n "You let her carry you home."
    

    return