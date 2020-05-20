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
    
    play music "audio/relax.mp3" fadeout 1.0 fadein 1.0
    
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
    "Like, you could just stick a switch onto your back and switch it on, and be able to endure just about anything, like a zen monk."
    "Guess that's just a pipe dream after all."
    "Before that turns into reality, the only choice humans have is to train their ability to tolerate things they dislike..."
    
    stop music
    
    scene bg gray
    with fade
    
    "Before we go on any further, it's time for a disclaimer."
    "In case you haven't already realised..."
    "This is going to be an incredibly boring game."
    "Which is completely not going to be worth your time."
    "Not to mention, the production value of this game is close to zero."
    "The lack of character sprites are proof of that, though I guess I could just argue that it's trying to be avant-garde."
    "That's the standard excuse isn't it? From movies with ridiculous endings to songs with nonsensical lyrics to TV shows with actors who can't act."
    "And of course, a visual novel with a non-existent plot."
    "It will seem as if these are ramblings I've written down and forgotten, and then all of a sudden shamelessly decide to create a visual novel about it."
    
menu:
    "Now, despite this warning, do you still want to continue wasting your time playing this ridiculous game?"
    "Hell yeah":
        jump yeah
    "Hell no":
        jump no
    
label no:
    "I see..."
    "Well, I don't blame you, surely you have more important things to do with your life."
    "Besides..."
    "Tsundere service~"
    "Don't get the wrong idea! It's not like I wanted you to play this game or anything!"    
    "{b}.:. Bad End.{b}"
    return
    
