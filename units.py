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
        content = analize_spec_file().get(self.unit_type(), 0)
        if content == 0:
            print("There was a problem while retrieving {0} data".format(self.unit_type()))
            return None
        self.set_discipline(content["discipline"])
        self.set_versus(content["versus"])
        self.set_offence(content["offence"])
        self.set_defense(content["defense"])
        
    def pre_modify(self):
        """
        pre : -
        post : returns a dictionnary containing the data to put in the unit_specs.txt file
        """
        if analize_spec_file().get(self.unit_type(), 0) == 0:
            print("error")
            return None
        odic = analize_spec_file()
        ndic = {self.unit_type() : {"discipline" : str(self.discipline()), "versus" : str(self.versus()), "offence" : str(self.offence()), "defense" : str(self.defense())}}
        odic.update(ndic)
        return odic
    
    def modify(self):
        """
        pre : -
        post : modify the data associated to the UnitSpecs's attribute __unit_type
        in the unit_specs.txt file
        """
        content = self.pre_modify()
        to_register = ""
        for key in content:
            to_register += key
            for sub_key in content[key]:
                to_register += " {0}={1}".format(sub_key, content[key][sub_key])
            to_register += "\n\n"
        with open("unit_specs.txt", "w") as file:
            file.writelines(to_register)