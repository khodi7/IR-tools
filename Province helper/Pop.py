class PopGroup:
    """Pop is a group of pops from Imperator: Rome (I:R)

    Attributes:
        amount (int) : quantity of pop in the group.
        base_happiness (float) : base happiness of the group's pops
        culture (int) : 0 if state culture, 1 if not core culture but culture group, 2 otherwise.
        religion (boolean) : True if state religion, False otherwise.
        
        base_output(float) : base output of one pop of the PopGroup
    """
    
    def __init__(self, amount, culture, religion, base_happiness, base_output):
        self._amount = amount
        self._base_happiness = base_happiness
        self._culture = culture
        self._religion = religion
        
        self._base_output = base_output
        
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
    
class PopOutput:
    """Output of a pop.

    Attributes :
        commerce : commerce value
        manpower : local manpower
        research : research points
        tax : base tax
    """
    
    def __init__(self, com = 0, mp = 0, res = 0, tx = 0):
        """
        Args :
            com : commerce
            mp : manpower
            res : research
            tx : tax
        """
        self._commerce = com
        self._manpower = mp
        self._research = res
        self._tax = tx
    
    @property
    def commerce(self):
        return self._commerce
    
    @property
    def manpower(self):
        return self._manpower
    
    @property
    def research(self):
        return self._research
    
    @property
    def tax(self):
        return self._tax
        
    
class CitizensGroup(PopGroup):
    
    def __init__(self, amount, culture, religion):
        super().__init__(amount, culture, religion, 0.2, PopOutput(com = 0.01, res = 0.25))

class FreemenGroup(PopGroup):
    
    def __init__(self, amount, culture, religion):
        super().__init__(amount, culture, religion, 0.25, PopOutput(mp = 0.01))


class TribesmenGroup(PopGroup):
    
    def __init__(self, amount, culture, religion):
        super().__init__(amount, culture, religion, 0.2, PopOutput(mp = 0.005, tx = 0.015))


class SlavesGroup(PopGroup):
    
    def __init__(self, amount, culture, religion):
        super().__init__(amount, culture, religion, 0.2, PopOutput(tx = 0.035))
