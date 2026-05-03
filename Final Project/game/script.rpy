# ---------- CHARACTERS ----------
define n = Character(None)
define k = Character("Kyle")
define c = Character("Commander")
define a = Character("Aide")
define s = Character("Server")
define t = Character("Tanner")

# ---------- AUDIO ----------
define audio.intro_crawl = "audio/intro.mp3"
define audio.door_open = "audio/door open.wav"
define audio.brief = "audio/brief.mp3"
define audio.birds = "audio/birds.mp3"
define audio.city = "audio/city.mp3"
define audio.buzz = "audio/phone buzz.wav"

# ---------- IMAGES ----------
image bedroom = "images/bg/bedroom.jpg"
image brief = "images/bg/briefing room.jpg"
image city = "images/bg/city.jpg"
image diner = "images/bg/diner.jpg"

image kyle = "images/char/kyle.png"
image tanner = "images/char/tanner.png"

# ---------- VARIABLES ----------
default get_up_clicks = 0
default bed_time_left = 8.0
default hunger_pressure = 0
default city_progress = 0
default food_locked = False
default used_peek = False
default used_compare = False
default used_food = False
default used_commit = False


# ---------- TRANSFORMS ----------
transform crawl_text:
    xalign 0.5
    ypos 1.15
    rotate 0
    zoom 1.0
    linear 36.0 ypos -3.2 zoom 0.6

transform kyle_reveal:
    alpha 0.0
    pause 18.0
    linear 0.8 alpha 1.0

transform kyle_title_pos:
    yalign 0.40

transform kyle_prompt_pos:
    yalign 0.68


# ---------- SCREENS ----------
screen opening_crawl():

    modal True

    timer 24.0 action Return("auto_end")

    add Solid("#000000")

    fixed:
        xfill True
        yfill True

        text """
        DAWN OF THE FINAL DAY

        The year is 2112. A lot of stuff
        has happened.

        The President of Humanity
        has been held ransom for weeks
        by a group of AI terrorists
        known as Lizard Squad.

        They have demanded five million
        V-Bucks, which now operate as
        the world's universal currency,
        in exchange for the President's
        safe return.

        If the ransom is not paid,
        the President will be
        executed and the human realm
        will descend into chaos.

        The price has been deemed
        unreasonable by the world
        government. Instead, they
        have enlisted the planet's
        greatest super soldier to
        destroy Lizard Squad
        once and for all.

        Countless battles have
        been won at his command.
        Countless clankers
        have fallen to his blades.

        He is humanity's last hope.

        He is...
        """:
            color "#f6d45b"
            size 40
            text_align 0.5
            layout "tex"
            xalign 0.5
            yalign 0.0
            xmaximum 800
            at crawl_text

        text "Kyle.":
            color "#f6d45b"
            size 56
            text_align 0.5
            xalign 0.5
            at kyle_reveal, kyle_title_pos

        text "Click to continue":
            color "#f6d45b"
            size 22
            text_align 0.5
            xalign 0.5
            at kyle_reveal, kyle_prompt_pos

        button:
            action Return("click_end")
            xfill True
            yfill True
            background None


screen bed_choice():

    modal True

    timer 0.1 repeat True action SetVariable("bed_time_left", bed_time_left - 0.1)

    if bed_time_left <= 0:
        timer 0.01 action Return("timeout")

    frame:
        xalign 0.5
        yalign 0.5
        padding (35, 35)

        vbox:
            spacing 22

            if bed_time_left > 5:
                text "The room is quiet." size 24
            elif bed_time_left > 2.5:
                text "Time keeps moving." size 24
            else:
                text "The morning is slipping away." size 24

            if get_up_clicks < 5:
                textbutton "Get out of bed":
                    action Return("try_get_up")
            else:
                textbutton "Get out of bed":
                    action Return("get_up")

