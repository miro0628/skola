class elev:

    def __init__(self, namn, id, utbildning):
        self.namn = namn
        self.id = id
        self.utbildning = utbildning

    def get_elev(self):
        svar = self.name+ " | Program: " +self.utbildning+ " | ID: " + self.id

        return svar