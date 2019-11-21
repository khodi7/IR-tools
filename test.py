import units

file = open("unit_specs.txt", "r")
lst = file.readlines()

#assert units.look_for(lst, "ArCher") == (True, 0)
#assert units.look_for(lst, "light_cavalry") == (True, 2)
#assert units.look_for(lst, "heavy_infantry") == (True, 4)
#assert units.look_for(lst, "light_infantry") == (True, 6)
#assert units.look_for(lst, "space_marine") == (False, -1)