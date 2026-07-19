from abc import ABC, abstractmethod

class Instrument(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass



class Guitar(Instrument):

    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print(self.name, " Strum Strum ")



class Piano(Instrument):

    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print(self.name, "plank plonk")


class Drum(Instrument):

    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print(self.name, " Boom Boom ")



g = Guitar("Guitar")
p = Piano("Piano")
d = Drum("Drum")

print("Music Instrument Sound Show ")

g.sound()
p.sound()
d.sound()