label airlock:
    hide screen airlockbutton
    $ say_style = "Cutscene"
    scene desk with fade:
        size(1920, 1080)
    n "You stare at the airlock hatch."
    n "Something comes over you. A lightness. An ease. This sense that… in an instant, nothing would have mattered. Nothing you’ve done will have amounted to anything at all. You could just be free of it."
    n "In seconds, this could all go away."
    n "You stare at her through the monitor."
    n "You press the button."
    n "Her lights go out. A flashing alarm replaces them. Panic enters her eyes."
    n "She’s at the speaker in an instant, bracing herself against it. Her face takes up the camera’s whole frame."
    scene quarantine_room_v2 with fade:
        size(1920, 1080)
    show wife scared
    w "WHAT ARE YOU DOING?"
    n "You have nothing to say. Even the deepest parts of you know you can’t dignify any of this with an explanation. You just know this is how it ends."
    w "LANGSTON! LANGSTON, PLEASE!" 
    w "YOU’RE GOING TO KILL ME!"
    n "You know."
    n "The ship rumbles. The gears turn. She bangs her fist against the wall."
    n "Then, the hatch opens."
    n "She’s sucked backwards. Into the vacuum. Into the silence."
    scene airlock_open:
        size(1920, 1080)
    n "That’s the last you see of her; you avert your gaze. In her absence, the hatch shuts itself."
    n "After a while, you compose yourself. You stand from the monitors, turning them off."
    n "The ease has left you. An emptiness has taken its place. You will embrace it in kind."

return