class Tile:
    """The Tile represents a settlement or a city in Imperator: Rome (I:R).

    Attributes :
        buildings (list of Buildings) : buildings in the tile.
        name (str) : is the name of the tile.
        pop (list) : is a list of ints containing the amount of each kind of pop in a tile.
        [citizen amount, freeman amount, tribesman amount, slave amount]
        province (Province) : is the Province in wich Tile is located
        terrain (int) : is the index of the terrain type the tile is built on in the following list :
        ["Desert", "Farmland", "Forest", "Hills", "Jungle", "Marsh", "Mountains", "Plains"]
        trade_good (TradeGood) : tile's trade good.
        
        other_modifiers (list) : list of Modifier's.
    """
    
    
    """
