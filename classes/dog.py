from classes.mammal import Mammal

class Dog(Mammal):

    def __init__(self, name, is_good=True):
        super().__init__(name=name, rested=True)
        self.is_good = is_good

    def __repr__(self):
        return f"Dog(name={self.name}, rested={self.rested}, is_good={self.is_good})"

    def make_sound(self):
        return "generic DOG sound"

    def sleep(self):
        super().sleep()
        print("SNORE")

    def run_around(self):
        super().run_around()
        print("PANT")