class Pet:
    def __init__(self):
        self.food = 5
        self.happiness = 5
        self.energy = 5
        self.sleep = False

        self.locations = {}

    def sleep(self):
        self.sleep = True

    def wakeUp(self):
        self.sleep = False

    def pet(self):
        self.happiness += 1

    def feed(self):
        self.food += 3
        self.energy += 1
        self.happiness += 1

    def play(self):
        self.happiness += 3
        self.energy -= 2