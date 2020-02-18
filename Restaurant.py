class Restaurant:

    def __init__(self, name, image, directions):
        self.id = id(self)
        self.name = name
        self.image = image
        self.directions = directions
    
def __repr__(self):
    return "Restaurant('{}', '{}', '{}', '{}')".format(self.id, self.name, self.image, self.directions)