label yeah:
    
    play music "audio/relax.mp3" fadeout 1.0 fadein 1.0
    
    "I see..."
    "Well then, it's time for a short introduction."
    "This visual novel you're playing now is all about..."
    "..."
    "My unremarkable everyday life..."
    "..."
    "Surely you already guessed that from the title..."
    "So yeah, this game is just for me to have fun experimenting with this software."
    "And talking about pretentious shit which I occasionally think about, even though nobody cares, because I have no life."
    "Speaking of which, sometimes I just can't help but feel like my time on this earth isn't being spent efficiently."
    "Just thinking about what successful people around my age has already achieved with their lives make me depressed..."
    "Talented artists who have drawings sold for millions..."
    "Or amazing programmers who invented life-changing apps with millions of downloads..."
    "Or even actors who have starred in blockbusters..."
    "All of them are living their lives to the fullest."
    "Not to mention they are all probably younger than me."
    "And me? I'm nothing but an average university student..."
    "Some might say that that's good enough for one life..."
    "But this is an era where graduates are forced to lower career expectations because of the over-saturation of graduates."
    "Graduates are a dime a dozen, so even if you graduated, you are not exempt from facing tough competition everywhere."
    "In addition, my grades are nothing to boast about."
    "If anything, I should be a little ashamed."
    "Yet, it's not terrible."
    "It's simply unremarkable."
    
    scene bg bedroom
    with fade
    
    "Anyway today has been a tiring day."
    "I reached home and settled down in half an hour or so, before surfing the net for my daily sources of entertainment, just like everyone else."
    "You know, the usual...listening to music, watching uneducational videos etc."
    "Sometimes I wonder what would have become of me if I had some discipline to work on something productive every single day instead of following mediocrity."
    "Perhaps I would actually achieve something?"
    "Ironically, thoughts like this of wanting to be productive would only occur to me when I'm wasting time like this."
    "But the thing is...wasting time is what life's all about."
    "The more time you spend doing \"pointless\" stuff, the better off you'll be."
    "It's the secret to enjoying life."
    me "That's right, I have a tutorial in the morning tomorrow."
    me "I better get to bed early."
    
    scene bg black
    with fade
    
    "..."
    
    scene bg school
    with fade
    
    friend "Yo."
    me "Yo."
    "We exchanged light greetings with each other. If you could even call that a greeting whatsoever."
    
    stop music fadeout 1.0
    "As I was listening to the tutor's endless blatter about fourier transforms and complex numbers, I thought back to the past where I was full of anticipation for the future."
    play music "audio/sad past.mp3" fadeout 1.0 fadein 1.0
    
    "Now, my life is truly a boring one."
    "That's probably because I'm a boring person."
    "What makes this even worse is that I'm aware of it, painfully so..."
    "But I don't particularly hate myself for it."
    "I admit that I dislike and avoid unnecessary change."
    "For example, I don't go out of my way to pick up new hobbies."
    "Though that's probably also why I'll never be successful in my lifetime."
    "In my opinion, when it comes to hobbies and interests, anything is fine, even if it's stupid crap."
    "Whatever it is, they can be considered \"hooks\" to land as many \"fishes\" as possible."
    "Finding friends you can talk about some common interest with is a really valuable thing."
    "After all, you never know when those friends you have around you can give you that slight push you need to succeed in whatever you're trying to do."
    "..."
    "Having said that, I'm sure that even if I pick up some hobby, I wouldn't want to get involved with anybody who pursues the same interest."
    "I prefer doing things I like alone."
    "It's just easier that way."
    "I don't have to go about justifying my reasons for picking that hobby up or losing interest in that hobby."
    "Also, there's no need to compare with other people all the time."
    "..."
    friend "Hey copy that down, it's important."
    me "Okay, ... convolution ..."
    "While copying, I continued my train of thought."
    "Putting aside the fact that I basically have no hobbies, I think my personality is mostly to blame after all for my boring lifestyle."
    "The fact that I sense no urgency in having to improve my life is proof of that."
    "Here I am, pursuing a university degree simply because I had nothing else I really wanted to do in life."
    "Simply living an unremarkable everyday life is more than enough for me."
    "In fact, it might actually be considered a blessing to be able to live life without anything going on."
    "The saying goes: No news is good news."
    "..."
    "I wonder if I will ever regret thinking like this in the future?"
    "Just imagining my future self laughing at me right now the same way I do to my past self."
    "After all, my past self was pretty dumb, but I didn't realise it at the time."
    "I never imagined my future to be nothing but dark, with no dreams to chase after."
    "I had lots of dreams when I was little."
    "\"Becoming a firefighter to save lives sounds heroic!\""
    "\"Becoming an actor and getting all that attention didn't seem too bad either...\""
    "But all of those were simply a \"if I had to choose\""
    "There were no real convictions behind them."
    "Every attempt I make ends up being half-hearted."
    "I'm nothing but a mess of contradictions."
    "Simply by living a mediocre life, I was unable to face hardship, which was the drive I needed to succeed."
    "And now, I'll never get that back."
    "My vague life will just pass away with nothing but regrets."
    "Perhaps the biggest mistake I made while growing up was always being a \"good kid\"."
    "I would never get into any huge trouble, and I would always listen to others."
    "Adults around me would have increased expectations, and then it eventually seemed like it was normal no matter what I would do."
    "..."
    me "Well, no point in remembering stupid stuff."
    "As the tutorial approached its end, I started packing my stuff."

    play music "audio/relax.mp3" fadeout 1.0 fadein 1.0
    
    scene bg canteen
    with fade
    
    "I head to the canteen with my friend to have lunch."
    friend "Hey, what do you want to eat?"
    me "Whatever..."
    "..."
    "When it comes to meals, I don't have huge likes or dislikes."
    "Some people say that means I'm not a picky eater, but to be honest, I'm just not interested enough in what I eat to bother."
    "Perhaps an aftermath of the lessons beaten into me during the days I had been in military."
    "To put it nicely, the military would serve food which would drastically lower your expectations of what tasted good."
    "And thus, I've come to adopt the notion that a full stomach and adequete nutrition is all I really need from a meal."
    "That's not to say that I can't appreciate a good meal, it's just that I don't go out of my way to look for one."
    "Of course if the meal tastes good, that's a nice little bonus, but that shouldn't be the primary concern."
    "If I eat out, the only thing I'm concerned about is how much time it would take to queue for and finish my meal."
    "On the other hand, I'm somewhat puzzled by how some people are ridiculously picky eaters."
    "Always only looking for the kinds of food they like, not willing to try new food, and worse of all, being somewhat proud of that."
    "Saying things like \"I can only eat this.\" or \"I will never try this.\" all the time."
    "It's okay to have food you dislike, but to reject something before even trying it is beyond me."
    "In my opinion, you'll only embarrass yourself when you insist that you hate some food you've never eaten."
    "Then again, with the increasing number of vegetarians and vegans in the world raising their children with the exact opposite mindset, I might have to reconsider my opinion to avoid getting as much hate as possible."
    "In fact, religions as well, have quite a few dietary restrictions as well if I remember correctly."
    "That said, if the day ever comes when I would tell my child what they can eat and what they cannot eat without a proper reason..."
    "I think that'll be the day I go bungee jumping off the roof of a tall building without a cord."
    # To be continued
    "{b}.:. Good End.{b}"
