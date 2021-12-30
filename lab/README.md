# Lab: Soul of a new machine

## Overview

In the 1960s, the first chatbot, [Eliza](https://web.njit.edu/~ronkowit/eliza.html), appeared on the scene. When users chatted with the bot, [they experienced all kids of unusual emotions](https://99percentinvisible.org/episode/the-eliza-effect/); in essence, many people thought they were chatting with a real person. They asked it deep questions and it responded. They asked for life advice, and it was there. 

What we're going to do today is much more "naive" -- that is, simpler -- but it's still an interesting idea that a chatbot can modulate (i.e. change) how we feel about ourselves and our interactions with technology. 

Today you'll program a conversation with a chatbot named `Robby`, and understand a bit about "states" -- both techincal and physical. You can make them happy, sad, or confused. But, the point is that you will be able to take an action and cause a change in an object. 

In this lab, you'll practice using:

* files
  * `JSON` particularly
* objects
* methods
* general problem solving
* curiously, compassion

This exercise will rely heavily on previous knowledge and abstracting -- that is, generalizing -- how you can use these ideas to solve the tasks this week.

## Requirements

More practically, you're going to "train" the chatbot on a file (`words.json`) located in the neighbor `data` folder, and then talk to the bot. The rules are that there are four methods to use with `Robby`:

|Method |Parameters |Description |
|:------|:----------|:-----------|
|`on()`   |None       |Powers `Robby` on; this must be done to talk to it |
|`off()`  |None       |Powers `Robby` off; do this before ending the program |
|`train()`|A `dictionary` of terms with relative scores representing "positive" or "negative" meaning|Gives `Robby` context as to what humans think is positive or negative |
|`tell()` |A `string` of text to tell `Robby`|Talks to `Robby`, receives a response |

### Program

Your program must:

* allow you onduct a conversation with `Robby` until you've said "Goodbye"
  * here, consider using `upper()` or `lower()` to guarantee it happens
  * this should involve a loop of a specific type -- consider which best models _behavior_
* looks like the sample below
* uses all four methods of the `robby` object 
* implement`load_file` function to load the `JSON` file (`data/words.json`)
* `train`s `ROBBY` on the above-named file
* contains at least `10` comments describing various state changes and functionality
  * i.e. "ROBBY on", et al.

#### Sample output

```
ROBBY > I'm alive!
YOU > Hi
ROBBY > Hello.
YOU > Are you a good or evil robot?
ROBBY > I'm happy to hear that!
What do you think?
YOU > Thanks for being so willing to hear my ethical questions.
ROBBY > I'm happy to hear that!
YOU > I think you're evil.
ROBBY > That makes me sad.
YOU > Like, very evil.
ROBBY > That makes me sad.
YOU > I'm sorry to make you sad, but you're, well...EVIL!
ROBBY > That makes me sad.
YOU > Goodbye
ROBBY goes to sleep.
```

## Writing

* A [completed reflection](writing/reflection.md) which:
  * Is at least `250` words
  * Features _no_ `TODO`s