screen city_choice_screen():

    modal True

    frame:
        xalign 0.5
        yalign 0.55
        padding (30, 30)

        vbox:
            spacing 12

            if not food_locked:

                if hunger_pressure < 2:

                    textbutton "Keep walking toward District Nine":
                        text_size 22
                        action Return("walk")

                    if not used_food:
                        textbutton "Check the food deal":
                            text_size 28
                            action Return("food")

                elif hunger_pressure < 4:

                    textbutton "Keep walking":
                        text_size 18
                        action Return("walk")

                    if not used_food:
                        textbutton "Check the food deal":
                            text_size 28
                            action Return("food")

                    if not used_peek:
                        textbutton "Just look at the menu for a second":
                            text_size 26
                            action Return("peek")

                    if not used_food:
                        textbutton "See how far away it is":
                            text_size 24
                            action Return("food")

                elif hunger_pressure == 4:

                    if not used_food:
                        textbutton "Open the coupon":
                            text_size 30
                            action Return("food")

                    if not used_compare:
                        textbutton "Check nearby breakfast spots":
                            text_size 28
                            action Return("compare")

                    if not used_commit:
                        textbutton "Look at directions":
                            text_size 26
                            action Return("commit")

                    if not used_compare:
                        textbutton "Compare breakfast combos":
                            text_size 26
                            action Return("compare")

                    if not used_peek:
                        textbutton "Just check the menu":
                            text_size 25
                            action Return("peek")

                else:

                    if not used_food:
                        textbutton "Open the coupon":
                            text_size 30
                            action Return("food")

                    if not used_compare:
                        textbutton "Check nearby breakfast spots":
                            text_size 28
                            action Return("compare")

                    if not used_commit:
                        textbutton "Look at directions":
                            text_size 26
                            action Return("commit")

                    if not used_compare:
                        textbutton "Compare breakfast combos":
                            text_size 26
                            action Return("compare")

                    if not used_food:
                        textbutton "See if there's a faster option":
                            text_size 24
                            action Return("food")

                    if not used_peek:
                        textbutton "Just check the menu":
                            text_size 25
                            action Return("peek")

            else:

                if not used_food:
                    textbutton "Open the coupon":
                        text_size 30
                        action Return("food")

                if not used_compare:
                    textbutton "Check nearby breakfast spots":
                        text_size 28
                        action Return("compare")

                if not used_commit:
                    textbutton "Look at directions":
                        text_size 26
                        action Return("commit")

                if not used_compare:
                    textbutton "Compare breakfast combos":
                        text_size 26
                        action Return("compare")

                if not used_commit:
                    textbutton "Pick the closest location":
                        text_size 24
                        action Return("commit")

# ---------- GAME START ----------
label start:

    play music intro_crawl fadein 1.0

    scene black
    $ crawl_result = renpy.call_screen("opening_crawl")
    if crawl_result == "auto_end":
        $ renpy.call_screen("opening_crawl")

    stop music fadeout 1.0

    jump bedroom_intro


# ---------- BEDROOM INTRO ----------
label bedroom_intro:

    scene bedroom

    play music birds fadein 1.0

    n "{fi=0-1.2-60}Today is the day.{/fi}"
    n "The ransom expires in twelve hours."
    n "The President of Humanity is still captive."
    n "The world is waiting for its greatest super soldier."

    k "..."
    k "Yawn..."

    $ get_up_clicks = 0
    $ bed_time_left = 8.0

    jump bed_loop


# ---------- BEDROOM LOOP ----------
label bed_loop:
    
    $ result = renpy.call_screen("bed_choice")

    if result == "try_get_up":
        jump get_up_attempt

    elif result == "get_up":
        jump got_up_in_time

    elif result == "timeout":
        jump bed_timeout


# ---------- FAILED GET-UP ATTEMPTS ----------
label get_up_attempt:

    $ get_up_clicks += 1

    if get_up_clicks == 1:
        k "{fi=0-0.5-20}Jeez, what time is it?{/fi}"
    elif get_up_clicks == 2:
        k "Oh damn, I should probably get up soon..."
    elif get_up_clicks == 3:
        k "{sc=3}God, the sun is bright.{/sc}"
    elif get_up_clicks == 4:
        k "{sc=4}Alright. No more messing around.{/sc}"
    elif get_up_clicks == 5:
        k "{omega=SC=3@FI=0-0.8}On your feet, soldier.{/omega}"

    if bed_time_left <= 0:
        jump bed_timeout

    jump bed_loop


