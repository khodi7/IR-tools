import Modifier
import Pop
class Tile:
    """The Tile represents a settlement or a city in Imperator: Rome (I:R).

    Attributes :
        buildings (list of Buildings) : buildings in the tile.
        name (str) : is the name of the tile.
        pop (list of Pops)
        terrain (int) : is the index of the terrain type the tile is built on in the following list :
        ["Desert", "Farmland", "Forest", "Hills", "Jungle", "Marsh", "Mountains", "Plains"]
        trade_good (TradeGood) : tile's trade good.
        
        other_modifiers (list of Modifiers)
    """
    
    def __init__(self, nam, ter, trade_g, other = [], builds = [], pop = []):
        """
        Args:
            builds (list of Buildings)
            nam (str) : name
            pop (list of ints) : pop
            prov (Province) : province
            ter (int) : terrain
            trade_g (TradeGood) : trade_good
        """
        self._buildings = builds
        self._name = nam
        self._pop = pop
        self._terrain = ter
        self._trade_good = trade_g
        self._other_modifiers = other
    
    @property
    def buildings(self):
        """
        The amount of building a tile has cannot exceed its building capacity.
        """
        return self._buildings
    
    @buildings.setter
    def buildings(self, nbuilds):
        self._buildings = nbuilds
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, nname):
        self._name = nname
        
    @property
    def pop(self):
        return self._pop
    
    @pop.setter
    def pop(self, npop):
        self.pop = npop
    
    @property
    def terrain(self):
        return self._terrain
    
    @property
    def trade_good(self):
        return self._trade_good
    
    @property
    def other_modifiers(self):
        return self._other_modifiers
    
    @other_modifiers.setter
    def other_modifiers(self, nmod):
        self._other_modifiers = nmod
    
class Settlement(Tile):
    pass

class City(Tile):
    pass

class Metropolis(City):
    pass