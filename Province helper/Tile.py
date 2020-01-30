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
    
    def __init__(self, nam, prov, ter, trade_g, other = [], builds = [], pop = []):
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
    
class Settlement(Tile):
    pass

class City(Tile):
    pass

class Metropolis(City):
    pass