# ---------- SUCCESS PATH ----------
label got_up_in_time:

    show kyle_sleepy at left

    k "{fi=0-1.0-40}Ugh... this sucks.{/fi}"
    n "Kyle swings his legs over the side of the bed and finally stands."
    n "He rubs his neck to loosen up the stiffness from a restless night."
    k "Okay... time to be the hero."

    jump mission_prep

# ---------- TIMEOUT PATH ----------
label bed_timeout:

    play sound door_open
    n "The door slams open."

    show aide neutral at right

    a "Sir, I hate to bother you but, uh..."
    a "You really need to get up. The President's life is on the line here."
    a "Based on how many fingers we've gotten in the mail, he only has like four left."

    show kyle_sleepy at left

    k "I know, I know. Just uhh... give me a minute, okay?"
    k "I'll be in the briefing room in a bit."

    hide commander
    with dissolve
    
    k "Okay... time to be the hero."

    jump mission_prep


# ---------- MISSION PREP ----------
label mission_prep:

    stop music fadeout 1.0

    scene brief:
        zoom 2
    with fade

    show commander neutral at right
    show aide neutral at left
    show kyle at center:
        zoom 1.5

    play music brief fadein 1.0

    n "There is a great clamor in the briefing room as the world's greatest super soldier enters."
    n "The Commander and his Aide are waiting for him."
    n "Several analysts stop arguing long enough to stare."

    a "He's here."

    c "Finally."

    k "Sorry for the delay, everyone."
    k "Any status updates before I wipe out these fools?"

    c "We received another transmission from Lizard Squad twelve minutes ago."
    c "They've relocated President Graham to an abandoned research facility in District Nine and reiterated their demands."

    k "Still five million V-Bucks?"

    a "They also want access to our internal servers so they can scrape combat data and use it to improve their algorithms."
    a "They seem to have quite the fascination with your work."

    k "Well, they're gonna get a good idea of what I'm capable of by the end of the day, that's for sure."
    k "And I'm gonna be the only scraping..."
    k "scraping their..."
    k "ya know, {sc=}remains{sc} off my armor after I'm done with them."
    k "..."
    k "Sorry, my one-liners are rusty."

    c "Focus, Kyle."

    n "The Commander waves his hand over the holographic table."
    n "A flickering map of the city rises between them, crowded with red markers, warning icons, and dramatic blinking lights."

    c "This is the target zone."
    c "Lizard Squad controls the outer perimeter and most of the airspace with their freaky drones."
    c "No conventional unit has been able to break through."

    a "Every recon team we've sent in has either retreated or been turned into what the report describes as 'debris.'"

    k "Sounds about right."

    c "That's why we need you."
    c "You are the only operative with the experience, grit, and sheer narrative importance necessary to pull this off."

    k "I've heard that before."

    c "And with all the training simulations you've done over the past month to prepare, we have full confidence that you can pull this off solo."

    k "Right..."
    k "It's still weird to me that we didn't just give them the money, though. Is this mission really worth the risk?"

    c "We don't negotiate with terrorists, Kyle. Especially not these disgusting clankers."
    
    a "This is taxpayer money we're talking about. We have potholes to fix and yacht clubs to maintain."
    a "Besides, we ran the numbers using our internal AI."
    a "Your odds of success are astronomically higher than everyone else's."

    k "Never tell me the odds."

    c "Your insertion route is already prepared. You'll have to touch down in District Four and make your way to the objective on street level to avoid suspicion."
    c "We suggest you leave immediately."

    n "Kyle looks over the map, still waking up."
    n "The room expects confidence. Heroism. A speech, maybe."
    n "Instead, he sighs and mentally prepares himself for a long day at work."

    c "Do you understand the mission?"

    menu:
        "Yeah. Save the President, stop the terrorists, try not to die.":
            c "Good."
            a "I knew he was listening."
            k "Let's get this done."
            jump mission_launch

        "No, explain the obvious plan to me one more time.":
            c "Fine."
            c "You will infiltrate District Nine, breach the facility, neutralize hostile resistance, secure the President, and extract before the deadline."
            a "So, in summary, save the President, stop the terrorists, try not to die."
            k "Great. Another day, another V-Buck."
            jump mission_launch


