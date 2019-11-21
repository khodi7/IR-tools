def look_for(lst, word):
    """
    pre : lst is a list of strings like those obtained through a "file.readlines()" function.
    word is a string.
    post : returns a tuple (True, pos) where pos is the index of word in lst if word is in lst.
    Returns a tuple (False, -1) otherwise.
    """
    for i in range(len(lst)):
        if lst[i][0].strip().lower() == word.lower():
            return (True, i)
    return (False, -1)

def decompose(line):
    """
    pre : "line" is a line from the "unit_specs.txt" file.
    post : returns a list of the different values of the line.
    """
    line = line.strip("\n")
    line = line.split()
    n_line = []
    #Here, 
    #We start reading the list "line" at the index 1
    #because we know that the index 0 in "line" is the unit type.
    for i in range(1, len(line)):
        n_line.append(line[i].split("="))
class Unit:
    def __init__(self, ut, us, mor, strenght = 1.0, dis = 0.0, exp = 0.0):
        """
        pre : ut is a string.
        mor, strenght, dis and exp are floats.
        us is a UnitSpecs object.
        post : creates an object Unit.
        """
        self.morale = mor
        self.strenght = strenght
        self.discipline = dis
        self.experience = exp
        self.type = ut
        #add method to define UnitSpecs
        
class UnitSpecs:
    def __init__(self, ut):
        """
        pre : ut is a string representing the unit type.
        post : creates a UnitSpecs object.
        """
        self.type = ut
        self.discipline = 0.0
        self.versus = []
        self.offence = 0.0
        self.defense = 0.0
    def retrieve():
        """
        Use this function to get the caracteristics of a unit from the "unit_specs.txt" file.
        pre : the "unit_specs.txt" file exists.
        "self.type" is a type contained inside that file.
        post : modify the UnitSpecs obect according to the file's data.
        """
    def modify():
        """
        Use this function to modify the caracteristics of a certain unit type
        """
        pass