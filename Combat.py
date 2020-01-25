from Units import Unit

class Combat:
    """
    Contains two lines (lists of lists containing units and their target)
    """
    def __init__(self, attacker_line, defender_line, ter, attacker_reserve = [], defender_reserve = [], cros = 0, roll = 0, attcker_martial = 0, defender_martial = 0):
        """
        Initializes a Combat object.
        pre : attacker_line and defender_line are lists in the following form :
        [[Unit1, target1], ..., [Unitn, targetn]]
        where Unitx are units or None, target are ints or None and n is the combat width.
        attacker_reserve and defender_reserve may be lists of Units.
        ter is a string representing the terrain on wich the battle is fought.
        cros is an int and the malus for crossing a river, a strait or landing. It must be null or negative.
        roll is the value of the dice for the attacking side.
        attcker_martial and defender_martial are the martial value of both generals.
        """
        self.__lines = [attacker_line, defender_line]
        self.__reserves = [attacker_reserve, defender_reserve]
        self.__terrain = ter
        self.__crossing = cros
        self.__roll = roll
        self.__martials = [attcker_martial, defender_martial]
        
#-------Accessors-------#
        
    def getlines(self):
        return self.__lines
    
    def getreserves(self):
        return self.__reserves
    
    def getterrain(self):
        return self.__terrain
    
    def getterrain_modifier(self):
        modifier = 0
        if self.getterrain() is in ["forest", "hills", "marsh"]:  #TODO : check jungle (the wiki says it's 0)
            modifier -= 1
        elif self.getterrain() == "mountains":
            modifier -= 2
        return (modifier + self.getcrossing())
    
    def getcrossing(self):
        return self.__crossing
    
    def getroll(self):
        return self.__roll
    
    def getmartials(self):
        return self.__martials
    
#-------Methods-------#
    
    def fight(self):
        """
        pre : -
        post : return a
        """
        pass
    
    def base_damage_done(self, attacker, defender):
        """
        pre : attacker and defender are both Units.
        post : returns the base damage done to defender by attacker.
        """
        #The two first lines can be replaced by a class attribute.
        general_bonus = max(0, (self.getmartials()[0] - self.getmartials()[1]) // 2) #This line needs some testing in game.
        raw_base_damage = min(0.36, 0.096 + 0.024 * (self.getroll() - getterrain_modifier(self) + general_bonus))
        #TODO add tactics, experience and second terrain modifier
        base_damage = raw_base_damage * attacker.getstrenght() * (1 + attacker.getdiscipline()) * (attacker.getversus()[defender.getunit_type()])\
                      * (1 + attacker.getoffense() - defender.getdefense())
        return base_damage
    
    def morale_damage_done(self, attacker, defender):
        """
        pre : attacker and defender are both Units.
        post : returns the morale damage done to defender by attacker.
        """
        morale_dmg = self.base_damage_done(attacker, defender) * attacker.getmorale() * defender.getmorale_damage_taken() * 1.5 * 0.5
        return morale_dmg
    
    def strenght_damage_done(self, attacker, defender):
        """
        pre : attacker and defender are both Units.
        post : returns the strenght damage done to defender by attacker.
        """
        #TODO add tactics modifier
        strenght_dmg = self.base_damage_done(attacker, defender) * defender.getstrenght_damage_taken() * 0.2
    
    def target(self, pos, line):
        pass
    
    def refreshtargets(self):
        pass
    
    def refreshpos(self):
        pass
    
    def deployment(self):
        pass