label mission_launch:

    n "The briefing room erupts into motion again."
    n "Technicians shout over one another. Screens shift from red to amber. Somewhere nearby, an alarm begins pulsing in a slow, theatrical rhythm."

    c "Get suited up."
    c "We're out of time."

    k "Yeah."
    k "Story of my life."

    stop music fadeout 1.0

    jump city

# ---------- CITY ----------
label city:

    scene city
    
    play music city fadein 1.0

    show kyle:
        zoom 1.5

    $ hunger_pressure = 0
    $ city_progress = 0
    $ food_locked = False
    $ used_peek = False
    $ used_compare = False
    $ used_food = False
    $ used_commit = False

    k "Here we go... just gotta walk three miles and sneak into enemy territory."
    k "Man, my stomach is growling."

    jump city_loop

label city_menu_return:

    jump city_decision


# ---------- CITY LOOP ----------
label city_loop:

    if city_progress >= 5:
        jump mission_path

    if city_progress == 0:
        n "Kyle starts down the avenue toward District Nine."
    elif city_progress == 1:
        n "He makes decent progress before the city starts thinning out."
    elif city_progress == 2:
        n "The streets ahead look emptier now. The target zone can't be much farther."

    jump city_interrupt


# ---------- DISTRACTION INTERRUPT ----------
label city_interrupt:

    play sound buzz
    n "{sc=3}bzzz{/sc}"

    if hunger_pressure == 0:
        n "Kyle's wrist vibrates. He lifts his arm and checks the holographic display."
    else:
        n "Another notification."   

    if hunger_pressure == 0:
        n "\"All-Star Breakfast Jam now available two blocks away.\""
        n "\"20 percent off for first responders, active soldiers, and chosen heroes!\""
        k "That does sound pretty good, actually."
    elif hunger_pressure == 1:
        n "\"Reminder: breakfast combo expires soon.\""
        n "\"Includes flapjacks, pancakes, and hotcakes!\""
        k "I do love all of those things..."
    elif hunger_pressure == 2:
        n "\"You are 0.4 miles from a participating location.\""
        n "\"Estimated detour: minimal.\""
        k "I guess it wouldn't take too long to swing by..."
    elif hunger_pressure == 3:
        n "\"Skipping meals reduces combat performance by 18 percent.\""
        n "\"Would you like directions?\""
        k "Okay, now it's giving tactical advice."
    else:
        n "\"FINAL CALL: All-Star Breakfast Jam.\""
        n "\"Be honest. You are not going to save the President on an empty stomach.\""
        k "God, these targeted ads creep me out."

    jump city_thoughts


# ---------- INTRUSIVE THOUGHTS ----------
label city_thoughts:

    if hunger_pressure == 0:
        n "{fi=0-0.4-15}You can just chug the nutrient sludge in your suit later.{/fi}"
    elif hunger_pressure == 1:
        n "{fi=0-0.4-15}Then again, it would only take five minutes.{/fi}"
        n "{sc=2}You'd think better with food.{/sc}"
    elif hunger_pressure == 2:
        n "{fi=0-0.4-15}Better to eat now and just get it over with.{/fi}"
        n "You know it'll be on your mind all day if you don't."
    elif hunger_pressure == 3:
        n "{fi=0-0.4-15}This is basic preparation.{/fi}"
        n "{sc=3}No one fights well on an empty stomach.{/sc}"
        n "{move}Just check the menu.{/move}"
    else:
        n "{fi=0-0.4-15}You're already thinking about breakfast.{/fi}"
        n "{sc=4}You are not focused.{/sc}"
        n "{move}You should just eat first.{/move}"

    jump city_decision


