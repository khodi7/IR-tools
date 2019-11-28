from Units import Unit

class Combat:
    """
    Contains two lines (lists of lists containing units and their target)
    """
    def __init__(self, line1, line2, ter, reserve1 = [], reserve2 = [], cros = 0, randice = False, martial1 = 0, martial2 = 0):
        """
        Initializes a Combat object.
        pre : line1 and line2 are lists in the following form :
        [[Unit1, target1], ..., [Unitn, targetn]]
        where Unitx are units or None, target are ints or None and n is the combat width.
        reserve1 and reserve2 may be lists of Units.
        ter is a string representing the terrain on wich the battle is fought.
        cros is an int the malus for crossing a river, a strait or landing.
        randice is a boolean telling wheter or not random dices may be used.
        martial1 and martial2 are the martial value of both generals.
        """
        self.__lines = [line1, line2]
        self.__reserves = [reserve1, reserve2]
        self.__terrain = ter
        self.__crossing = cros
        self.__randomdice = randice
        self.__martials = [martial1, martial2]
        
#-------Accessors-------#
        
    def getlines(self):
        return self.__lines
    
    def getreserves(self):
        return self.__reserves
    
    def getterrain(self):
        return self.__terrain
    
    def getcrossing(self):
        return self.__crossing
    
    def getrandomdice(self):
        return self.__randomdice
    
    def getmartials(self):
        return self.__martials
    
#-------Methods-------#
    
    def fight(self):
        pass
    
    def solofight(self, attacker, defender):
        """
        pre : attacker and defender are both Units.
        post : returns the damage done to defender by attacker.
        """
    
    def target(self, pos, line):
        pass
    
    def refreshtargets(self):
        pass
    
    def refreshpos(self):
        pass
    
    def deployment(self):
        pass