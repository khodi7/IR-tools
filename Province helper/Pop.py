class PopGroup:
    """Pop is a group of pops from Imperator: Rome (I:R)

    Attributes:
        amount (int) : quantity of pop in the group.
        base_happiness (float) : base happiness of the group's pops
        culture (int) : 0 if state culture, 1 if not core culture but culture group, 2 otherwise.
        religion (boolean) : True if state religion, False otherwise.
        
        base_output(float) : base output of one pop of the PopGroup
    """
    
    def __init__(self, amount, culture, religion):
        self._amount = amount
        self._base_happiness = 0
        self._culture = culture
        self._religion = religion
        
        self._base_output = 0.0
        
    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, namount):
        self._amount = namount
        
    @property
    def base_happiness(self):
        return self._base_happiness
    
    @property
    def culture(self):
        return self._culture
    
    @property
    def religion(self):
        return self._religion
    
    @property
    def base_output(self):
        return self._base_output
        
    
class CitizensGroup(PopGroup):
    pass

class FreemenGroup(PopGroup):
    pass

class TribesmenGroup(PopGroup):
    pass

class SlavesGroup(PopGroup):
    pass