# ---------- CITY DECISION ----------
label city_decision:

    $ city_choice = renpy.call_screen("city_choice_screen")

    if city_choice == "walk":
        jump ignore_food
    elif city_choice == "walk_hard":
        jump ignore_food_hard
    elif city_choice == "food":
        $ food_locked = True
        $ used_food = True
        jump food_branch
    elif city_choice == "peek":
        $ food_locked = True
        $ used_peek = True
        jump food_peek
    elif city_choice == "compare":
        $ food_locked = True
        $ used_compare = True
        jump food_compare
    elif city_choice == "commit":
        $ food_locked = True
        $ used_commit = True
        jump food_commit


# ---------- IGNORE FOOD ----------
label ignore_food:

    $ hunger_pressure += 1
    $ city_progress += 1

    if hunger_pressure == 1:
        k "No. Mission first."
        n "Kyle lowers his arm and keeps moving."
    elif hunger_pressure == 2:
        k "My nutrient sludge will be just fine."
        n "A delivery drone cuts overhead, trailing the smell of grease and sugar."
    elif hunger_pressure == 3:
        k "I am not getting derailed by a breakfast ad."
        n "He keeps walking, but now he's thinking about various cakes."
    else:
        k "This is getting stupid."
        n "Kyle shoves the display out of sight and picks up the pace."

    jump city_loop


# ---------- HARDER IGNORE ----------
label ignore_food_hard:

    $ hunger_pressure += 1
    $ city_progress += 1

    k "No."
    k "No, I'm doing the mission."

    play sound buzz
    n "{sc=4}bzzz{/sc}"
    n "Another notification appears before he can drop his arm."

    n "\"Last chance to claim your breakfast reward.\""

    if hunger_pressure >= 5:
        n "{sc=3}Kyle looks up. Somehow, several more minutes are gone.{/sc}"

    k "Oh, come on."

    jump city_loop


# ---------- FOOD PEEK ----------
label food_peek:

    $ hunger_pressure += 1

    n "Kyle opens the notification and immediately regrets how easy that felt."
    n "\"All-Star Breakfast Jam. Limited time only.\""
    n "\"Combo includes a commemorative cup while supplies last!\""

    k "Oh, that's kinda neat."

    jump city_menu_return

# ---------- FOOD BRANCH ----------
label food_branch:

    n "Kyle hesitates for exactly long enough to count as a decision."

    k "Okay, this is not quitting the mission."
    k "This is a tactical breakfast."

    menu:
        "Get something quick and cheap":
            jump food_commit

        "Keep browsing":
            jump food_compare


# ---------- FOOD COMPARISON ----------
label food_compare:

    $ hunger_pressure += 1

    n "Kyle opens the list of nearby locations."

    k "Why are there so many options?"

    n "He scrolls for several seconds longer than necessary."

    jump food_compare_menu


label food_compare_menu:

    menu:
        "Pick the closest one":
            jump food_commit

        "Compare locations":
            n "\"The one on 14th street is 3 percent cheaper.\""
            n "\"The one on 12th street has better reviews.\""
            n "\"The one on 10th street is closest, but there are some weirdos who hang out there.\""
            k "This is a ridiculous amount of information."
            jump food_compare_menu


# ---------- FOOD COMMIT ----------
label food_commit:

    stop music fadeout 1.0

    n "Kyle turns sharply away from District Nine."
    n "The hostage site remains on the horizon, blinking red through the smog."

    k "Five minutes. Ten, max."
    k "Then I save the President."

    jump breakfast_scene


# ---------- MISSION PATH ----------
label mission_path:

    stop music fadeout 1.0

    n "Against all internal logic, Kyle keeps moving toward District Nine."
    n "The abandoned facility rises above the city like a bad decision someone else made."

    k "Okay."
    k "No more distractions."

    jump tower_approach

