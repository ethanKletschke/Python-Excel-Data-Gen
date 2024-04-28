import random as rnd

class Details:
    def __init__(self):
        self.uniqueID = ""
        self.fname = ""
        self.lname = ""
        self.age = 0
        self.city = ""
        self.owed = 0.00

    def set_id(self):
        if self.uniqueID == "" or self.uniqueID is None:
            if self.fname != "" or self.fname is not None:
                self.id = self.fname[0:2]
                self.id += str(self.age)
                self.id += self.city[-2:0]

    def randomise(self):
        fnames = [
            "Oscar",
            "Maria",
            "Viola",
            "Justin",
            "Marie",
            "Brian",
            "Lucille",
            "Amanda",
            "Jessie",
            "Bessie",
            "Isabella",
            "Sallie",
            "Hulda",
            "William",
            "Lelia",
            "Hannah",
            "Carrie",
            "William",
            "Nettie",
            "Virgie",
            "Susie",
            "Marion",
            "Ian",
            "Nat",
            "Piper",
            "Yoni",
            "Virgil"
        ]

        lnames = [
            "Ferguson",
            "Gross",
            "Higgins",
            "Paul",
            "Baldwin",
            "Burgess",
            "Phelps",
            "Perry",
            "Hammond",
            "Cohen",
            "Dunn",
            "Davidson",
            "Floyd",
            "Padilla",
            "Lewis",
            "Young",
            "Stone",
            "Hoffman",
            "Schneider",
            "Morales",
            "Jensen",
            "Alvarez",
            "Hart"
        ]

        cities = [
            "Orevanafe",
            "Sabakas",
            "Kijeebi",
            "Hudviza",
            "Toduwviw",
            "Nedubra",
            "Dolbewu",
            "Hudkibid",
            "Bebabejo",
            "Helukkir",
            "Jotsohoca",
            "Zacvuggav",
            "Sikunpu",
            "Heztusa",
            "Kimnool",
            "Wederji",
            "Koorwo",
            "Balbosboj",
            "Gajebus",
            "Polupif",
            "Bittaniv"
        ]

        self.fname = fnames[rnd.randint(0, len(fnames) - 1)]
        self.lname = lnames[rnd.randint(0, len(lnames) - 1)]
        self.city = cities[rnd.randint(0, len(cities) - 1)]
        self.age = rnd.randint(1,129)
        self.owed = rnd.randrange(0, 999)

        # Set the ID
        self.set_id()
