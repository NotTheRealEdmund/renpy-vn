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
    
    stop music fadeout 1.0
    
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
    "But all of those were simply a \"if I had to choose\"."
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

    play music "audio/normal.mp3" fadeout 1.0 fadein 1.0
    
    scene bg school
    with fade
    
    "I head to the venue where I'm supposed to have my next lecture."
    "Coincidentally, my friend had the same lecture as me, and we sat together again."
    "Lectures usually comprise of way more students than tutorials and are generally very one-sided, since only the lecturer is speaking, which makes it kinda boring."
    "Usually many students, such as my friend and I, don't pay much attention after a while."
    "My friend usually gets distracted by his phone games after we've lost our concentration within the first hour."
    "As for myself, I might seem like I'm paying attention, but in actual fact, I'm not. Not at all."
    "It's just that there was nothing to do. Nothing I could do. So I simply blanked out."
    "Speaking of phones, most people use phones for playing games it seems. I happen to be excluded from that group but I could understand how addicting they could be."
    "It's ironic that most people do not use phones for the primary purpose of contacting others, and that is especially true for me."
    "I could count the number of contacts I have in one hand, and I even have their numbers memorized."
    "But that's simply because a call from them is so rare that the moment the number pops up on my phone screen, I instantly think of who might be calling me and associate that number to that person."
    "The same thing applies for messages."
    "Then again, I don't really see the appeal of racking up a huge phone bill by firing off pointless texts or killing time with useless banter."
    "Sometimes I hear people having ridiculous amounts of mobile data per month and wonder if I could even use that much in an entire year."
    "To be honest, I view phones in general as a means to look up information rather than as a communication device."
    "Smartphones are pretty much a mini-computer which allows you to find out what you need to know anytime, and that's an undeniable convenience."
    "That said, there's also an aspect of smartphones which I find inconvenient."
    "The fact that there's an expectation that you'll answer the phone at any time, even if you're away from school or work."
    "There's no more escape." 
    "With communication being as powerful as it is now, you can still be told to work even if it's already past working hours."
    "Guess that's the price to pay for wanting to connect with others, you have no choice but to be connect even if you don't want to."
    "Before I knew it, the lecture has ended and I left the venue none the wiser. Nothing new, I guess."
    "..."
    friend "Bye."
    me "Bye."
    "The usual farewell."

    play music "audio/relax.mp3" fadeout 1.0 fadein 1.0
    
    scene bg bus
    with fade
    
    "On the bus back home, I started thinking about how my friend and I actually got along."
    "I mean, the obvious answer is probably coincidence."
    "We just happened to be in the same lectures and tutorials all the time."
    "Seeing each other all the time, we ended up as friends whether we liked it or not."
    "Truth to be told, I didn't expect to make friends with a single person at all since entering university."
    "Especially since my friend seemed just like me on the outside."
    "In other words, slightly anti-social, seemed difficult to approach."
    "But he proved to be quite a friendly person after getting to know him better."
    "The saying goes: Never judge a book by its cover."
    "This is a saying I can resonate with."
    "Just like with my friend, if I had just assumed his character back then, I might have to live through this boring school life all by myself."
    "It's dangerous to jump to conclusions about someone you don't know."
    "No matter your experiences in life, when you make a judgement without sufficient information, you're not going to be 100 percent right with your guesses."
    "And more often than not, that assumption comes back to bite you in the end."
    "On the frontlines, you might even end up dead."
    "Therefore, I try my best not to label others prematurely."
    "That being said, I guess some people actually do want to be labelled this way."
    "After all, it certainly takes way less time and effort to change your appearance than to change your personality."
    "And if people are distracted by your looks, then they probably wouldn't bother delving deeper into the skeletons in your closet."
    "Take women with all their make-up for example."
    "Isn't make-up basically something women use to hide stuff they don't want others to see?"
    "Like bags under their eyes, or freckles, or rough skin, or dry lips."
    "In my university, it's not uncommon to see women with make-up on their face while attending lectures and tutorials."
    "Although just me saying that is probably going to get me in lots of trouble."
    "..."
    "A man knows when to keep his trap shut."
    "That's something I've learnt far too late in life, but better late than never."
    
    scene bg bedroom
    with fade

    "As I was surfing the net, I've encountered the trolls of the internet once again."
    "These trolls are pretty much unavoidable, you'll encounter them no matter what you use the internet for."
    "They purposely say or do stupid things to get the attention of others by making them pissed off."
    "To be honest, some people dislike them, but I really enjoy their presence."
    "For one, to put in effort to reach a complete stranger like me...is quite admirable."
    "In real life, I am not recognised for who I am. To the university, I'm simply a university student. Nothing more, nothing less."
    "Nobody would go out of their way to make a \"light pole\" angry."
    "Another aspect that I really enjoy about their trolling is the proof that they are showing me their \"other face\"."
    "Those trolls would never show this side of them to their acquaintances in real life."
    "After all, human beings are multifaceted creatures."
    "In other words, there's usually more to people than meets the eye."
    "It's not uncommon for someone who seems one-dimensional at a glance to reveal a dramatically different side after getting to know them for a while."
    "In fact, many people don't stop at being \"two-faced\"."
    "There are plenty of people out there with three or four."
    "That explains why a scumbag would sometimes play the good guy, or vice versa."
    "These multiple faces are part of what makes people interesting, but they also complicate our relations with others."
    "No matter how slight it may be, no matter how well hidden it is, there will always be a side to a person's personality which will surprise you."
    "Which is why a lot of people want to protect their relations with others and end up never being able to show their \"other face\"."
    "The thing is though, that \"other face\" is also a part of them."
    "To completely disregard it is impossible."
    "So they need an outlet to express those sides of themselves."
    "For example though the internet, as trolls."
    "The anonymity which the internet provides can be very comforting to many and definitely should not be taken lightly."
    "..."
    "Here I am getting all empathetic over the trolls of the internet."
    "Must be a side-effect of living an unremarkable everyday life."
    "In fact, living such a unremarkable life demands certain skills of its own."
    "Such as the ability to find enjoyment in thinking up vague, meaningless matters that nobody cares about."
    "A skill like this is not completely useless though, since it's pretty much what politicians do all day anyway."
    "The only difference being that I don't get paid to do this on my own."
    "It also happens to be a skill that students require to write essays on how to solve a certain issue even though I'm pretty sure nobody actually cares about it."
    "Over the years, many batches of students must have already come up with thousands of ideas."
    "Yet none of them are actually implemented, otherwise there would be nothing much to discuss anymore."
    me "Now I'm just engaging in self-loathing..."
    me "..."
    me "Time to sleep..."
    
    scene bg black
    with fade
    
    "..."
    
    play music "audio/normal.mp3" fadeout 1.0 fadein 1.0
    
    scene bg train
    with fade
    
    "Today is a weekend."
    "Usually on weekends and holidays, I don't have anything in particular to do, and would usually get on the train."
    "There wouldn't be a destination in my mind though, I would simply take the train to wherever it took me, get off whenever I happened to feel like it, and explore the area."
    "It's not really something unusual for me."
    "Sounds like a waste of time, but as mentioned earlier, I happen to be quite good at it."
    "At times like this, I wonder what are normal ways of spending time?"
    "For people who aren't living an unremarkable life like me, for people who do things which makes them seem unique..."
    "They'd probably do things related to their dreams, passions, or at least interests."
    "And yet, knowing that, I don't have an urge to find one for myself, something to make me special."
    "..."
    "There are a lot of people who say that they don't want to become cogs in a machine."
    "They want to strive for excellence, to reach a position nobody can touch them."
    "Thing is, though, nobody's irreplaceable."
    "There's always somebody else who can do what you do."
    "In fact, there's no shame in being a cog, at least machines don't work without them."
    "For the most part, people who figure that out are the ones who turn out decent and manage to remain that way."
    "People who claim that they have achieved success, usually possess unconventional philosophies and only see the world through their own lens."
    "As strange as that sounds, these people obsess over the coherence of their twisted interpretation of reality even more than people who aren't successful."
    "A typical example would be the arrogance of software engineers."
    "Thinking that they are the best in their field, they end up looking down on everyone else, not knowing that the world doesn't only comprise of technology."
    "They end up being shunned by everyone else despite their expertise because they act like assholes all the time."
    "The same goes for CEOs and dictators."
    "That's not to say that all special people aren't decent, it's just that special people who aren't decent are usually able to cause greater damage to society."
    "A stopped cog will not cause a machine to explode, but an inexperienced engineer would."
    "..."
    "What are decent people like, anyway?"
    "Hard to say."
    "In fact, we're always told that \"unique\" individuals are valued by society for being able to think outside the box."
    "The way I see it, if you're too different from the rest of society, you're just going to be shunned and pushed outside the loop."
    "The saying goes: There's a fine line between genius and insanity."
    me "I can't be a cure, but at least I'm not poison, I'm just plain water..."
    "I smile wryly to myself as I got off the train."

    scene bg shop
    with fade
    
    "I walked around the unfamiliar street and entered a bookstore."
    "There were hardly any customers at all, and the bookstore was fairly old."
    "Not to mention, the products there probably wouldn't be displayed in the newer bookstores which were constantly being stocked up with only the latest items."
    "But that was exactly why I chose to enter this place."
    "It's a strange sensation, almost illogical in fact."
    "Sometimes, I end up being put off if the store is too classy."
    "In my opinion, every once in a while, something a little deteriorated is nicer."
    "In a way, it gives me a sense of relief."
    "For example, it's a lot more comfortable to eat in a simple fast food place than a restaurant even though a restaurant probably has better service."
    "When it comes to buying clothes, it's easier to step foot into a regular department store instead of a high-class store."
    "It's almost as if over-establishment can sometimes hurt a business."
    "Take the phone industry for example, phones have more and more unnecessary new features added to it over the years."
    "However, people don't really use them at all, in fact, those features only serve to increase the cost of phones which then put people off from buying them."
    "Sometimes I wonder if this applies to humans as well."
    "In other words, deliberately restricting one's potential in order to remain approachable, so that people around you don't feel insecure."
    "Then again, I guess those people are probably using that as an excuse for their mistakes."

    stop music fadeout 1.0
    "Strangely enough, I feel that this sensation is similar to how I would view people."
    "For example, a person who is good at everything, aces every examination, has an active lifestyle, and has no character flaws at all..."