# ---------- BREAKFAST ----------
label breakfast_scene:

    scene diner

    show kyle at left: 
        zoom 1.5

    k "Man, I haven't been here in forever. It has such a cool retro feel."
    
    show server at right  
    with fade
    s "Hey there, sweetie. What can I get ya?"

    k "Hi, I'll take the All-Star Breakfast Jam, please. And an orange juice with extra pulp."

    s "Oh sorry hon, we're all outta OJ. Global shortages and all."

    k "Right, of course. Just a water, then, thanks."

    hide server neutral
    with fade

    n "The intoxicating smell and comforting din of the restaurant puts Kyle at ease momentarily."
    n "Even so, every minute spent here feels like procrastination."
    n "The detour only adds to his simmering anxiety about the mission."
    n "There's a ticking clock somewhere in the background, and the President's life is hanging in the balance."
    n "Lost deep in thought, his food arrives before he realizes any time has passed at all."

    show server at right
    with fade
    s "Here ya go, shnookums. Pancakes, hotcakes, and flapjacks. Enjoy!"

    k "Thank you."

    hide server
    with fade

    n "Kyle enjoys his well-discounted meal."
    n "For a while, the mission, the ransom, and the whole weight of the day feel strangely far away."

    n "\"Kyle?\""

    show tanner at right:  
        zoom 2
    with fade

    k "..."

    k "Tanner?"

    t "No way! It is you."
    t "I thought that was you under that visor, but I figured there was no chance you would be eating breakfast alone in a place like this."

    k "Yeah, well... humanity's last hope has gotta eat sometimes." 

    t "Riiight, well you better get those macros settled or a clanker might kick your ass next time."

    k "*chuckle*"

    n "The years between them seem to collapse all at once."
    n "For a moment, Kyle is not a super soldier, or a national symbol, or the man responsible for saving the President."
    n "He's just a guy from college who got spotted by someone who knew him before everything changed."

    jump breakfast_tanner_intro


label breakfast_tanner_intro:

    t "Mind if I join you? I'm just enjoying a day out on the town."

    menu:
        "Yeah, sure.":
            k "But I'm not paying for your meal."
            t "Damn, even after all these years? You've changed, man."
        "(jokingly) I'm kind of in the middle of something, actually.":
            t "Oh, I get it. You're too famous for little ol' me."
            k "Nahhh, sit down."

    n "Tanner settles in across from him."
    n "Kyle suddenly becomes very aware of how long it has been since he had a conversation with someone who knew him before the armor."

    jump breakfast_tanner_intro_2


label breakfast_tanner_intro_2:

    k "So, uhh... how have you been?"

    t "Oh I've been great. Work is steady, family's doing well."
    t "The kids are four and six now, and Jessie's about five months along with our third."

    k "Oh wow, congrats. You're in dangerous territory now. You two are gonna be outnumbered in your own house."

    t "Ha, yeah... it won't be easy, but at least we'll be more prepared now. At least, I'd like to think so."
    t "What about you? How's the service treating you?"

    k "Not too bad, I suppose. I'm actually in the city for, uhh... well, you could probably guess why."

    t "Oh really, what's going on? Was there another attack or something? I don't really keep up with the news."

    k "..."
    k "Yeah, something like that."
    k "But we don't have to talk about that. My whole life revolves around the military." 
    k "It gets exhausting after a while."

    t "Oh for sure, I get it."

    $ talked_college = False
    $ talked_work = False
    $ talked_mission = False

    jump breakfast_tanner_hub

label breakfast_tanner_hub:

    if talked_work and talked_college and talked_mission:
        jump breakfast_tanner_wrapup
    
    menu:
        "Ask about work." if not talked_work:
            $ talked_work = True
            jump topic_work

        "Talk about college." if not talked_college:
            $ talked_college = True
            jump topic_college

        "Talk about the mission." if not talked_mission:
            $ talked_mission = True
            jump topic_mission


