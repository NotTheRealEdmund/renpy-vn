# Declare characters used by this game.
define friend = Character('Friend A', color="#ff8c00")
define me = Character('Player', color="#0000FF")

# To set to True,
# $ flag = True
default flag = False

# To check the flag, use the if statement:
# if flag:
#       // Do something

label start:
    
    play music "audio/song.mp3" fadeout 1.0 fadein 1.0
    
    scene bg school
    with fade

    friend "So how was the lecture?"
    me "It was okay I guess..."
    "To be honest, I had no idea what was being taught, but my pride prevented me from admitting that."
    "At least not in front of one of the few people who I still talk to in school to pass the time."
    "To me, having someone to talk to is somewhat of a privilege."
    "Used to solitude, I would say that having a friend by your side is definitely not something to be taken for granted."
    
    scene bg gray
    with fade
    
    friend "I'm taking this bus, bye."
    me "Bye, see you tomorrow at the tutorial."
    "My friend said as he got on the bus, while I am left waiting at the bus stop for the next bus to arrive possibly 15 minutes later."
    "..."
    "I swear, I wait absolutely ages for a bus to come, only to be greeted by 3 buses at once."
    "It's funny how the school boasts of it's bus tracking app being extremely accurate, when the bus drivers can't even coordinate to shorten the waiting time."
    "Instead of letting us know how long we have to wait, perhaps it would be more reasonable to not make us wait that long in the first place."
    "Then again, if there was no need to wait for the bus, the tracking app would lose its purpose..."
    "With such redundant thoughts in my mind, I got onto the bus which seemed to have the least number of people."
    
    scene bg bus
    with fade
    
    "Once I found a seat, I put on my earphones in an attempt to drown out all the other noises around me."
    "Blasting music did little to achieve that though, as the bus was still extremely packed, to my annoyance."
    "Can't say I'm a fan of crowds, but that doesn't mean I go out of my way to avoid them."
    "Every once in a while, hanging around with people you can't stand can bring about unexpected results."
    "Like learning to train your perseverance for example."
    "In this age of technological advancement, I've been thinking that it isn't too much of a stretch to expect someone to invent a machine which grants infinite self-control."
    "Like, you could just stick it onto your back and switch it on, and be able to endure just about anything, like a zen monk."
    "Guess that's just a pipe dream after all."
    "Before that turns into reality, the only choice humans have is to train their tolerance towards things they dislike..."
    
    stop music
    
    scene bg gray
    with fade
    
    "Before we go on any further, it's time for a short introduction."
    "This visual novel you're playing now is all about..."
    "..."
    "My unremarkable everyday life..."
    "..."
    "Surely you already guessed that from the title..."
    "But yeah, this game is just for me to have fun experimenting with this software."
    "And talking about pretentious shit which I occasionally think about, even though nobody cares, because I have no life."
    "Sometimes I can't help but feel like my time on this earth isn't being spent efficiently."
    "Just thinking about what successful people around my age has already achieved with their lives make me depressed..."
    "Talented artists who have drawings sold for millions..."
    "Or amazing programmers who invented life-changing apps with millions of downloads..."
    "Or even actors who have starred in blockbusters..."
    "All of them are living their lives to the fullest."
    "And me? I'm nothing but an average university student..."
    "And in case you haven't already realised..."
    "This is going to be an incredibly boring game."
    "Which is completely not going to be worth your time."
    "Not to mention, the production value of this game is close to zero."
    "The lack of character sprites are proof of that, though I guess I could just argue that it's trying to be avant-garde."
    "That's the standard excuse isn't it? From movies with ridiculous endings to songs with nonsensical lyrics to TV shows with actors who can't act."
    "And of course, a visual novel with a non-existent plot."
    
menu:
    "Now, despite all these warnings, do you still want to continue wasting your time playing this ridiculous game?"
    "Hell yeah":
        jump yeah
    "Hell no":
        jump no
            
label no:
    "I see..."
    "Well, I don't blame you, surely you have more important things to do with your life."
    "I'm sure you see playing this game as nothing more than a waste of time."
    "Just like I felt when creating this game."
    "But the thing is...wasting time is what life's all about."
    "The more time you spend doing \"pointless\" stuff, the better off you'll be."
    "It's the secret to enjoying life."
    "Besides..."
    "Don't get the wrong idea! It's not like I wanted you to play this game or anything!"    
    "{b}.:. Bad End.{b}"
    return
    
label yeah:
    play music "audio/song.mp3" fadeout 1.0 fadein 1.0
    "I see..."
    # To be continued
    "{b}.:. Good End.{b}"