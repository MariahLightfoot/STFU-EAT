class Restaurant:

    def __init__(self, name, image):
        self.id = id(self)
        self.name = name
        self.image = image
    
def __repr__(self):
    return "Restaurant('{}', '{}', '{}')".format(self.id, self.name, self.image)