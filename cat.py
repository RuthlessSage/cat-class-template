#Remove pass and complete the cat class



class Cat():
    def __init__(self):
        self.name = "Unknown"
        self.age = 0
    def speak(self):
        return "Meow"
    
garfield = Cat()
garfield.name = "Garfield"
garfield.age = 50
garfield.speak()



stella = Cat()
stella.name = "Stella"
stella.age = 7
stella.speak()