label topic_work:

    k "So, what do you do for work again?"
    
    t "I'm still at eCorp doing software development. I actually just got promoted last month, so I'm managing a few people now."
    t "I can't tell yet if the extra pay is worth the extra stress, but it's nice to have more stability for the family."

    k "Yeah, stable sounds nice."

    t "I guess your work's a little more exciting than mine though."
    t "Every time I catch a glimpse of you online, I still can't believe a philosophy major ended up a super soldier. That's pretty wild."

    k "Ha, yeah. It's been a weird journey. I'm still not sure how I got here, honestly."

    t "Yeah, everyone was stunned when you first enlisted after graduation. Just a total swerve from what we expected."

    k "Well, ya know, I was kind of lost after college. I thought about grad school for a while, but I couldn't justify it."
    k "Then the economy crashed for the eighth time in our lifetimes, and EarthGov started offering those signing bonuses."
    k "I felt like I had to do it just to stay afloat and find a purpose. And now, here I am ten years later..."
    k "A hero, allegedly."

    t "Don't act all modest! I heard about all those medal ceremonies. Your name comes up in the news a lot." 
    t "People look up to you."

    k "I thought you didn't watch the news?"

    t "Well, ya know... I catch things every now and then."

    k "Sure."
    k "..."
    k "Sorry, I just feel awkward talking about this stuff."
    k "I really don't see myself as anything special, but people keep treating me like I am. It's weird."

    t "I get that. It must be hard to live up to that kind of expectation all the time."

    k "To be honest, I don't really care what most people think of me. I just want to do my job and live comfortably."
    k "I don't know if just comes with the territory, but I feel like I have to disconnect myself from the reality of the situation."
    k "Like, I know what I do is important. I save people, and I make a real difference."
    k "But I don't feel like I belong in this role. I just happen to be really good at it."

    t "I guess I can relate. When I took that promotion, I knew it was the right move for my family, but I don't know if I really wanted to be a manager."
    t "But the bosses like me, and it seemed like the next step."

    k "I guess that's just work, huh?"
    k "The difference is if I'm not prepared or motivated to do my job, some seriously bad shit could happen."
    k "And for me, motivation is hard to come by."
    k "Like, I have so many important things I could be doing right now, but I stopped in here just to get a break from it all."
    k "Sometimes I feel like I'm back in college just finding any excuse to procrastinate on an essay because I can't will myself to work on something I don't care about."
   
    t "Ha, I remember those days. You'd be playing video games all day and then pull an all-nighter just to finish something that was due at 8am."
   
    k "Yeah, well I'd like to think I've grown a little bit since then at least."
    k "And I'm mostly used to the pressure of the job by now, but I still get overwhelmed sometimes when there are a million things begging for my attention."
    k "So many people waiting to be saved..."
    k "..."
    k "Sorry. I don't mean to vent. I don't get the chance to have real conversations very often."

    t "No worries, man. It's just nice to catch up."

    k "Yeah, it is."

    jump breakfast_tanner_hub


label topic_college:

    k "Man, it's crazy to think about how long it's been since college. It feels like a different lifetime."

    t "I know, right? We're so old now." 
    t "But I guess all that cybernetic stuff in your body keeps you looking young, right?"

    k "Among other things. But I don't think anything can undo the damage I did to my liver back then."

    t "Dude, you were an animal! I've never seen someone drink so many shots and stay on their feet the whole night."

    k "Yeah, alcoholism was so cool back then. Now everyone's gone all woke."

    t "Haha, they've gone what?"

    k "Never mind. That's just an old slang word from like a hundred years ago. I watch a lot of documentaries during peace time."

    t "Oh, that's interesting."

    k "Yeah, I think it's basically just a joking way of calling someone a goody-two-shoes."
    k "Like, they're trying to help and improve the world but..."
    k "Actually, now that I think about it, I don't know what the negative part is supposed to be."

    t "Well, I think it's for the best that we don't drink like that anymore."
    t "That's how my first kid happened, and I was way too young for that."

    k "Yeah, you really had to grow up fast, huh?"

    t "I sure did. But I don't regret any of it."
    t "We had a blast, I met lots of great people, and I didn't even go into debt."
    t "And the kid is cool too, I guess."

    k "Ha, no debt must be nice. No need to sell your body to the government to cover the 300,000 V-Bucks they're hunting you down for."

    t "I don't take it for granted, that's for sure."
    t "..."

    k "..."

    t "..."
    t "Do you ever think about how much simpler things were back then?"

    k "In college?"

    t "No, like in the far past. A hundred years ago, like the documentaries you mentioned."

    k "Oh, sure."

    t "I wouldn't give up my life now or anything, but I'd be so fascinated to live in, like, the 2020s for a while."
    t "They didn't know how good they had it."

    k "Yeah, I know what you mean. But I think every generation feels that way to some extent."
    k "Rose-colored glasses and all."

    t "Maybe. But that doesn't mean it's not true."

    k "Touché."

    jump breakfast_tanner_hub


