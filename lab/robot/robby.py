# /usr/bin/python

import string

class Robby:
    
    def __init__(self):
        
        self.power = False
        
        self.states = {
            "start": self.start,
            "neutral": self.neutral,
            "positive": self.positive,
            "negative": self.negative,
            "negate": self.negate,
            "error": self.error
        }
        
        self.responses = {
            "neutral": "I don't know how to feel about that.",
            "negative": "That makes me sad.",
            "positive": "I'm happy to hear that!",
            "error": "I'm sorry, I don't understand."
        }
        
        self.greetings = [
            "hi",
            "hello",
            "hey"
        ]
        
        self.goodbyes = [
            "bye",
            "goodbye"
        ]
        
        self.negatives = []
        self.positives = []
        
        self.question = False
        
    def tell(self, message, state = "start"):
        
        if state == None: state = self.start
        if not self.power: return "You must power Robby on."
        self.question = True if message[-1] == "?" else False
        
        message = "".join([ch for ch in message if ch not in string.punctuation])
        
        for word in message.split():
            if word.lower() in self.greetings:
                return f"ROBBY > Hello."
            if word.lower() in self.goodbyes:
                return f"ROBBY > Goodbye."
        
        handler = self.states[state]
        
        while True:
            state, message = handler(message)
            # End
            if len(message.split(None, 1)) < 1:
                response = f"ROBBY > {self.responses[state]}"
                if self.question:
                    response = f"{response}\nWhat do you think?"
                return response
            else:
                handler = self.states[state]
        print("Please provide a message.")
    
    def train(self, words):
        for word in words:
            if int(words[word]) < 0:
                self.negatives.append(word)
            else:
                self.positives.append(word)
    
    def parse(self, message):
        parts = message.split(None, 1)
        word, body = parts if len(parts) > 1 else (message, "")
        return word, body
    
    def on(self):
        print("ROBBY > I'm alive!")
        self.power = True
    
    def off(self):
        print("ROBBY goes to sleep.")
        self.power = False
    
    # States
    
    def start(self, message):
        word, body = self.parse(message)
        if body:
            state = "neutral"
        else:
            state = "error"
        return state, body
        
    def neutral(self, message):
        word, body = self.parse(message)
        if word == "not":
            state = "negate"
        elif word in self.positives:
            state = "positive"
        elif word in self.negatives:
            state = "negative"
        else:
            state = "neutral"
        return state, body
    
    def negate(self, message):
        word, body = self.parse(message)
        if word in self.positives:
            state = "negative"
        elif word in self.negatives:
            state = "positive"
        else:
            state = neutral
        return state, body
    
    def positive(self, message):
        word, body = self.parse(message)
        state = "positive"
        return state, body

    def negative(self, message):
        word, body = self.parse(message)
        state = "negative"
        return state, body
    
    def error(self, message):
        print("I don't know how to feel about that.")