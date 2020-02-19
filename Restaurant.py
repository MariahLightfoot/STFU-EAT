class Restaurant:

    def __init__(self, name, image, moreInfo):
        self.id = id(self)
        self.name = name
        self.image = image
        self.moreInfo = moreInfo
    
def __repr__(self):
    return "Restaurant('{}', '{}', '{}', '{}')".format(self.id, self.name, self.image, self.moreInfo)