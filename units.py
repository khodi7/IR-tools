import ast

def look_for(lst, word):
    """
    pre : lst is a list of strings like those obtained through a "file.readlines()" function.
    word is a string.
    post : returns a tuple (True, pos) where pos is the index of word in lst if word is in lst.
    Returns a tuple (False, -1) otherwise.
    """
    for i in range(len(lst)):
        line = decompose(lst[i])
        if line[0].lower() == word.lower():
            return (True, i)
    return (False, -1)

def decompose(line):
    """
    pre : "line" is a line from the "unit_specs.txt" file.
    post : returns a list of the different values of the line.
    """
    line = line.strip("\n")
    line = line.split()
    if len(line) == 0:
        return [""]
    n_line = []
    n_line.append(line[0])
    for i in range(1, len(line)):
        n_line.append(line[i].split("="))
    return n_line

def decompose_b(line):
    """
    pre : "line" is a line from the "unit_specs.txt" file.
    post : returns a list of the different values of the line.
    """
    line = line.strip("\n")
    line = line.split()
    if len(line) != 0:
        to_return = {line[0] : {}}
        for i in range(1, len(line)):
            splitted = line[i].split("=")
            to_return[line[0]].update({splitted[0] : splitted[1]})
    else :
        to_return = {}
    return to_return

def analize_spec_file():
    """
    pre : the unit_specs.txt file exists
    post : returns a dictionnary based on the file's content.
    It looks like this : {unit_type_1 : {char_1 : value_1, char_2 : value_2,...}, unit_type_2 : ...}
    """
    with open("unit_specs.txt", "r") as file:
        content = {}
        for line in file.readlines():
            content.update((decompose_b(line)))
    return content
    
class Unit:
    def __init__(self, ut, mor, strenght = 1.0, dis = 0.0, exp = 0.0):
        """
        pre : ut is a string.
        mor, strenght, dis and exp are floats.
        post : creates an object Unit.
        """
        #Adjusting the unit to UnitSpecs
        content = analize_spec_file()[ut]
        self.__morale = mor
        self.__strenght = strenght
        self.__discipline = dis + float(content["discipline"])
        self.__experience = exp
        self.__unit_type = ut
        self.__versus = ast.literal_eval(content["versus"])
        self.__offense = float(content["offense"])
        self.__defense = float(content["defense"])
      
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
    
    def versus(self):
        return self.__versus
    
    def offense(self):
        return self.__offense
    
    def defense(self):
        return self.__defense
    
    def set_morale(self, mor):
        self.__morale = mor
        
    def set_strenght(self, strenght):
        self.__strenght = strenght
    
    def add_to_morale(self, to_add):
        """
        pre : to_add is a number
        post : adds to_add to the Unit's __morale attribute
        """
        self.set_morale(self.morale() + to_add)
        
    def add_to_strenght(self, to_add):
        """
        pre : to_add is a number
        post : adds to_add to the Unit's __strenght attribute
        """
        self.set_strenght(self.strenght() + to_add)
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
    
    def set_discipline(self, d):
        self.__discipline = d
    
    def set_versus(self, vs):
        self.__versus = vs
    
    def set_offence(self, of):
        self.__offence = of
    
    def set_defense(self, de):
        self.__defense = de
        
    