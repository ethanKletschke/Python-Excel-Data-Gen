import random as rnd

class Details:
    """The `Details` class contains the details to append for each
    row in the CSV file.
    """
    def __init__(self):
        """The `__init__()` constructor initialises each field
        in the class as an empty value of its respective type, and 
        returns an instance of the `Details` class.
        """
        self.uniqueID = ""
        self.fname = ""
        self.lname = ""
        self.age = 0
        self.city = ""
        self.owed = 0.00

    def __set_id(self) -> None:
        """The `__set_id()` method sets the `uniqueID` field
        of the object after testing if the ID field is empty, 
        and then if the `fname` field is NOT empty.
        """
        # if the unique ID field is still empty
        if self.uniqueID == "" or self.uniqueID is None:
            # If the first name is not still empty
            if self.fname != "" or self.fname is not None:
                # Build a new ID
                # Append the uppercased first 2 letters of the first name
                self.uniqueID = self.fname[0:2].upper()
                # Append the age as a string
                self.uniqueID += str(self.age)
                # Append the lowercased last 2 letters of the city
                self.uniqueID += self.city[-2:].lower()

    def randomise(self) -> None:
        """The `randomise()` method randomises the details in this object
        with preset lists of values (for strings) and randomised integer numbers.
        """
        # A list of random first names to use
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

        # A list of random last names to use.
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

        # A list of random city names to use.
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

        # Randomly select values from the respective lists above.
        self.fname = fnames[rnd.randint(0, len(fnames) - 1)]
        self.lname = lnames[rnd.randint(0, len(lnames) - 1)]
        self.city = cities[rnd.randint(0, len(cities) - 1)]
        
        # Randomly generate an integer number for the age between 1 and 129, including both.
        self.age = rnd.randint(1,129)
        # Randomly generate a float number for the amount owed
        self.owed = rnd.randrange(0, 999)

        # Set the ID
        self.__set_id()
