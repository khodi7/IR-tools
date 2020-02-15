class Modifier:
    """Regroup the modifiers affecting ressource production.
    
    Attributes:
        citizen_output(float)
        commerce_modifier(float)
        freemen_output(float)
        manpower_modifier(float)
        slaves_output(float)
        research_modifier(float)
        tax_modifier(float)
        tribesmen_output(float)
    """
    
    def __init__(self, co = 0.0, cm = 0.0, fo = 0.0, mm = 0.0, so = 0.0, rm = 0.0, to = 0.0, tm = 0.0):
        """
        Args :
            co(float) : citizen output
            cm(float) : commerce modifier
            fo(float) : freemen output
            mm(float) : manpower modifier
            so(float) : slaves output
            rm(float) : research modifier
            to(float) : tribesmen output
            tm(float) : tax modifier
        """
        
        self._citizen_output = co
        self._commerce_modifier = cm
        self._freemen_output = fo
        self._manpower_modifier = mm
        self._slaves_output = so
        self._research_modifier = rm
        self._tribesmen_output = to
        self._tax_modifier = tm
    
#     @property
#     def citizen_output(self):
#         return self._citizen_output
#     
#     @citizen_output.setter
#     def citizen_output(self, n):
#         self._citizen_output = n
#         
#     @property
#     def commerce_modifier(self):
#         return self._commerce_modifier
#     
#     @commerce_modifier.setter
#     def commerce_modifier(self, n):
#         self._commerce_modifier = n
#         
#     @property
#     def freemen_output(self):
#         return self._manpower_output
#     
#     @manpower_output.setter
#     def manpower_output(self, n):
#         self._manpower_output = n
#         
#     @property
#     def manpower_modifier(self):
#         return self._manpower_modifier
#     
#     @manpower_modifier.setter
#     def manpower_modifier(self, n):
#         self._manpower_modifier = n
#         
#     @property
#     def research_output(self):
#         return self._research_output
#     
#     @research_output.setter
#     def research_output(self, n):
#         self._research_output = n
#         
#     @property
#     def research_modifier(self):
#         return self._research_modifier
#     
#     @research_modifier.setter
#     def research_modifier(self, n):
#         self._research_modifier = n
#         
#     @property
#     def tribesmen_output(self):
#         return self._tribesmen_output
#     
#     @tribesmen_output.setter
#     def tribesmen_output(self, n):
#         self._tribesmen_output = n
#         
#     @property
#     def tax_modifier(self):
#         return self._tax_modifier
#     
#     @tax_modifier.setter
#     def tax_modifier(self, n):
#         self._tax_modifier = n
        
        
class ModifyingAgent():
    """Object containing a modifier
    
    Attributes:
        amount(int): the amount of modifying agents.
        modifier(Modifier): the modifier linked to it.
        name(string): its name.
    """
    
    def __init__(self, n):
        self.amount = n
        self._modifier = None
        self._name = None
        
    @property
    def modifier(self):
        return self._modifier
    
    @property
    def name(self):
        return self._name
    
    
#--------Buildings--------#


class BuildingGroup(ModifyingAgent):
    """BuildingGroup is used to represent a group of buildings from I:R

    Attributes:
        type(int): indicates if the building can be built in settlements
        and/or cities. 0 for settlement, 1 for city and 2 for both.
    """
    
    def __init__(self, n):
        super.__init__(n)
        self._name = "Template building"
        self._type = 2
    
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
        self._name = "Academy"
        self._type = 1
        

#--------Trade goods--------#


class TradeGood(ModifyingAgent):
    """Trade good from I:R
    
    Attributes:
        amount(int)
        modifier(Modifier): Represents the modifier the first unit of the trade good
        gives.
        modifier2(Modifier): Represents the modifier one more unit of the trade good
        gives in the province capital.
        name(string)
    """
    
    def __init__(self, n):
        super().__init__(n)
        self._modifier2 = None
        self._name = "Template trade good"
        
    @property
    def modifier2(self):
        return self._modifier2


class Amber(TradeGood):
    
    def __init__(self, n):
        super().__init__(n)
        self._modifier = Modifier(tm = 0.1)
        self._modifier2 = Modifier(tm = 0.05)
        self._name = "Amber"


class BaseMetals(TradeGood):
    
    def __init__(self, n):
        super().__init__(n)
        self._modifier = Modifier(fo = 0.05)
        self._modifier2 = Modifier(fo = 0.025)
        self._name = "Base metals"


class Cloth(TradeGood):
    
    def __init__(self, n):
        super().__init__(n)
        self._modifier = Modifier(tm = 0.1)
        self._modifier2 = Modifier(tm = 0.05)
        self._name = "Cloth"


class Earthware(TradeGood):
    
    def __init__(self, n):
        super().__init__(n)
        self._modifier = Modifier(rm = 0.05)
        self._modifier2 = Modifier(rm = 0.01)
        self._name = "Earthware"


class Elephants(TradeGood):
    
    def __init__(self, n):
        super().__init__(n)
        self._modifier2 = Modifier(mm = 0.05)
        self._name = "Elephants"


class Gems(TradeGood):
    
    def __init__(self, n):
        super().__init__(n)
        self._modifier = Modifier(tm = 0.2)
        self._modifier2 = Modifier(tm = 0.1)
        self._name = "Gems"


class Hemp(TradeGood):
    
    def __init__(self, n):
        super().__init__(n)
        self._modifier = Modifier(so = 0.1)
        self._modifier2 = Modifier(so = 0.02)
        self._name = "Hemp"


class Honey(TradeGood):
    
    def __init__(self, n):
        super().__init__(n)
        self._modifier = Modifier(fo = 0.05)
        self._modifier2 = Modifier(fo = 0.025)
        self._name = "Honey"


class Incense(TradeGood):
    
    def __init__(self, n):
        super().__init__(n)
        self._modifier = Modifier(cm = 0.1)
        self._modifier2 = Modifier(cm = 0.02)
        self._name = "Incense"


class Iron(TradeGood):
    
    def __init__(self, n):
        super().__init__(n)
        self._modifier2 = Modifier(mm = 0.05)
        self._name = "Iron"


class Leather(TradeGood):
    
    def __init__(self, n):
        super().__init__(n)
        self._modifier = Modifier(so = 0.1)
        self._modifier2 = Modifier(so = 0.02)
        self._name = "Leather"


class Papyrus(TradeGood):
    
    def __init__(self, n):
        super().__init__(n)
        self._modifier = Modifier(rm = 0.2)
        self._modifier2 = Modifier(co = 0.05)
        self._name = "Papyrus"


class Silk(TradeGood):
    
    def __init__(self, n):
        super().__init__(n)
        self._modifier = Modifier(cm = 0.15)
        self._modifier2 = Modifier(cm = 0.05)
        self._name = "Silk"


class Spices(TradeGood):
    
    def __init__(self, n):
        super().__init__(n)
        self._modifier = Modifier(co = 0.05)
        self._modifier2 = Modifier(co = 0.025)
        self._name = "Spices"


class SteppeHorses(TradeGood):
    
    def __init__(self, n):
        super().__init__(n)
        self._modifier2 = Modifier(mm = 0.05)
        self._name = "Steppe horses"


class WildGames(TradeGood):
    
    def __init__(self, n):
        super().__init__(n)
        self._modifier = Modifier(to = 0.1)
        self._modifier2 = Modifier(to = 0.05)
        self._name = "Spices"


class Wood(TradeGood):
    
    def __init__(self, n):
        super().__init__(n)
        self._modifier2 = Modifier(tm = 0.03)
        self._name = "Wood"