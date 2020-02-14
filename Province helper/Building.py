import Modifier


class BuildingGroup:
    """BuildingGroup is used to represent a group of buildings from I:R

    Attributes:
        amount(int): the amount of buildings in the BuildingGroup.
        modifier(Modifier): the modifier linked to the building.
        name(string): how the buildings are called.
        type(int): indicates if the building can be built in settlements
        and/or cities. 0 for settlement, 1 for city and 2 for both.
    """
    
    def __init__(self, n):
        """
        Args:
            n: the amount of buildings
        """
        self.amount = n
        self._modifier = None
        self._name = "Template building"
        self._type = 2
    
    @property
    def modifier(self):
        return self._modifier
    
    @property
    def name(self):
        return self._name
    
    @property
    def type(self):
        return self.type


class TrainingCampGroup(BuildingGroup):
    
    def __init__(self, n):
        super().__init__(n)
        self._modifier = Modifier.Modifier(mm = 0.1)
        self._name = "Training camp"
        self._type = 1


class BarracksGroup(BuildingGroup):
    # Unimplemented happiness and pop capacity
    
    def __init__(self, n):
        super().__init__(n)
        self._modifier = Modifier.Modifier(mm = 0.2)
        self._name = "Barrack"
        self._type = 0


# Check how the building works ingame
# class FoundryGroup(BuildingGroup):
#     
#     def __init__(self, n):
#         super().__init__(n)
#         self._modifier = Modifier.Modifier(co = 0.01, mo = 0.01, ro = 0.01, to = 0.01)
#         self._name = "Foundry"
#         self._type = 1


class MarketGroup(BuildingGroup):
    
    def __init__(self, n):
        super().__init__(n)
        self._modifier = Modifier.Modifier(cm = 0.25)  # Not sure. Check in case of bug
        self._name = "Market"
        self._type = 1


class TaxOfficeGroup()
    def __init__(self, n)
        super().__init__(n)
        self._modifier = Modifier.Modifier(tm = 0.1)
        self._name = "Tax office"
        self._type = 1
        

class AcademyGroup()
    def __init__(self, n)
        super().__init__(n)
        self._modifier = Modifier.Modifier(rm = 0.075)
        self._name = "Tax office"
        self._type = 1