menu:
    "Such a person..."
    "is someone I should strive to become":
        jump bad
    "would just creep me out":
        jump good

label bad:
    play music "audio/sad past.mp3" fadeout 1.0 fadein 1.0
    "Such a person is someone I should strive to become."
    "..."
    "That's right."
    "There's got to be a better way to living than this."
    "It doesn't have to be this way, I don't want to live an unremarkable life anymore."
    "It's not too late to change."
    "I can't change my past, but I can change my future."
    "I should not give up."
    "I'm sure I can do it!"

    scene bg rooftop
    with fade

    "Fast forward to 5 years later..."
    me "The wind here sure is strong..."
    "Here I am, on the rooftop of an abandoned building."
    "Surrounding the rooftop, was a very high fence, about 2 meters in height."
    "A wall you couldn't get past without climbing."
    me "Well, it's probably there to prevent suicide..."
    "It was simple enough to understand without having to ask anyone."
    "There was no need to make it so high for mere safety reasons."
    "Beyond that wall marking the divide between life and death, I stood at a standstill."
    "And not on the safe side, but in the \"death zone\" beyond the fence."
    me "How did it come to this?"
    "5 years ago, after I had a change of heart, I did everything I could to break out of my unremarkable everyday life."
    "I disregarded everything in the pursuit of success."
    "I became someone I couldn't recognise anymore."
    "I went out of my way to approach all the high-flyers, only to be avoided by them."
    "Somehow or another, they probably saw right through me, the fact that I only had intentions to use them."
    "Not only that, the one and only person I could call a friend left me."
    "At the same time, I couldn't ignore the feeling that I made a grave mistake."
    "Distracted by despair, I couldn't do well in studies or at work."
    "In the end, I yearned for a successful life, but was not able to achieve it."
    me "Finally, I understood my own powerlessness."
    "Whether it was my heightened expectations I had for myself, or my misunderstandings of what I was actually capable of..."
    "It doesn't matter anymore."
    "This is the only way I can escape from my wretched self."
    "If I had to single out one significant moment which lead to this day, it would be that moment at the bookstore."
    "Tempted by the notion of achieving excellence, I had given up my unremarkable everyday life..."
    "One which I was not ready to give up just yet."

    scene bg black
    with fade

    "I closed my eyes."
    me "Well then..."
    "I took a step forward."
    "..."
    "{b}.:. Bad End.{b}"
    return

