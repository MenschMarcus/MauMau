class Card:

    def __init__(self, name):
        self.color = name[0]
        self.value = name[1]

    def get_color(self):
        return self.color

    def get_value(self):
        return self.value

    def get_name(self):
        return self.color+self.value
