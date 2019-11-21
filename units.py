def look_for(lst, word):
    """
    pre : lst is a list of strings like those obtained through a "file.readlines()" function.
    word is a string.
    post : returns a tuple (True, pos) where pos is the index of word in lst if word is in lst.
    Returns a tuple (False, -1) otherwise.
    """
    for i in range(len(lst)):
        line = decompose(lst[i])
        if line[0].strip().lower() == word.lower():
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
        self.__morale = mor
        self.__strenght = strenght
        self.__discipline = dis
        self.__experience = exp
        self.__unit_type = ut
        #add method to define UnitSpecs
        
    def morale(self):
        return self.__morale
    
    def strenght(self):
        return self.__strenght
    
    def discipline(self):
        return self.__discipline
    
    def experience(self):
        return self.__experience
    
    def unit_type(self):
        return self.__unit_type
        
class UnitSpecs:
    def __init__(self, ut):
        """
        pre : ut is a string representing the unit type.
        post : creates a UnitSpecs object.
        """
        self.__unit_type = ut
        self.__discipline = 0.0
        self.__versus = []
        self.__offence = 0.0
        self.__defense = 0.0
    
    def unit_type(self):
        return self.__unit_type
    
    def discipline(self):
        return self.__discipline
    
    def versus(self):
        return self.__versus
    
    def offence(self):
        return self.__offence
    
    def defense(self):
        return self.__defense
    
    def set_unit_type(self, ut):
        self.__unit_type = ut
    
    def set_discipline(self, d):
        self.__discipline = d
    
    def set_versus(self, vs):
        self.__versus = vs
    
    def set_offence(self, of):
        self.__offence = of
    
    def set_defense(self, de):
        self.__defense = de
    def retrieve(self):
        """
        Use this function to get the caracteristics of a unit from the "unit_specs.txt" file.
        pre : the "unit_specs.txt" file exists.
        "self.type" is a type contained inside that file.
        post : modify the UnitSpecs obect according to the file's data.
        """
        
    def modify(self):
        """
        Use this function to modify the caracteristics of a certain unit type
        """
        pass
