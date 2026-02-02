# ---------- CHARACTERS ----------
define e = Character("Eileen")
define l = Character("Lucy")

# ---------- IMAGES ----------
image desert = "images/bg/desert.jpg" # Stock image from pexels.com
image cave = "images/bg/bg cave.jpg"
image resort = "images/bg/resort.jpg" # Another stock image
image concert = "images/bg/concert1.png"

image e concerned = "images/chars/eileen concerned.png"
image e happy = "images/chars/eileen happy.png"
image e vhappy = "images/chars/eileen vhappy.png"
image l neutral = "images/chars/lucy happy.png"
image l mad = "images/chars/lucy mad.png"

# ---------- GAME START ----------
label start:

    scene desert
    with fade

    show e concerned at center
    show l neutral at right

    e "Well, now you've done it, protagonist. You got us lost in a freaking desert."
    l "Seriously, I am NEVER letting you plan a vacation again."

    # ---------- MENU 1 ----------
    menu:
        "Yeah, we should probably turn back the way we came...":
            l "Finally, you're listening to reason! We've wasted so much time already!"
            show e happy
            e "Okay, let's get going before some sort of exotic predator eats us alive."
            jump resort
        "Listen, I got this! I swear we'll find civilization right over the next dune.":
            show l mad
            l "OH MY GOD, you are the absolute worst! We might actually die out here."
            show e happy
            e "Calm down, Lucy. We can't be THAT far away from the resort. I'm sure we'll get there in no time!"
            jump cave


# ---------- PATH ONE ----------
label resort:

    scene resort
    with dissolve

    show e vhappy at center
    show l neutral at right

    e "Yay! We finally made it! This place is incredible! And I bet they treat all their employees super well!"
    l "Wow, it's beautiful! If only I had a third expression to convey the joy in my heart at this current moment..."

    # ---------- MENU 2 ----------
    menu:
        "See, I told you to trust me! Now, let's go check out that band playing over there.":
            e "Heck yeah, I love anime girl rock music!"
            l "Ugh, I hate loud noises. I'm just gonna go sunbathe."
            e "Suit yourself, nerd!"
            jump concert
        "It really is nice! But I'm exhausted from all that dune climbing. I'm gonna get some sleep.":
            e "Okay, see ya later! Lucy, let's go swimming!"
            l "Fiiine, if you insist. Have a good nap, protagonist."
            jump ending_one


# ---------- PATH TWO ----------
label cave:

    scene cave:
        zoom 1.5
    with dissolve

    show e concerned at left
    show l neutral at right

    e "Okay, I'm getting a bit worried..."
    show l mad
    l "WHERE are we going?! This is ridiculous!"
    e "Yeah, protagonist, I really think we should--"
    l "OH MY GOD, WHAT IS THAT??"

    jump ending_three


# ---------- PATH THREE ----------
label concert:

    scene concert
    with dissolve

    show e vhappy 

    e "Woo! This is awesome! I'm not a big Creed fan, but she really makes this song her own!"

    jump ending_two


# ---------- ENDINGS ----------
label ending_one:

    scene black
    with fade

    "You walk back to your room and quickly pass out."

    return


label ending_two:

    scene sunset
    with fade

    show e happy at center

    e "I had so much fun today, protagonist. This place has so much to do! And look at that sunset..."

    e "Don't you think it's a bit... romantic?"

    "You and Eileen fall in love and live happily ever after."

    return

label ending_three:
    scene black

    "It was a giant spider. There were no survivors."

    return