label good:
    play music "audio/normal.mp3" fadeout 1.0 fadein 1.0
    "Such a person would just creep me out."
    "..."
    "Now I feel bad thinking that way. Since they're people who we should look up to."
    "I remember reading somewhere that you are the average of all the people who surround you."
    "In this case, shouldn't I be surrounding myself with people like that?"
    "Who knows?"
    "Not to mention, I'm definitely not of any interest to those people..."
    me "..."
    me "So stupid..."
    "I realised that hanging around people I don't like in order to change myself..."
    "...That is not my path."
    "If it was, I probably wouldn't be living such an unremarkable everyday life in the first place."
    "For better or for worse, I asked for this. No point in running away now and denying my entire way of life."
    me "..."
    "A smirk found its way onto my face."
    "Deciding that I've spent enough time at the bookstore, I left without buying anything."
    
    scene bg train
    with fade

    "Back on the train, I thought back to those people who were the embodiment of success."
    me "That is surely a lie."
    "If it seems too good to be true, it probably is."
    "They simply have very well hidden shortcomings, ones which people probably wouldn't even imagine."
    "This advice isn't limited to people either."
    "It can be applied to all sorts of things, from discounts to job offers to just about anything in this world."
    "Pull back when you are experiencing an advantage that, objectively speaking, shouldn't be possible."
    "Always keep that in mind unless you enjoy being taken advantage of."
    "The saying goes that there's no free lunch in the world." 
    "Truth is, nobody would even give you air if they can charge you for it."
    "In order to obtain something, you need to sacrifice something else."
    "Sometimes that may be money, sometimes that may be time." 
    "There are all sorts of possibilities, depending on the circumstances."
    "No matter what you have to let go of, it's fine if you get something back in return."
    "The problem comes when the latter doesn't hold true."
    "Even if I was to be the richest, most successful person in the world."
    "I might not really want that."
    "Then again, I'm probably just comforting myself at this point."
    me "Ah, so pathetic..."
    "..."
    "Suddenly, I saw the train approaching a familiar stop."
    "A place where I've been to quite a few times in the past."
    "A nostalgic place which I haven't been to in a while."
    "..."
    "I alighted at the next stop and headed to the destination in my mind."

    play music "audio/relax.mp3" fadeout 1.0 fadein 1.0

    scene bg rooftop
    with fade

    "This rooftop...holds some memories for me."
    "There were a few times where I tried to end my life here in the past when I despaired over my unremarkable everyday life."
    "Usually, those were over stupid things not even mentioning."
    "I always came here when I was sad."
    "But I haven't been here for a good while."
    "Probably because I no longer felt any sadness in my way of life."
    "Perhaps I matured without even knowing it."
    "Sounds a little silly, being in misery over something like that."
    "However, it's impossible to weigh one kind of unhappiness against another."
    "Another person's misfortune may seem trivial to you, but if it brings genuine distress and suffering, anything can be a tragedy to anyone."
    "Say, the grief of a man who has lost a lifelong friend, and the bitter sulking of a young girl forced to eat something she doesn't like."
    "There's no scale by which we can objectively measure misery."
    "People have the tendency to judge themselves happier or less happy relative to others, but such comparisons rest on the flawed assumption that all of us think and feel alike."
    "The suffering you experience is your own."
    "The pain you feel will never belong to anyone else. That's why it's precious."
    "That explains why some people, usually kids, tend to kick up a fuss over literally nothing."
    "Or why mentally ill patients have problems with living their lives even though that life might be a dream they had wanted to reach."
    "..."
    "Strangely enough, it felt as if..."
    "If the choice I made in the bookstore earlier was slightly different..."
    "I might have came back here but for a reason similar to those I had in the past..."
    "And I might have lost my life..."
    "..."
    "The meaning of life..."
    "Everyone who's ever felt powerless has worried about the meaning of their life at least once."
    "It's an unsolvable problem that everyone thinks about, and everyone believes a certain way about, but no one can answer for sure."
    "Maybe that's why the question has such an allure."
    "As for me, I don't need a meaning."
    "There is no need to hesitate in the face of my incomprehensible existence."
    "There's no need to look for a meaning in life."
    "I don't need to add anything to my world."
    "It is simply what it is."
    "In other words, the least and the most I can do..."
    "...is to live happily."
    "The same goes for you!"
    "No matter how unremarkable you believe your life to be, you must live happily!"
    "I created such a meaningless visual novel just to tell you this."
    "Guess I'm not cut out to be a writer. Haha! *bitter laugh*"
    "{b}.:. Good End.{b}"