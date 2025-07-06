label candy_route: 

    scene bedroom_dark:
        size(1920, 1880)
    
    n "You pace." 
    n "From across the room, your computer monitor blares red. All your samples’ vials have run dry, toppled over across your desk. You’re surrounded by crumpled pieces of paper, all of them report the same thing, the same finding, the same truth." 
    n "She was right."
    n "You see it now." 
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

    scene they_call_me_doctor_desk_long 

    p "I knew you'd come."
    n "She stands directly in front of the speaker. Her face is perfectly placid. Almost… enticed."
    l "I thought things over."    
    p "And what did we discover?"
    l "..."
    p "I see."
    n "She turns over her shoulder, checking the door." 
    p "And yet the airlock is unopened."
    p "I have not been cast into the void."
    p "Why is that?" 
    l "I have questions."
    p "Back to basics, then."
    p "Unless we decided to switch things up."
    l "..."
    l "What did you have in mind?"
    n "She leans into the camera. Her eyes take up the bulk of the monitor."
    p "Quid pro quo."
    p "Like I said before. Let's keep things mutual."
    label act2candyquestion1: # if hit no, loop back to original yes/no prompts
        menu: 
            "> NO":
                p "Shoot me out the airlock, then."
                p "This doesn't go any other way, I'm afraid." 
            "> YES":
                p "I knew you'd come around, sweetheart."
                p "I'll let you go first, then."
                l "..."
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
                l "It felt like everything I wanted was gone. All that we'd built, all that I'd fought for... it was all out of my control."
                l "I thought it might be easier to accept it. No. It was so much more horrifying."
                l "But..."
                p "But...?"
                l "I had to know."
            "> FASCINATED":
                l "From a clinical perspective, this is... unheard of. Not outside of insects and invertebrates."
                l "Your face, your voice; it's uncanny."
                l "On a personal level, however..."
                l "..."
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
                l "..."
                p "One at a time, Langston."
    p "Now let's see."
    p "Hm..."
    p "I know how she felt about things. But I've only had assumptions about you."
    p "You had a life. You had dreams. Why did you follow hers?"
    label act2candyquestion5:
        menu:
            "> SCARED OF CHANGE":
                l "We had something. We had a routine. Things weren't perfect, but they worked."
                l "She wanted to throw everything away. For what?"
                l "I hate this ship. I hate this... vacuum. This silence."
                l "But being here was easier to swallow than giving up {i} everything {/i}."
                p "You could rebuild it."
                p "If you wanted."
                l "But without her?"
                p "We don't need her."
                p "We have each other now."
                l "..."
            "> SCARED OF LOSING HER":
                l "What if she came here and found something she liked more?"
                l "What if she decided she didn't want to come home?"
                l "What was I supposed to do? Just let her go?"
                l "She was everything to me."
                p "And now she's gone."
                p "Now what."
                l "..."
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
                p "But..."
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
                    "> NO": 
                        n "PATT: LOOP BACK AROUND TO ORIGINAL YES/NO QUESTION"
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
    s "But... I don't want to dismiss any concern."
    s "Did she ever explain what happened to her helmet?"
    l "It came off during the attack. She removed it to free herself."
    k "Convenient."
    s "..."
    s "Your report seems sound. I don't see anything that sticks out to me as insecure."
    s "We have no reason to believe Dr. Langston's assessment isn't accurate."
    s "We can hesitate in the way of fear all we like. But at the end of the day, the call we make could end an innocent woman's life."
    s "Is that a call you're willing to make?"
    k "..."
    k "No."
    k "I don't know."
    s "We've left her in there long enough."
    n "You release your breath. You've been smiling to yourself for hours, but now you allow the others to see it."
    n "Knight gives you a parting look before departing with the rest of the crew."

    return