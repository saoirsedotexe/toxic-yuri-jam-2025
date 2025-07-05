# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character(None, what_prefix="{i}", what_suffix="{/i}")

define l = Character("Langston", color="#96D8C3")

define w = Character("Wife", color="#8FB688")

define c = Character("Comms Officer", color="#E0FBA9")

define e = Character("Ecologist", color="#92A6E4")

define p = Character("Parasite")

define s = Character("Stickfigure")

default vitals = False
default scans = False

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "cell.png" or "cell.jpg") to the
    # images directory to show it.

    $ say_style = "Interrogation" #Cutscene or Interrogation

    scene dream

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
    
    scene bedroom
    
    n "And then you wake up. Your pager trills."
    c "Langston."
    c "We need you at the bridge."
    c "Something’s wrong."
    n "You hear your heartbeat in your ears. Static dances over your skin, like a holdover from pins and needles. There’s a weight in your gut."
    n "You take a deep breath, forcing it to pass."
    l "Alright."
    l "I’m on my way."
    n "You get out of bed."
    
    #[TRANSITION TO BRIDGE]
    
    scene bridge
    
    n "By the time you arrive at the bridge, the COMMS OFFICER stands hunched over his control deck with his hands pressed to both sides of his headset. The ship’s engineer works hard at something on the ship’s panel, only to turn back to the COMMS OFFICER, and shake his head."
    show CommOfficer
    n "The COMMS OFFICER taps on his microphone."
    c "Captain, do you read me? THE ECOLOGIST. THE NAVIGATOR. Do you read?"
    l "Have we lost signal?"
    n "He glances over his shoulder at you. His brows crease together."
    c "It’s no use. Nothing’s getting through."
    l "What’s the last thing you heard?"
    c "THE ECOLOGIST mentioned wanting to get some further samples from Site C. We confirmed with the schedule, THE NAVIGATOR led them back, then… nothing."
    n "You turn to the ship’s sonar. Each of the payload sites have their own red dot. Another blinking dot represents the party. They’re hovering near the outside of the C dot."
    l "Has Site C ever been a problem before?"
    c "No. Never. We have a transmitter between it and Site D."
    l "How long has it been?"
    c "Fifteen minutes."
    n "You take a deep breath. You stare outside the viewport as if by some miracle, she’ll appear."
    n "She doesn’t."
    l "We need to get out there then. Who else can go?"
    c "They still have time. Protocol is thirty."
    l "Are you joking? Someone needs to go find them — now."
    c "I don’t like it anymore than you do, Langston, but we don’t have a choice. Until it’s a qualifiable emergency, we’d put everyone at risk."
    l "This is ridiculous. This isn’t an emergency to you?"
    n "He gives you a long, hard look."
    c "They’re my friends too, Doctor."
    l "It’s just just friends out there."
    n "Something crackles from his headset. His eyes widen, you jerk upward. He switches the transmitter so you both can hear."
    f "— back — ship —"
    c "Captain? Captain, do you read?"
    f "COMMS OFFICER. Something — down. We need —"
    n "A screech crackles over the transmitter. Followed by something visceral and wet."
    c "Captain? Captain!"
    l "NAVIGATOR? Are you there?"
    n "There’s a rustling on the other end. Like the receiver’s being dragged through dirt. Until suddenly it cuts out. Replaced by heavy breathing."
    w "Mayday, mayday, do you read me?"
    n "You let out a breath you didn’t know you were holding. Your nails bite into your palms. You brush past COMMS OFFICER to lean out the viewport."
    c "NAVIGATOR what’s going on?"
    w "There’s something — It got them. And — coming back."
    n "There’s a jostling of clothing and gear. She’s running."
    c "What do you mean it got them? NAVIGATOR?"
    l "Just come back. Just make it back."
    w "I’m coming."
    n "COMMS OFFICER gives you a look, before diverting his attention back."
    c "NAVIGATOR —"
    w "They’re gone."
    n "COMMS OFFICER’s shoulders collapse. There’s a gentle shake to his hands."
    w "Start the ship!"
    n "The engineer breaks from his trance and moves to the control panel. They wait for the COMMS OFFICER’s orders."
    l "What are you doing?"
    c "I need to think."
    n "THE NAVIGATOR bursts from the treeline outside the viewport."
    l "We don’t have time!"
    c "The Captain —"
    l "— The Captain’s dead. You have to decide."
    n "He hesitates. THE NAVIGATOR comes closer and closer, checking over her shoulder. He squints at her from afar."
    c "Where’s her helmet?"
    l "Start the ship!"
    w "COMMS OFFICER!"
    c "Wait."
    n "From the treeline. Someone else. THE NAVIGATOR turns to look."
    w "ECOLOGIST!"
    n "As ECOLOGIST approaches, they start waving their arms at the ship. Their voice shouts into the NAVIGATOR’S distant receiver."
    e "STOP! STOP!"
    
    scene quarantine_room_v2
    
    n "You stare at the monitors before you. Her various charts fluctuate with every breath, every heartbeat, every muscle twitch. Meanwhile, she sits on the floor, chin on her knees, staring at the ground."
    show wife_base
    n "Your heart clenches."
    n "COMMS OFFICER walks up behind you. His gaze is solemn. It looks like he hasn’t slept since the funeral."
    c "I hope you know what you’re doing."
    l "I do."
    c "You know her best, after all."
    n "He sighs. Then he leaves you with her."
    label checks:
        menu:
            "> CHECK VITALS":
                n "The feed from her wristband monitor seems normal. No elevated pulse, no abnormal rhythm. It’s as if nothing’s changed at all."
                $ vitals = True
                if vitals == True and scans == True:
                    jump after
                else:
                    jump checks
                
            "> CHECK SCANS":
                n "You sort between thermal scans, electrical scans, and internal scans of her body. Nothing out of place."
                $ scans = True
                if vitals == True and scans == True:
                    jump after
                else:
                    jump checks

    # These display lines of dialogue.
    
    scene after
    label after:

    l "I'm doctor misery. She needs medicine drug to live."

    w "I would like medicine drug."

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
