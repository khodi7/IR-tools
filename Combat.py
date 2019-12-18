from Units import Unit

class Combat:
    """
    Contains two lines (lists of lists containing units and their target)
    """
    def __init__(self, attacker_line, defender_line, ter, attacker_reserve = [], defender_reserve = [], cros = 0, randice = False, attcker_martial = 0, defender_martial = 0):
        """
        Initializes a Combat object.
        pre : attacker_line and defender_line are lists in the following form :
        [[Unit1, target1], ..., [Unitn, targetn]]
        where Unitx are units or None, target are ints or None and n is the combat width.
        attacker_reserve and defender_reserve may be lists of Units.
        ter is a string representing the terrain on wich the battle is fought.
        cros is an int the malus for crossing a river, a strait or landing.
        randice is a boolean telling wheter or not random dices may be used.
        attcker_martial and defender_martial are the martial value of both generals.
        """
        self.__lines = [attacker_line, defender_line]
        self.__reserves = [attacker_reserve, defender_reserve]
        self.__terrain = ter
        self.__crossing = cros
        self.__randomdice = randice
        self.__martials = [attcker_martial, defender_martial]
        
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
    
    def base_damage_done(self, attacker, defender, attacker_martial, defender_martial, ter = 0, roll = 0):
        """
        pre : attacker and defender are both Units.
        attacker_martial and defender_martial are both ints.
        ter and roll are ints.
        post : returns the base damage done to defender by attacker.
        """
        general_bonus = max(0, (attacker_martial - defender_martial) // 2) #This line needs some testing in game.
        raw_base_damage = min(0.36, 0.096 + 0.024 * (roll - ter + general_bonus))
        #TODO add tactics, experience and second terrain modifier
        base_damage = raw_base_damage * attacker.getstrenght() * (1 + attacker.getdiscipline()) * (attacker.getversus()[defender.getunit_type()])\
                      * (1 + attacker.getoffense() - defender.getdefense())
        return base_damage
    
    def morale_damage_done(self, attacker, defender):
        """
        pre : attacker and defender are both Units.
        post : returns the morale damage done to defender by attacker.
        """
        pass
    
    def strenght_damage_done(self, attacker, defender):
        """
        pre : attacker and defender are both Units.
        post : returns the strenght damage done to defender by attacker.
        """
        pass
    
    def target(self, pos, line):
        pass
    
    def refreshtargets(self):
        pass
    
    def refreshpos(self):
        pass
    
    def deployment(self):
        pass