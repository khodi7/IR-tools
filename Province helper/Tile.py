class Tile:
    """The Tile represents a settlement or a city in Imperator: Rome (I:R).

    Attributes :
        name (str) : is the name of the tile
        terrain (int) : is the index of the terrain type the tile is built on in the following list :
        ["Desert", "Farmland", "Forest", "Hills", "Jungle", "Marsh", "Mountains", "Plains"]
        civilization (float)
        unrest (float)
        migration (float)
        pop (list) : is a list of ints containing the amount of each kind of pop in a tile.
        [citizen amount, freeman amount, tribesman amount, slave amount]
        buildings (list) : list of building objects.
    
    
    """
