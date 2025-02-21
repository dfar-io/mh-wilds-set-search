import random

class Result:
    def __init__(self, helm, mail, braces, coil, greaves):
        self.helm = helm
        self.mail = mail
        self.braces = braces
        self.coil = coil
        self.greaves = greaves

    def __repr__(self):
        return f"{self.defense()}: {self.helm.name}, {self.mail.name}, {self.braces.name}, {self.coil.name}, {self.greaves.name}"

    def defense(self):
        return self.helm.defense + self.mail.defense + self.braces.defense + self.coil.defense + self.greaves.defense
    
    def matches_search_criteria(self, search_criteria):
        # leaving off here - take a look at the TypeScript code for reference
        random_number = random.random() * 10
        return random_number > 9