label topic_mission:

    k "So you really have no idea what's going on in District Nine?"
    
    t "I've heard a few things in passing, but I don't really know much. Some more clankers causing trouble, I guess?"

    k "Yeah, but it's pretty serious this time."

    t "Oh man, we're not gonna go into another lockdown are we? I'm supposed to go to a concert this weekend."

    k "Nah, I'll take care of it. They don't stand a chance."
    k "I just have to, ya know... make my way there and complete the objective."

    t "So why are you here eating griddlecakes?"

    k "..."
    k "Eating what?"

    t "Griddlecakes, dude. You have three plates of griddlecakes on the table right now."
    t "I know you're a big buff hero, but that's a ton of carbs."

    k "I can't even..."
    k "Okay, these are flapjacks..."
    k "These are pancakes..."
    k "And these are hotcakes. It's a well-balanced meal."

    t "Pfft, whatever you say, Kyle."
    t "But seriously, why are you here in your armor? Are you like, on the clock right now?"

    k "I'm just killing time, I guess. And it's been a long time since I had a real meal."
    k "When I'm on active duty, I'm only allowed to eat this nutrient sludge they give to all the soldiers."
    k "They track my body like I'm a pig they're trying to fatten up for an auction."

    t "Damn, that sucks. So when's the last time you had a milkshake from Jimmy's?"

    k "Oh jeez... senior year?"
    k "God, I miss that place. Those things were so damn good."

    t "Well, believe it or not, they're just as good as you remember. Private equity hasn't ruined them yet."

    k "That's a relief."

    jump breakfast_tanner_hub

label breakfast_tanner_wrapup:

    n "What starts as a quick catch-up turns into something deeper."
    n "Kyle and Tanner talk for a long time, reminiscing about the past and sharing their thoughts on life, work, and the future."
    n "They lose track of time as they sink into their old friendship."

    t "Man. I didn't mean to keep you this long."

    k "No, it's fine."
    k "This was nice."

    t "Still."
    t "You've probably got somewhere to be."

    k "Eh, I'll figure it out. I always do."
    k "Even if it's at the last minute."

    t "Well hey, we should hang out sometime if you're in the city again. Maybe you could meet the family." 
    t "Or just a guy's night out, whatever you feel like doing."

    k "Yeah, that would be cool."

    t "Well, it was good seeing you, Kyle."
    t "Be safe out there."

    k "You too, Tanner. See you around."

    hide tanner
    with fade

    n "Kyle sits there for a moment after Tanner leaves, feeling the weight of the day settle back onto him."
    n "There is work to be done."
    n "With a sigh, he stands up and exits the diner, ready to bear the burden of his role."

    jump city_return

# --------- ENDING ----------
label city_return:

    scene city
    with fade

    play music city fadein 1.0

    show kyle:  
        zoom 1.5
    n "The city feels louder when Kyle steps back outside."
    n "Traffic drones scream overhead. Somewhere in the distance, an emergency siren rises and falls."
    n "The mission is still waiting."

    play sound buzz
    n "{sc=3}bzzz{/sc}"

    k "..."

    n "Kyle checks the time."
    n "It's later than he expected."

    k "Welp, time to save the world again."
    k "No more distractions."

    n "To be continued..."
    return